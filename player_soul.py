from params import *
import field
import collision
import some_func
import math
import pygame as pg


class PlayerSoul(field.FieldObject):
    RADIUS = 12
    SPEED = 300
    STAY = "Player stay condition"
    FLY = "Player fly condition"
    CONDITIONS = [STAY, FLY]

    SMALL_DRAW_RADIUS = 8
    SECOND_COLOR = COLOR_WHITE

    def __init__(self, fight, point):
        super().__init__(fight)
        self.catch_point(point)

    def command_move_to_point(self, point):
        if self.q == PlayerSoul.STAY and self.point != point:
            px = point.x
            py = point.y
            dx = px - self.x
            dy = py - self.y
            l = some_func.vector_length((dx, dy))
            self.vx = self.SPEED * dx / l
            self.vy = self.SPEED * dy / l
            self.q = PlayerSoul.FLY

    def draw(self, screen):
        pg.draw.circle(screen,
                       POINT_COLORS[self.element],
                       (math.ceil(self.x), math.ceil(self.y)),
                       self.RADIUS)
        pg.draw.circle(screen,
                       self.SECOND_COLOR,
                       (math.ceil(self.x), math.ceil(self.y)),
                        self.SMALL_DRAW_RADIUS)

    def update(self, dt):
        self.move(dt)
        if self.q == PlayerSoul.FLY:
            self.try_catch_point()

    def try_catch_point(self):
        for p in self.fight.points:
            if p != self.point and\
                    collision.is_collide(collision.dot(self.x, self.y),
                                         p.get_form()):
                self.catch_point(p)

    def catch_point(self, p):
        self.x = p.x
        self.y = p.y
        self.vx = self.vy = 0
        self.point = p
        self.element = p.element
        self.q = PlayerSoul.STAY

        for combo in self.fight.combos:
            combo.element_activated(self.element)

    def get_form(self):
        return collision.Circle(self.x, self.y, self.RADIUS)
