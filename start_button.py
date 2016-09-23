import pygame.font

class Play_button(object):
	def __init__(self, screen, button_text):
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#Set the width, height, size and color of the buttom image
		self.width = 250
		self.height = 100
		self.button_color = 0, 200, 150
		self.text_color = 255, 255, 255

		#set font
		self.font = pygame.font.Font(None, 52 )#(style/None=default, size/pixels)
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center  #button set at center
		self.setup_message(button_text)

	def setup_message(self, button_text):
		#Render the image inside of image message
		self.image_message = self.font.render(button_text, True, self.text_color)
		self.image_message_rect = self.image_message.get_rect()
		self.image_message_rect.center = self.rect.center

	def draw_button(self):	
		#equiv to stroke.fill
		self.screen.fill(self.button_color, self.rect)
		#draw stroke
		self.screen.blit(self.image_message, self.image_message_rect)
