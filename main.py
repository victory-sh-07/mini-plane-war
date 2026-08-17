import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((480, 700))
pygame.display.set_caption("飞机大战")

running = True  #开关
while running:  #循环控制开关，开着的时候进入循环，点击关闭按钮，开关变为False，循环结束
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20,20,50))
    pygame.display.flip()

pygame.quit()   # 退出pygame
sys.exit()      # 退出系统