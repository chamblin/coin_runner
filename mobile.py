from utility import *
import pygame
from globals import Globals

class Mobile(pygame.sprite.Sprite):
	FACING_DOWN = 2
	FACING_UP = 0
	FACING_LEFT = 1
	FACING_RIGHT = 3
	
	def __init__(self, pos, **kwargs):
		pygame.sprite.Sprite.__init__(self)
		self._frames = None
		
		self.face(Mobile.FACING_DOWN)
		self.stop()
		
		self._start = pygame.time.get_ticks()
		self._delay = 1000 / kwargs.get('fps', 17)
		self._last_update = 0
		self._frame = -1
		self.__speed = kwargs.get('speed', 2)
		
		self._next_frame()
		self.rect = self.image.get_rect()
		self.rect.midtop = pos
		
	def stop(self):
		self._moving = False
	
	def start_moving(self):
		self._moving = True
		
	def face(self, direction):
		self._facing = direction
		
	def hit_rect(self):
		return self.rect.inflate(-15, -15)
		
	def score(self):
		return self.__score
		
	def update(self, t):
		if t - self._last_update > self._delay:
			self._next_frame()
			self._last_update = t
		if self._moving:
			self._move_rect()

	def _move_rect(self):
		if self._moving:
			newpos = self.rect.move((self._x_movement(), self._y_movement()))
			self.rect = newpos
			
	def _x_movement(self):
		r = 0
		if self._moving:
			if self._facing == Mobile.FACING_LEFT and self.rect.left > 0:
				r = -1		
			elif self._facing == Mobile.FACING_RIGHT and self.rect.right < Globals.WIDTH:
				r = 1
		return r * self.__speed
		
	def _y_movement(self):
		r = 0
		if self._moving:
			if self._facing == Mobile.FACING_DOWN and self.rect.bottom < Globals.HEIGHT:
				r = 1
			elif self._facing == Mobile.FACING_UP and self.rect.top > Globals.HUD_HEIGHT:
				r = -1
		return r * self.__speed
		
	def _next_frame(self):
		self._frame += 1
		if self._frame >= len(self._images()):
			self._frame = 0
		self.image = self._images()[self._frame]
		
	def _images(self):
		return []
