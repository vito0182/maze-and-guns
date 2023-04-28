import pygame
from pygame.locals import *
from settings import *
import maze_generator
import pygame._sdl2

from  level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

window = pygame._sdl2.Window.from_display_module()
renderer = pygame._sdl2.Renderer.from_window(window)

maze = maze_generator.Maze(30, 30)

map = maze.track_unvisited()

map[0][0] = "P"

level = Level(map, screen)

while True:


	for event in pygame.event.get():
		if event.type == QUIT or pygame.key.get_pressed()[K_q]:
			pygame.quit()
			quit()

	screen.fill("#7ac014")

	level.run()

	pygame.display.update()
	print(clock.get_fps())
	clock.tick(60)
