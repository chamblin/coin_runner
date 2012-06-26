from utility import *
import pygame
from globals import Globals
import mobile

class Hero(mobile.Mobile):
	def __init__(self, pos, **kwargs):
		super(Hero, self).__init__(pos, **kwargs)
		
		self._frames = None
		
		self.__walking_sounds = None
		self.__walking_step = 0
		
		self.__score = 0
	
	def handle_keydown(self, key):
		if key in self._keys().keys():
			self.face(self._keys()[key])
			self.start_moving()
		
	def handle_keyup(self, key):
		if key in self._keys().keys() and (self._keys()[key] == self._facing):
			self.stop()
		
	def _keys(self):
		return { K_DOWN : Hero.FACING_DOWN,
		         K_UP : Hero.FACING_UP,
		         K_LEFT : Hero.FACING_LEFT,
		         K_RIGHT : Hero.FACING_RIGHT }
		
	def score(self):
		return self.__score
		
	def update(self, t, collidables):
		if t - self._last_update > self._delay:
			self._next_frame()
			self._last_update = t
		if self._moving:
			self._move_rect()
			#self._walking_sound().play()
		self.check_for_collisions(collidables)
	
	def check_for_collisions(self, collidables):
		_collisions = self._collided_sprites(collidables)
		if len(_collisions) > 0:
			for sprite in _collisions:
				if type(sprite).__name__ == "Coin":
					sprite.pickup()
					self.__score += 100
		
	def _collided_sprites(self, collidables):
		indices = self.rect.collidelistall([collidable.hit_rect() for collidable in collidables])
		return [collidables[i] for i in indices]
	
	def _walking_sound(self):
		if self.__walking_sounds is None:
			self.__walking_sounds = [load_sound(sound_file) for sound_file in ["step_sound1.wav", "step_sound2.wav"]]
		self.__walking_step = (self.__walking_step + 1) % len(self.__walking_sounds)
		return self.__walking_sounds[self.__walking_step]
		
	def _images(self):
		if self._frames is None:
			self._frames = load_sliced_sprites("hero.png", 64, 64)
		if self._moving:
			return self._frames[self._facing][1:]
		else:
			return self._frames[self._facing][0:1]
			