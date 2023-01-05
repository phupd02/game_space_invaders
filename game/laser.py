import pygame
''' Để tạo 1 laser cần truyền vào: toạ độ và ảnh của laser'''
class Laser:
    def __init__(self,x,y,img):
        self.x = x + 65
        self.y = y + 80
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x,self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y < height and self.y >= 0)

    # check_va cham
    def collide(self,obj):
        offset_x = self.x - obj.x
        offset_y = self.y - obj.y
        return self.mask.overlap(obj.mask, (offset_x,offset_y)) != None
    