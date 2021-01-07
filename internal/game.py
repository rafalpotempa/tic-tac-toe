import pygame

import time
import internal.view as view
from internal.view import View
from internal.board import Board

player_x = 'player_x'
player_o = 'player_o'
draw = 'draw'

class Game:
	view: View
	board: Board
	player: str
	winner: str

	def __init__(self, view):
		self.board = Board()
		self.view = view
		self.view.board = self.board
		self.view.draw_board(full=True)

		self.player = player_x
		self.winner = None

	def mainloop(self):
		while True:
			while self.winner is None:
				self.game_screen()
			else:
				self.winner_screen()

	def game_screen(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				try:
					if self.player == player_x: self.board.set_x(*self.translate_click(event))
					if self.player == player_o: self.board.set_o(*self.translate_click(event))
					self.swap_player()
					self.view.draw_board()
					score = self.board.evaluate()
					if score == 3:
						self.winner = player_x
					if score == -3:
						self.winner = player_o
					if score == -10:
						self.winner = draw
				except: pass
	
	def winner_screen(self):
		if self.winner is not draw:
			winner_message = self.view.font.render(f"'{self.winner[-1].upper()}' won!", False, view.foreground_color)
		else:
			winner_message = self.view.font.render(f"Draw!", True, view.foreground_color)
		winner_popup = pygame.Surface(winner_message.get_size())
		winner_popup.fill(view.background_color)
		winner_popup.blit(winner_message, (0, 0))
		self.view.screen.blit(winner_popup, (view.width/2 - winner_popup.get_width()/2, view.height/2 - view.font_size/2))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				self.winner = None
				self.board = Board()
				self.view.board = self.board
				self.view.draw_board(full=True)

	def translate_click(self, event):
		i, j = None, None
		x, y = event.pos
		i = (3*(y-view.margin)) // (view.height - 2*view.margin)
		j = (3*(x-view.margin)) // (view.width - 2*view.margin)
		return i, j

	def swap_player(self):
		if self.player == player_o: self.player = player_x
		else: self.player = player_o
