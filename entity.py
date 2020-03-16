import pygame as pg
import config as c
import os


class Entity:

	def __init__(self, surface, x, y, icon, sprite, direction=None):
		self.x = x
		self.y = y
		self.surface = surface
		self.direction = direction
		self.sprite = pg.image.load(os.path.join(sprite))
		self.icon = pg.image.load(os.path.join(icon))
		self.rect = self.icon.get_rect()
		self.make_entity()

	def make_entity(self):
		if self.direction == 'right':
			new_image = pg.transform.flip(self.sprite, True, False)
			self.surface.blit(new_image, (self.x, self.y))
		else:
			self.surface.blit(self.sprite, (self.x, self.y))
