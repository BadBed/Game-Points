import pygame as pg
from params import *


class Fight(object):
    def __init__(self):
        self.points = []
        self.enemies = []
        self.skills = []
        self.field_objects = []
        self.player = None
        self.screen = None

    def children(self):
        for p in self.points:
            yield p
        for e in self.enemies:
            yield e
        for o in self.field_objects:
            yield o
        yield self.player

    def run(self):
        while True:
            pg.timer.tick(FPS)

            for e in pg.event.get():
                self.event(e)

            self.update(1/FPS)
            self.draw(self.screen)

    def draw(self, screen):
        pg.draw.rect(screen, COLOR_BLACK, (0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))
        for c in self.children():
            c.draw(self, screen)
        pg.display.update()

    def update(self, dt):
        for c in self.children():
            c.update(self, dt)

    def event(self, e):
        for c in self.children():
            c.event(self, e)


class FightObject(object):
    def __init__(self):
        pass

    def update(self, fight, dt):
        pass

    def draw(self, fight, screen):
        pass

    def event(self, fight, event):
        pass
