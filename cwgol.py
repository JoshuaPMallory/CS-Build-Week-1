import sys
from os import system, name

import numpy as np


class GOL():
	def __init__(self, grid = np.matrix([])):
		self.dim    = [29, 119] # 29, 119
		self.grid   = np.matrix(np.random.choice([False, True], size = self.dim))
		self.conv   = {False: ' ', True: '█'}

	def step(self):
		grid = self.grid.copy()
		for x in range(self.grid.shape[0]):
			for y in range(self.grid.shape[1]):
				summy = self.grid[x - 1:x + 2
					             ,y - 1:y + 2].sum()

				if self.grid[x, y] == 1:
					if summy < 3 or summy > 4:
						grid[x, y] = 0
				else:
					if summy == 3:
						grid[x, y] = 1

		self.grid = grid

	def clear(self):
		# windows
		if name == 'nt':
			_ = system('cls')
		# mac / linux
		else:
			_ = system('clear')

	def display(self):
		display = ''

		for x in range(self.grid.shape[0]):
			for y in range(self.grid.shape[1]):
				# display += self.conv[self.grid[x, y]]
				sys.stdout.write(self.conv[self.grid[x, y]])
			sys.stdout.write('\n')
			# display += '\n'
		# print(display[:-2])

	def play(self):
		while True:
			try:
				self.display()
				self.step()
				self.clear()
			except KeyboardInterrupt:
				break

stuff = GOL()
stuff.play()
