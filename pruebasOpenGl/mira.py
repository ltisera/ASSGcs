from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *


class mira:
    def __init__(self, x, y, z):
        self.xPos = x
        self.yPos = y
        self.zPos = z
        self.size = 1
        self.lineWidth = 2
        self.color = (1, 0, 1)

    @property
    def xPos(self):
        return self.__xPos

    @xPos.setter
    def xPos(self, x):
        self.__xPos = x

    @property
    def yPos(self):
        return self.__yPos

    @yPos.setter
    def yPos(self, y):
        self.__yPos = y

    @property
    def zPos(self):
        return self.__zPos

    @zPos.setter
    def zPos(self, z):
        self.__zPos = z

    def getPos(self):
        return self.xPos, self.yPos, self.zPos

    def setPos(self, vecPos):
        self.xPos = vecPos[0]
        self.yPos = vecPos[1]
        self.zPos = vecPos[2]

    def dibujar(self):
        glLineWidth(self.lineWidth)
        glColor3f(self.color[0], self.color[1], self.color[2])
        glBegin(GL_LINES)
        glVertex3f(self.xPos - self.size, self.yPos, self.zPos)
        glVertex3f(self.xPos + self.size, self.yPos, self.zPos)
        glVertex3f(self.xPos, self.yPos - self.size, self.zPos)
        glVertex3f(self.xPos, self.yPos + self.size, self.zPos)
        glVertex3f(self.xPos, self.yPos, self.zPos - self.size)
        glVertex3f(self.xPos, self.yPos, self.zPos + self.size)
        glEnd()
