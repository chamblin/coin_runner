from utility import *
import pygame
from globals import Globals
import mobile

import random

class Monster(mobile.Mobile):
	def __init__(self, pos, **kwargs):
		super(Monster, self).__init__(pos, **kwargs)
		
	def update(self, t):
		if t - self._last_update > self._delay:
			self._next_frame()
			self._last_update = t
		if self._moving:
			self._move_rect()
		self._handle_movement(t)
		
	def _handle_movement(self, t):
		pass
			
	def _images(self):
		pass
		
	def _face_random_direction(self):
		a = [Monster.FACING_LEFT, Monster.FACING_RIGHT, Monster.FACING_UP, Monster.FACING_DOWN]
		a.remove(self._facing)
		random.shuffle(a)
		self.face(a[0])