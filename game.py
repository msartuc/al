import sys
import pygame

class AlienInvasion:
    """ overall class to set up the game behaviour and variable """

    def __init__(self):
        """ initialize the game """
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ starts the main loop for the game """
        while True:
            """ listen to the keyboard and mouse """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run it
    ai = AlienInvasion()
    ai.run_game()
    