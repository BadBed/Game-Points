import fight
import pygame as pg
import collision


class PlayerIntellect(fight.FightObject):
    def __init__(self, player):
        super().__init__()
        self.player = player

    def event(self, fight, e):
        if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
            mdot = collision.Circle(e.pos[0], e.pos[1], 0)
            for p in fight.points:
                if collision.is_collide(mdot, p.get_form()):
                    self.player.command_move_to_point(p)
