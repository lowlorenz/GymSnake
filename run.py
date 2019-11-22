from Screen import Screen
from Snake import Snake
from Gameinterfaces import Gameinterface, BotGameinterface
from Apple import Apple
import time
import random

player = 'AI'

movements = {
    'w': 'up',
    's': 'down',
    'd': 'right',
    'a': 'left'
}

frametime = 0.1

screen = Screen()
snake = Snake()

gameinterface = Gameinterface(screen) if player == 'human' else BotGameinterface(screen)
apple = Apple(snake)

last_valid_key = 'd'

screen.draw_background()
screen.draw_apple(apple.position)
screen.draw_body(snake.body)
screen.update()

time.sleep(frametime)
while True:

    start = time.time()

    if snake.body[0] == apple.position:
        snake.expand() 
        gameinterface.score += 1
        apple.spawn_apple()

    key = gameinterface.get_move()
    if key in ['q', 'a', 'w', 's', 'd']:
        last_valid_key = key

    if last_valid_key == 'q':
        break

    try:
        snake.move(movements.get(last_valid_key))
        screen.draw_background()
        screen.draw_apple(apple.position)
        screen.draw_body(snake.body)
        screen.update()
    except ValueError as e:
        print(e)
        print('Score: {}'.format(len(snake.body)-2))
        break
    
    gameinterface.tick += 1
    end = time.time()
    time.sleep(frametime - end + start)