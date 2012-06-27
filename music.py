import pygame
from utility import *

class Music:
	DEFAULT = "music.mp3"
	
	def __init__(self):
		self.__song = Music.DEFAULT
	
	def play(self):
		pygame.mixer.music.load(asset_filename(self.__song))
		pygame.mixer.music.play(-1)
	
	def stop(self):
		pygame.mixer.music.stop()