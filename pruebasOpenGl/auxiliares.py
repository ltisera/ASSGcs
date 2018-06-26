from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *


def dibujarCuadricula():
    glLineWidth(2.5)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(100, 0, 0)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0, 100, 0)
    glEnd()

    glColor3f(0, 0, 1)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0, 0.0)
    glVertex3f(0, 0, 100)
    glEnd()

    glColor3f(1, 1, 1)
    glLineWidth(1)

    for i in range(-10, 10):
        glBegin(GL_LINES)
        glVertex3f((i * 10), 0, -100)
        glVertex3f((i * 10), 0, 100)
        glVertex3f(-100, 0, (i * 10))
        glVertex3f(100, 0, (i * 10))
        glEnd()
    glColor3f(0.41, 0.41, 0.41)
    for i in range(-10, 10):
        glBegin(GL_LINES)
        glVertex3f((i), 0, -10)
        glVertex3f((i), 0, 10)
        glVertex3f(-10, 0, (i))
        glVertex3f(10, 0, (i))
        glEnd()
