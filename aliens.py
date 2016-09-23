import pygame
from pygame.sprite import Sprite
from hero import Hero
import random

class Alien(Sprite):
	def __init__(self, screen, game_settings):
		super(Alien, self).__init__()
		self.screen = screen

		self.image = pygame.image.load("images/fire_eye_alien.png")
		self.rect = self.image.get_rect()
		self.speed = game_settings.alien_speed
		self.y = float(self.rect.y)
		print self.y
		#make random x...to do
		self.x = ((random.random() * 800))
		self.rect.x = self.x
		print self.x


	def update(self):
		self.y += self.speed
		self.rect.y = self.y
		

		#chase ...
		# dx = self.rect.x - hero.rect.x
		# dy = self.rect.y - hero.rect.y
		# dist = math.hypot(dx, dy)
		# dx = dx / dist
		# dy = dy / dist
		# self.rect.x -= dx * speed
		# self.rect.y -= dy * speed

	

	def draw_alien(self):
		self.screen.blit(self.image, self.rect)

	# def add_alien(screen, game_settings):
	# 	new_alien = Alien(screen, game_settings)
	# 	aliens.add(new_alien)



