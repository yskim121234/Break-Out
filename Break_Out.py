import pygame as pg
from Utillity.Colors import *
from Object.Ball import *
from Object.Pad import Pad
from Object.Brick import Brick
import numpy as np

def Dead():
    if len(health) <= 0:
        running = False
    else:
        health.pop()

#초기화
pg.init()
pg.display.init()

#화면 세팅
pg.display.set_caption("Break Out")
display = pg.display.set_mode([600, 800])

# 게임 실행 변수 초기화
running = True
clock = pg.time.Clock()

# 패드 생성 및 초기화
pad = Pad(0, 765, 200, 25)
pad.Max_Range_X = display.get_width()

# 공 생성 및 초기화
ball = Ball(25, 0, 0)
ball.Max_Range_X = display.get_width()
ball.Max_Range_Y = display.get_height()

# 벽돌 리스트 선언
bricks = []

# 스코어 보드 설정 및 변수 초기화
scoreboard = pg.font.SysFont(None, 30)
score = 0

# 체력 리스트 및 아이콘 생성
health = [pg.Rect(5+2.5*i+i*10, 30, 10, 10) for i in range(3)]

# 스테이지 관련 변수 초기화
stage = 0
clear = True

# 디버깅 모드 변수
debug = False

#게임 루프
while running:
    # 초당 100번의 Tick
    clock.tick(100)

    # 이벤트 루프
    for event in pg.event.get():
        # 윈도우의 X 버튼을 눌렀을 경우
        if event.type == pg.QUIT:
            running = False
        else:
            # 키가 눌렸을 경우
            if event.type == pg.KEYDOWN:
                # 그 키가 ESC일 경우
                if event.key == pg.K_ESCAPE:
                    running = False
                # 그 키가 왼쪽 컨트롤일 경우
                if event.key == pg.K_LCTRL:
                    debug = not debug
    # 입력한 키들을 리스트로 저장
    keys = pg.key.get_pressed()

    # 화면을 검은색으로 채운다.
    display.fill(BLACK)

    # 만약 체력이 0보다 작거나 같은 경우
    if len(health) <= 0:
        # text 설정
        text = scoreboard.render('Your Score is : ' + str(score), True, WHITE, None)

        # 중앙 좌표 설정
        x = (display.get_width()-text.get_width())/2
        y = (display.get_height()-text.get_height())/2

        # text 출력
        display.blit(text, (x, y))
        bricks.clear()

        if keys[pg.K_SPACE]:
            health = [pg.Rect(5+2.5*i+i*10, 30, 10, 10) for i in range(3)]
            score = 0
            stage = 0
            ball.Base_Speed = 5
    
    # 체력이 0보다 큰 경우
    else:
        # 벽돌 갯수가 0보다 큰 경우
        if len(bricks) <= 0:
            clear = True
            ball.Is_Ready = True
        
        # 공이 준비 상태인 경우
        if ball.Is_Ready:
            ball.Reset(pad)
        
        # 스테이지를 클리어한 경우
        if clear == True:
            # 다음 스테이지
            stage += 1
            ball.Base_Speed = ball.Base_Speed * (1+ stage/10)
            # 벽돌 배치
            for i in range(4+stage):
                for j in range(4+stage):
                    bricks.append(Brick(i*(display.get_width()/(4+stage)), j*((display.get_height()/4+stage)/4), display.get_width()/(4+stage), (display.get_height()/4+stage)/4))
            # 변수 초기화
            clear = False
        
        # 공이 패드보다 위에 있을 경우
        if ball.centery <= pad.y:
            #충돌했을 경우
            if ball.colliderect(pad) == True:
                # 공이 충돌한 위치에 따라 튕겨지는 방향이 정해지는 방식
                # 공과 패드 중앙 사이의 거리
                distance_from_center = ball.centerx - pad.centerx
                # 패드 절반 너비
                pad_width_half = pad.w/2
                # 패드 중앙과의 거리 퍼센트 => 반사각 비율 (100% = 80도)
                reflection_ratio = distance_from_center/pad_width_half
                # 반사각
                reflection_angle = np.radians(15+ reflection_ratio * (80 - 15))

                ball.Speed_X = ball.Base_Speed * np.sin(reflection_angle)
                ball.Speed_Y = -ball.Base_Speed * np.cos(reflection_angle)
                # 단순히 튕겨지기만 하는 방식
                #ball.Speed_Y = -ball.Base_Speed

        # 모든 벽돌에 대해 반복
        for brick in bricks:
            # 공이 벽돌에 충돌했을 경우
            if ball.colliderect(brick):
                #공의 좌표가 벽돌의 가로 범위에 포함될 경우
                #=> 공이 위나 아래에서 충돌 되었을 경우
                if ball.centerx > brick.x and ball.centerx < brick.x + brick.w:
                    ball.Speed_Y = -ball.Speed_Y
                #=> 공이 왼쪽이나 오른쪽에서 충돌 되었을 경우
                else:
                    ball.Speed_X = -ball.Speed_X
                # 해당 벽돌 삭제
                del bricks[bricks.index(brick)]
                # 점수 증가
                score += 1
        # 키보드 입력에 따른 패드 이동
        pad.Move_Keyboard(keys)
        # 키보드 입력을 받을 시, 공 발사
        ball.Shot(keys)
        # 공의 움직임
        ball.Move()

        # 죽었을 경우
        if ball.Is_Dead:
            Dead()
            ball.Is_Dead = False
        
        # 오브젝트들 그리기
        for brick in bricks:
            brick.Draw(display)
        for h in health:
            pg.draw.rect(display, WHITE, h)
            
        
        
        if debug == True:
            pg.draw.line(display, RED, ball.center, (ball.centerx ,pad.y))
            pg.draw.line(display, RED, ball.center, pad.center)
            text = scoreboard.render(f'%0.1f\n%0.1f' %(ball.Speed_X,ball.Speed_Y), True, WHITE, None)
        else:
            text = scoreboard.render(str(score), True, WHITE, None)
        display.blit(text, (0,0))
    
        pad.Draw(display)
        ball.Draw(display)
    
    # 화면 업데이트
    pg.display.flip()
        