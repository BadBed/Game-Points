from fight import Fight, FightObject
from elem_combo import Combo
import random
import pygame as pg
from params import *


class Enemy(FightObject):
    MAX_HP = None
    ATTACK_COMBO_LEN = None

    def __init__(self, fight: Fight):
        super().__init__(fight)
        self.hp = self.MAX_HP
        self.combo = Combo(lambda: self.get_damage(10), self.ATTACK_COMBO_LEN, fight)

    def get_damage(self, dmg):
        self.hp -= dmg
        if (self.hp <= 0):
            self.die()

    def draw(self, screen):
        pos = self.fight.get_enemy_pos(self)
        self.draw_body(screen, pos)
        self.draw_hp(screen, pos)
        self.draw_combo(screen, pos)

    def draw_body(self, screen, pos):
        pg.draw.rect(screen, COLOR_GRAY,
                     pg.Rect(*pos, ENEMY_DRAW_WIDTH, ENEMY_DRAW_HEIGHT))

    def draw_hp(self, screen, pos):
        pos = (pos[0], pos[1] - HPBAR_OTSTUP)
        pg.draw.rect(screen, COLOR_RED, pg.Rect(*pos, HPBAR_WIDTH, HPBAR_HEIGHT))
        pg.draw.rect(screen, COLOR_GREEN,
                     pg.Rect(*pos, HPBAR_WIDTH*self.hp/self.MAX_HP, HPBAR_HEIGHT))

    def draw_combo(self, screen, pos):
        self.combo.draw(screen, (pos[0], pos[1] + ENEMY_DRAW_COMBO_OTSTUP))

    def die(self):
        self.fight.enemies.remove(self)


class DefaultEnemy(Enemy):
    MAX_HP = 100
    ATTACK_COMBO_LEN = 3
