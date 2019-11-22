from gym_snake.envs.Screen import Screen
from gym_snake.envs.Snake import Snake
from gym_snake.envs.Gameinterfaces import Gameinterface, BotGameinterface
from gym_snake.envs.Apple import Apple
import numpy as np
import gym
import time
import random

class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.movements = np.array(['up', 'right', 'down', 'left'])
        self.screen = Screen()
        self.snake = Snake()
        self.apple = Apple(self.snake)


    def step(self, action):
        reward = 0
        # calculate reward of the last action
        if self.snake.body[0] == self.apple.position:
            self.snake.expand() 
            reward = 1
            self.apple.spawn_apple()

        # move snake and set episode_over, if the game ends
        episode_over = False
        move = self.movements[action.astype(bool)][0]
        try:
            self.snake.move(move)
        except ValueError as e:
            episode_over = True


        state = self.calculate_state()
        
        return state, reward, episode_over, {}

    def _reset(self):
        pass

    def render(self, mode='human', close=False):
        try:
            self.screen.draw_background()
            self.screen.draw_apple(self.apple.position)
            self.screen.draw_body(self.snake.body)
            self.screen.update()
        except ValueError as e:
            pass

    def calculate_state(self):
        state = np.zeros((3,30,30), dtype=bool)
        # represent the current state of the snake game as an numpy array
        # set snake head
        x,y = self.snake.body[0]
        state[0,x,y] = True

        # set snake body
        for x,y in self.snake.body[1:]:
            state[1,x,y] = True

        # set apple
        x,y = self.apple.position
        state[2,x,y] = True

        return state

    def reset(self):
        self.screen = Screen
        self.snake = Snake()
        self.apple.spawn_apple()
        