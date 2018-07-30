from fight import Fight, FightObject
from elem_combo import Combo
import random
from params import *


class Enemy(FightObject):
    MAX_HP = None
    ATTACK_COMBO_LEN = None

    def __init__(self, fight):
        super().__init__(fight)
        self.hp = self.MAX_HP
        self.combo = Combo(lambda: self.get_damage(10), self.ATTACK_COMBO_LEN)

    def get_damage(self, dmg):
        self.hp -= dmg

    def draw(self, screen):
        self.draw_body(screen)
        self.draw_hp(screen)
        self.draw_combo(screen)


class DefaultEnemy(Enemy):
    MAX_HP = 100
    ATTACK_COMBO_LEN = 3
