import gym
import PapiLearn
import pygame
# env = gym.make('MountainCar-v0')
env = gym.make('PapiLearn-v0')
import time 

# Number of steps you run the agent for 
num_steps = 1500

# for step in range(num_steps):
#     # take random action, but you can also do something more intelligent
#     # action = my_intelligent_agent_fn(obs) 
#     action = env.action_space.sample()
    
#     # apply the action
#     obs, reward, done, info = env.step(action)
    
#     # Render the env
#     env.render()

#     # Wait a bit before the next frame unless you want to see a crazy fast video
#     time.sleep(0.001)
    
#     # If the epsiode is up, then start another one
#     if done:
#         env.reset()


# basic game loop for testing

obs = env.reset()
action = 2
while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                action = 1
            if event.key == pygame.K_RIGHT:
                action = 0
            if event.key == pygame.K_UP:
                action = 2
    obs, reward, done, info = env.step(action)
    env.render()
    time.sleep(0.01)
    if done:
        obs = env.reset()


# Close the env
env.close()