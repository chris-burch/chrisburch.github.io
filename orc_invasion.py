import sys

import pygame

from settings import Settings
from archer import Archer
from arrow import Arrow
from orc import Orc

class OrcInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Orc Invasion")

		self.archer = Archer(self)
		self.arrows = pygame.sprite.Group()
		self.orcs = pygame.sprite.Group()

		self._create_gang()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self.archer.update() 
			self._update_arrows()
			self._update_orcs()
			self._update_screen()
			

	def _check_events(self):
		"""Repsond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_DOWN:
			self.archer.moving_down = True
		elif event.key == pygame.K_UP:
			self.archer.moving_up = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._shoot_arrow()

	def _check_keyup_events(self,event):
		""" Repond to key releases."""
		if event.key == pygame.K_DOWN:
			self.archer.moving_down = False
		elif event.key == pygame.K_UP:
			self.archer.moving_up = False

	def _shoot_arrow(self):
		"""Create a new arrow and add it to the arrow group."""
		if len(self.arrows) < self.settings.arrows_allowed:
			new_arrow = Arrow(self)
			self.arrows.add(new_arrow)

	def _update_arrows(self):
		"""Update the position of arrows and get rid of old arrows."""
		# Update arrow potions.
		self.arrows.update()

		# Get rid of arrows that have disappeared.
		for arrow in self.arrows.copy():
			if arrow.rect.left >= 1400:
				self.arrows.remove(arrow)

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.archer.blitme()
		for arrow in self.arrows.sprites():
			arrow.draw_arrow()
		self.orcs.draw(self.screen)

		pygame.display.flip()

	def _create_gang(self):
		"""Create a gang of q."""
		# Create an orc and find the number of orcs in a row.
		# Spacing between each orc is eqaul to one orc width.
		orc = Orc(self)
		orc_width, orc_height = orc.rect.size
		available_space_y = self.settings.screen_height - (orc_width)
		number_orcs_y = available_space_y // (orc_width)

		# Determine the number of rows of orcs that fit on the screen.
		archer_height = self.archer.rect.height
		available_space_x = (self.settings.screen_width - (orc_height) - archer_height)
		number_rows = available_space_x // (orc_height)

		# Create the full gang of orcs.
		for row_number in range(number_rows):
			for orc_number in range(number_orcs_y):
				self._create_orc(orc_number, row_number)

	def _create_orc(self, orc_number, row_number):
		"""Create an orc and place it in the row."""
		orc = Orc(self)
		orc_width, orc_height = orc.rect.size
		orc.y = orc_width + 1.5* orc_width * orc_number
		orc.rect.y = orc.y
		orc.rect.x = orc.rect.height + orc.rect.height * row_number
		self.orcs.add(orc)

	def _check_gang_edges(self):
		"""Respond appropriately if any orcs have reached an edge."""
		for orc in self.orcs.sprites():
			if orc.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the gangs direction"""
		for orc in self.orcs.sprites():
			orc.rect.y += self.settings.gang_drop_speed
		self.settings.gang_direction *= -1

	def _update_orcs(self):
		"""
		Check if the gang is at an edge,
		then update the positions of all orcs in the gang.
		"""
		self._check_gang_edges()
		self.orcs.update()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = OrcInvasion()
	ai.run_game()
