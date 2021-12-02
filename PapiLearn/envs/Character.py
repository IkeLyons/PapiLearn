import pygame

class Character:
    def __init__(self, img, pos):
        self.sprite = pygame.image.load(img)
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.pos = pos
        self.speed = 0

    def draw(self, screen):
        screen.blit(self.sprite, self.pos)

    def update(self):
        self.pos[0] = self.pos[0] + self.speed