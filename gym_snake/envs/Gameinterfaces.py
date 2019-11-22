from gym_snake.envs.Bot import SimpleBot

class Gameinterface:

    def __init__(self, screen):
        self.screen = screen
        self.tick = 0
        self.score = 0

    def get_move(self):
        return self.screen.key

    def get_field(self):
        pass

class BotGameinterface(Gameinterface):

    def __init__(self, screen):
        super().__init__(screen)
        self.bot = SimpleBot()
        self.get_move = self.bot.get_move

