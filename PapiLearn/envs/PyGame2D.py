import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame
import random
import numpy as np
import math
#import PapiLearn
#from PapiLearn import envs 
#print('Path to module:',envs.__file__)
from PapiLearn.envs import Character as ch
from PapiLearn.envs import Box as box

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
        self.boxs = self.spawn_boxes(80)
        self.cameraY = 0
        self.min_height = 700 # higest the player has reached, called min cause pygame 0,0 is top left
        self.timer = 0

    def spawn_boxes(self, spawn_rate):
        boxes = []
        for i in range(spawn_rate):
            boxes.append(box.Box('box.png', [random.randrange(-100, screen_width), random.randrange(-screen_height, screen_height)]))
        return boxes

    def act(self, action):
        self.timer+=1
        if action == 0:
            self.char.xspeed += .1
        elif action == 1:
            self.char.xspeed -= .1
        elif action == 2: # stop
            self.char.xspeed = 0

        self.char.update(self.screen)

    def eval(self):
        if self.char.pos[1] > self.screen_height:
            #print('fell off screen')
            return -200
        if self.char.pos[0] < 0 - self.char.sprite.get_width() or self.char.pos[0] > self.screen_width:
            #print('went off side')
            return -200
        return -1*int(self.char.yspeed) -10*(self.char.xspeed==0)
        #pass

    def view(self):
        self.screen.fill((255, 255, 255))
        self.cameraY = self.char.pos[1] - self.screen_height/1.3
        # spawn boxes as player moves higher
        if self.char.pos[1] < self.min_height:
            self.min_height = self.char.pos[1]
            if random.random() < 0.1:
                x = random.randrange(-100, screen_width)
                y = random.randrange(int(self.min_height - screen_height - 20), int(self.min_height - screen_height))
                self.boxs.append(box.Box('box.png', [x, y]))

        self.char.draw(self.screen, self.cameraY)
        for b in self.boxs:
            b.draw(self.screen, self.cameraY)
        pygame.display.flip()
        self.clock.tick(self.game_speed)

    def observe(self):
        #keep all values b/n 0 and 10
        state=[0,0,0,0, 0,0, 0,0, 0,0, 0,0, 0,0]
        state[0] = min(max(int(self.char.pos[0]/40), 0), 10)
        #state[1] = int(self.char.pos[1]) #its height is kinda irrelevant?
        state[2] = 5+min(max(int(self.char.xspeed), -5), 5)
        state[3] = 5+min(max(int(self.char.yspeed), -5), 5)
        nearest5boxes = [self.boxs[0], self.boxs[1], self.boxs[2], self.boxs[3], self.boxs[4]]
        for newBox in self.boxs:
            #test it, and potentially move others back (99% chance it's sorted)
            box = newBox
            if abs(self.char.pos[1]-box.pos[1]) < abs(self.char.pos[1]-nearest5boxes[0].pos[1]):
                temp=nearest5boxes[0]
                nearest5boxes[0]=box
                box=temp
            if abs(self.char.pos[1]-box.pos[1]) < abs(self.char.pos[1]-nearest5boxes[1].pos[1]):
                temp=nearest5boxes[1]
                nearest5boxes[1]=box
                box=temp
            if abs(self.char.pos[1]-box.pos[1]) < abs(self.char.pos[1]-nearest5boxes[2].pos[1]):
                temp=nearest5boxes[2]
                nearest5boxes[2]=box
                box=temp
            if abs(self.char.pos[1]-box.pos[1]) < abs(self.char.pos[1]-nearest5boxes[3].pos[1]):
                temp=nearest5boxes[3]
                nearest5boxes[3]=box
                box=temp
            if abs(self.char.pos[1]-box.pos[1]) < abs(self.char.pos[1]-nearest5boxes[4].pos[1]):
                temp=nearest5boxes[4]
                nearest5boxes[4]=box
                box=temp
        for i in range(5):
            state[4+2*i] = 5+min(max(int((self.char.pos[0]-nearest5boxes[i].pos[0])/80), -5), 5)
            state[5+2*i] = 5+min(max(int((self.char.pos[1]-nearest5boxes[i].pos[1])/20), -5), 5)
        #print(state)
        '''
        state = np.fliplr(np.flip(np.rot90(pygame.surfarray.array3d(
            pygame.display.get_surface()).astype(np.uint8))))
        '''
        return state

    def finished(self):
        if self.char.pos[1] > self.screen_height:
            #print('fell off screen')
            return True
        if self.char.pos[0] < 0 - self.char.sprite.get_width() or self.char.pos[0] > self.screen_width:
            #print('went off side')
            return True
        if self.timer>200:
            #print('out of time')
            return True
        return False


