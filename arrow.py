import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
	"""A class to manage arrows fired from the archer"""

	def __init__(self, ai_game):
		"""Create a bullet object at the ship's current position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.arrow_color

		# Create an arrow rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0,0, self.settings.arrow_width, self.settings.arrow_height)
		self.rect.midleft = ai_game.archer.rect.midleft

		#Store the arrow's poition as a decimal value.
		self.x = float(self.rect.x)

	def update(self):
		"""Move the arrow to the right of the screen"""
		# Update the decimal portion of the arrow.
		self.x += self.settings.arrow_speed
		# Update the rect poistion.
		self.rect.x = self.x

	def draw_arrow(self):
		"""Draw the arrow to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)


