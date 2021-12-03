import pygame
import random
import numpy as np
import PapiLearn.envs.Character as ch
import PapiLearn.envs.Box as box

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
        self.char = ch.Character('character.png', [175, 600])
        self.boxs = self.spawn_boxes(20)
        self.cameraY = 0

    def spawn_boxes(self, spawn_rate):
        boxes = []
        for i in range(spawn_rate):
            boxes.append(box.Box('box.png', [random.randrange(0, screen_width), random.randrange(0, screen_height)]))
        return boxes

    def act(self, action):
        if action == 0:
            self.char.xspeed += 5
        elif action == 1:
            self.char.xspeed -= 5
        elif action == 2: # stop
            self.char.xspeed = 0

        self.char.update(self.screen)

    def eval(self):
        pass

    def view(self):
        self.screen.fill((255, 255, 255))
        self.cameraY = self.char.pos[1] - self.screen_height/2
        self.char.draw(self.screen, self.cameraY)
        for box in self.boxs:
            box.draw(self.screen, self.cameraY)
        pygame.display.flip()
        self.clock.tick(self.game_speed)

    def observe(self):
        state = np.fliplr(np.flip(np.rot90(pygame.surfarray.array3d(
            pygame.display.get_surface()).astype(np.uint8))))
        return state

    def finished(self):
        if self.char.pos[1] > self.screen_height:
            return True
        return False


