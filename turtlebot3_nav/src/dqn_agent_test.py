#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import numpy as np
import math
from math import pi
import os
import json
import sys
import time
import random
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from std_msgs.msg import Float32MultiArray
from collections import deque
from dqn_env import Environment
from keras.models import Sequential, load_model
from keras.optimizers import RMSprop, Adam
from keras.layers.core import Dense, Dropout, Activation


EPISODES = 3000


class DQLAgent:

    def __init__(self, state_size, action_size):
        self.pub_result = rospy.Publisher('result', Float32MultiArray, queue_size=5)
        self.dirPath = os.path.dirname(os.path.realpath(__file__))
        self.dirPath = self.dirPath.replace('turtlebot3_nav/src', 'turtlebot3_nav/src/save_model/dqn_agent_')
        self.result = Float32MultiArray()

        self.load_model = True
        self.load_episode = 10
        self.state_size = state_size
        self.action_size = action_size
        self.episode_step = 500
        self.discount_factor = 0.95
        self.learning_rate = 0.001

        self.model = self.buildModel()

        if self.load_model:
            self.model.set_weights(load_model(self.dirPath + str(self.load_episode) + ".h5").get_weights())

    def buildModel(self):
        model = Sequential()
        dropout = 0.2

        model.add(Dense(64, input_shape=(self.state_size,), activation='relu', kernel_initializer='lecun_uniform'))

        model.add(Dense(64, activation='relu', kernel_initializer='lecun_uniform'))
        model.add(Dropout(dropout))

        model.add(Dense(self.action_size, kernel_initializer='lecun_uniform'))
        model.add(Activation('linear'))
        model.compile(loss='mse', optimizer=RMSprop(lr=self.learning_rate, rho=0.9, epsilon=1e-06))
        model.summary()

        return model

    def getQvalue(self, reward, next_target, done):
        if done:
            return reward
        else:
            return reward + self.discount_factor * np.amax(next_target)

    def getAction(self, state):
        q_value = self.model.predict(state.reshape(1, len(state)))
        self.q_value = q_value
        return np.argmax(q_value[0])        
        

if __name__ == "__main__":
    rospy.init_node('dqn_agent_test')
    pub_result = rospy.Publisher('result', Float32MultiArray, queue_size=5)
    pub_get_action = rospy.Publisher('get_action', Float32MultiArray, queue_size=5)
    result = Float32MultiArray()
    get_action = Float32MultiArray()
    
    state_size = 28
    action_size = 5
    
    agent = DQLAgent(state_size, action_size)
    scores, episodes = [], []
    global_step = 0
    start_time = time.time()
    
    env = Environment(action_size)
    
    result.data = [0, 0]
    pub_result.publish(result)

    for e in range(agent.load_episode + 1, EPISODES):
        done = False
        state = env.reset()
        score = 0

        for t in range(agent.episode_step):
            action = agent.getAction(state)
            next_state, reward, done = env.step(action)
            
            score += reward
            state = next_state
            get_action.data = [action, score, reward]
            pub_get_action.publish(get_action)
            
            if done:
                result.data = [score, np.max(agent.q_value)]
                pub_result.publish(result)
                break