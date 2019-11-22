import random

class Apple:

    def __init__(self, snake):
        self.snake = snake
        self.spawn_apple()

    def spawn_apple(self): 
        pos = (random.randint(0,29), random.randint(0,29))

        while pos in self.snake.body:
            pos = (random.randint(0,29), random.randint(0,29))

        self.position = pos