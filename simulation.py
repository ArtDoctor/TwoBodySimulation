import pygame
import sys
import math
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode((1000, 800))
screen.fill(THECOLORS['black'])

amount_of_bodies = 3
x = [100.0, 500.0, 900]
y = [400.0, 400.0, 400]
Vx = [0.0, 0.0, 0.0]
Vy = [-770.0, 0.0, 720.0]
m = [1.0, 10010.0, 1.0]
ax = [0.0] * amount_of_bodies
ay = [0.0] * amount_of_bodies
xs = [0.0] * amount_of_bodies
ys = [0.0] * amount_of_bodies
dt = 0.0001
G = 100000.0
k = 0.0
r0 = 380


def force(body):
    Fx = 0.0
    Fy = 0.0
    n1 = 0
    while n1 < amount_of_bodies:
        if n1 != body:
            distance = math.sqrt((x[n1] - x[body]) ** 2 + (y[n1] - y[body]) ** 2)
            F = G * m[n1] * m[body] / distance ** 2 + k * (distance - r0)
            Fx += F * (x[n1] - x[body]) / distance
            Fy += F * (y[n1] - y[body]) / distance
        n1 += 1
    return Fx, Fy


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #     Main
    n = 0
    while n < amount_of_bodies:
        ax[n] = force(n)[0] / m[n]
        ay[n] = force(n)[1] / m[n]
        Vx[n] = Vx[n] + ax[n] * dt
        Vy[n] = Vy[n] + ay[n] * dt
        xs[n] = x[n]
        ys[n] = y[n]
        x[n] = x[n] + Vx[n] * dt
        y[n] = y[n] + Vy[n] * dt
        pygame.draw.line(screen, THECOLORS['white'], (xs[n], ys[n]), (x[n], y[n]), width=1)
        # print(n, " - ", x[n], ", ", y[n])
        n += 1
    pygame.display.flip()
