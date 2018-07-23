import pygame as pg
from params import *
import field
import collision


class Point(field.FieldObject):
    RADIUS = 20

    FORM = collision.Circle(RADIUS)

    def __init__(self, element, x=0, y=0, index=-1):
        super().__init__(x, y)
        self.element = element
        self.color = POINT_COLORS[element]
        self.form = Point.FORM
        self.index = index

    def draw(self, fight, screen):
        pg.draw.circle(screen,
                       self.color,
                       (self.x, self.y),
                       self.RADIUS)
