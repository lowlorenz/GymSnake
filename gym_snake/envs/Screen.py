from tkinter import *

class Screen:

    def __init__(self, debug = False):
        self.master = Tk()

        self.canvas_width = 600
        self.canvas_height = 600

        self.screen = Canvas(self.master, 
                width=self.canvas_width,
                height=self.canvas_height)

        self.draw_background()
        self.screen.pack()

        self.debug = debug
        if debug:
            self.debug_Label = Label(self.master)
            self.debug_Label.pack()

    def draw_background(self):
        self.screen.create_rectangle(0,0, self.canvas_width+1, self.canvas_height+1, fill='gray')

    def debug_state(self, action ,reward, episode_over):
        if self.debug:
            self.debug_Label['text'] = 'Action: {}\nReward: {}\nEpisode over: {}'.format(action, reward, episode_over)

    def draw_head(self, point):
        self.check_position_boundings(point)
        x,y = point
        y = 29 - y
        self.screen.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill="yellow")

    def draw_body(self, point_list):
        if len(point_list) == 0:
            raise ValueError("Pointlist is empty")
        
        self.draw_head(point_list[0])

        if len(point_list) == 1:
            return
    
        for p in point_list[1:]:
            x,y = p
            y = 29 - y
            self.screen.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill="orange")

    def draw_apple(self, point):
        self.check_position_boundings(point)
        x,y = point
        y = 29 - y
        self.screen.create_rectangle(x*20, y*20, (x+1)*20, (y+1)*20, fill="red")

    def check_position_boundings(self, point):
        x,y = point
        y = 29 - y
        if x < 0:
            raise ValueError("X value is too small")
        if x >= 30:
            raise ValueError("X value is too high")
        if y < 0:
            raise ValueError("Y value is too small")
        if y >= 30:
            raise ValueError("Y value is too high")
    
    def update(self):
        self.screen.update()
        self.screen.delete('ALL')
        
    def reset(self):
        if self.debug:
            self.debug_Label['text'] = ''
        self.screen.delete('ALL')
        self.draw_background()    

    def close(self):
        self.screen.delete('ALL')
        self.master.destroy()