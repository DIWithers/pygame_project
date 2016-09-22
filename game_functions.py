# We will put all main game functions here
import sys
import pygame

def check_events():
	for event in pygame.event.get(): #run through all pygame events
		if event.type == pygame.QUIT:
			sys.exit() #quit
		elif event.type == pygame.KEYDOWN:
			if event.key -- pygame.K_RIGHT:
				hero.rect.centerx += 10
			elif event.key == pygame.K_LEFT:
				hero.rect.centerx -= 10
#Handle all the screen updates and drawing
def update_screen(settings, screen, hero):
	screen.fill(settings.bg_color) #fill screen with bg_color
	hero.draw_me() #call the draw method and put the hero on the screen
	pygame.display.flip()