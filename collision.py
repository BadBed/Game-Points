import pygame as pg
import some_func

RECT_FORM = "Rectangle"
CIRCLE_FORM = "Circle"


class Rect(object):
    def __init__(self, h, w):
        self.type = RECT_FORM
        self.h = h
        self.w = w


class Circle(object):
    def __init__(self, r):
        self.type = CIRCLE_FORM
        self.r = r


def is_collide(o1, o2):
    if o1.form.type == CIRCLE_FORM and o2.form.type == RECT_FORM:
        return some_func.vector_length(pos1, pos2) <= o1.r + form2.r
    else:
        raise Exception("Can't cross this objects with forms: "
                        + str(form1.type) + " and " + str(form2.type))
