import pygame as pg
import coordinate_holder as ch
import math


class Projectile:

	def __init__(self, x, y, speed, surface, mouse_pos, character_pos):

		self.x = x
		self.y = y
		self.speed = speed
		self.is_moving = False
		self.surface = surface
		self.living = True
		self.mouse_pos_on_fire = mouse_pos
		self.character_on_fire = character_pos
		self.image = pg.image.load('arrow.png').convert_alpha()

	def update_projectile(self):

		if self.living:

			x = self.mouse_pos_on_fire[0] - self.character_on_fire[0]
			y = self.mouse_pos_on_fire[1] - self.character_on_fire[1]

			angle = math.atan2(y, x)

			self.x += math.cos(angle) * self.speed
			self.y += math.sin(angle) * self.speed

			rotation = math.degrees(math.atan2(self.mouse_pos_on_fire[1] - self.character_on_fire[1], self.mouse_pos_on_fire[0] - self.character_on_fire[0])) + 180
			rot_image = pg.transform.rotate(self.image, 360 - angle * 60)

			self.surface.blit(rot_image, (round(self.x), round(self.y)))

	# def kill_self(self):


