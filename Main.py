# -*- coding:utf-8 -*-
import pygame
import L1

from pygame.locals import *
from codepack.playerOFball import playerClass
from codepack.HUD import blood


#--------------------------------------------------level 1 (collide)
def level1_collide():
    global speed
    global done
    global speed
    global health_number
    global complete
    if pygame.sprite.spritecollide(L1.p1b, playerGroup, False):   # 如果球碰到底部, 停止它的跳跃并下落
        player.rect.top = L1.p1b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(L1.p1t, playerGroup, False):    # 当球碰到平台的碰撞检测
        player.rect.top = L1.p1t.get_y()-100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(L1.p2b, playerGroup, False):
        player.rect.top = L1.p2b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(L1.p2t, playerGroup, False):
        player.rect.top = L1.p2t.get_y()-100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(L1.p3b, playerGroup, False):
        player.rect.top = L1.p3b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(L1.p3t, playerGroup, False):
        player.rect.top = L1.p3t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(L1.p4b, playerGroup, False):
        player.rect.top = L1.p4b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(L1.p4t, playerGroup, False):
        player.rect.top = L1.p4t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(L1.p5b, playerGroup, False):
        player.rect.top = L1.p5b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(L1.p5t, playerGroup, False):
        player.rect.top = L1.p5t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(L1.p6b, playerGroup, False):
        player.rect.top = L1.p6b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(L1.p6t, playerGroup, False):
        player.rect.top = L1.p6t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(L1.p7b, playerGroup, False):
        player.rect.top = L1.p7b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(L1.p7t, playerGroup, False):
        player.rect.top = L1.p7t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(L1.p8b, playerGroup, False):
        player.rect.top = L1.p8b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(L1.p8t, playerGroup, False):
        player.rect.top = L1.p8t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(L1.tp2, playerGroup, False):
        player.rect.top = L1.p7b.get_y() - 180

    if pygame.sprite.spritecollide(L1.tp1, playerGroup, False):
        player.rect.top = L1.p4b.get_y() - 180
        player.rect.left = L1.p4t.get_x() + 100

    if pygame.sprite.spritecollide(L1.lb1, playerGroup, False):
        player.rect.top = L1.p6b.get_y() - 180
        player.rect.left = L1.p6t.get_x() + 100
        health_number -= 1

    if pygame.sprite.spritecollide(L1.lb2, playerGroup, False):
        player.rect.top = L1.p8b.get_y() - 180
        player.rect.left = L1.p8t.get_x() + 100
        health_number -= 1

    if pygame.sprite.spritecollide(L1.lb3, playerGroup, False):
        player.rect.top = L1.p8b.get_y() - 180
        player.rect.left = L1.p8t.get_x() + 100
        health_number -= 1

    if pygame.sprite.spritecollide(L1.psp, playerGroup, False):
        complete = True
#--------------------------------------------------level 1

pygame.init()
fps = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN, 32)  # 创建一个全屏窗口
screen.fill([99, 200, 233])
pygame.display.flip()

pygame.key.set_repeat(30, 10)
bg = pygame.image.load("./image/background.png").convert_alpha()
bg2 = pygame.image.load("./image/background.png").convert_alpha()

health = blood.BloodHUD(blood.HUD_image, [10, 10])

player = playerClass.Player(playerClass.image, [580, 740])


playerGroup = pygame.sprite.Group()
playerGroup.add(player)

jump = True
done = False
health_number = 5  # 血量的设定
speed = -25  # 球的跳跃速度为25像素
y = 1080
level_ID = 1    # 当前关卡ID

# 游戏结束时的字体设置
over_x = 485
over_y = -250  # 440
over_text = "You Failed!"
over_font = pygame.font.Font("./image/arial.ttf", 180)
over_surf = over_font.render(over_text, 1, (255, 0, 0))
over_pos = [over_x, over_y]

# 过关时的字体设置
pass_x = 170
pass_y = -250  # 440
pass_text = "Complete the level!"
pass_font = pygame.font.Font("./image/arial.ttf", 180)
pass_surf = pass_font.render(pass_text, 1, (69, 188, 28))
pass_pos = [pass_x, pass_y]

bg_x = 0
bg2_x = 1920
complete = False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # 当按下ESC键, 关闭窗口
                running = False

    keys = pygame.key.get_pressed()   # 键盘事件处理
    if keys[K_a]:
        player.move([-12, 0])
    if keys[K_d]:
        player.move([12, 0])
        if player.rect.left >= 1200:    # 如果球的x轴大于1500, 背景移动并移动平台
            player.rect.left = 1200
            bg_x -= 5
            bg2_x -= 5

            L1.level_move()     # 第1关用于移动平台所调用的函数

    if keys[K_w]:
        jump = True
    #if keys[K_s]:
        #playerOFball.move([0, 8])

    if jump:  # 跳跃机制
        if player.rect.top >= -200:  # 当球的y坐标大于100时, 将它的速度一直减少, 实现跌落
            player.move([0, speed])
            speed += 0.80    # 减少球的速度

        if player.rect.top >= y-100:   # 当球着地时, 将速度设置为0, 将done变量设定为True, 将速度重新初始化为-25
            speed = 0
            done = True
            player.rect.top = 1080-100
            jump = False

        if done:  # done变量用于初始化速度
            speed = -25
            done = False
            jump = False

    health_number_text = str(health_number)     # 关于血量的显示
    health_font = pygame.font.Font("./image/arial.ttf", 50)
    health_surf = health_font.render(health_number_text, 1, (0, 0, 0))
    health_pos = [86, 15]


# -------------------------------------------------------------------------
    if player.rect.left <= 0:
        player.rect.left = 0

    if level_ID == 1:
        level1_collide()    # 第1关的碰撞检测
# --------------------------------------------------------------------------

    screen.blit(bg, [bg_x, 0])   # 加载背景位图
    screen.blit(bg2, [bg2_x, 0])

    L1.draw_level(screen)

    if health_number <= 0:  # 当机会为0次时, 将球移除并显示 You Failed!
        player.rect.top = -2000
        player.rect.left = 0
        screen.blit(over_surf, over_pos)
    if player.rect.top == 980:
        health_number = 0

    if player.rect.top == -2000:    # You Failed 的动画效果
        over_y += 20
        over_pos = [over_x, over_y]
        screen.blit(over_surf, over_pos)
        if over_y >= 440:
            over_y = 440

    if complete:
        player.rect.top = -1000
        player.rect.left = 0
        screen.blit(pass_surf, pass_pos)
    if player.rect.top == -1000:
        pass_y += 20
        pass_pos = [pass_x, pass_y]
        screen.blit(pass_surf, pass_pos)
        if pass_y >= 440:
            pass_y = 440

    screen.blit(player.image, player.rect)  # 加载球的位图
    screen.blit(health.image, health.rect)
    screen.blit(health_surf, health_pos)
    pygame.display.flip()   # 重绘
    fps.tick(60)   # 以每秒60fps的帧速率更新图像

    if bg_x <= -1920:
        bg_x = 1920
    if bg2_x <= -1920:
        bg2_x = 1920

pygame.quit()
