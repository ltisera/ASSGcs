from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *


class cuadrado:

    def __init__(self, x, y, z, size, color):
        self.cx = x
        self.cy = y
        self.cz = z
        self.size = size
        self.color = color
        self.tx = 0
        self.ty = 0
        self.tz = 0

    def getTrans(self):
        return self.tx, self.ty, self.tz

    def getCoordX(self):
        return self.cx

    def getCoordY(self):
        return self.cy

    def getCoordZ(self):
        return self.cz

    def setCoordX(self, x):
        self.cx = x

    def setCoordY(self, y):
        self.cy = y

    def setCoordZ(self, z):
        self.cz = z

    def mover(self, x, y, z):
        self.tx = x
        self.ty = y
        self.tz = z

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.tx, self.ty, self.tz)
        glColor3f(1, 1, 1)
        glBegin(GL_POLYGON)
        glVertex3f(self.cx - self.size, self.cy + self.size, self.cz)
        glVertex3f(self.cx + self.size, self.cy + self.size, self.cz)
        glVertex3f(self.cx + self.size, self.cy - self.size, self.cz)
        glVertex3f(self.cx - self.size, self.cy - self.size, self.cz)

        glEnd()
        glPopMatrix()
