import pygame
from Utillity.Colors import *
import numpy

class Brick(pygame.Rect):
    def __init__(self, x, y, w, h):
        # 부모 생성자 호출
        super().__init__(x, y, w, h)
        # 랜덤 색상 설정
        self.color = (numpy.random.randint(1,256), numpy.random.randint(1,256), numpy.random.randint(1,256))
        self.item = 0
    # 그리기
    def Draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.w, self.h])

    def Break(self):
        if self.item > 0:
            self.Drop()
    
    def Drop(self):
        pass