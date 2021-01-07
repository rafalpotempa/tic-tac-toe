import pygame
from internal.board import Board

width, height = 320, 320
margin = 20
background_color = 255, 255, 255
foreground_color = 0, 0, 0
font_size = 50

class View:
	screen: pygame.surface
	board: Board

	dw: float
	dh: float

	def __init__(self):
		self.dw = (width-2*margin) / 3.0
		self.dh = (height-2*margin) / 3.0

		self.screen = pygame.display.set_mode((width, height))

		pygame.font.init()
		self.font = pygame.font.SysFont(None, font_size)

		pygame.display.flip()

	def draw_board(self, full=False):
		if full:
			self.screen.fill(background_color)
			self.draw_grid()

		for i, row in enumerate(self.board.state):
			for j, field in enumerate(row):
				if field == 1:
					self.draw_x(i, j)
				elif field == -1:
					self.draw_o(i, j)
				else:
					continue

	def draw_grid(self):
		pygame.draw.line(self.screen, foreground_color,
						 (self.dw + margin, margin), 
						 (self.dw + margin, height - margin), 
						 width=3)
		pygame.draw.line(self.screen, foreground_color,
						 (2*self.dw + margin, margin), 
						 (2*self.dw + margin, height - margin), 
						 width=3)

		pygame.draw.line(self.screen, foreground_color,
						 (margin, self.dh + margin), 
						 (width - margin, self.dh + margin), 
						 width=3)
		pygame.draw.line(self.screen, foreground_color,
						 (margin, 2*self.dh + margin), 
						 (width - margin, 2*self.dh + margin), 
						 width=3)		
		pygame.display.flip()

	def draw_x(self, i, j):
		pygame.draw.line(self.screen, foreground_color,
		 				 (margin+self.dw*j+15, margin+self.dh*i+15), 
						 (margin+self.dw*(j+1)-15, margin+self.dh*(i+1)-15), 
						 width=4)
		pygame.draw.line(self.screen, foreground_color,
		 				 (margin+self.dw*j+15, margin+self.dh*(i+1)-15), 
						 (margin+self.dw*(j+1)-15, margin+self.dh*(i)+15), 
						 width=4)
		pygame.display.flip()

	def draw_o(self, i, j):
		pygame.draw.circle(self.screen, foreground_color,
						   (margin + self.dw*(j + 0.5), margin + self.dh*(i + 0.5)),
						   radius=(min(self.dw, self.dh)/2 - 10), width=3)
		pygame.display.flip()
		