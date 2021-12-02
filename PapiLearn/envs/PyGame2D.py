import pygame

screen_width = 800
screen_height = 600

class PyGame2D:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.clock = pygame.time.Clock()

    def act(self, action):
        pass

    def eval(self):
        pass

    def view(self):
        pass

    def observe(self):
        pass

    def finished(self):
        pass


