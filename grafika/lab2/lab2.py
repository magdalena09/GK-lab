import sys
from random import random

from glfw.GLFW import *

from OpenGL.GL import *

level = 4
d = random()


def startup():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    update_viewport(None, 400, 400)


def shutdown():
    pass

##################################################
def triangle_3():
    #glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-50.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 50.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(50.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glEnd()
##################################################
def rectangle_3_5(x, y, a, b):  #(x,y) środek
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)                       #pierwszy trójkąt   |---/
    glVertex2f(x+(-(1/2)*a), y+(1/2)*b)         #lewy górny         |  /
    glVertex2f(x+(1/2)*a, y+(1/2)*b)            #prawy górny        | /
    glVertex2f(x+(-(1/2)*a), y+(-(1/2)*b))      #lewy dolny         |/
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)                       #drugi trójkąt         /|
    glVertex2f(x+(-(1/2)*a), y+(-(1/2)*b))      #lewy dolny           / |
    glVertex2f(x+(1/2)*a, y+(1/2)*b)            #prawy górny         /  |
    glVertex2f(x+(1/2)*a, y+(-(1/2)*b))         #prawy dolny        /___|
    glEnd()

    # glColor3f(0.0, 1.0, 0.0)
    # glBegin(GL_TRIANGLES)
    # glVertex2f(x-a, y+b)
    # glVertex2f(x+a, y+b)
    # glVertex2f(x-a, y-b)
    # glEnd()
    #
    # glColor3f(0.0, 1.0, 0.0)
    # glBegin(GL_TRIANGLES)
    # glVertex2f(x-a, y-b)
    # glVertex2f(x+a, y+b)
    # glVertex2f(x+a, y-b)
    # glEnd()
##################################################
def rectangle_4(x, y, a, b, d=0.0):
    a = a*d
    b = b*d
    glColor3f(0.0, d, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x+(-(1/2)*a), y+(1/2)*b)
    glVertex2f(x+(1/2)*a, y+(1/2)*b)
    glVertex2f(x+(-(1/2)*a), y+(-(1/2)*b))
    glEnd()

    glColor3f(0.0, d, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x+(-(1/2)*a), y+(-(1/2)*b))
    glVertex2f(x+(1/2)*a, y+(1/2)*b)
    glVertex2f(x+(1/2)*a, y+(-(1/2)*b))
    glEnd()
##################################################

def rectangle(x, y, a, b):
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-a, y+b)
    glVertex2f(x+a, y+b)
    glVertex2f(x-a, y-b)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-a, y-b)
    glVertex2f(x+a, y+b)
    glVertex2f(x+a, y-b)
    glEnd()


def rectangle2(x, y, a, b):
    a = (1/3)*a
    b = (1/3)*b
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-a, y+b)
    glVertex2f(x+a, y+b)
    glVertex2f(x-a, y-b)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-a, y-b)
    glVertex2f(x+a, y+b)
    glVertex2f(x+a, y-b)
    glEnd()


def together(x, y, a, b):
    rectangle(x, y, a, b)
    rectangle2(x, y, a, b)


def eight(tabX, tabY, o):
    together(tabX[0], tabY[1], o, o)
    together(tabX[0], tabY[0], o, o)
    together(tabX[1], tabY[0], o, o)
    together(tabX[1], tabY[1], o, o)
    together(tabX[0], tabY[2], o, o)
    together(tabX[1], tabY[2], o, o)
    together(tabX[2], tabY[0], o, o)
    together(tabX[2], tabY[1], o, o)


def one_part(x, y, o, level):
    for _ in range(level - 1):
        rectangle2(x, y, o, o)
        o = (1 / 3) * o

        tabX = [x - 2 * o, x + 2 * o, x]
        tabY = [y - 2 * o, y + 2 * o, y]

        eight(tabX, tabY, o)

        #x = 2 * o   # prawy gorny
        #y = 2 * o
        one_part(x, y, o, 1)


def show_4_5(x, y, a, b):
    rectangle(x, y, a, b)
    if level == 1:
        rectangle2(x, y, a, b)
    else:
        one_part(x, y, a, level)


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    # triangle_3()
    # rectangle_3_5(0.0, 0.0, 80.0, 50.0)
    # rectangle_4(0.0, 0.0, 80.0, 50.0, d)
    show_4_5(0.0, 0.0, 90, 90)  # nie rysuje dookoła
    glFlush()


def update_viewport(window, width, height):
    if height == 0:
        height = 1

    if width == 0:
        width = 1
    aspectRatio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio, 1.0, -1.0)
    else:
        glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0, 1.0, -1.0)

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