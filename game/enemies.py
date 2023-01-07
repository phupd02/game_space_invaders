
import random
from enemy import *

class Enemies:
    WIDTH, HEIGHT = 800, 550
    enemies = []
    
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives


    def create_level(self):
        wave_length = 0
        if len(Enemies.enemies) == 0:
            self.level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy1 = Enemy(random.randrange(50, Enemies.WIDTH-280), random.randrange(-1000, -100), random.choice(["first_ufo", "second_ufo", "third_ufo"]))
                Enemies.enemies.append(enemy1)


    def attack(self, player1):
        for enemy1 in Enemies.enemies[:]:
            enemy1.move(enemy1.enemy_vel)
            enemy1.move_lasers(enemy1.laser_vel, player1)

            # enemy sinh ra ở các vị trí ngẫu nhiên
            if random.randrange(0, 2*30) == 1:
                enemy1.shoot_laser()

            # nếu có va cham giữa player và enemy 
            if enemy1.check_collisions(player1):
                player1.health -= 10
                Enemies.enemies.remove(enemy1)
                    
            elif enemy1.y + enemy1.get_height() > Enemies.HEIGHT:
                self.lives -= 1
                Enemies.enemies.remove(enemy1)