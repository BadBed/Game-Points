import random


def color_mix(c1, c2, alpha=0.5):
    if (alpha < 0 or alpha > 1):
        raise Exception("uncorrect arguments for color_mix: alpha = " + str(alpha))

    beta = 1.0 - alpha
    out = (0, 0, 0)
    for i in range(3):
        out[i] = alpha * c1[i] + beta * c2[i]
    return out


def open_file(name):
    f = open(name)
    s = f.read()
    return s.split()


def is_collision(o1, o2):
    if (o1.FORM == "Circle" and o2.FORM == "Circle"):
        return dist(o1, o2) <= o1.RADIUS + o2.RADIUS
    else:
        print("can't cross this objects with forms: ", o1.FORM, o2.FORM)


def dist(o1, o2):
    return ((o1.x - o2.x) ** 2 + (o1.y - o2.y) ** 2) ** 0.5


def vector_length(pos1, pos2=(0, 0)):
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5


def randint_without(l, r, v):
    out = random.randint(l, r - 1)
    if out == v:
        out = r
    return out