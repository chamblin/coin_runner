from utility import *
import pygame
from globals import Globals

class HUD:
	def __init__(self, screen, height=Globals.HUD_HEIGHT):
		self._screen = screen
		self._height = height
		
		self.__surface = None
		
		self.__score = 0
		
	def draw(self):
		self._draw_box()
		self._draw_score(self.__score)
		self._screen.blit(self._surface(), (0, 0))
		
	def set_score(self, new_score):
		self.__score = new_score
	
	def _draw_score(self, score):
		font = pygame.font.Font(asset_filename("pixel-font.ttf"), 16)
		text = font.render("SCORE: %s" % str(score).rjust(10, "0") , 0, (255, 255, 255))
		self._surface().blit(text, (0, 0))
		
	def _draw_box(self):
		pygame.draw.rect(self._screen, (0, 0, 0), self._surface().get_rect())
	
	def _surface(self):
		if self.__surface is None:
			rect = self.__rect()
			self.__surface = Surface((rect.w, rect.h))
		return self.__surface
		
	def __rect(self):
		return pygame.Rect(0, 0, self._screen.get_width(), self._height)