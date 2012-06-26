import os, sys
from pygame import *
import pygame

def asset_filename(name):
	return os.path.join('assets', name)

def load_image(name, colorkey=None):
	fullname = asset_filename(name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print "Cannot load image: ", name
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image, image.get_rect()
		
def load_sound(name):
	class NoneSound:
		def play(self): pass
	if not pygame.mixer:
		return NoneSound
	fullname = asset_filename(name)
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error, message:
		print "Cannot load sound: ", name
		raise SystemExit, message
	return sound
	
def load_sliced_sprites(filename, w, h):
	'''
	Specs :
	Master can be any height.
	Sprites frames width must be the same width
	Master width must be len(frames)*frame.width
	Assuming you ressources directory is named "ressources"
	'''
	images = []
	master_image = load_image(filename, -1)[0].convert()

	master_width, master_height = master_image.get_size()
	for j in xrange(int(master_height/h)):
		row = []
		for i in xrange(int(master_width/w)):
			row.append(master_image.subsurface((i*w,j*h,w,h)))
		images.append(row)
	return images