import pygame

#시작화면보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    #흰색 동그라미, 반지름60, 두께5

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

#게임루프
running = True #게임실행중인가?
while running:
    #이벤트루프
    for event in pygame.event.get(): #어떤이벤트가발생하였는가?
        if event.type == pygame.QUIT: #창이닫혔는가?
            running = False #게임이더이상실행중이아님

    #화면전체를까맣게칠함
    screen.fill(BLACK)

    #시작화면표시
    display_start_screen()

    #화면업데이트
    pygame.display.update()
#게임종료
pygame.quit()