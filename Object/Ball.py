import pygame
from Utillity.Colors import *
import numpy

class Ball(pygame.Rect):
    def __init__(self, size, x=0, y=0):
        #부모 생성자 호출
        super().__init__(x,y,size,size)
        # 색
        self.color = WHITE
        # 기본 속도
        self.Base_Speed = 5
        # 축 속도
        self.Speed_X = 0
        self.Speed_Y = 0
        #최대 범위 0~
        self.Max_Range_X = None
        self.Max_Range_Y = None
        #발사 준비
        self.Is_Ready = True
        #죽음
        self.Is_Dead = False

    # 발사
    def Shot(self, keys):
        # 발사 준비 상태라면
        if self.Is_Ready:
            # 스페이스바가 눌렸을 경우
            if keys[pygame.K_SPACE] == True:
                self.Speed_Y = -self.Base_Speed * numpy.cos(45)

                # ranint의 범위는 0~1 => False or True
                if numpy.random.randint(0,2):
                    self.Speed_X = self.Base_Speed * numpy.sin(45)
                else:
                    self.Speed_X = -self.Base_Speed * numpy.sin(45)
                #발사 준비 상태 해제
                self.Is_Ready = False

    # 이동
    def Move(self):
        # 각 축에 속도를 더함
        self.x += self.Speed_X
        self.y += self.Speed_Y

        # 최대 X 범위가 지정되었을 경우
        if self.Max_Range_X != None:
            # 왼쪽 벽과 충돌 시
            if self.x <= 0:
                self.Speed_X = -self.Speed_X
                self.x = 0
            # 오른쪽 벽과 충돌 시
            if self.x >= self.Max_Range_X-self.w:
                self.Speed_X = -self.Speed_X
                self.x = self.Max_Range_X-self.w
        # 최대 Y범위가 지정되었을 경우
        if self.Max_Range_Y != None:
            #천장과 충돌 시
            if self.y <=0:
                self.Speed_Y = -self.Speed_Y
            #바닥과 충돌 시
            if self.y >= self.Max_Range_Y-self.h:
                #죽음
                self.Dead()
    
    # 죽었을 경우
    def Dead(self):
        self.Is_Ready = True
        self.Is_Dead = True
    
    # 위치 및 속도 초기화
    def Reset(self, pad):
        self.Speed_X = 0
        self.Speed_Y = 0
        self.x = pad.centerx-self.w/2
        self.y = pad.y-self.h
        
    # 그리기
    def Draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.width/2)

