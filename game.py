import sys # we will need the user to be able to quit
import pygame #imports package with all available pygame modules
from hero import Hero #bring in the hero class with all it's methods and glory
from settings import Settings

#Set up the main core function
def run_game():
	pygame.init() #initializes pygame modules
	game_settings = Settings()
	screen_size = (1000, 800)
	# screen = pygame.display.set_mode((1000, 800)) #set screen size, need double parenthesis, or set width and height to variable
	screen = pygame.display.set_mode(game_settings.screen_size)
	pygame.display.set_caption("Monster Attack") #set msg on status bar

	bg_color = (82, 111, 53) #green grass color

	hero = Hero(screen) #set variable equal to the class and pass it to the screen

	while 1: #1 is true, run this loop forever...
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#fill the background(bg) with our green
		screen.fill(game_settings.bg_color)
		hero.draw_me() #call the draw method and put the hero on the screen
		pygame.display.flip()


run_game() #start the game
