import pygame as pg
class Nickname_input():
    def __init__(self):
        self.font = pg.font.Font(None, 32)
        self.text = ''
        self.rect = pg.Rect(0, 0,140, 32)
        self.rect_color = pg.Color("white")

    def Render(self, surface, x, y):
        self.text_surface = self.font.render(self.text, True, (255,255,255))
        self.rect.x = x
        self.rect.y = y
        self.rect.w = self.text_surface.get_width() + 10
        pg.draw.rect(surface, self.rect_color, self.rect, 2)
        surface.blit(self.text_surface, (x+5, y+5))
    

       
