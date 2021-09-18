import math
from random import randint

from cell import Cell
from constants import *

class GameRegistry():
	def __init__(self):
		self.cell_registry = [] # contains cell.Cell objects
		self.claimed_positions_registry = [] # contains (cell id, pygame.Rect) tuples
	
	def add_cell(self, x, y, height, width, speed=1, color=WHITE, border_width=1, border_color=BLACK, awareness_radius=5):
		self.cell_registry.append(Cell(self, x, y, height, width, speed, color, border_width, border_color))
	
	def remove_cell(self, id_):
		index = None
		for i in range(len(self.cell_registry)):
			if self.cell_registry[i].id_ == id_:
				index = i
				break
		if index:
			del self.cell_registry[index]
		index = None
		for i in range(len(self.claimed_positions_registry)):
			if self.claimed_positions_registry[i][0] == id_:
				index = i
				break
		if index:
			del self.claimed_positions_registry[index]

	def update_cells(self):
		for cell in self.cell_registry:
			cell.update()

	def populate(self, n, height=30, width=30, speed=1, color=WHITE, border_width=1, border_color=BLACK, awareness_radius=5):
		for i in range(n):
			if len(self.cell_registry) == 0:
				pos = pygame.math.Vector2(randint(0, SIMULATION_WIDTH - math.ceil(width / 2)), randint(0, HEIGHT - math.ceil(height / 2)))
				self.add_cell(pos.x, pos.y, height, width, speed, color, border_width, border_color)
				continue
			spawned = False
			while not spawned:
				pos = pygame.math.Vector2(randint(0, SIMULATION_WIDTH - math.ceil(width / 2)), randint(0, HEIGHT - math.ceil(height / 2)))
				candidate_rect = pygame.Rect(pos.x, pos.y, width, height)
				collides = False
				for cell in self.cell_registry:
					cell_rect = pygame.Rect(cell.x, cell.y, cell.width, cell.height)
					if candidate_rect.colliderect(cell_rect):
						collides = True
				if not collides:
					self.add_cell(pos.x, pos.y, height, width, speed, color, border_width, border_color)
					spawned = True