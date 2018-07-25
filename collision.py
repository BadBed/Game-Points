import pygame as pg
import some_func

RECT_FORM = "Rectangle"
CIRCLE_FORM = "Circle"


class Rect(object):
    def __init__(self, x, y, h, w):
        self.type = RECT_FORM
        self.x = x
        self.y = y
        self.h = h
        self.w = w


class Circle(object):
    def __init__(self, x, y, r):
        self.type = CIRCLE_FORM
        self.x = x
        self.y = y
        self.r = r


def is_collide(form1, form2):
    if form1.type == CIRCLE_FORM and form2.type == CIRCLE_FORM:
        return some_func.vector_length((form1.x, form1.y), (form2.x, form2.y))\
               <= form1.r + form2.r
    else:
        raise Exception("Can't cross this objects with forms: "
                        + str(form1.type) + " and " + str(form2.type))
