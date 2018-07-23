import pygame as pg
import math
import random
from params import *


class Game_Object():
    FORM = "Circle"
    RADIUS = 0
    SIZE_X = 0
    SIZE_Y = 0

    def __init__(self, x=0, y=0):
        self.init_game_object(x, y)

    def init_game_object(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.live = True
        self.color = (255, 255, 255)

    def draw(self, screen):
        self.draw_circle(screen)

    def draw_circle(self, screen):
        draw.circle(screen, self.color, (math.ceil(self.x),
                                         math.ceil(self.y)), self.RADIUS)

    def draw_sprite(self, screen):
        screen.blit(self.pic, (self.x, self.y))

    def update(self):
        self.move()

    def move(self):
        self.x += self.vx
        self.y += self.vy


class List_Of_Objects():
    def __init__(self):
        self.a = []

    def add(self, obj):
        self.a.append(obj)
        self.a[-1].index = len(self.a) - 1
        print("Element added, size: ", len(self.a))

    def use_function(self, f):
        for i in range(len(self.a)):
            l_break = f(self.a[i])
            if l_break == False:
                break

    def update(self):
        for i in range(len(self.a)):
            self.a[i].update()
        anew = []
        for i in self.a:
            if i.live:
                anew.append(i)
        self.a = anew

    def event(self, e):
        for i in range(len(self.a)):
            self.a[i].event(e)

    def draw(self, screen):
        for i in range(len(self.a)):
            self.a[i].draw(screen)


class Enemy(Game_Object):
    HP = 100
    pic = image.load("sprites/enemy.jpg")
    HIT_COMBO_MAX = 5
    HIT_COMBO_MIN = 3

    D_HCOM_RADIUS = 5
    D_HCOM_DIST = 12
    D_HCOM_X0 = 8
    D_HCOM_Y0 = 56
    D_HP_X0 = 0
    D_HP_Y0 = 0
    D_HP_W = 10
    D_HP_H = 10

    def __init__(self, x=0, y=0):
        self.init_game_object(x, y)
        self.init_enemy()

    def init_enemy(self):
        self.hp = self.HP
        self.hit_combo = [-1] * self.HIT_COMBO_MAX
        self.gen_hit_combo()

    def gen_hit_combo(self):
        global ELEM_K
        for i in range(self.HIT_COMBO_MAX):
            self.hit_combo[i] = random.randint(0, ELEM_K - 1)

    def gen_hit_combo_spec(self):
        global ELEM_K
        for i in range(self.HIT_COMBO_MAX):
            if i == 0:
                self.hit_combo[i] = random.randint(0, ELEM_K - 1)
            else:
                self.hit_combo[i] = randint_without(0,
                                                    ELEM_K - 1,
                                                    self.hit_combo[i - 1])

    def draw(self, screen):
        self.draw_sprite(screen)
        self.draw_hit_combo(screen)
        self.draw_hp(screen)

    def draw_hit_combo(self, screen):
        global POINT_COLORS
        for i in range(self.HIT_COMBO_MAX):
            pos = (self.x + self.D_HCOM_X0 + i * self.D_HCOM_DIST,
                   self.y + self.D_HCOM_Y0)
            draw.circle(screen, POINT_COLORS[self.hit_combo[i]],
                        pos, self.D_HCOM_RADIUS)

    def draw_hp(self, screen):
        x = self.D_HP_X0 + self.x
        y = self.D_HP_Y0 + self.y
        w = self.D_HP_W
        h = self.D_HP_H
        draw.rect(screen, COLOR_RED, (x, y, w, h))
        draw.rect(screen, COLOR_GREEN, (x, y, w * self.hp / self.HP, h))


###########################################################################


def load_level(a):
    global list_of_points, playersoul
    list_of_points = List_Of_Objects()

    i = 0
    n = int(a[i])
    i += 1
    for j in range(n):
        list_of_points.add(Point(x=int(a[i]), y=int(a[i + 1]),
                                 element=int(a[i + 2])))
        i += 3

    playersoul = Player_Soul(int(a[i]))
    i += 1


pygame.init()
FPS = 60
screen = pygame.display.set_mode(DISPLAY_MODE)
timer = pygame.time.Clock()
game()
