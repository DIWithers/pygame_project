import pygame
import pygame.font
from bullets import Bullet 
from hero import Hero 
from aliens import Alien
from settings import Settings

class Score_board(object):
	def __init__(self, screen, score_text):
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.width = 100
		self.height = 50
		self.color = 100, 200, 150
		self.text_color =  255, 255, 255

		self.font = pygame.font.Font(None, 30)
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		# self.rect.x = 50
		# self.rect.y = 20
		self.rect.center = 50, 50
		self.score_message(score_text)

	def score_message(self, score_text):
		self.score_message = self.font.render(score_text, True, self.text_color)
		self.score_message_rect = self.score_message.get_rect()
		self.score_message_rect.center = self.rect.center

	def draw_scoreboard(self, game_settings):
		# self.screen.fill(self.score_board_color, self.rect)
		# self.screen.blit(self.score_message, self.score_message_rect)
		pygame.draw.rect(self.screen, self.color, self.rect) 
		self.screen.blit(self.score_message, self.score_message_rect)
	def update(self, game_settings):
		self.score = game_settings.score
		# print self.score

