import pygame

class Character:
    def __init__(self, img, pos):
        self.sprite = pygame.image.load(img)
        self.sprite = pygame.transform.scale(self.sprite, (25, 25))
        self.pos = pos
        self.xspeed = 0
        self.yspeed = 0
        self.gravity = 0.1

    def draw(self, screen):
        screen.blit(self.sprite, self.pos)

    def update(self):
        # self.pos[0] = self.pos[0] + self.xspeed
        self.pos[1] = self.pos[1] + self.yspeed
        if self.yspeed < 10:
            self.yspeed = self.yspeed + self.gravity