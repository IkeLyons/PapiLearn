import gym
from gym import spaces
import numpy as np
from PapiLearn.envs.PyGame2D import PyGame2D

class PapiLearnEnv(gym.Env):
    #metadata = {'render.modes': ['human']}
    def __init__(self):
        self.pygame = PyGame2D()
        #left, right, or no action
        self.action_space = spaces.Discrete(2)
        #this might work, but also might need to define better observation space
        #self.observation_space = spaces.Box(low=0, high=255, shape=(self.pygame.screen_height, self.pygame.screen_width, 3), dtype=np.uint8)
        self.observation_space = spaces.Box(low=0, high = 10, shape=(14,), dtype=np.uint8)
    
    def reset(self):
        del self.pygame
        self.pygame = PyGame2D()
        self.pygame.char.yspeed=-5
        return self.pygame.observe()

    def step(self, action):
        self.pygame.act(action)
        obs = self.pygame.observe()
        reward = self.pygame.eval()
        done = self.pygame.finished()
        return obs, reward, done, {}

    def render(self, mode='human', close=False):
        self.pygame.view()
