import pygame as pg

class Button():
	"""
	Represents a button on the user interface.

	Attributes:
		text: the text that will be displayed on the button.
		x: the x position of the button.
		y: the y position of the button.
		mouse_is_clicked: a boolean value that tracks whether or not the mouse IS clicked, default = False.
		mouse_was_clicked: a boolean value that tracks whether or not the mouse WAS clicked, default = False.
"""
	
	def __init__(self, text, x, y):
		"""
		Constructor for the Button class
		"""
		self.text = text
		self.x = x
		self.y = y
		self.mouse_is_clicked = False
		self.mouse_was_clicked = False

	def draw_button(self, screen):
		"""
		Method that draws a button to the screen, based on its x,y Attributes.

		Parameters:
			screen: the pygame display that the button is drawn to.
		"""
		mouse = pg.mouse.get_pos()
		font = pg.font.Font('freesansbold.ttf', 20)
		text = font.render(self.text, True, (120,130,135))
		textRect = text.get_rect()
		textRect.center = (self.x+100, self.y+50)
		screen.blit(text, textRect)
		pg.draw.rect(screen, (20, 20, 20),(self.x,self.y,185,90),2)
		if(self.is_mouse_on_button()):
			pg.draw.rect(screen, (204, 204, 255),(self.x-7.5,self.y-5,200,100),8)


	def is_mouse_on_button(self):
		"""
		Method that determines whether or not the mouse is hovering over the button based on the 
		button's and mouse's x,y Attributes.

			Parameters:
				none.

			Returns:
				True: if the mouse IS hovering over the button.
				False: if the mouse is NOT hovering over the button.
		"""
		mouse = pg.mouse.get_pos()
		if(mouse[0] > self.x and self.y+100 > mouse[1] > self.y):
			return True
		else:
			return False

	def is_mouse_clicked_on_button(self):
		"""
		Method that determines whether or not the mouse has clicked on a button.

			Parameters:
				none.

			Returns:
				True: if the button has beeen clicked.
				False: if the button has not been clicked.
		"""
		mouse = pg.mouse.get_pos()
		click = pg.mouse.get_pressed()
		if(self.is_mouse_on_button()):
			self.mouse_is_clicked = click[0] == 1
			if (not self.mouse_is_clicked and self.mouse_was_clicked):
				self.mouse_was_clicked = False
				return True
			elif (self.mouse_is_clicked):
				self.mouse_was_clicked = True
				return False
		return False