import pygame

class Character:
    def __init__(self, img, pos):
        self.sprite = pygame.image.load(img)
        self.sprite = pygame.transform.scale(self.sprite, (25, 25))
        self.pos = pos
        self.xspeed = 0
        self.yspeed = 0
        self.gravity = 0.1
        self.camera_offset = 0

    def draw(self, screen, offset):
        screen.blit(self.sprite, (self.pos[0], self.pos[1] - offset))
        self.camera_offset = offset

    def collision(self, screen):
        if self.pos[1] + self.sprite.get_height() < screen.get_height() : # boundary checking
            if self.yspeed > 0: # if the character is falling
                if screen.get_at((int(self.pos[0]), int(self.pos[1] + 25 - self.camera_offset))) == (0, 0, 0):
                    return True

    def update(self, screen):
        # self.pos[0] = self.pos[0] + self.xspeed
        self.pos[1] = self.pos[1] + self.yspeed
        if self.yspeed < 5:
            self.yspeed = self.yspeed + self.gravity
        if self.collision(screen):
            self.yspeed = -5