import pygame

class Ship:
    
    def __init__(self, ai_game):
        """ initialize the ship and its starting position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('png/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """ update the ships x position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
            

    def blitme(self):
        """ draw the ship at its current location """
        self.screen.blit(self.image, self.rect)