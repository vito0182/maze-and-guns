import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill("black")
		self.rect = self.image.get_rect(topleft=pos)


	def update(self, x=0,y=0):

		self.rect.centerx -= x
		self.rect.centery -= y