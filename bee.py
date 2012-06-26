from utility import *
import pygame
from globals import Globals
import monster
import random

class Bee(monster.Monster):
	def __init__(self, pos, **kwargs):
		super(Bee, self).__init__(pos, **kwargs)
		self._frames = None
		
		self.start_moving()
		
		self.__going_this_direction_frames = 0
		
	def update(self, t):
		if t - self._last_update > self._delay:
			self._next_frame()
			self._last_update = t
		if self._moving:
			self._move_rect()
		self._handle_movement(t)
		
	def _handle_movement(self, t):
		self._aim(t)
			
	def _images(self):
		if self._frames is None:
			self._frames = load_sliced_sprites("bee.png", 32, 32)
		if self._moving:
			return self._frames[self._facing]
		else:
			return self._frames[self._facing][0:1]
			
	def _aim(self, t):
		if self.__going_this_direction_frames < 30:
			self.__going_this_direction_frames += 1
		if self.__going_this_direction_frames > 3000 or random.random() > 0.96:
			self._face_random_direction()