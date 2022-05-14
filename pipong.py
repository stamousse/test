from pygame import *

class GameSprite(sprite.Sprite):
	def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
		super().__init__()
		self.image = transform.scale(image.load(player_image), (wight, height))
		self.speed = player_speed
		self.rect.x = player_x
		self.rect.y = player_y
		
	def reset(self):
		window.blit(self.image, (self.rect.x, self.rect.y))
		
class Player(GameSprite):
	def update_r(self):
		keys = key.get_pressed()
		if keys[K_UP] and self.rect.y > 5:
			self.rect.y -self.speed
		if keys[K_DOWN] and self .rect.y < win_height - 80:
			self.rect.y += self.speed
	def update_l(self):
		keys = key.get_pressed()
		if keys[K_w] and self.rect.y > 5:
			self.rect.y -self.speed
		if keys[K_s] and self .rect.y < win_height - 80:
			self.rect.y += self.speed

background = (0, 153, 153)
win_width = 1200
win_height = 1000
window = display.set_mode((win_width, win_height))
window.fill(background)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket_1 = Player('racket.png', 60, 400, 8, 100, 300)
racket_2 = Player('racket.png', 1400, 400, 8, 100, 300)
ball = GameSprite('square.png', 540, 400, 8, 100, 100)

font.init()
font = font.Font(None, 35)
win1 = font.render('PLAYER 1 WINS!!!', True, (0, 204, 0))
win2 = font.render('PLAYER 2 WINS!!!', True, (0, 204, 0))

speed_x = 3
speed_y = 3
