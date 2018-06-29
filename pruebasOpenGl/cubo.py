from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *


class cubo:

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

        posX = self.cx + self.size
        negX = self.cx - self.size
        posY = self.cy + self.size
        negY = self.cy - self.size
        posZ = self.cz + self.size
        negZ = self.cz - self.size

        glColor3f(self.color[0][0], self.color[0][1], self.color[0][2])
        glBegin(GL_POLYGON)
        glVertex3f(negX, negY, posZ)
        glVertex3f(negX, posY, posZ)
        glVertex3f(negX, posY, negZ)
        glVertex3f(negX, negY, negZ)
        glEnd()

        glColor3f(self.color[0][0] - 0.3, self.color[0][1], self.color[0][2])
        glBegin(GL_POLYGON)
        glVertex3f(posX, posY, negZ)
        glVertex3f(posX, posY, posZ)
        glVertex3f(posX, negY, posZ)
        glVertex3f(posX, negY, negZ)
        glEnd()

        glColor3f(self.color[1][0], self.color[1][1], self.color[1][2])
        glBegin(GL_POLYGON)
        glVertex3f(negX, posY, posZ)
        glVertex3f(posX, posY, posZ)
        glVertex3f(posX, posY, negZ)
        glVertex3f(negX, posY, negZ)
        glEnd()

        glColor3f(self.color[1][0], self.color[1][1] - 0.3, self.color[1][2])
        glBegin(GL_POLYGON)
        glVertex3f(posX, negY, negZ)
        glVertex3f(posX, negY, posZ)
        glVertex3f(negX, negY, posZ)
        glVertex3f(negX, negY, negZ)
        glEnd()

        glColor3f(self.color[2][0], self.color[2][1], self.color[2][2])
        glBegin(GL_POLYGON)
        glVertex3f(negX, posY, negZ)
        glVertex3f(posX, posY, negZ)
        glVertex3f(posX, negY, negZ)
        glVertex3f(negX, negY, negZ)
        glEnd()

        glColor3f(self.color[2][0], self.color[2][1], self.color[2][2] - 0.3)
        glBegin(GL_POLYGON)
        glVertex3f(posX, negY, posZ)
        glVertex3f(posX, posY, posZ)
        glVertex3f(negX, posY, posZ)
        glVertex3f(negX, negY, posZ)
        glEnd()

        glPopMatrix()
