import pygame
from pygame.locals import *
import math

class Player(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		self.image = pygame.Surface((64, 64))
		self.image.fill("blue")
		self.rect = self.image.get_rect(topleft=pos)

		self.movement = [0,0,0]
		self.vel = 10
		self.diagonal_vel = round(self.vel / math.sqrt(2), 1)
		self.orig_vel = self.vel
		self.last_dash = 0
		self.dash_cooldown = 1000
		self.on_dash = False
		self.gravity = 0.0
		self.max_fall_velocity = 10

		self.on_ground = False
		self.on_ceiling = False
		self.on_right = True
		self.on_left = False


	def get_input(self):

		key = pygame.key.get_pressed()

		if key[K_a] and key[K_d]:
			self.movement[0] = 0
		elif key[K_a]:
			self.movement[0] = -1
		elif key[K_d]:
			self.movement[0] = 1
		else:
			self.movement[0] = 0

		if key[K_w] and key[K_s]:
			self.movement[2] = 0
		elif key[K_w]:
			self.movement[2] = -1
		elif key[K_s]:
			self.movement[2] = 1
		else:
			self.movement[2] = 0

		if (key[pygame.K_a] and (key[pygame.K_w] or key[pygame.K_s])) or (key[pygame.K_d] and (key[pygame.K_w] or key[pygame.K_s])):

			if not self.diagonal:
				self.vel = self.diagonal_vel
				self.diagonal = True

		else:
			self.diagonal = False
			if not self.on_dash:
				self.vel = self.orig_vel


	def apply_gravity(self):

		self.movement[1] += self.gravity
		if self.movement[1] > 15:
			self.movement[1] = 15
		self.rect.centery += self.movement[1]

	
	def update(self):

		self.apply_gravity()

		self.get_input()

		print(self.vel)

