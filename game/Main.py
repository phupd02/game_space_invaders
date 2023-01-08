import pygame
import os
import time
from level import *
from player import *
from enemy import *

# Initialize font
pygame.font.init()
pygame.init()

# thay đổi laser
LINK_LASER_IMG1 = os.path.join("data","laser_ver1.png")
LINK_LASER_IMG2 = os.path.join("data","laser_ver2.png")

# Window
WIDTH, HEIGHT = 800, 550 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Project Python")

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("data","background1.png")), (WIDTH,HEIGHT))
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

    # Tạo một player
    player1 = Player(450, 400)
    
    # Đoi tuong Enemies
    enemies1 = Level(0, 5)

     # list enemy
    enemies = enemies1.enemies

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

    clock = pygame.time.Clock()

    # SUBFUNCTION 2: VẼ LẠI CỬA SỔ
    def show_parameter(): # parameter bao gồm: điểm (scores), mạng (lives), cấp độ (level)
        if scores >= 10:
            WIN.blit(BG2, (0,0))
        else:
            WIN.blit(BG, (0,0))
            
        # color
        WHITE = 255, 255, 255

        # Draw text
        level_label = main_font.render(f"Level: {enemies1.level}", 1, WHITE)
        lives_label = main_font.render(f"Lives: {enemies1.lives}", 1, WHITE)
        score_label = main_font.render(f"Score: {scores}", 1, WHITE)

        # Draw parameter on the screen
        WIN.blit(score_label, ((WIDTH - level_label.get_width())/2,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10,10))
        WIN.blit(lives_label, (10,10))

        # Draw enemies on the screen
        for enemy in enemies:
            enemy.draw(WIN)
        player1.draw(WIN)

        # If lose, draw "Game over"
        if lost:
            lost_label = lost_font.render("Game over", 1, (255,255,255))
            
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 250))
            pygame.display.update()
        
    # SUBFUCNTION: Pause the game
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

        # Thua cuộc
        if lives <= 0 or player1. health <= 0:
            lost = True
            lost_count += 1
        
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        # control board
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player1.x - player1.player_vel > 0: # move left
            player1.x -= player1.player_vel
        if keys[pygame.K_d] and player1.x + player1.player_vel + player1.get_width() < WIDTH: # move right
            player1.x += player1.player_vel
        if keys[pygame.K_w] and player1.y - player1.player_vel > 0: # up
            player1.y -= player1.player_vel 
        if keys[pygame.K_s] and player1.y + player1.player_vel + player1.get_height() + 20 < HEIGHT: # down
            player1.y += player1.player_vel
        if keys[pygame.K_SPACE]: # shoot
            
            # Nâng cấp đạn người chơi theo level
            rank_laser = scores // 10
            if rank_laser % 2 == 0:
                player1.shoot_laser(LINK_LASER_IMG1)
            else:
                player1.shoot_laser(LINK_LASER_IMG2)
        
            # Âm thanh khi bắn
            pygame.mixer.music.load(os.path.join("data", "bullet.wav"))
            pygame.mixer.music.play()
           
        enemies1.create_attack()
        enemies1.attack(player1)

        # Update điểm số
        scores = player1.scores
        level = enemies1.level
        lives = enemies1.lives
        
        player1.move_lasers(-player1.laser_vel, enemies)
        pygame.display.update()

# main_menu
def main_menu():
    title_font = pygame.font.SysFont("comicsans", 50)
    run = True
    while run:
        WIN.blit(BG, (0,0))

        title_label = title_font.render("Press the mause to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 250))
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