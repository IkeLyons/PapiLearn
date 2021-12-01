import gym
from gym import spaces
import numpy as np
from PapiLearn.envs.PyGame2D import PyGame2D

class PapiLearnEnv(gym.Env):
    #metadata = {'render.modes': ['human']}
    def __init__(self):
        self.pygame = PyGame2D()
        self.action_space = spaces.Discrete(3)
        #this might work, but also might need to define better observation space
        self.observation_space = spaces.Box(low=0, high=255, shape=(self.pygame2d.screen_height, self.pygame2d.screen_width, 3), dtype=np.uint8)
    
    def reset(self):
        del self.PyGame2D
        self.pygame = PyGame2D()
        return self.pygame.observe()

    def step(self, action):
        pass

    def render(self, mode='human', close=False):
        self.pygame.view()
