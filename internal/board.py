class Board:
	state: list

	def __init__(self):
		self.state = [[0, 0, 0],
			 		  [0, 0, 0],
			 		  [0, 0, 0]]

	def set_x(self, i, j):
		if self.state[i][j] == 0:
			self.state[i][j] = 1
		else:
			raise Exception()
		print('x', i, j)

	def set_o(self, i, j):
		if self.state[i][j] == 0:
			self.state[i][j] = -1
		else:
			raise Exception()
		print('o', i, j)

	def evaluate(self):
		for i in range(3):
			score = self.evaluate_row(i)
			if abs(score) == 3: return score
		for j in range(3):
			score = self.evaluate_column(j)
			if abs(score) == 3: return score
		for up in [True, False]:
			score = self.evaluate_diagonal(up)
			if abs(score) == 3: return score
		
	def evaluate_row(self, i):
		return sum(self.state[i])

	def evaluate_column(self, j):
		return sum([self.state[i][j] for i in range(3)])

	def evaluate_diagonal(self, up: bool):
		if up == True:
			return sum([self.state[2-i][i] for i in range(3)])
		else:
			return sum([self.state[i][i] for i in range(3)])
