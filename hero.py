import pygame

class Hero(object):
	def __init__(self, screen):
		self.screen = screen #give the hero the ability to control the screen
		#load the hero image, get it's rect
		self.image = pygame.image.load("images/alienblaster.png")
		self.rect = self.image.get_rect() #pygame gives us get_rect on any object so we can get some dims
		self.screen_rect = screen.get_rect()#assign a var so the hero class knows how big and where...
		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen #sety
		self.rect.bottom = self.screen_rect.bottom #setx

		#Set up movement booleans
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	#Keep all updated in the hero class
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 10
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= 10
			#note to self, add top and bottom
		elif self.moving_up and self.rect.top > self.screen_rect.top:
			self.rect.y -= 10
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += 10

	def draw_me(self):
		self.screen.blit(self.image, self.rect) #draw the Surface: (the image/source, the where/dest)
