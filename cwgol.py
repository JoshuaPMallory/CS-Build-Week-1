import sys
from os import system, name
from time import sleep

# import pygame
# from pygame.locals import *
from numpy import random, matrix, savetxt, loadtxt


class GOL():
	def __init__(self, dim = (29, 120)): # 29, 119
		self.dim    = dim
		self.frames = [matrix(random.choice([False], size = self.dim))]
		self.conv   = {False: ' ', True: '█'}

	def save(self, filename = 'grid.txt'):
		with open(filename, 'wb') as file:
			for line in self.frames[0]:
				savetxt(file, line, fmt = '%.2f')
		print('Saved!')

	def load(self, filename = 'grid.txt'):
		self.frames[0] = loadtxt(file)
		print('Loaded!')


	def randomize(self, boole = True):
		'''Boole lets you just make an empty grid for False.
		True actually randomizes it all.
		'''

		choices = [False]

		if boole == True:
			choices.append(True)

		self.frames = [matrix(random.choice(choices, size = self.dim))]

	def step(self, steps = 1):
		while steps != 0:
			steps -= 1
			curg   = self.frames[-1]
			newg   = self.frames[-1].copy()

			for x in range(curg.shape[0]):
				for y in range(curg.shape[1]):
					summy = curg[x - 1:x + 2
								,y - 1:y + 2].sum()

					if curg[x, y] == True:
						if summy < 3 or summy > 4:
							newg[x, y] = False
					else:
						if summy == 3:
							newg[x, y] = True
			self.frames.append(newg)

	def skip(self, gen = 10):
		self.step(10)
		self.frames = self.frames[-1:]
		self.display()
		sleep(1)


	def clear(self):
		# windows
		if name == 'nt':
			_ = system('cls')
		# mac / linux
		else:
			_ = system('clear')

	def display(self):
		for x in range(self.frames[0].shape[0]):
			for y in range(self.frames[0].shape[1]):
				sys.stdout.write(self.conv[self.frames[0][x, y]])
			sys.stdout.write('\n')
		

	def play(self, time = 0):
		while True:
			try:
				self.clear()
				self.display()
				if len(self.frames) == 1:
					self.step(1)
				self.frames = self.frames[1:]
				if time != 0:
					sleep(time)
			except KeyboardInterrupt:
				break
