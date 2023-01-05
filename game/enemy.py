import ship
import laser
import pygame
import os

class Enemy(ship.Ship):
    # Tàu của enemy
    RED_SPACE_SHIP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","red_enemy.png")), (140, 88))
    GREEN_SPACE_SHIP_IMG = pygame.transform.scale( pygame.image.load(os.path.join("data","green_enemy.png")), (140, 80))
    BLUE_SPACE_SHIP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","blue_enemy.png")), (140, 60))

    # Đạn tuong ung voi moi con tau
    RED_LASER_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","red_laser.png")), (30, 30))
    GREEN_LASER_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","green_laser.png")), (30, 30))
    BLUE_LASER_IMG = pygame.transform.scale(pygame.image.load(os.path.join("data","blue_laser.png")), (30, 30))
    # Tu dien, ta se sinh cac con tau có màu ngẫu nhiên kèm theo đạn tuong ứng
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP_IMG, RED_LASER_IMG),
        "green": (GREEN_SPACE_SHIP_IMG, GREEN_LASER_IMG),
        "blue": (BLUE_SPACE_SHIP_IMG, BLUE_LASER_IMG)
    }

    # Constructor
    def __init__(self,x,y,color,health=100):
        super().__init__(x,y,health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self,vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser1 = laser.Laser(self.x-20,self.y,self.laser_img)
            self.lasers.append(laser1)
            self.cool_down_counter = 1

