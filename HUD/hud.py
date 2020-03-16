import pygame as pg
import config as c
import items
import os


def make_hud(surface, player_object):

	pg.font.init()

	hot_bar_rect = pg.Rect(0, 0, 430, 80)
	hot_bar_rect.center = (c.window_width / 2, c.window_height - 50)
	pg.draw.rect(surface, c.MOHAGANY, hot_bar_rect)

	hot_bar_starting_x = hot_bar_rect.left + 10
	hot_bar_starting_y = hot_bar_rect.top + 10

	sword = pg.image.load(os.path.join('sword.png'))
	sword_rect = sword.get_rect()

	xp_bar = pg.draw.line(surface, c.WHITE, (hot_bar_rect.left, hot_bar_rect.top - 11), (hot_bar_rect.right - 1, hot_bar_rect.top - 11), 20)
	xp_amount = pg.draw.line(surface, c.GREEN, (hot_bar_rect.left, hot_bar_rect.top - 11), (hot_bar_rect.left + 100, hot_bar_rect.top - 11), 20)
	xp_level = pg.font.Font.render(c.AMATIC_BOLD, 'Lvl 3', True, c.BLACK)
	surface.blit(xp_level, (hot_bar_rect.left + 5, hot_bar_rect.top - 23))

	# Draws the items in the player's inventory to the hotbar
	for inv_item, inv_item_attribute in player_object.inventory.items():

		this_image = pg.image.load(os.path.join(inv_item_attribute['icon']))
		this_rect = this_image.get_rect()

		# print(inv_item_attribute)

		if inv_item_attribute['equipped']:
			pg.draw.rect(surface, c.FIERCE_YELLOW, (hot_bar_starting_x - 2, hot_bar_starting_y - 2, 64, 64))

		surface.blit(this_image, (hot_bar_starting_x, hot_bar_starting_y))
		item_quantity = pg.font.Font.render(c.AMATIC_BOLD, str(inv_item_attribute['quantity']) + 'x', True, c.WHITE)
		surface.blit(item_quantity, (hot_bar_starting_x + 5, hot_bar_starting_y + 35))
		hot_bar_starting_x += 70
