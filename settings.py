class Settings:
	"""A class to store all settings for Orc Invasion."""

	def __init__(self):
		""" Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)

		# Archer settings
		self.archer_speed = 1.5

		# Arrow Settings
		self.arrow_speed = 10
		self.arrow_width = 15
		self.arrow_height = 3
		self.arrow_color = (222,184,135)
		self.arrows_allowed = 3

		# Orc Settings
		self.orc_speed = 1.0
		self.gang_drop_speed = 10
		# gang_direction of 1 represents down; - 1 represents up.
		self.gang_direction = 1