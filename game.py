import pygame #imports package with all available pygame modules
from hero import Hero #bring in the hero class with all it's methods and glory
from aliens import Alien
from settings import Settings
import game_functions as gf #aliased with 'gf' 
from pygame.sprite import Group, groupcollide
from start_button import Play_button
from score_board import Score_board
import threading

#Set up the main core function
def run_game():
	pygame.init() #initializes pygame modules
	game_settings = Settings()#create instance of settings class
	# screen = pygame.display.set_mode((1000, 800)) #set screen size, need double parenthesis, or set width and height to variable
	screen = pygame.display.set_mode(game_settings.screen_size)
	pygame.display.set_caption("Alien Attack") #set msg on status bar
	hero = Hero(screen) #set variable equal to the class and pass it to the screen

	pygame.mixer.music.load("sounds/music.wav")
	pygame.mixer.music.play(-1)

	play_button = Play_button(screen, "PLAY")
	score_board = Score_board(screen, "Score = ")
	bullets = Group() #set the bullets to group
	aliens = Group()

	

	# def set_interval(func, sec):
	# 	def func_wrapper():
	# 		set_interval(func, sec)
	# 		func()
	# 	t = threading.Timer(sec, func_wrapper)
	# 	t.start()
	# 	return t
	tick = 0
	def setInterval(interval, time = -1):
		def outer_wrap(function):
			def wrap(*args, **kwargs):
				stop = threading.Event()
				def inner_wrap():
					i = 0
					while i != times and not stop.isSet():
						stop.wait(interval)
						function(*args, **kwargs)
						i += 1
				t = threading.Timer(0, inner_wrap)
				t.daemon = True
				t.start()
				return stop
			return wrap
		return outer_wrap



	@setInterval(5)
	def add_alien(screen, game_settings, aliens):
		print "SPAWNING!!!!!"
		new_alien = Alien(screen, game_settings)
		# aliens.add(Alien(screen, game_settings))
		aliens.add(new_alien)

	
	
	while 1: #1 is true, run this loop forever...
		gf.check_events(hero, bullets, game_settings, screen, aliens, play_button, score_board)
		gf.update_screen(game_settings, screen, hero, bullets, aliens, play_button, score_board) #call method to update screen

		if game_settings.game_active:
			hero.update() #update the hero flags
			bullets.update()
			aliens.update()
			tick += 1
			if tick % 30 == 0:
				aliens.add(Alien(screen, game_settings))
			theDict = groupcollide(aliens, bullets, True, True)
			# print theDict
			
			if (theDict): # if theDict not empty
				game_settings.score = len(theDict)
			


			#fill the background(bg) with our color
			gf.update_screen(game_settings, screen, hero, bullets, aliens, play_button, score_board) #call method to update screen
			#get rid of bullets that are off the screen
			for bullet in bullets:
				if bullet.rect.bottom <= 0: #bullet bottom is at the top of the screen
					bullets.remove(bullet) #call remove against the group


run_game() #start the game
