from params import *
import field
import collision
import some_func
import math
import pygame as pg

STAY = "Player stay condition"
FLY = "Player fly condition"


class PlayerSoul(field.FieldObject):
    RADIUS = 12
    SPEED = 6
    CONDITIONS = [STAY, FLY]
    FORM = collision.Circle(RADIUS)

    SMALL_DRAW_RADIUS = 8
    SECOND_COLOR = COLOR_WHITE

    def __init__(self, point):
        super().__init__()
        self.point = point
        self.x = point.x
        self.y = point.y
        self.element = point.element
        self.q = STAY
        self.form = self.FORM

    def command_move_to_point(self, point):
        if self.q == STAY and self.point != point:
            px = point.x
            py = point.y
            dx = px - self.x
            dy = py - self.y
            l = some_func.vector_length((dx, dy))
            self.vx = self.SPEED * dx / l
            self.vy = self.SPEED * dy / l
            self.q = FLY

    def draw(self, fight, screen):
        pg.draw.circle(screen,
                       POINT_COLORS[self.element],
                       (math.ceil(self.x), math.ceil(self.y)),
                       self.RADIUS)
        pg.draw.circle(screen,
                       COLOR_WHITE,
                       (math.ceil(self.x), math.ceil(self.y)),
                        self.SMALL_DRAW_RADIUS)

    def update(self, fight, dt):
        self.move(dt)
        if self.q == FLY:
            self.try_catch_point(fight)

    def try_catch_point(self, fight):
        for p in fight.points:
            if collision.is_collide(self, p):
                self.catch_point(p)

    def catch_point(self, p):
        self.x = p.x
        self.y = p.y
        self.vx = self.vy = 0
        self.point = p.index
        self.element = p.element
        self.q = STAY
