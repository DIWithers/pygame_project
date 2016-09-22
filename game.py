import pygame #imports package with all available pygame modules
from hero import Hero #bring in the hero class with all it's methods and glory
from settings import Settings
import game_functions as gf #aliased with 'gf' 

#Set up the main core function
def run_game():
	pygame.init() #initializes pygame modules
	game_settings = Settings()#create instance of settings class
	# screen = pygame.display.set_mode((1000, 800)) #set screen size, need double parenthesis, or set width and height to variable
	screen = pygame.display.set_mode(game_settings.screen_size)
	pygame.display.set_caption("Monster Attack") #set msg on status bar
	hero = Hero(screen) #set variable equal to the class and pass it to the screen

while 1: #1 is true, run this loop forever...
	gf.check_events(hero)
	#fill the background(bg) with our green
	gf.update_screen(game_settings, screen, hero) #call method to update screen
	


run_game() #start the game
