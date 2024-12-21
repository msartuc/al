import sys
import pygame
from settings import Settings

class AlienInvasion:
    """ overall class to set up the game behaviour and variable """

    def __init__(self):
        """ initialize the game """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()   
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        

    def run_game(self):
        """ starts the main loop for the game """
        while True:
            """ listen to the keyboard and mouse """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)   
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # make a game instance and run it
    ai = AlienInvasion()
    ai.run_game()
    