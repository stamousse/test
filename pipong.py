from pygame import *

class GameSprite(sprite.Sprite):
	def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
		super().__init__()
		self.image = transform.scale(image.load(player_image), (wight, height))
		self.speed = player_speed
		self.rect = self.image.get_rect()
		self.rect.x = player_x
		self.rect.y = player_y
		

	def reset(self):
		window.blit(self.image, (self.rect.x, self.rect.y))
		
class Player(GameSprite):
	def update_r(self):
		keys = key.get_pressed()
		if keys[K_UP] and self.rect.y > 5:
			self.rect.y -= self.speed
		if keys[K_DOWN] and self .rect.y < win_height - 80:
			self.rect.y += self.speed
	def update_l(self):
		keys = key.get_pressed()
		if keys[K_w] and self.rect.y > 5:
			self.rect.y -= self.speed
		if keys[K_s] and self .rect.y < win_height - 80:
			self.rect.y += self.speed

background = (255, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(background)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket_1 = Player('racket.png', 40, 200, 4, 50, 100)
racket_2 = Player('racket.png', 625, 200, 4, 50, 100)
ball = GameSprite('square.png', 350, 200, 4, 25, 25)

font.init()
font = font.Font(None, 35)
win1 = font.render('PLAYER 1 WINS!!!', True, (0, 204, 0))
win2 = font.render('PLAYER 2 WINS!!!', True, (0, 204, 0))

speed_x = 3
speed_y = 3

while game:
	for e in event.get():
		if e.type == QUIT:
			game = False
	if finish !=  True:
		window.fill(background)
		racket_1.update_l()
		racket_2.update_r()
		ball.rect.x += speed_x
		ball.rect.y += speed_y
	
		if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
			speed_x *= -1
			speed_y *= 1

		if ball.rect.y > win_height - 50 or ball.rect.y < 0:
			speed_y *= -1

		if ball.rect.x < 0:
			finish = True
			window.blit(win2, (250, 200))
		
		if ball.rect.x > 700:
			finish = True
			window.blit(win1, (250, 200))

	racket_1.reset()
	racket_2.reset()
	ball.reset()

	display.update()
	clock.tick(FPS)
