from utility import *
import pygame

class Coin(pygame.sprite.Sprite):
	def __init__(self, pos, fps=10):
		pygame.sprite.Sprite.__init__(self)
		self.__images = None
		
		self._start = pygame.time.get_ticks()
		self._delay = 1000 / fps
		self._last_update = 0
		self._frame = -1
		
		self._next_frame()
		self.rect = self.image.get_rect()
		self.rect.midtop = pos
		
		self.__sound = None
		
	def update(self, t):
		if t - self._last_update > self._delay:
			self._next_frame()
			self._last_update = t
	
	def hit_rect(self):
		return self.rect.inflate(-15, -15)
	
	def _next_frame(self):
		self._frame += 1
		if self._frame >= len(self._images()):
			self._frame = 0
		self.image = self._images()[self._frame]
		
	def _images(self):
		if self.__images is None:
			self.__images = load_sliced_sprites("coin.png", 32, 32)[0]
		return self.__images
		
	def pickup(self):
		self._sound().play()
		self.kill()
		
	def _sound(self):
		if self.__sound is None:
			self.__sound = load_sound("coin_pickup.wav")
		return self.__sound