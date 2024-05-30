import pygame as pg

class Click_Rect(pg.Rect):
    def __init__(self, x, y, w, h):
        super().__init__(int(x), int(y), w, h)
        self.Color = pg.Color(255,255,255)
        self.Clicked_Color = pg.Color(0,0,0)
        self.Clicked = False
    
    def Is_Hoverd(self, mouseX, mouseY):
        if mouseX <= self.x + self.w and self.x <= mouseX:
            if mouseY <= self.y + self.h and self.y <= mouseY:
                return True
        return False