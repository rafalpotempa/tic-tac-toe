from internal.board import Board
from internal.view import View


if __name__ == "__main__":
	board = Board()
	view = View(board)
	view.draw_board()

	import time; time.sleep(2)
