import pygame
from Utillity.Colors import *

class Pad(pygame.Rect):
    def __init__(self, x, y, w, h):
        # 부모 생성자 호출
        super().__init__(x,y,w,h)
        # 색
        self.color = WHITE
        # 최대 X 범위
        self.Max_Range_X = None

    # 키보드 이동
    def Move_Keyboard(self, keys):
        # 키에 따라 이동
        # 왼쪽(-X) 이동시 : (0 - 1)*10 = -1*10 = -10
        # 오른쪽(X) 이동시: (1 - 0)*10 = 1*10 = 10
        self.x += (keys[pygame.K_d] - keys[pygame.K_a]) * 10
        
        # 최대 X 범위가 지정되었을 경우
        if self.Max_Range_X != None:
            # 왼쪽 벽에 충돌한 경우
            if self.x < 0:
                self.x = 0
            # 오른쪽 벽에 충돌한 경우
            if self.x > self.Max_Range_X-self.w:
                self.x = self.Max_Range_X-self.w
    # 그리기
    def Draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.w, self.h])