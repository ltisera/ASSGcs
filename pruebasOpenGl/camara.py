from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from mira import mira


class camara:
    def __init__(self):
        self.xCam = 0.0
        self.yCam = 10.0
        self.zCam = 10.0
        self.xMira = 0.0
        self.yMira = 0.0
        self.zMira = 0.0

        self.miMira = mira(0, 0, 0)
        self.anguloApertura = 45.0
        self.gradosTheta = 56
        self.gradosFi = 45
        self.distanciaCam = 10

    @property
    def gradosFi(self):
        return self._gradosFi

    @gradosFi.setter
    def gradosFi(self, gradosFi):
        self._gradosFi = gradosFi

    @property
    def gradosTheta(self):
        return self._gradosTheta

    @gradosTheta.setter
    def gradosTheta(self, gradosTheta):
        self._gradosTheta = gradosTheta

    @property
    def xCam(self):
        return self._xCam

    @xCam.setter
    def xCam(self, x):
        self._xCam = x

    @property
    def yCam(self):
        return self._yCam

    @yCam.setter
    def yCam(self, y):
        self._yCam = y

    @property
    def zCam(self):
        return self._zCam

    @zCam.setter
    def zCam(self, z):
        self._zCam = z

    @property
    def xMira(self):
        return self._xMira

    @xMira.setter
    def xMira(self, x):
        self._xMira = x

    @property
    def yMira(self):
        return self._yMira

    @yMira.setter
    def yMira(self, y):
        self._yMira = y

    @property
    def zMira(self):
        return self._zMira

    @zMira.setter
    def zMira(self, z):
        self._zMira = z

    @property
    def distanciaCam(self):
        return self._distanciaCam

    @distanciaCam.setter
    def distanciaCam(self, distancia):
        self._distanciaCam = distancia

    def inicializar(self, width, heigth, pcerca, plejos):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.anguloApertura, width / heigth, pcerca, plejos)

    def mover(self, x, y, z):
        self.xCam += x
        self.yCam += y
        self.zCam += z

    def mirarA(self, x, y, z):
        gluLookAt(self.xCam, self.yCam, self.zCam,
                  self.xMira, self.yMira, self.zMira,
                  0, 1, 0)

