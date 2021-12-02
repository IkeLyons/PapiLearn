import pygame
import numpy as np
import PapiLearn.envs.Character as ch

screen_width = 400
screen_height = 700

class PyGame2D:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.clock = pygame.time.Clock()
        self.game_speed = 60
        self.char = ch.Character('character.png', (200, 100))

    def act(self, action):
        pass

    def eval(self):
        pass

    def view(self):
        self.screen.fill((0, 0, 0))
        self.char.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.game_speed)

    def observe(self):
        state = np.fliplr(np.flip(np.rot90(pygame.surfarray.array3d(
            pygame.display.get_surface()).astype(np.uint8))))
        return state

    def finished(self):
        pass


