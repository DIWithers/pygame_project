# We will put all main game functions here
import sys
import pygame

def check_events(hero):
	for event in pygame.event.get(): #run through all pygame events
		if event.type == pygame.QUIT:
			sys.exit() #quit
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				hero.moving_right = True
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT: #right arrow
				hero.moving_right = False
			if event.key == pygame.K_LEFT: #left arrow
				hero.moving_left = False
			#note to self, add top and bottom

#Handle all the screen updates and drawing
def update_screen(settings, screen, hero):
	screen.fill(settings.bg_color) #fill screen with bg_color
	hero.draw_me() #call the draw method and put the hero on the screen
	pygame.display.flip()