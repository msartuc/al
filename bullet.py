import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ a class to manage bullets fired from ship """
    def __init__(self, ai_game):
        """ create a bullet object at the ships position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # create a bullet at 0,0 then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store bullet position as float
        self.y = float(self.rect.y)

    def update(self):
        #moving the bullet
        self.y -= self.settings.bullet_speed
        #update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)