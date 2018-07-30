from fight import Fight, FightObject
from params import *
import random


class Combo(object):
    def __init__(self, func, combo_len):
        self.func = func
        self.len = combo_len
        self.gen_combo()
        self.combo_progress = 0

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