import random

class Apple:

    def __init__(self, snake, dist=29):
        self.snake = snake
        self.spawn_apple(dist=dist)

    def spawn_apple(self, dist=29): 
        if dist >= 29:
            dist = 29
        pos = (random.randint(0,dist), random.randint(0,dist))

        while pos in self.snake.body:
            pos = (random.randint(0,dist), random.randint(0,dist))

        self.position = pos
