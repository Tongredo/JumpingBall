# -*- coding:utf-8 -*-
from codepack.platform import platformClass
import pygame
#import Main
from pygame.locals import *


p1t = platformClass.Platform(platformClass.image, [560, 840])
p1b = platformClass.Platform(platformClass.image_bottom, [560, 860])

p2t = platformClass.Platform(platformClass.image, [850, 640])
p2b = platformClass.Platform(platformClass.image_bottom, [850, 660])

p3t = platformClass.Platform(platformClass.image, [1100, 440])
p3b = platformClass.Platform(platformClass.image_bottom, [1100, 460])

p4t = platformClass.Platform(platformClass.image, [1700, 440])
p4b = platformClass.Platform(platformClass.image_bottom, [1700, 460])

p5t = platformClass.Platform(platformClass.image, [2100, 640])
p5b = platformClass.Platform(platformClass.image_bottom, [2100, 660])

p6t = platformClass.Platform(platformClass.image, [3020, 820])
p6b = platformClass.Platform(platformClass.image_bottom, [3020, 840])

p7t = platformClass.Platform(platformClass.image, [3500, 350])
p7b = platformClass.Platform(platformClass.image_bottom, [3500, 370])

p8t = platformClass.Platform(platformClass.image, [4000, 650])
p8b = platformClass.Platform(platformClass.image_bottom, [4000, 670])

tp2 = platformClass.Platform(platformClass.tp_image, [3120, 1020])
tp1 = platformClass.Platform(platformClass.tp_image, [2600, 820])

lb1 = platformClass.Platform(platformClass.lose_health_image, [3550, 820])
lb2 = platformClass.Platform(platformClass.lose_health_image, [4500, 450])
lb3 = platformClass.Platform(platformClass.lose_health_image, [4500, 850])

psp = platformClass.Platform(platformClass.pass_image, [4730, 250])


def draw_level(surface):
    surface.blit(p1t.image, p1t.rect)
    surface.blit(p2t.image, p2t.rect)
    surface.blit(p3t.image, p3t.rect)
    surface.blit(p4t.image, p4t.rect)
    surface.blit(p5t.image, p5t.rect)
    surface.blit(p6t.image, p6t.rect)
    surface.blit(p7t.image, p7t.rect)
    surface.blit(p8t.image, p8t.rect)

    surface.blit(p1b.image, p1b.rect)
    surface.blit(p2b.image, p2b.rect)
    surface.blit(p3b.image, p3b.rect)
    surface.blit(p4b.image, p4b.rect)
    surface.blit(p5b.image, p5b.rect)
    surface.blit(p6b.image, p6b.rect)
    surface.blit(p7b.image, p7b.rect)
    surface.blit(p8b.image, p8b.rect)

    surface.blit(tp1.image, tp1.rect)
    surface.blit(tp2.image, tp2.rect)

    surface.blit(lb1.image, lb1.rect)
    surface.blit(lb2.image, lb2.rect)
    surface.blit(lb3.image, lb3.rect)

    surface.blit(psp.image, psp.rect)


def level_move():
    p1t.move([-5, 0])  # 移动平台顶部
    p1b.move([-5, 0])  # 移动平台底部
    p2t.move([-5, 0])
    p2b.move([-5, 0])
    p3t.move([-5, 0])
    p3b.move([-5, 0])
    p4t.move([-5, 0])
    p4b.move([-5, 0])
    p5t.move([-5, 0])
    p5b.move([-5, 0])
    p6t.move([-5, 0])
    p6b.move([-5, 0])
    p7t.move([-5, 0])
    p7b.move([-5, 0])
    p8t.move([-5, 0])
    p8b.move([-5, 0])
    tp1.move([-5, 0])
    tp2.move([-5, 0])
    lb1.move([-5, 0])
    lb2.move([-5, 0])
    lb3.move([-5, 0])
    psp.move([-5, 0])


def coi(speed, done, keys, player, health_number, complete, playerGroup):

    if pygame.sprite.spritecollide(p1b, playerGroup, False):
        player.rect.top = p1b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(p1t, playerGroup, False):
        player.rect.top = p1t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(p2b, playerGroup, False):
        player.rect.top = p2b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(p2t, playerGroup, False):
        player.rect.top = p2t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(p3b, playerGroup, False):
        player.rect.top = p3b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(p3t, playerGroup, False):
        player.rect.top = p3t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(p4b, playerGroup, False):
        player.rect.top = p4b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(p4t, playerGroup, False):
        player.rect.top = p4t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(p5b, playerGroup, False):
        player.rect.top = p5b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(p5t, playerGroup, False):
        player.rect.top = p5t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(p6b, playerGroup, False):
        player.rect.top = p6b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(p6t, playerGroup, False):
        player.rect.top = p6t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(p7b, playerGroup, False):
        player.rect.top = p7b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(p7t, playerGroup, False):
        player.rect.top = p7t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(p8b, playerGroup, False):
        player.rect.top = p8b.get_y() + 18
        speed = 0
    if pygame.sprite.spritecollide(p8t, playerGroup, False):
        player.rect.top = p8t.get_y() - 100
        speed = 0
        if keys[K_w]:
            done = True

    if pygame.sprite.spritecollide(tp2, playerGroup, False):
        player.rect.top = p7b.get_y() - 180

    if pygame.sprite.spritecollide(tp1, playerGroup, False):
        player.rect.top = p4b.get_y() - 180
        player.rect.left = p4t.get_x() + 100

    if pygame.sprite.spritecollide(lb1, playerGroup, False):
        player.rect.top = p6b.get_y() - 180
        player.rect.left = p6t.get_x() + 100
        health_number -= 1

    if pygame.sprite.spritecollide(lb2, playerGroup, False):
        player.rect.top = p8b.get_y() - 180
        player.rect.left = p8t.get_x() + 100
        health_number -= 1

    if pygame.sprite.spritecollide(lb3, playerGroup, False):
        player.rect.top = p8b.get_y() - 180
        player.rect.left = p8t.get_x() + 100
        health_number -= 1

    if pygame.sprite.spritecollide(psp, playerGroup, False):
        complete = True


