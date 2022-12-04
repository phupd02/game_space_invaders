import pygame
import os
import time
import random
pygame.font.init()
WIDTH, HEIGHT = 650, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - Project Python")

#Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("data","spaceship.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("data","spaceship.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("data","spaceship.png"))

#Player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("data","spaceship.png"))

#Bullet
RED_LASER = pygame.image.load(os.path.join("data","bullet.png"))
GREEN_LASER = pygame.image.load(os.path.join("data","bullet.png"))
BLUE_LASER = pygame.image.load(os.path.join("data","bullet.png"))
YELLOW_LASER = pygame.image.load(os.path.join("data","bullet.png"))

#background
BG = pygame.transform.scale(pygame.image.load(os.path.join("data","background.png")), (WIDTH,HEIGHT))


#Ship class
class Ship:
    def __init__(self, x, y,health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
       

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

#Ship class
class Player(Ship): # Ke thua
    def __init__(self, x, y, health = 100):
        super().__init__(x , y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health



def main():
    run = True
    FPS = 60
    level = 1
    lives = 5 # mạng
    main_font = pygame.font.SysFont("comicsans", 50)
    
    player_vel = 5
    player = Player(300, 400)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG,(0,0))
        # draw text
        lives_label = main_font.render(f"Level: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        
        WIN.blit(lives_label,(10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10,10))
        
        player.draw(WIN)
        
        pygame.display.update()

    #game loop
    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # di chuyen con tau
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player.get_width() >= 0: # left, neu phim do bi nhan (tuc TRue) thi
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player.get_height() > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: # down
            player.y += player_vel
main()
# Da xem den class enemy - phut 53p28



