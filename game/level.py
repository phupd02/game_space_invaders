
import random
from enemy import *

class Level:
    WIDTH, HEIGHT = 800, 550
    enemies = []
    
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    # sinh ra các đợt tấn công  
    def create_attack(self):
        wave_length = 0
        # Nếu list enemies rỗng, tức kẻ thù đã bị tiêu diệt hết, cần tạo đợt tấn công
        if len(Level.enemies) == 0:
            self.level += 1

            # Xử lý level
            if self.level == 1: # Nếu level == 1, có 5 kẻ địch
                wave_length += 5
                for i in range(wave_length):
                    enemy1 = Enemy(random.randrange(50, Level.WIDTH-280), random.randrange(-1000, -100), random.choice(["first_ufo", "second_ufo", "third_ufo"]))
                    Level.enemies.append(enemy1)
            elif self.level == 2: # Nếu leve == 2, có 10 kẻ địch
                wave_length += 10
                for i in range(wave_length):
                    enemy1 = Enemy(random.randrange(50, Level.WIDTH-280), random.randrange(-500, -50), random.choice(["first_ufo", "second_ufo", "third_ufo"]))
                    Level.enemies.append(enemy1)
            else: # Nếu level >= 3, có 15 kẻ địch
                wave_length += 15
                for i in range(wave_length):
                    enemy1 = Enemy(random.randrange(50, Level.WIDTH-280), random.randrange(-300, -20), random.choice(["first_ufo", "second_ufo", "third_ufo"]))
                    Level.enemies.append(enemy1)
            
    def attack(self, player1):
        for enemy1 in Level.enemies[:]:
            enemy1.move(enemy1.enemy_vel)
            enemy1.move_lasers(enemy1.laser_vel, player1)

            if random.randrange(0, 2*30) == 1:
                enemy1.shoot_laser()

            # nếu có va cham giữa player và enemy 
            if enemy1.check_collisions(player1):
                player1.health -= 10
                Level.enemies.remove(enemy1)

            # Ngoài màn hình, xoá địch  
            elif enemy1.y + enemy1.get_height() > Level.HEIGHT:
                self.lives -= 1
                Level.enemies.remove(enemy1)