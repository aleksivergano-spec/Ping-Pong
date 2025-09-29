from pygame import*
from label  import Label
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
    def update(self,window,temps, player1, player2):
        self.bounce(window,temps, player1, player2)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def bounce(self,window,temps, player1=None, player2=None):
        bounce_sound = mixer.Sound('Ping sound.wav')
        self.score(window, temps)
        if self.rect.y+self.rect.width > window.get_height() or self.rect.y<0:
            self.speed_y *= -1
            bounce_sound.play()
        if self.rect.colliderect( player1.rect) or self.rect.colliderect(player2.rect):
            self.speed_x *= -1
            bounce_sound.play()
    def reset(self, window):
        self.rect.x = window.get_width()/2-self.rect.width/2
        self.rect.y = window.get_height()/2 +self.rect.height/2
        self.speed_x *= -1
        self.speed_y *= 1
    def score(self, window, temps):
        if self.rect.x < 0:
            self.j2points += 1
            self.Show_Text(window,'Player 1 Loose', temps)
            self.reset(window)
        if self.rect.x+self.rect.width > window.get_width():
            self.j1points += 1
            self.Show_Text(window,'Player 2 Loose', temps)
            self.reset(window)
    def Show_Text(self,window=display.set_mode((0,0)), text=str(),temps=int()):
        Text=Label(window.get_width()/2,window.get_height()/2,0,0,(0,0,0))
        Text.set_text(text,100)
        Text.draw(window)
        display.update()
        time.delay(1000*temps)
    def show_score(self, window, fsize):
        score1=Label(10,10, 0, 0, (0,0,0))
        score="Score: " + str(self.j1points)
        score1.set_text(score, fsize)
        score2=Label(window.get_width()-100,10, 0, 0, (0,0,0))
        score="Score: " + str(self.j2points)
        score2.set_text(score, fsize)
        score1.draw(window)
        score2.draw(window)
