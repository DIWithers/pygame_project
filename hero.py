import pygame

class Hero(object):
	def __init__(self, screen):
		self.screen = screen #give the hero the ability to control the screen
		#load the hero image, get it's rect
		self.image = pygame.image.load("ball.gif")
		self.rect = self.image.get_rect() #pygame gives us get_rect on any object so we can get some dims
		self.screen_rect = screen.get_rect()#assign a var so the hero class knows how big and where...
		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen #sety
		self.rect.bottom = self.screen_rect.bottom #setx

	def draw_me(self):
		self.screen.blit(self.image, self.rect) #draw the Surface: (the image/source, the where/dest)
