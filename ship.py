import pygame

class Ship:
    
    def __init__(self, ai_game):
        """ initialize the ship and its starting position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('png/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """ draw the ship at its current location """
        self.screen.blit(self.image, self.rect)