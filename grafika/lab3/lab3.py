#!/usr/bin/env python3
import sys
import math
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

N = 30
tab = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
R = [random.random(), random.random(), random.random()]
A = [random.random(), random.random(), random.random()]
NN = [random.random(), random.random(), random.random()]
D = [random.random(), random.random(), random.random()]
O = [random.random(), random.random(), random.random()]
M = [random.random(), random.random(), random.random()]


def x(u, v):
    return (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * (math.cos(math.pi * v))


def y(u):
    return 160 * u ** 4 - 320 * u ** 3 + 160 * u ** 2


def z(u, v):
    return (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) * (math.sin(math.pi * v))


def populate():
    for u in range(N):
        for v in range(N):
            tab[u][v][0] = x(u / (N - 1), v / (N - 1))
            tab[u][v][1] = y(u / (N - 1))
            tab[u][v][2] = z(u / (N - 1), v / (N - 1))


def egg_points():
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.5)
    for u in range(N):
        for v in range(N):
            glVertex3f(tab[u][v][0], tab[u][v][1] - 5, tab[u][v][2])
    glEnd()


def egg_lines():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.5)
    for i in range(N - 1):
        for j in range(N - 1):
            glVertex3f(tab[i][j][0], tab[i][j][1] - 5, tab[i][j][2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1] - 5, tab[i + 1][j][2])

            glVertex3f(tab[i][j][0], tab[i][j][1] - 5, tab[i][j][2])
            glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1] - 5, tab[i][j + 1][2])
    glEnd()


def egg_triangles():
    glBegin(GL_TRIANGLES)
    for i in range(N - 1):
        for j in range(N - 1):
            glColor3f(R[0], R[1], R[2])
            glVertex3f(tab[i][j][0], tab[i][j][1] - 5, tab[i][j][2])
            glColor3f(A[0], A[1], A[2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1] - 5, tab[i + 1][j][2])
            glColor3f(NN[0], NN[1], NN[2])
            glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1] - 5, tab[i][j + 1][2])

            glColor3f(D[0], D[1], D[2])
            glVertex3f(tab[i + 1][j + 1][0], tab[i + 1][j + 1][1] - 5, tab[i + 1][j + 1][2])
            glColor3f(O[0], O[1], O[2])
            glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1] - 5, tab[i][j + 1][2])
            glColor3f(M[0], M[1], M[2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1] - 5, tab[i + 1][j][2])
    glEnd()


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time*180/3.1415)
    axes()
    populate()
    #egg_points()
    #egg_lines()
    egg_triangles()
    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
