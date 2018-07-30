from fight import Fight, FightObject
import pygame as pg
import collision
from player_soul import PlayerSoul


class PlayerIntellect(FightObject):
    def __init__(self, fight: Fight, soul: PlayerSoul):
        super().__init__(fight)
        self.soul = soul
        self.next_point = None

    def event(self, e):
        if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
            mdot = collision.Circle(e.pos[0], e.pos[1], 0)
            for p in self.fight.points:
                if collision.is_collide(mdot, p.get_form()):
                    self.next_point = p


    def update(self, dt):
        if not self.next_point is None and self.soul.q == PlayerSoul.STAY:
            self.soul.command_move_to_point(self.next_point)
