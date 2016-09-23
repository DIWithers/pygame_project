import pygame
from pygame.sprite import Sprite #already available in pygame

class Bullet(Sprite):
	def __init__(self, screen, hero, game_settings):
		#bullet settings defined in settings.py
		super(Bullet, self).__init__()
		self.screen = screen

		self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height) #Make a bullet
		self.rect.centerx = hero.rect.centerx #align with hero
		self.rect.top = hero.rect.top #align with hero
		self.color = game_settings.bullet_color
		self.speed = game_settings.bullet_speed
		self.y = float(self.rect.y)

	def update(self):
		self.y -= self.speed
		self.rect.y = self.y #update rect position

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)