import pygame

class Ship:
    
    def __init__(self, ai_game):
        """ initialize the ship and its starting position """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('png/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    
        #store a float for the ships exact position
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """ update the ships x position based on the movement flag"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """ draw the ship at its current location """
        self.screen.blit(self.image, self.rect)