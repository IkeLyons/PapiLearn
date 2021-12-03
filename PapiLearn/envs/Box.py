import pygame

class Box:
    def __init__(self, img, pos):
        self.sprite = pygame.image.load(img)
        self.sprite = pygame.transform.scale(self.sprite, (200, 10))
        self.pos = pos
        self.speed = 0

    def draw(self, screen, offset):
        screen.blit(self.sprite, (self.pos[0], self.pos[1] - offset))