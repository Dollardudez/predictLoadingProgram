import pygame as pg

class Button:
	
	def __init__(self, text, x, y):
		self.text = text
		self.x = x
		self.y = y
		self.mouse_is_clicked = False
		self.mouse_was_clicked = False

	def draw_button(self, screen):
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
		mouse = pg.mouse.get_pos()
		if(mouse[0] > self.x and self.y+100 > mouse[1] > self.y):
			return True
		else:
			return False

	def is_mouse_clicked_on_button(self, screen):
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