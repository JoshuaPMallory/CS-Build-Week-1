import sys
from os import system, name
from time import sleep

import numpy as np


class GOL():
	def __init__(self):
		self.dim    = [29, 119] # 29, 119
		self.grid   = np.matrix(np.random.choice([False, True], size = self.dim))
		self.conv   = {False: ' ', True: '█'}

	def save(self):
		with open('grid.txt','wb') as file:
		    for line in self.grid:
		        np.savetxt(file, line, fmt = '%.2f')
		print('Saved!')

	def load(self, file):
		self.grid = np.loadtxt(file)
		print('Loaded!')

	def step(self):
		grid = self.grid.copy()
		for x in range(self.grid.shape[0]):
			for y in range(self.grid.shape[1]):
				summy = self.grid[x - 1:x + 2
					             ,y - 1:y + 2].sum()

				if self.grid[x, y] == True:
					if summy < 3 or summy > 4:
						grid[x, y] = False
				else:
					if summy == 3:
						grid[x, y] = True
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

	def skip(self, gen):
		while gen != 0:
			gen -= 1
			self.step()
		self.display()

stuff = GOL()
# stuff.load('grid.txt')
# stuff.skip(10)
# sleep(1)
stuff.play()
