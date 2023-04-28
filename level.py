import pygame
from entities import *
from settings import *
from tiles import *
import os
import math


class Level:
	def __init__(self, level_data, surface):
		self.display_surface = surface
		self.setup_level(level_data)
		self.world_shift = [0, 0]

		self.current_x = 0

		self.desired_screen_position = [screen_width/2, screen_height/2]

	def setup_level(self, map):
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()

		for row_index, row in enumerate(map):
			for col_index, cell in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size

				if cell == "X":
					tile = Tile((x, y), tile_size)
					self.tiles.add(tile)

				if cell == "P":
					player = Player((x, y))
					self.player.add(player)

	def scroll_x(self):
		player = self.player.sprite
		player_centerx = player.rect.centerx

		relative_position_x = (player_centerx - self.desired_screen_position[0])/20

		if relative_position_x < 0:
			player.rect.centerx -= math.floor(relative_position_x)
			self.world_shift[0] = math.floor(relative_position_x)
		else:
			player.rect.centerx -= math.ceil(relative_position_x)
			self.world_shift[0] = math.ceil(relative_position_x)

	def scroll_y(self):
		player = self.player.sprite

		relative_position_y = (player.rect.centery -
							   self.desired_screen_position[1])/10

		if relative_position_y < 0:
			player.rect.centery -= math.floor(relative_position_y)
			self.world_shift[1] = math.floor(relative_position_y)

		else:
			player.rect.centery -= math.ceil(relative_position_y)
			self.world_shift[1] = math.ceil(relative_position_y)

	def get_collisions(self, rect):
		collisions = []
		for tile in self.tiles.sprites():
			if tile.rect.colliderect(rect):
				collisions.append(tile)
		return collisions


	def x_collisions(self):
		player = self.player.sprite

		player.rect.centerx += player.movement[0] * player.vel

		collisions = self.get_collisions(player.rect)

		for tile in collisions:
			if player.movement[0] > 0:
				player.rect.right = tile.rect.left
			elif player.movement[0] < 0:
				player.rect.left = tile.rect.right

	def y_collisions(self):
		player = self.player.sprite

		player.rect.centery += player.movement[2] * player.vel

		collisions = self.get_collisions(player.rect)

		for tile in collisions:

			if player.movement[2] > 0:
				player.rect.bottom = tile.rect.top

			elif player.movement[2] < 0:
				player.rect.top = tile.rect.bottom

	def run(self):

		self.player.update()
	

		self.x_collisions()
		self.scroll_x()
		self.tiles.update(x=self.world_shift[0])

		self.y_collisions()
		self.scroll_y()
		self.tiles.update(y=self.world_shift[1])

		self.tiles.draw(self.display_surface)
		self.player.draw(self.display_surface)


if __name__ == "__main__":
	os.system("python main.py")
