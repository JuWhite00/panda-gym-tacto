# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:24:08 2022

@author: bouff
"""

import panda_gym
import gymnasium as gym 
from panda_gym.envs.panda_tasks import DoosanTest


env = DoosanTest(render= True)

observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()
        
env.close()