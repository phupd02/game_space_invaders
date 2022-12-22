import ship
import laser
import pygame
import os

class Enemy(ship.Ship):
    # Tàu của enemy
    RED_SPACE_SHIP = pygame.image.load(os.path.join("data","shape1.png"))
    GREEN_SPACE_SHIP = pygame.image.load(os.path.join("data","shape2.png"))
    BLUE_SPACE_SHIP = pygame.image.load(os.path.join("data","shape3.png"))

    # Đạn tuong ung voi moi con tau
    RED_LASER = pygame.image.load(os.path.join("data","laser.png"))
    GREEN_LASER = pygame.image.load(os.path.join("data","laser.png"))
    BLUE_LASER = pygame.image.load(os.path.join("data","laser.png"))

    # Tu dien, ta se sinh cac con tau có màu ngẫu nhiên kèm theo đạn tuong ứng
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
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

    # # # Kiểm tra xem có va chạm với player hay ko
    # def collide_player(self, obj):
    #     if super().collide(obj) and isinstance(obj, Player):
    #         return True
    #     return False