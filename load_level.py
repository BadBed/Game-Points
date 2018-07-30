import pygame as pg
from fight import Fight
from params import *
from player_intellect import PlayerIntellect
from player_soul import  PlayerSoul
from point import Point


def load_level():
    fight = Fight()
    fight.screen = pg.display.set_mode(SCREEN_SIZE)

    fight.points = [Point(fight, 0, 100, 100),
                    Point(fight, 1, 300, 100),
                    Point(fight, 2, 100, 300)]
    fight.player_soul = PlayerSoul(fight, fight.points[0])
    fight.player_intellect = PlayerIntellect(fight, fight.player_soul)
    return fight
