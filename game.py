import pygame as pg 
import config as c
import os
import map as m
import HUD.hud as hud
from player import Player
import coordinate_holder as ch
from entity import Entity
from items import item_dict
import math
import projectile


class Game:

	def __init__(self):
		pg.init()

		self.clock = pg.time.Clock()

		self.screen = pg.display.set_mode((c.window_width, c.window_height))
		self.caption = pg.display.set_caption(c.window_title)

		background_surface = pg.Surface((c.window_width, c.window_height))
		# m.generate_tiles(background_surface)

		self.running = True

		self.time_elapsed = 0

		moving_animation = 1

		character = Player(self.screen, ch.master_coordinates['player']['x'], ch.master_coordinates['player']['y'])

		shot = False
		click_coords = []
		bullet_coords = []

		bullets = []

		is_bg_drawn = False

		while self.running:

			pg.display.set_caption(str(self.clock.get_fps()))

			self.time_elapsed += 1

			# checking pressed keys
			keys = pg.key.get_pressed()
			mouse = pg.mouse.get_pos()

			for event in pg.event.get():

				if event.type == pg.QUIT:
					self.running = False

				if event.type == pg.MOUSEBUTTONUP:
					shot = True

					bullets.append(projectile.Projectile(character.x + 10, character.y + 10, 40, self.screen, (mouse[0], mouse[1]), (character.x, character.y)))

			# repaints the background <- Why do i need this?
			self.screen.fill((255, 255, 255))

			# self.screen.blit(background_surface, (0, 0))

			direction = 'right'

			if not keys[pg.K_w] or [pg.K_a] or [pg.K_s] or [pg.K_d]:
				character.is_moving = False
			if keys[pg.K_w]:
				character.y -= 8
				character.is_moving = True
			if keys[pg.K_s]:
				character.y += 8
				character.is_moving = True
			if keys[pg.K_a]:
				character.x -= 8
				character.is_moving = True
			if keys[pg.K_d]:
				character.x += 8
				character.is_moving = True
			if keys[pg.K_f]:
				self.collision_detect(character)

			if mouse[0] > character.x + 10:
				character.direction = 'right'
			else:
				character.direction = 'left'

			if keys[pg.K_1]:
				character.equip_hotbar_item(0)

			if keys[pg.K_2]:
				character.equip_hotbar_item(1)

			if keys[pg.K_3]:
				character.equip_hotbar_item(2)

			if shot:
				for bullet in bullets:
					bullet.update_projectile()

			# If the time is a multiple of ten and the player is not moving, move them up by one pixel #
			if self.time_elapsed % 10 == 0 and not character.is_moving:
				character.make_player(character.x, character.y - 3)

			# If the player is moving #
			elif character.is_moving:
				# If the time is a multiple of five run one animation #

				if self.time_elapsed % 3 == 0:
					character.make_player(character.x, character.y, moving_animation)

					if moving_animation > 1:
						moving_animation = 1

					else:
						moving_animation += 1
						character.make_player(character.x, character.y, moving_animation)

			else:
				# character = Player(self.screen, ch.master_coordinates['player']['x'], ch.master_coordinates['player']['y'])
				character.make_player(character.x, character.y)

			# Drawing non-player entities to the surface #
			for entity, entity_attributes in ch.master_coordinates.items():
				if entity != 'player':
					inst_entity = Entity(self.screen, entity_attributes['x'], entity_attributes['y'], item_dict[entity]['icon'], item_dict[entity]['sprite'])

			pg.draw.line(self.screen, c.FIERCE_YELLOW, (character.x + 10, character.y + 10), mouse)

			hud.make_hud(self.screen, character)

			pg.display.update()
			self.time_delta = self.clock.tick(60)

	# This function checks for both actual collision and when entities are near each other #
	def collision_detect(self, player_object):
		broad_detect = 10
		narrow_detect = 0

		# The purpose of the kill list is to remove items that are picked up #
		kill_list = []

		for reference_entity, reference_entity_attributes in ch.master_coordinates.items():
			for entity, entity_attributes in ch.master_coordinates.items():

				ex = entity_attributes['x']
				ey = entity_attributes['y']
				rex = reference_entity_attributes['x']
				rey = reference_entity_attributes['y']

				# Detect if an entity is near another entity #

				if entity != reference_entity:
					if ex + entity_attributes['width'] > rex - broad_detect and ex < rex + reference_entity_attributes['width'] + broad_detect:
						if ey + entity_attributes['height'] > rey - broad_detect and ey < rey + reference_entity_attributes['height'] + broad_detect:

							if entity != 'player':
								killed_item = player_object.pickup_item(entity, item_dict[entity])
								kill_list.append(killed_item)

							if ex + entity_attributes['width'] > rex and ex < rex + reference_entity_attributes['width']:
								if ey + entity_attributes['height'] > rey and ey < rey + reference_entity_attributes['height']:
									print('entity has collided')

		for item in kill_list:
			ch.master_coordinates.pop(item)
			kill_list.remove(item)
