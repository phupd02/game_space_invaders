
import pygame
import os
import time
import random
from player import *
from enemy import *
# Initialize font
pygame.font.init()
pygame.init()

# Window
WIDTH, HEIGHT = 650, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Project Python")

#background
BG = pygame.transform.scale(pygame.image.load(os.path.join("data","background.png")), (WIDTH,HEIGHT))


# main
def main():
    run = True

    FPS = 60
    # Level, Mạng sống
    level = 0
    lives = 5
    # Thua
    lost = False
    lost_count = 0

    # Font main, lost
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    # Mảng chứa các enemy
    enemies = []
    wave_length = 0

    # Tốc độ di chuyển của enemy, laser, player
    enemy_vel = 1
    laser_vel = 6 
    player_vel = 5

    # Tạo một player
    player1 = Player(300, 500)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))

        # draw text
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10,10))

        for enemy in enemies:
            enemy.draw(WIN)
        
        player1.draw(WIN)

        if lost:
            lost_label = lost_font.render("Game over", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()


    # game loop
    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player1.health <= 0:
            lost = True
            lost_count += 1
        
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy1 = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        

        # control board
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player1.x - player_vel > 0: # move left
            player1.x -= player_vel
        if keys[pygame.K_d] and player1.x + player_vel + player1.get_width() < WIDTH: # move right
            player1.x += player_vel
        if keys[pygame.K_w] and player1.y - player_vel > 0: # up
            player1.y -= player_vel
        if keys[pygame.K_s] and player1.y + player_vel + player1.get_height() + 20 < HEIGHT: # down
            player1.y += player_vel
        if keys[pygame.K_SPACE]:
            player1.shoot()


        for enemy1 in enemies[:]:
            enemy1.move(enemy_vel)
            enemy1.move_lasers(laser_vel, player1)

            if random.randrange(0, 2*60) == 1:
                enemy1.shoot()

            if enemy1.collide(player1):
                player1.health -= 10
                enemies.remove(enemy1)
            elif enemy1.y + enemy1.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy1)

        player1.move_lasers(-laser_vel, enemies)

# main_menu
def main_menu():
    title_font = pygame.font.SysFont("comicsans", 50)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Press the mause to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()

main_menu()