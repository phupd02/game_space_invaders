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

# Laser Class
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return self.y <= height and self.y >= 0
    
    def collision(self, obj):
        return collide(obj, self)

#Ship class
class Player(Ship): # Ke thua
    def __init__(self, x, y, health = 100):
        super().__init__(x , y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


#Enemy Class
class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }

    def __init__(self, x, y, color, health = 100): 
        super().__init__(x, y, health)
        self.ship_img,self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, vel):
        self.y += vel

def collide(obj1, obj2):
    pass

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5 # mạng
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    # di chuyen enemies, sinh vin tri ngau nhien 
    enemies = []
    wave_length = 5
    enemy_vel = 5

    player_vel = 5

    player = Player(300, 400)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG,(0,0))
        # draw text
        lives_label = main_font.render(f"Level: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        
        WIN.blit(lives_label,(10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10,10))
        
        # Phan nay ve cac component ra man hinh
        for enemy in enemies:
            enemy.draw(WIN)
        # Ve player
        player.draw(WIN)
        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width()/2, 300))

            
        pygame.display.update()

    #game loop
    while run:
        clock.tick(FPS)
        redraw_window()

        # Khi nao thi thua
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        # Neu so luong ke thu = 0, tang level
        if len(enemies) == 0:
            level += 1
            wave_length += 5 # tang so luong ke thu len 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500 , -100), random.choice(["red","blue","green"])) # sinh ke thu o cac vi tri am
                enemies.append(enemy)

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
        
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
        redraw_window()
main()
# Tiep tuc hoan thien ham collide o dong 95



