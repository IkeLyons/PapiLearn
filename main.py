import gym
import PapiLearn
import pygame
# env = gym.make('MountainCar-v0')
env = gym.make('PapiLearn-v0')
import time 
import numpy as np
import math

# Number of steps you run the agent for 
num_steps = 1500

# The basis for the Q-learning algorithm was inspired by the link below, 
# but we made multiple changes due to the vastly larger dimensionality of our problem
# [https://towardsdatascience.com/getting-started-with-reinforcement-learning-and-open-ai-gym-c289aca874f]

# Define Q-learning function
def QLearning(env, learning, discount, epsilon, min_eps, episodes):
    # Determine size of discretized state space
    num_states = (env.observation_space.high - env.observation_space.low)*\
        np.array(([0.5, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0, 0, 0, 0]))
    num_states = np.round(num_states, 0).astype(int) + 1
    print("Starting Q-Learning...")
    #print(num_states)
    #print(num_states.shape())
    #print((math.pow(2, 40*70),
    #                              env.action_space.n))
    
    # Initialize Q table
    Q = np.random.uniform(low = -1, high = 1, 
                          size = (6, 6, 6, 6, 6, 6, 6, 6, 6, 
                                  env.action_space.n))
    
    #print(Q[0,0,0,0,0,0,0,0,0,0])
    # Initialize variables to track rewards
    reward_list = []
    ave_reward_list = []
    
    # Calculate episodic reduction in epsilon
    reduction = (epsilon - min_eps)/episodes
    
    # Run Q learning algorithm
    for i in range(episodes):
        # Initialize parameters
        done = False
        tot_reward, reward = 0,0
        state = env.reset()
        
        # Discretize state
        state_adj = (state - env.observation_space.low)*np.array(([0.5, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0, 0, 0, 0]))
        state_adj = np.round(state_adj, 0).astype(int)
    
        while done != True:   
            # Render environment for last five episodes
            if i >= 0:#(episodes - 20):
                env.render()
                
            # Determine next action - epsilon greedy strategy
            if np.random.random() < 1 - epsilon:
                action = np.argmax(Q[state_adj[0], state_adj[2], state_adj[3], state_adj[4], state_adj[5], state_adj[6], state_adj[7], state_adj[8], state_adj[9]]) 
            else:
                action = np.random.randint(0, env.action_space.n)
                
            # Get next state and reward
            state2, reward, done, info = env.step(action) 
            
            # Discretize state2
            state2_adj = (state2 - env.observation_space.low)*np.array(([0.5, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0, 0, 0, 0]))
            state2_adj = np.round(state2_adj, 0).astype(int)
            
            #Allow for terminal states
            if done and state2[0] >= 0.5:
                Q[state_adj[0], state_adj[2], state_adj[3], state_adj[4], state_adj[5], state_adj[6], state_adj[7], state_adj[8], state_adj[9], action] = reward
                
            # Adjust Q value for current state
            else:
                #print(Q[state_adj[0], state_adj[2], state_adj[3], state_adj[4], state_adj[5], state_adj[6], state_adj[7], state_adj[8], state_adj[9]])
                delta = learning*(reward + 
                                 discount*np.max(Q[state_adj[0], state_adj[2], state_adj[3], state_adj[4], state_adj[5], state_adj[6], state_adj[7], state_adj[8], state_adj[9]]) - 
                                 Q[state_adj[0], state_adj[2], state_adj[3], state_adj[4], state_adj[5], state_adj[6], state_adj[7], state_adj[8], state_adj[9],action])
                Q[state_adj[0], state_adj[2], state_adj[3], state_adj[4], state_adj[5], state_adj[6], state_adj[7], state_adj[8], state_adj[9],action] += delta
                                     
            # Update variables
            tot_reward += reward
            state_adj = state2_adj
        
        # Decay epsilon
        if epsilon > min_eps:
            epsilon -= reduction
        
        # Track rewards
        reward_list.append(tot_reward)
        
        if (i+1) % 40 == 0:
            ave_reward = np.mean(reward_list)
            ave_reward_list.append(ave_reward)
            reward_list = []
            
        if (i+1) % 40 == 0:    
            print('Episode {} Average Reward: {}'.format(i+1, ave_reward))
            
    env.close()
    
    return ave_reward_list, Q



loadedQs = np.fromfile('myQ2.txt', dtype=float)
obs = env.reset()
obs, reward, done, info = env.step(2)
# basic game loop for testing
for step in range(num_steps):
     # take random action, but you can also do something more intelligent
     # action = my_intelligent_agent_fn(obs) 
     # action = env.action_space.sample()
     # unflatten array
     index = math.pow(6, 8)*int(obs[0]*0.5) + math.pow(6, 7)*int(obs[2]*0.5) + math.pow(6, 6)*int(obs[3]*0.5) + math.pow(6, 5)*int(obs[4]*0.5) + math.pow(6, 4)*int(obs[5]*0.5) + math.pow(6, 3)*int(obs[6]*0.5) + math.pow(6, 2)*int(obs[7]*0.5) + math.pow(6, 1)*int(obs[8]*0.5) + math.pow(6, 0)*int(obs[9]*0.5)
     index = int(index)
     if (loadedQs[index*3]>loadedQs[index*3+1] and loadedQs[index*3]>loadedQs[index*3+2]):
        action = 0
     elif (loadedQs[index*3+1]>loadedQs[index*3] and loadedQs[index*3+1]>loadedQs[index*3+2]):
        action = 1
     else:
        action=2
   
     # apply the action
     obs, reward, done, info = env.step(action)
   
     # Render the env
     env.render()
     # Wait a bit before the next frame unless you want to see a crazy fast video
     time.sleep(0.001)
    
     # If the epsiode is up, then start another one
     if done:
         env.reset()
obs = env.reset()



# Run Q-learning algorithm
'''
rewards, Q = QLearning(env, 0.2, 0.9, 0.8, 0, 5000)

Q.tofile('myQ2.txt')
Q2 = np.fromfile('myQ2.txt', dtype=float)
Q=Q.flatten()
print(Q[0])
print(Q2[0])
print(Q == Q2)
'''


# Human mode
'''
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
'''