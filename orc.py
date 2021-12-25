import pygame
from pygame.sprite import Sprite

class Orc(Sprite):
	"""A class to represent a single orc in the band."""

	def __init__(self, ai_game):
		"""Initiialize the alien and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the orc image and set its rect attribute.
		self.image = pygame.image.load('images/Orc.bmp')
		self.rect = self.image.get_rect()

		# Start each new orc near the right of the screen
		self.rect.x = self.rect.height
		self.rect.y = self.rect.width

		#store the orc's exact vertical position
		self.y = float(self.rect.y)

	def update(self):
		"""Move the orc top or down."""
		self.y += (self.settings.orc_speed*self.settings.gang_direction)
		self.rect.y = self.y

	def check_edges(self):
		"""Return True if orc is at the edge of the screen."""
		screen_rect = self.screen.get_rect()

		if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
			return True



