import pygame
from pygame import *
import math
import random

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
POINT_COLORS = [COLOR_RED, COLOR_GREEN, COLOR_BLUE]

DISPLAY_MODE = (1024, 768)
ELEM_K = 3

FILE_LEVELS = ["levels\\lvl1.txt"]

class Game_Object():
	FORM = "Circle"
	RADIUS = 0
	SIZE_X = 0
	SIZE_Y = 0

	def __init__ (self, x=0, y=0):
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
	def draw_circle (self, screen):
		draw.circle(screen, self.color, (math.ceil(self.x), math.ceil(self.y)), self.RADIUS)
	def draw_sprite (self, screen):
		screen.blit(self.pic, (self.x, self.y))
	
	def update (self):
		self.move()
	def move (self):
		self.x += self.vx
		self.y += self.vy

class Point(Game_Object):
	RADIUS = 20
	def __init__ (self, element, x = 0, y = 0, index = -1):
		global POINT_COLORS
		self.x = x
		self.y = y
		self.element = element
		self.color = POINT_COLORS[element]
		self.index = index

	def event(self, e):
		if e.type == MOUSEBUTTONDOWN and e.button == 1:
			global playersoul
			if playersoul.point != self.index and vector_length(e.pos, (self.x, self.y)) < self.RADIUS:
				playersoul.move_to_point(self.index)

class Player_Soul(Game_Object):
	RADIUS = 12
	SMALL_DRAW_RADIUS = 8
	V = 6
	

	def __init__(self, v):
		self.init_game_object(x = 0, y = 0)
		self.init_player_soul(v)
	def init_player_soul(self, v):
		global list_of_points
		self.x = list_of_points.a[v].x
		self.y = list_of_points.a[v].y
		self.element = list_of_points.a[v].element
		self.color = COLOR_WHITE
		self.q = "stay"#stay fly
		self.element = 0
		self.point = 0

	def move_to_point(self, v):
		if self.q == "stay" and self.point != v:
			global list_of_points
			px = list_of_points.a[v].x
			py = list_of_points.a[v].y
			dx = px - self.x
			dy = py - self.y
			l = (dx**2 + dy**2)**0.5
			self.vx = self.V*dx/l
			self.vy = self.V*dy/l
			self.q = "fly"

	def draw(self, screen):
		self.color_update()
		self.draw_circle(screen)
		draw.circle(screen, COLOR_WHITE, (math.ceil(self.x), math.ceil(self.y)), self.SMALL_DRAW_RADIUS)
	def color_update(self):
		global POINT_COLORS
		self.color = POINT_COLORS[self.element]

	def update(self):
		self.move()
		self.try_catch_point()
	def try_catch_point(self):
		global list_of_points
		for p in list_of_points.a:
			if vector_length((p.x, p.y), (self.x, self.y)) <= self.RADIUS and self.point != p.index:
				self.catch_point(p)
	def catch_point(self, p):
		self.x = p.x
		self.y = p.y
		self.vx = self.vy = 0
		self.point = p.index
		self.element = p.element
		self.q = "stay"

		global controller
		controller.hit_ball(p.element)

class List_Of_Objects():
	def __init__(self):
		self.a = []

	def add(self, obj):
		self.a.append(obj)
		self.a[-1].index = len(self.a)-1
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
			

class Game_Controller:
	def __init__(self):
		pass
		#print("i am created")

	def hit_ball(self, element):
		pass

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

	def __init__(self, x = 0, y = 0):
		self.init_game_object(x, y)
		self.init_enemy()
	def init_enemy(self):
		self.hp = self.HP
		self.hit_combo = [-1]*self.HIT_COMBO_MAX
		self.gen_hit_combo()
		
	def gen_hit_combo(self):
		global ELEM_K
		for i in range(self.HIT_COMBO_MAX):
			self.hit_combo[i] = random.randint(0, ELEM_K-1)
	def gen_hit_combo_spec(self):
		global ELEM_K
		for i in range(self.HIT_COMBO_MAX):
			if i == 0:
				self.hit_combo[i] = random.randint(0, ELEM_K-1)
			else:
				self.hit_combo[i] = randint_without(0, ELEM_K-1, self.hit_combo[i-1])

	def draw(self, screen):
		self.draw_sprite(screen)
		self.draw_hit_combo(screen)
		self.draw_hp(screen)
	def draw_hit_combo(self, screen):
		global POINT_COLORS
		for i in range(self.HIT_COMBO_MAX):
			pos = (self.x + self.D_HCOM_X0 + i*self.D_HCOM_DIST, self.y + self.D_HCOM_Y0)
			draw.circle(screen, POINT_COLORS[self.hit_combo[i]], pos, self.D_HCOM_RADIUS)
	def draw_hp(self, screen):
		x = self.D_HP_X0 + self.x
		y = self.D_HP_Y0 + self.y
		w = self.D_HP_W
		h = self.D_HP_H
		draw.rect(screen, COLOR_RED, (x, y, w, h))
		draw.rect(screen, COLOR_GREEN, (x, y, w*self.hp/self.HP, h))

##################################################################################################

def color_mix(c1, c2, alpha = 0.5):
	if (alpha < 0 or alpha > 1):
		print("uncorrect arguments for color_mix: alpha = ", alpha)

	beta = 1.0 - alpha
	out = (0, 0, 0)
	for i in range(3):
		out[i] = alpha*c1[i] + beta*c2[i]
	return out

def open_file(name):
	f = open(name)
	s = f.read()
	return s.split()

def is_collision(o1, o2):
	if (o1.FORM == "Circle" and o2.FORM == "Circle"):
		return dist(o1, o2) <= o1.RADIUS + o2.RADIUS
	else:
		print ("can't cross this objects with forms: ", o1.FORM, o2.FORM)

def dist(o1, o2):
	return ((o1.x - o2.x)**2 + (o1.y - o2.y)**2)**0.5

def vector_length(pos1, pos2 = (0, 0)):
	return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

def randint_without(l, r, v):
	out = random.randint(l, r-1)
	if out == v:
		out = r
	return out

def load_level(a):
	global list_of_points, playersoul
	list_of_points = List_Of_Objects()

	i = 0
	n = int(a[i])
	i += 1
	for j in range(n):
		list_of_points.add(Point(x = int(a[i]), y = int(a[i+1]), element = int(a[i+2])))
		i += 3

	playersoul = Player_Soul(int(a[i]))
	i += 1

def game():
	list_of_points = List_Of_Objects()
	controller = Game_Controller()
	load_level(open_file(FILE_LEVELS[0]))
	list_of_enemy = List_Of_Objects()
	list_of_enemy.add(Enemy(50, 500))

	while True:
		timer.tick(FPS)

		for e in pygame.event.get():
			list_of_points.event(e)

		list_of_points.update()
		list_of_enemy.update()
		playersoul.update()

		draw.rect(screen, COLOR_BLACK, (0, 0, DISPLAY_MODE[0], DISPLAY_MODE[1]))
		list_of_points.draw(screen)
		list_of_enemy.draw(screen)
		playersoul.draw(screen)
		pygame.display.update()


pygame.init()
FPS = 60
screen = pygame.display.set_mode(DISPLAY_MODE)
timer = pygame.time.Clock()
game()
