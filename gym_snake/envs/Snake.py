
class Snake:
    def __init__(self):
        self.body = [(10,10),(10,11)]
        self.add_cell = False


    def move(self, direction):
        x,y = self.body[0]
        new_head = None

        if direction == 'left':
            if x-1 < 0:
                raise ValueError('Snake dies to the left wall')
            new_head = (x-1, y)

        if direction == 'right':
            if x+1 >= 30:
                raise ValueError('Snake dies to the right wall')
            new_head = (x+1, y)

        if direction == 'down':
            if y-1 < 0:
                raise ValueError('Snake dies to the bottom wall')
            new_head = (x, y-1)
            
        if direction == 'up':
            if y+1 >= 30:
                raise ValueError('Snake dies to the upper wall')
            new_head = (x, y+1)


        if new_head in self.body[1:]:
            raise ValueError('Snake dies because it bites itself')

        if self.add_cell:
            self.body = [new_head] + self.body
        else: 
            self.body = [new_head] + self.body[:-1]
        
        self.add_cell = False


    def expand(self):
        self.add_cell = True