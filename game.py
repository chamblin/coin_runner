import os, sys
import pygame
from pygame.locals import *
from utility import *
from background import Background
from coin import Coin
from hero import Hero
from hud import HUD
from globals import Globals

if not pygame.font: print "Warning: fonts disabled"
if not pygame.mixer: print "Warning: sound disabled"
	
class Game:
	def __init__(self):
		pygame.init()
		self.__screen = None
		self.__background = None
		self.__coins = None
		self.__hero = None
		self.__hero_group = None
		self._setup_screen()
		
	def run(self):
		self._screen().blit(self._background(), (0, 0))
		pygame.display.flip()
		clock = pygame.time.Clock()
		while 1:
			clock.tick()
			
			self._draw_background()
			self._draw_hero()
			self._draw_coins()
			self._draw_hud()
			
			pygame.display.flip()
			
			
			for event in pygame.event.get():
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					return
				elif event.type == KEYDOWN:
					self.hero().handle_keydown(event.key)
				elif event.type == KEYUP:
					self.hero().handle_keyup(event.key)
	
	def _draw_background(self):
		self._screen().blit(self._background(), (0, 0))
	
	def _draw_hero(self):
		heroes = self.hero_group()
		heroes.update(pygame.time.get_ticks(), self.coins().sprites())
		heroes.draw(self._screen())
	
	def _draw_coins(self):
		coins = self.coins()
		coins.update(pygame.time.get_ticks())
		coins.draw(self._screen())
		
	def _draw_hud(self):
		hud = HUD(self._screen())
		hud.set_score(self.hero().score())
		hud.draw()
		
	def hero(self):
		if self.__hero is None:
			self.__hero = Hero((300, 400))
		return self.__hero
	
	def hero_group(self):
		if self.__hero_group is None:
			self.__hero_group = pygame.sprite.RenderUpdates((self.hero()))
		return self.__hero_group
		
	def coins(self):
		if self.__coins is None:
			coins = []
			coin1 = Coin((450, 550))
			coin2 = Coin((75, 83))
			self.__coins = pygame.sprite.RenderUpdates((coin1, coin2))
		return self.__coins
		
	
	def _background(self):
		if self.__background is None:
			self.__background = pygame.Surface(self._screen().get_size())
			self.__background = self.__background.convert()
			bg = Background(self.__background)
			bg.fill()
		return self.__background
	
	def _screen(self):
		if self.__screen is None:
			self.__screen = pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT))
		return self.__screen
	
	def _setup_screen(self):
		self._screen()
		pygame.display.set_caption("Coin Runner")
		self._background()

game = Game()
game.run()