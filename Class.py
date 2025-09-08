
from pygame import*
class GameSprite():
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def show(self,windows):
        windows.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height, id):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.id = id
    def move(self):
        if self.id == 1:
            self.update_l()
        else:
            self.update_r()
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.speed_x = 3
        self.speed_y = 3
        self.j1points = 0
        self.j2points = 0
    def update(self,window_width, window_height, player1, player2):
        self.bounce(window_width, window_height, player1, player2)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def bounce(self,window_width, window_height, player1=None, player2=None):
        bounce_sound = mixer.Sound('Ping sound.wav')
        if self.rect.y+self.rect.width/2 > window_height or self.rect.y-self.rect.width/2 < 0:
            self.speed_y *= -1
            bounce_sound.play()
        if sprite.collide_rect(self, player1.rect) or sprite.collide_rect(self, player2.rect):
            self.speed_x *= -1
            bounce_sound.play()
    def reset(self):
        self.rect.x = 200
        self.rect.y = 200
        self.speed_x *= -1
        self.speed_y *= 1
    def score(self, window_width):
        if self.rect.x < 0:
            self.j2points += 1
            self.reset()
        if self.rect.x > window_width:
            self.j1points += 1
            self.reset()
    def show_score(self, window, font):
        score1 = font.render("Score: " + str(self.j1points), True, (255, 255, 255))
        score2 = font.render("Score: " + str(self.j2points), True, (255, 255, 255))
        window.blit(score1, (10, 10))
        window.blit(score2, (window.get_width() - score2.get_width() - 10, 10))

