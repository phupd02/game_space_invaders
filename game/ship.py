import pygame
import laser
from pygame import mixer
class Ship:
    COOLDOWN = 30
    WIDTH, HEIGHT = 800, 550 # kích cỡ của sổ
    '''
    Lớp Ship chính là lớp cơ sở
    - Player và Enemy đều kế thừa từ lớp này
    - Các atribute của Ship
    + x, y: Toạ độ của Ship
    + health: Sức khoẻ(Máu)
    + ufo_image: Ảnh hiển thị Ship
    + laser[]: Là một mảng, dùng để lưu trữ các đối tượng Laser
    '''

    # Construtor
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ufo_image = None
        self.lasers = []
        self.cooldown_number = 0


    # Function
    # Vẽ Ship ra màn hình
    def draw(self, window):
        window.blit(self.ufo_image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    # Di chuyển các viên đạn
    def move_lasers(self, velocity, object):
        self.cooldown()
        for laser1 in self.lasers:
            laser1.move(velocity)
            if laser1.over_height(self.HEIGHT) or laser1.check_collisions(object):
                self.lasers.remove(laser1)
                if laser1.check_collisions(object):
                    object.health -= 10

    # get width của con tàu
    def get_width(self):
        return self.ufo_image.get_width()

    # get height của con tàu
    def get_height(self):
        return self.ufo_image.get_height()

    # Hệ so hồi chiêu
    def cooldown(self):
        if self.cooldown_number > 0:
            self.cooldown_number += 1
            if self.cooldown_number > self.COOLDOWN:
                self.cooldown_number = 0
    
    def shoot_laser(self, link_laser):
        if self.cooldown_number == 0:
            laser_img = pygame.transform.scale(pygame.image.load(link_laser), (40, 60))
            laser1 = laser.Laser(self.x,self.y,laser_img)
            self.lasers.append(laser1)
            self.cooldown_number = 1

    # check va cham giữa self với vật thể bất kỳ
    def check_collisions(self,obj):
        offset = (int(self.x - obj.x), int(self.y - obj.y))
        return self.mask.overlap(obj.mask, offset) != None
