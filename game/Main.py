
import pygame
import os
import time
import random
from pygame import mixer
from player import *
from enemy import *
from button import *

# Initialize font
pygame.font.init()
pygame.init()

# Window
WIDTH, HEIGHT = 650, 550 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Project Python")

#background
BG = pygame.transform.scale(pygame.image.load(os.path.join("data","background.png")), (WIDTH,HEIGHT))

# âm thanh nền
pygame.mixer.music.load(os.path.join("data", "background.wav"))
pygame.mixer.music.play(-1)


# main, run chương trình
def main():
    run = True

    FPS = 60
    # Level, Mạng sống
    level = 0
    lives = 5
    scores = 0
    # Thua
    lost = False
    lost_count = 0

    # Font main, lost
    main_font = pygame.font.SysFont("comicsans", 40)
    lost_font = pygame.font.SysFont("comicsans", 60)

    # Mảng chứa các enemy
    enemies = []
    wave_length = 0

    # Tốc độ di chuyển của enemy, laser, player
    enemy_vel = 1
    laser_vel = 6 
    player_vel = 5

    # Tạo một player
    player1 = Player(400, 450)
    clock = pygame.time.Clock()

    # SUBFUNCTION 1: VẼ LẠI CỬA SỔ
    def show_parameter(): # parameter bao gồm: điểm (scores), mạng (lives), cấp độ (level)
        WIN.blit(BG, (0,0))

        # draw text
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        score_label = main_font.render(f"Score: {scores}", 1, (255,255,255))

        # draw parameter on the screen
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10,10))
        WIN.blit(score_label, ((WIDTH - level_label.get_width())/2 - 20,10))

        # draw enemies on the screen
        for enemy in enemies:
            enemy.draw(WIN)
        player1.draw(WIN)

        # If lose, draw "Game over"
        if lost:
            lost_label = lost_font.render("Game over", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

    # game loop
    while run:
        start_time = time.time()
        clock.tick(FPS)
        show_parameter() # cập nhật lại những thay đổi như điểm số, mạng sống, level

        # Thay đổi lives, lost nếu có
        if lives <= 0 or player1.health <= 0:
            lost = True
            lost_count += 1
        
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        # Bắt sự kiện, nếu QUIT
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
            pygame.mixer.music.load(os.path.join("data", "bullet.wav"))
            pygame.mixer.music.play()
            
            
        # Tạo ra các làn sóng tấn công
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy1 = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy1)
                

        # enemy di chuyển, bắn laser
        for enemy1 in enemies[:]:
            enemy1.move(enemy_vel)
            enemy1.move_lasers(laser_vel, player1)

            # enemy sinh ra ở các vị trí ngẫu nhiên
            if random.randrange(0, 2*30) == 1:
                enemy1.shoot()

            # nếu có va cham giữa player và enemy 
            if enemy1.collide(player1):
                player1.health -= 10
                enemies.remove(enemy1)
            
            elif enemy1.y + enemy1.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy1)

        scores = player1.scores
        player1.move_lasers(-laser_vel, enemies)
        pygame.display.update()

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
    os.quit()

main_menu()