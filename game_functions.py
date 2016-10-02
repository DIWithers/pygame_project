# We will put all main game functions here
import sys
import pygame
from bullets import Bullet
from aliens import Alien
from score_board import Score_board
from settings import Settings



def check_events(hero, bullets, game_settings, screen, aliens, play_button, score_board):
	for event in pygame.event.get(): #run through all pygame events
		if event.type == pygame.QUIT:
			sys.exit() #quit

		#button handler	
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			# print mouse_x
			# print mouse_y
			if play_button.rect.collidepoint(mouse_x, mouse_y):
				game_settings.game_active = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				hero.moving_right = True
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True
			elif event.key == pygame.K_UP:
				hero.moving_up = True
			elif event.key == pygame.K_DOWN:
				hero.moving_down = True
			elif event.key == pygame.K_SPACE:
				new_bullet = Bullet(screen, hero, game_settings)
				bullets.add(new_bullet)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT: #right arrow
				hero.moving_right = False
			if event.key == pygame.K_LEFT: #left arrow
				hero.moving_left = False
			if event.key == pygame.K_UP:
				hero.moving_up = False
			if event.key == pygame.K_DOWN:
				hero.moving_down = False
			#note to self, add top and bottom
	


#Handle all the screen updates and drawing
def update_screen(settings, screen, hero, bullets, aliens, play_button, score_board):

	
	
	screen.fill(settings.bg_color) #fill screen with bg_color
	score_board.draw_scoreboard(settings)
	score_board.update(settings)
	hero.draw_me() #call the draw method and put the hero on the screen
	for alien in aliens.sprites():
		alien.draw_alien()
	# if len(bullet) < 20: #bullet limit
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#score_board_button.draw_scoreboard

	if not settings.game_active: #game_settings
		play_button.draw_button()
		
		
	pygame.display.flip()