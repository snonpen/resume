

import numpy as np
import gym
import random

env = gym.make('CartPole-v1')
state_space = env.observation_space.shape[0]
action_space = env.action_space.n

q_table = np.zeros((state_space, action_space))

total_episodes = 5000
learning_rate = 0.8
max_steps = 500
gamma = 0.95

epsilon = 1.0
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.01

for episode in range(total_episodes):
    state, info = env.reset()
    state = np.array(state)
    state = state.reshape(1, state_space) 

    done = False
    rewards = 0
    for step in range(max_steps):
        if random.uniform(0, 1) > epsilon:
            action = np.argmax(q_table[np.int32(state), :])
        else:
            action = env.action_space.sample()

        new_state, reward, done, info, _ = env.step(action)
        new_state = new_state.reshape(1, state_space)  

        q_table[np.int32(state), np.int32(action)] = q_table[np.int32(state), np.int32(action)] + learning_rate * (reward + gamma * np.max(q_table[np.int32(new_state), :]) - q_table[np.int32(state), np.int32(action)])
        

        rewards += reward
        state = new_state
        if done:
            break

    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

print("Q-table:\n", q_table , "\nReward", rewards)
