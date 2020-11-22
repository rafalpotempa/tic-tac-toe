class Board:
	state: list

	def __init__(self):
		self.state = [[1, -1, 0],
			 		  [0, 0, 0],
			 		  [0, 0, 0]]

	def set_x(self, i, j):
		if self.state[i][j] == 0:
			self.state[i][j] = 1
		else:
			raise Exception()

	def set_o(self, i, j):
		if self.state[i][j] == 0:
			self.state[i][j] = -1
		else:
			raise Exception()

	def evaluate(self):
		winner = None
		for i in range(3):
			score = self.evaluate_row(i)
			if score == 3: winner = 'player_x'
			elif score == -3: winner = 'player_o'
		for j in range(3):
			score = self.evaluate_column(j)
			if score == 3: winner = 'player_x'
			elif score == -3: winner = 'player_o'
		for up in [True, False]:
			score = self.evaluate_diagonal(up)
			if score == 3: winner = 'player_x'
			elif score == -3: winner = 'player_o'
		print(winner)
		
	def evaluate_row(self, i):
		return sum(self.state[i])

	def evaluate_column(self, j):
		return sum([self.state[i][j] for i in range(3)])

	def evaluate_diagonal(self, up: bool):
		if up == True:
			return sum([self.state[2-i][i] for i in range(3)])
		else:
			return sum([self.state[i][i] for i in range(3)])
