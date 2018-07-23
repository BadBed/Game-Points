import fight
from params import *


class FieldObject(fight.FightObject):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.vx = self.vy = 0

    def update(self, fight, dt):
        self.move(dt)

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
