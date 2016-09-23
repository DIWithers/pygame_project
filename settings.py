#A place for settings...
class Settings():
	def __init__(self):
		self.screen_size = (1000, 800)
		self.bg_color = (0, 0 , 50)
		# (82, 111, 53) #green grass color
		self.bullet_speed = 5 #pixels
		self.bullet_width = 5
		self.bullet_height = 20
		self.bullet_color = 100, 200 , 100
		self.alien_speed = 2
		self.mans_left = 3
		self.game_active = False #init game as not active

