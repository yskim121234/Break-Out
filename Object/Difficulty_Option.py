import pygame as pg
from Object.Click_Rect import Click_Rect

class Diff_Option():
    def __init__(self, x, y):
        self.x = x - 100
        self.y = y

        self.font = pg.font.Font(None, 32)

        self.Easy_Rect = Click_Rect(self.x-75, self.y, 100, 75)
        self.Easy_Rect.Color = pg.Color(100,255,100)
        self.Easy_Rect.Clicked_Color = pg.Color(0, 155, 0)

        self.Hard_Rect = Click_Rect(self.x+75, self.y, 100, 75)
        self.Hard_Rect.Color = pg.Color(255,0,0)
        self.Hard_Rect.Clicked_Color = pg.Color(155,0,0)
    
    def Draw(self, surface):
        self.Text_Easy = self.font.render('Easy', True, (255,255,255))

        if self.Easy_Rect.Clicked:
            pg.draw.rect(surface, self.Easy_Rect.Clicked_Color, self.Easy_Rect)
        else:
            pg.draw.rect(surface, self.Easy_Rect.Color, self.Easy_Rect)
        surface.blit(self.Text_Easy, (self.Easy_Rect.x+5, self.Easy_Rect.y+5))


        self.Text_Hard = self.font.render('Hard', True, (255,255,255))

        if self.Hard_Rect.Clicked:
            pg.draw.rect(surface, self.Hard_Rect.Clicked_Color, self.Hard_Rect)
        else:
            pg.draw.rect(surface, self.Hard_Rect.Color, self.Hard_Rect)
        surface.blit(self.Text_Hard, (self.Hard_Rect.x+5, self.Hard_Rect.y+5))