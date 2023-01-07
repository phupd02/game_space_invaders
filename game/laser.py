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

    def over_height(self, height):
        return (self.y > height or self.y <= 0)

    # check_va cham
    def check_collisions(self,obj):
        offset = (int(self.x - obj.x), int(self.y - obj.y))
        return self.mask.overlap(obj.mask, offset) != None

    