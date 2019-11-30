#!/usr/bin/python3.6

from gym_snake.envs.Screen import Screen
from gym_snake.envs.Snake import Snake
from gym_snake.envs.Apple import Apple
import numpy as np
import gym
import time
import random
from gym import spaces

from math import *

def getAngleBetweenPoints(x_orig, y_orig, x_landmark, y_landmark):
    deltaY = y_landmark - y_orig
    deltaX = x_landmark - x_orig
    return atan2(deltaY, deltaX)/pi

class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, debug=True):

        self.debug = debug

        self.observation_space = spaces.Box(0, 1, (3, 30, 30))
        self.action_space = spaces.Box(0, 1, (4,))
        self.movements = np.array(['up', 'right', 'down', 'left'])

        self.screen = Screen(debug=debug)
        self.snake = Snake()
        self.apple = Apple(self.snake, dist=2)
        self.last_dist = None
        self.last_angle = getAngleBetweenPoints(*self.snake.body[0], *self.apple.position)

    def step(self, action):
        # move snake and set episode_over, if the game ends
        episode_over = False
        
        move = self.movements[action]

        try:
            self.snake.move(move)
        except ValueError:
            episode_over = True

        observation = self.calculate_state()
        
        reward = 0
        x1, y1 = self.apple.position
        x2, y2 = self.snake.body[0]
        
        dist = abs(x1-x2) + abs(y1-y2)

        if self.last_dist is None:
            self.last_dist = dist

        if self.last_dist > dist:
            reward = 0.1

        # calculate reward of the last action
        if self.snake.body[0] == self.apple.position:
            self.snake.expand() 
            reward = 10
            self.apple.spawn_apple()

        if episode_over:
            reward = -1000

        if self.debug:
            self.screen.debug_state(action, reward, episode_over)

        return observation, reward, episode_over, {}

    def render(self, mode='human', close=False):
        if close:
            self.close()

        try:
            self.screen.draw_background()
            self.screen.draw_apple(self.apple.position)
            self.screen.draw_body(self.snake.body)
            self.screen.update()
            
        except ValueError as e:
            pass

    def calculate_state(self):
        state = np.ones((4))
        field = np.zeros((30,30))

        for x,y in self.snake.body[1:]:
            field[x, y] = -1
        
        x,y = self.snake.body[0]
        for i, x_i, y_i in [(0,1,0),(1,-1,0),(2,0,1),(3,0,-1)]:
            try:
                state[i] = field[x+x_i, y+y_i]
            except IndexError:
                state[i] = -1

        a = getAngleBetweenPoints(*self.snake.body[0], *self.apple.position)
        angle = np.array([a])
        return np.concatenate((state, angle), axis=None)

    def reset(self):
        self.screen.reset()
        self.snake = Snake()
        self.apple.spawn_apple()
        self.last_dist = None
        self.last_angle = getAngleBetweenPoints(*self.snake.body[0], *self.apple.position)

        return self.calculate_state()
        