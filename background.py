import itertools
from utility import *
from pygame import *

class Background:
	def __init__(self, surface):
		self.__surface = surface
		self.__image = None
		
	def fill(self):
		self.surface().fill((255, 50, 50))
		for x,y in itertools.product(range(0, self.surface().get_width(), self.image().get_width()),
		                             range(0, self.surface().get_height(), self.image().get_height())):
			self.surface().blit(self.image(), (x, y))
		
	def image(self):
		if self.__image is None:
			self.__image = load_image("grass.png")[0].convert()
		return self.__image
	
	def surface(self):
		return self.__surface
		