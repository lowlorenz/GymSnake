import random

valid_keys = ['w', 'a', 's', 'd']

according_key = {
    'w': 's',
    'a': 'd',
    'd': 'a',
    's': 'w'
}

class SimpleBot:
    def __init__(self):
        self.last_key = 'd'

    def get_move(self):
        key = according_key[self.last_key]
        while key == according_key[self.last_key]:
            key = random.choice(valid_keys)
        self.last_key = key
        return self.last_key

