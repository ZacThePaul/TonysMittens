import pygame as pg
import config as c
import coordinate_holder as ch
import os
import items


class Player:

	def __init__(self, surface, x, y, direction='right'):
		self.x = x
		self.y = y
		self.velocity = 8
		self.surface = surface
		self.animations = ['char.png', 'char_move_1.png', 'char_move_2.png']
		self.is_moving = False
		self.direction = direction
		self.equipped_item = ''
		self.inventory = {}

	def make_player(self, x=None, y=None, animation=0):

		# Need to update master coordinate list in order to get accurate collision detection #
		ch.master_coordinates['player']['x'] = self.x
		ch.master_coordinates['player']['y'] = self.y

		image = pg.image.load(os.path.join(self.animations[animation]))
		image_rect = image.get_rect()

		fatimg = pg.transform.scale(image, (image_rect[2] * 3, image_rect[3] * 3))

		if self.direction == 'right':
			fatimg = pg.transform.flip(fatimg, True, False)
			self.surface.blit(fatimg, (x, y))
		elif self.direction == 'left':
			self.surface.blit(fatimg, (x, y))

		if len(self.equipped_item) > 1:
			equipped_item_sprite = pg.image.load(os.path.join(items.item_dict[self.equipped_item]['sprite']))
			self.surface.blit(equipped_item_sprite, (x + 10, y + 15))

	def add_to_inventory(self, item_key, item_dict):

		# This function needs to return the item that needs to be removed from the flow of the game #
		# So when the player picks it up, it disappears from the map #

		if item_key in self.inventory:
			self.inventory[item_key]['quantity'] += 1
		elif item_key not in self.inventory:
			self.inventory[item_key] = item_dict

		return item_key

	def pickup_item(self, item, item_attributes):
		self.inventory[item] = item_attributes
		return item

	def equip_hotbar_item(self, selection):
		for item in self.inventory:
			self.inventory[item]['equipped'] = False
		self.inventory[list(self.inventory)[selection]]['equipped'] = True
		self.equipped_item = list(self.inventory)[selection]
