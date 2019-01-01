import pygame as pg
from params import *


class Fight(object):
    def __init__(self):
        self.points = []
        self.enemies = []
        self.skills = []
        self.other_objects = []
        self.combos = []
        self.player_soul = None
        self.player_intellect = None

        self.screen = None

    def children(self):
        for p in self.points:
            yield p
        for e in self.enemies:
            yield e
        for o in self.other_objects:
            yield o
        yield self.player_soul
        yield self.player_intellect

    def run(self):
        clock = pg.time.Clock()
        while True:
            clock.tick(FPS)

            for e in pg.event.get():
                self.event(e)

            self.update(1/FPS)
            self.draw(self.screen)

    def draw(self, screen):
        pg.draw.rect(screen, COLOR_BLACK, (0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))
        for c in self.children():
            c.draw(screen)
        pg.draw.rect(screen, COLOR_WHITE, pg.Rect(*FIELD_BEGIN, *FIELD_SIZE), 5)
        pg.display.update()

    def update(self, dt):
        for c in self.children():
            c.update(dt)

    def event(self, e):
        for c in self.children():
            c.event(e)

    def get_enemy_pos(self, e):
        i = self.enemies.index(e)
        return (ENEMY_DRAW_POSITION_X + ENEMY_DRAW_POSITION_DX*i,
                ENEMY_DRAW_POSITION_Y)


class FightObject(object):
    def __init__(self, fight):
        self.fight = fight

    def update(self, dt):
        pass

    def draw(self, screen):
        pass

    def event(self, event):
        pass
