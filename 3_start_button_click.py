import pygame

#시작화면보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    #흰색 동그라미, 중심은 start_button의 중심, 반지름60, 두께5

#게임화면보여주기
def display_game_screen():
    print("Game Start")

#pos에해당하는버튼확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

#초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

#시작버튼
start_button = pygame.Rect(0,0, 120, 120)
start_button.center = (120, screen_height - 120)

#색깔
BLACK = (0, 0, 0) #RGB
WHITE = (255, 255, 255)

#게임시작여부
start = False

#게임루프
running = True #게임실행중인가?
while running:
    click_pos = None

    #이벤트루프
    for event in pygame.event.get(): #어떤이벤트가발생하였는가?
        if event.type == pygame.QUIT: #창이닫혔는가?
            running = False #게임이더이상실행중이아님
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
    #화면전체를까맣게칠함
    screen.fill(BLACK)

    if start:
        display_game_screen() #게임화면표시

    else:
        display_start_screen() #시작화면표시
    if click_pos: #어딘가클릭
        check_buttons(click_pos)

    #화면업데이트
    pygame.display.update()

#게임종료
pygame.quit()