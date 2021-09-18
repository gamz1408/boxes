import math
from random import randint
import uuid

import pygame

from constants import *


class Cell():
	def __init__(self, registry, x, y, height, width, speed=1, color=WHITE, border_width=1, border_color=BLACK, awareness_radius=5):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.center_x = x + width / 2
		self.center_y = y + height / 2
		self.color = color
		self.border_width = border_width
		self.border_color = border_color
		self.speed = speed
		self.normalized_speed = self.speed * COS45

		self.goal = None

		self.registry = registry
		self.has_registered_position = False
		self.id_ = uuid.uuid4().hex

	def set_goal(self):
		self.goal = pygame.math.Vector2(randint(0, SIMULATION_WIDTH - math.ceil(self.width / 2)), randint(0, HEIGHT - math.ceil(self.height / 2)))
		print(f'set goal to: {self.goal} ({self.id_})')

	def find_next_pos(self):
		if self.goal is None:
			return None
		possible_positions = [(self.x + self.speed, self.y), (self.x + self.normalized_speed, self.y + self.normalized_speed), (self.x, self.y + self.speed), (self.x - self.normalized_speed, self.y + self.normalized_speed), (self.x - self.speed, self.y), (self.x - self.normalized_speed, self.y - self.normalized_speed), (self.x, self.y - self.speed), (self.x + self.normalized_speed, self.y - self.normalized_speed)]
		distance_table = []
		possible_positions_sorted = []
		for pos in possible_positions:
			possible_positions_sorted.append((pos[0], pos[1], math.pow(abs(pos[0] - self.goal.x), 2) + math.pow(abs(pos[1] - self.goal.y), 2)))

		possible_positions_sorted.sort(key=lambda tup: tup[2], reverse=False)
		'''
		possible_positions_sorted = [(self.x + self.speed, self.y)]
		for i in range(1, len(possible_positions)):
			index = 0
			for j in range(len(possible_positions_sorted)):
			 	i_dist = math.pow(possible_positions[i][0], 2) + math.pow(possible_positions[i][1], 2)
			 	j_dist = math.pow(possible_positions_sorted[j][0], 2) + math.pow(possible_positions_sorted[j][1], 2)
			 	if j_dist <= i_dist:
			 		index = j
			possible_positions_sorted.insert(index, possible_positions[i])
		'''

		debug_list = []
		for pos in possible_positions_sorted:
			debug_list.append(math.pow(abs(pos[0] - self.goal.x), 2) + math.pow(abs(pos[1] - self.goal.y), 2))
		#print('---------------')
		#print(', '.join(str(x) for x in debug_list))

		if len(self.registry.claimed_positions_registry) == 0:
			return possible_positions_sorted[0]

		for pos in possible_positions_sorted:
			new_pos_rect = pygame.Rect(pos[0], pos[1], self.width, self.height)
			collides = False
			for claim in self.registry.claimed_positions_registry:
				if claim[0] == self.id_:
					continue
				if new_pos_rect.colliderect(claim[1]):
					collides = True
					break
			if not collides:
				return pos
		return None


	def move(self):
		if self.goal is None:
			self.set_goal()
		next_pos = self.find_next_pos()
		if next_pos:
			self.x, self.y = next_pos[0], next_pos[1]
			if not self.has_registered_position:
				self.registry.claimed_positions_registry.append((self.id_, pygame.Rect(self.x, self.y, self.width, self.height)))
				self.has_registered_position = True
			else:
				for i in range(len(self.registry.claimed_positions_registry)):
					if self.registry.claimed_positions_registry[i][0] == self.id_:
						self.registry.claimed_positions_registry[i] = (self.id_, pygame.Rect(self.x, self.y, self.width, self.height))
			if abs(self.x - self.goal.x) <= CELL_TARGET_ACCURACY and abs(self.y - self.goal.y) <= CELL_TARGET_ACCURACY:
				self.goal = None

	def draw(self):
		pygame.draw.rect(WIN, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

	def update_center(self):
		self.center_x = self.x + self.width / 2
		self.center_y = self.y + self.height / 2

	def update(self):
		self.move()
		self.update_center()
		self.draw()