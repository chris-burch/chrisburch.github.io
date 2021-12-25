import pygame

class Archer:
	"""A class to mange the archer."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/archer.bmp')
		self.rect = self.image.get_rect()

		#Start each new archer at the left center of the screen.
		self.rect.midleft = self.screen_rect.midleft

		# Store a decimal value for the archer's veritical position.
		self.y = float(self.rect.y)

		# Movement flag
		self.moving_down = False
		self.moving_up = False

	def update(self):
		"""Update the archer's position based on the movement flags."""
		# Update the ship's y value, not the rect.
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.archer_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.archer_speed

		# Update rect object from self.y.
		self.rect.y = self.y

	def blitme(self):
		"""Draw the archer at its current location."""
		self.screen.blit(self.image, self.rect)


		
