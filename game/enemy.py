import random
from ufo import *
import laser
import pygame
import os


class Enemy(Ufo):

    # Tàu của enemy
    FIRST_UFO_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","red_enemy.png")), (140, 88))
    SECOND_UFO_IMG = pygame.transform.scale( pygame.image.load(os.path.join("data","green_enemy.png")), (140, 80))
    THIRD_UFO_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","blue_enemy.png")), (140, 60))

    # Đạn tuong ung voi moi con tau
    FIRST_BULLET_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","red_laser.png")), (30, 30))
    SECOND_BULLET_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","green_laser.png")), (30, 30))
    THIRD_BULLET_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","blue_laser.png")), (30, 30))

    # Tu dien, ta se sinh cac con tau có màu ngẫu nhiên kèm theo đạn tuong ứng
    TYPE_DICT = {
        "first_ufo": (FIRST_UFO_IMG, FIRST_BULLET_IMG),
        "second_ufo": (SECOND_UFO_IMG, SECOND_BULLET_IMG),
        "third_ufo": (THIRD_UFO_IMG, THIRD_BULLET_IMG)
    }

    # Constructor
    def __init__(self,x,y,type,blood=100):
        super().__init__(x,y, blood)
        self.ufo_image, self.bullet_image = self.TYPE_DICT[type]
        self.mask = pygame.mask.from_surface(self.ufo_image)
        # self.enemies = []
        self.enemy_vel = 1
        self.laser_vel = 6

    def move(self,vel):
        self.y += vel

    def shoot_laser(self):
        if self.cooldown_number == 0:
            laser1 = laser.Laser(self.x-20,self.y,self.bullet_image)
            self.lasers.append(laser1)
            self.cooldown_number = 1
