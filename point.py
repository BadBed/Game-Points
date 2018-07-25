import pygame as pg
from params import *
import field
import collision
import math


class Point(field.FieldObject):
    RADIUS = 20

    def __init__(self, element, x=0, y=0):
        super().__init__(x, y)
        self.element = element
        self.color = POINT_COLORS[element]

    def draw(self, fight, screen):
        pg.draw.circle(screen,
                       self.color,
                       (math.ceil(self.x), math.ceil(self.y)),
                       self.RADIUS)

    def get_form(self):
        return collision.Circle(self.x, self.y, self.RADIUS)
