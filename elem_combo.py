from fight import Fight, FightObject
from params import *
import random
import some_func
import pygame as pg


class Combo(object):
    def __init__(self, func, combo_len, fight : Fight):
        self.func = func
        self.len = combo_len
        self.gen_combo()
        self.combo_progress = 0
        self.fight = fight
        fight.combos.append(self)

    def __del__(self):
        self.fight.combos.remove(self)

    def gen_combo(self):
        self.combo = [random.randint(0, ELEM_K-1) for i in range(self.len)]

    def element_activated(self, elem):
        if self.combo[self.combo_progress] == elem:
            self.combo_progress += 1
        else:
            self.combo_progress = 0
        if self.combo_progress == self.len:
            self.func()
            self.combo_progress = 0
            self.gen_combo()

    def draw(self, screen, pos):
        for i, c in enumerate(self.combo):
            color = POINT_COLORS[c]
            if i < self.combo_progress:
                color = some_func.color_mix(color, COLOR_BLACK)
            pg.draw.circle(screen,
                           color,
                           (pos[0] + COMBO_DRAW_RADIUS + COMBO_DRAW_OTSTUP*i,
                            pos[1] + COMBO_DRAW_RADIUS),
                            COMBO_DRAW_RADIUS)
