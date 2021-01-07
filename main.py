from internal.board import Board
from internal.view import View
from internal.game import Game

if __name__ == "__main__":
	try:
		Game(View()).mainloop()
	except KeyboardInterrupt:
		exit()