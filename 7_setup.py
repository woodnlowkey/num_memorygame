import pygame
from random import *

#레벨설정
def setup(level):
    global display_time #얼마동안숫자를보여줄것인가
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1) #얼마나많은숫자를보여줄것인가
    number_count = (level // 3) + 5
    number_count = min(number_count, 20) #20을초과하면20으로
    shuffle_grid(number_count) #실제화면에grid형태로숫자랜덤배치

#숫자섞기
def shuffle_grid(number_count):
    rows = 5
    columns = 9
    cell_size = 130 #각gridcell별가로세로크기
    button_size = 110 #gridcell그려질버튼크기
    screen_left_margin = 55 #전체스크린왼쪽여백
    screen_top_margin = 20 #전체스크린윗쪽여백
    grid = [[0 for col in range(columns)] for row in range(rows)] #5*9
    number = 1 #시작숫자1부터number_count까지숫자랜덤배치
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)
        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1
            #현재그리드셀위치기준x,y위치구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)
            #숫자버튼만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

#시작화면보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    #흰색 동그라미, 중심은 start_button의 중심, 반지름60, 두께5
    msg = game_font.render(f"{curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)

#게임화면보여주기
def display_game_screen():
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time:
            hidden = True
    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            pygame.draw.rect(screen, GRAY, rect)
        else:
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect) #실제숫자텍스트

#pos에해당하는버튼확인
def check_buttons(pos):
    global start, start_ticks
    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()

def check_number_buttons(pos):
    global start, hidden, curr_level
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                del number_buttons[0]
                if not hidden:
                    hidden = True #숫자숨김처리
            else: #잘못된숫자클릭
                game_over()
            break
    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)

#게임종료처리
def game_over():
    global running
    running = False
    msg = game_font.render(f"your level is {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))
    screen.fill(BLACK)
    screen.blit(msg, msg_rect)

#초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120) #폰트정의
#시작버튼
start_button = pygame.Rect(0,0, 120, 120)
start_button.center = (120, screen_height - 120)
#색깔
BLACK = (0, 0, 0) #RGB
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

number_buttons = [] #플레이어가눌러야하는버튼들
curr_level = 1 #현재레벨
display_time = None #숫자를보여주는시간
start_ticks = None #시간계산
start = False #게임시작여부
hidden = False #숫자숨김여부(1클릭또는시간초과)
setup(curr_level) #기본설정

#게임루프
running = True #게임실행중인가?
while running:
    click_pos = None #이벤트루프
    for event in pygame.event.get(): #어떤이벤트가발생하였는가?
        if event.type == pygame.QUIT: #창이닫혔는가?
            running = False #게임이더이상실행중이아님
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
    screen.fill(BLACK) #화면전체를까맣게칠함
    if start:
        display_game_screen() #게임화면표시
    else:
        display_start_screen() #시작화면표시
    if click_pos: #어딘가클릭
        check_buttons(click_pos)
    pygame.display.update() #화면업데이트

pygame.time.delay(5000)
pygame.quit() #게임종료