import pygame as pg
import coordinate_holder as ch
from items import item_dict

pg.font.init()

# This is the config file #

# This fits 44 tiles wide and 25 tiles tall = 1100 tiles on screen
window_width = 1408
window_height = 800
window_title = "game"

# Colors #

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (252, 40, 3)
BLUE = (11, 3, 252)
GREEN = (18, 143, 7)
DARK_GREEN = (19, 103, 41)
MOHAGANY = (192, 64, 0)

GREY = (161, 161, 161)
LIGHT_GREY = (174, 176, 174)
DARK_GREY = (102, 102, 102)


FIERCE_YELLOW = (252, 186, 3)

# Fonts #

AMATIC_REG = pg.font.Font("assets/fonts/amatic-reg.ttf", 15)
AMATIC_BOLD = pg.font.Font("assets/fonts/amatic-bold.ttf", 20)

# Tiles #
TILE_WIDTH = 16
TILE_HEIGHT = 16

# Player Information #

stack_limits = {
	'sword': 1,
	'bandage': 3,
}

PLAYER_INVENTORY = {
	# 'bandage': item_dict['bandage']
}
