import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
class Bird(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(220,260)
        self.step_index = 0



    def draw(self, screen):
        self.step_index += 1
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        if self.step_index >=10:
            self.step_index = 0
        screen.blit(self.image, (self.rect.x , self.rect.y))