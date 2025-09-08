from pygame import*
class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = Rect(x, y, width, height) #rectangle
      self.fill_color = color


  def color(self, new_color):
      self.fill_color = new_color


  def fill(self,wind):
      draw.rect(wind, self.fill_color, self.rect)
  def outline(self,wind, frame_color, thickness): #outline of an existing rectangle
    draw.rect(wind, frame_color, self.rect, thickness)


  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)


'''class label'''


class Label(Area):
  def set_text(self, text, fsize=8, text_color=(255, 255, 255)):
      self.image = font.SysFont('Arial', fsize).render(text, True, text_color)
 

  def draw(self,wind, shift_x=0, shift_y=0):
      self.fill(wind)
      wind.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
