import pygame   
import sys

pygame.init()   #初始化pygame
screen = pygame.display.set_mode((480, 700))    #创建窗口
pygame.display.set_caption("飞机大战")  #窗口标题

#游戏对象与设置
SPEED = 5  #飞机移动速度
player = pygame.Rect(220,600,40,60) #玩家飞机
clock = pygame.time.Clock()  #限速器：把游戏固定在每秒60帧
BULLET_SPEED = 8  #子弹移动速度
bullets = []  #子弹列表

running = True  #开关

while running:  #循环控制开关，开着的时候进入循环，点击关闭按钮，开关变为False，循环结束
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#子弹发射
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  #按下空格键
            new_bullet = pygame.Rect(player.x + player.width // 2 - 2,player.y - 10, 4, 10)
            bullets.append(new_bullet)  #把新子弹加入子弹列表
    
#键盘移动
    keys = pygame.key.get_pressed()  #获取键盘按键状态
    if keys[pygame.K_LEFT]: #左方向键正被按住
        player.x -= SPEED   #飞机向左移动
    if keys[pygame.K_RIGHT]:    # 右方向键正被按住
        player.x += SPEED   #飞机向右移动

#边界保护
    if player.x < 0:   #左边缘越界？
        player.x = 0   #按回最左边
    if player.x + player.width > screen.get_width():  #右边缘越界？
        player.x = screen.get_width() - player.width  #按回最右边

#子弹移动
    for bullet in bullets[:]:  #遍历子弹列表的副本
        bullet.y -= BULLET_SPEED  #子弹向上移动
        if bullet.y + bullet.height < 0:  #子弹飞出屏幕？
            bullets.remove(bullet)  #从子弹列表中移除

#绘制背景
    screen.fill((20,20,50)) #填充背景颜色
    pygame.draw.rect(screen, (0,255,0), player)  #绘制玩家飞机
    for bullet in bullets:
        pygame.draw.rect(screen, (255,255,0), bullet)  #绘制子弹
    pygame.display.flip()  #更新屏幕显示

#帧率控制
    clock.tick(60)  #每秒60帧

pygame.quit()   # 退出pygame
sys.exit()      # 退出系统