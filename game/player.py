import pygame
import ship
import os
from enemy import *

class Player(ship.Ship):
    WIDTH, HEIGHT = 800, 550
    LINK_PLAYER_IMG = os.path.join("data","player.png")


    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ufo_image = pygame.transform.scale(pygame.image.load(self.LINK_PLAYER_IMG), (160, 110))
        self.mask = pygame.mask.from_surface(self.ufo_image)
        self.max_health = health
        self.scores = 0
        self.player_vel = 5
        self.laser_vel = 6

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser1 in self.lasers:
            laser1.move(vel)
            if laser1.over_height(self.HEIGHT):
                self.lasers.remove(laser1)
            else:
                for obj in objs:
                    # Nếu va chạm với 1 vật thể bất kỳ ()
                    if laser1.check_collisions(obj):
                        objs.remove(obj)
                        self.scores += 1
                        if laser1 in self.lasers:
                            self.lasers.remove(laser1)

    def create_healthbar(self,window):
        pygame.draw.rect(window, (255,0,0), (self.x,self.y+self.ufo_image.get_height() + 10, self.ufo_image.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x,self.y+self.ufo_image.get_height() + 10, self.ufo_image.get_width() * (self.health/self.max_health), 10))

    def draw(self, window):
        super().draw(window)
        self.create_healthbar(window)



    
        
    