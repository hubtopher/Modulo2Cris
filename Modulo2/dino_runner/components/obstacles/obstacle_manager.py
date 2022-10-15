from ast import Break
import pygame
import random
from dino_runner.utils.constants import RUNNING
from dino_runner.utils.constants import  HEART_TYPE, SHIELD_TYPE , HAMMER_TYPE
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:  
                if random.randint(0,1)==0:
                    cactus_type = 'SMALL' if random.randint(0, 1) == 0 else 'LARGE'
                    cactus = Cactus(cactus_type)
                    self.obstacles.append(cactus) 
                else:
                    bird = Bird(BIRD)
                    self.obstacles.append(bird)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle):

############################
                if game.player.type ==SHIELD_TYPE:
                    game.playing = True
                    break
                
############################
                elif game.player.type == HAMMER_TYPE:
                    
                    game.playing = True
                    
                    self.obstacles.remove(obstacle)
                    break
                    

###########################
                elif game.player.type == HEART_TYPE:
                    health=0
                    while health <=2:
                        if game.player.dino_rect.colliderect(obstacle):
                           self.obstacles.remove(obstacle)
                           game.playing = True
                           health += 1
                        else:
                            game.playing = False
                        break  
                else:
                    game.playing = False
                    game.death_count += 1
############################                    
                



    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []