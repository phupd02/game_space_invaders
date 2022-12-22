import pygame
import os
import time
import random
from player import *
from enemy import *
from button import *

# Initialize font
pygame.font.init()
pygame.init()

# thay đổi laser
LINK_LASER_IMG1 = os.path.join("data","laser.png")
LINK_LASER_IMG2 = os.path.join("data","laser_ver2.png")

# Window
WIDTH, HEIGHT = 650, 550 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Project Python")

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("data","background.png")), (WIDTH,HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load(os.path.join("data","background2.png")), (WIDTH,HEIGHT))
# Âm thanh nền
pygame.mixer.music.load(os.path.join("data", "background.wav"))
pygame.mixer.music.play(-1)

BLACK = 255, 255, 255
# Main, run chương trình
def main():
    run = True
    pause = False
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
        if scores > 15:
            WIN.blit(BG2, (0,0))
        else:
            WIN.blit(BG, (0,0))
        # color
        WHITE = 255, 255, 255

        # Draw text
        level_label = main_font.render(f"Level: {level}", 1, WHITE)
        lives_label = main_font.render(f"Lives: {lives}", 1, WHITE)
        score_label = main_font.render(f"Score: {scores}", 1, WHITE)

        # Draw parameter on the screen
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10,10))
        WIN.blit(score_label, ((WIDTH - level_label.get_width())/2 - 20,10))

        # Draw enemies on the screen
        for enemy in enemies:
            enemy.draw(WIN)
        player1.draw(WIN)

        # If lose, draw "Game over"
        if lost:
            lost_label = lost_font.render("Game over", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
        
    # Pause the game
    def pause(stop):
        pause_font = pygame.font.SysFont("comicsans", 60)
        text_surface = pause_font.render("Paused", True, BLACK)
        rect = text_surface.get_rect(center = (WIDTH / 2, HEIGHT / 2))
        WIN.blit(text_surface, rect)

        while stop:
            for event in pygame.event.get():
                # quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()
                clock.tick(15)
                # un pause the game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        stop = False

    # game loop
    while run:
        start_time = time.time()
        clock.tick(FPS)
        show_parameter() # cập nhật lại những thay đổi như điểm số, mạng sống, level

        # Bắt sự kiện, nếu QUIT, PAUSE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # pause the game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    stop = True
                    pause(stop)

        # Thay đổi lives, lost nếu có
        if lives <= 0 or player1.health <= 0:
            lost = True
            lost_count += 1
        
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

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
        if keys[pygame.K_SPACE]: # shoot
            # Thay đổi đạn, cứ bắn 5 mục tiêu(scores tăng lên 5) thì đổi đạn 1 lần
            level_laser = scores // 10
            if level_laser % 2 == 0:
                player1.shoot(LINK_LASER_IMG1)
            else:
                player1.shoot(LINK_LASER_IMG2)
            pygame.mixer.music.load(os.path.join("data", "bullet.wav"))
            pygame.mixer.music.play()
    
        # Tạo ra các làn sóng tấn công, mối làn sóng có 5 enemy
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy1 = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1000, -100), random.choice(["red", "blue", "green"]))
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

        # Update điểm số
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

# run game
main_menu()