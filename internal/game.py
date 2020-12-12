import pygame

import internal.view as view
from internal.view import View
from internal.board import Board

player_x = 'player_x'
player_o = 'player_o'

class Game:
	view: View
	board: Board
	player: str
	winner: str

	def __init__(self, board, view):
		self.board = board
		self.view = view
		self.view.board = board
		self.view.draw_board()

		self.player = player_x
		self.winner = None

	def mainloop(self):
		while self.winner is None:
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
					except: pass
		else:
			print(self.winner)

	def translate_click(self, event):
		i, j = None, None
		x, y = event.pos
		i = (3*(y-view.margin)) // (view.height - 2*view.margin)
		j = (3*(x-view.margin)) // (view.width - 2*view.margin)
		return i, j

	def swap_player(self):
		if self.player == player_o: self.player = player_x
		else: self.player = player_o
