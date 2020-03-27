import pygame as pg
from pygame.locals import *


class Game(object):
    def __init__(self):
        super().__init__()

        self.quit = False

    def event_loop(self):
        for event in pg.events.get():
            if event.type == QUIT:
                self.quit = True

    def update(self):
        pass

    def draw(self):
        pass

    def game(self):
        while not self.quit:
            self.event_loop()
            self.update()
            self.draw()


class Cell(object):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pg.Vector2(x, y)
        
