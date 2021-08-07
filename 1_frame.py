import pygame

#초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

#게임루프
running = True #게임실행중인가?
while running:
    #이벤트루프
    for event in pygame.event.get(): #어떤이벤트가발생하였는가?
        if event.type == pygame.QUIT: #창이닫혔는가?
            running = False #게임이더이상실행중이아님
#게임종료
pygame.quit()