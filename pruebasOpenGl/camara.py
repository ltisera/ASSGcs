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
        self.gradosTita = 0
        self.gradosPhi = 0
        self.distanciaCam = 20

    @property
    def gradosPhi(self):
        return self._gradosPhi

    @gradosPhi.setter
    def gradosPhi(self, gradosPhi):
        if(gradosPhi < 0):
            gradosPhi = 359
        if(gradosPhi > 360):
            gradosPhi = 1
        self._gradosPhi = gradosPhi

    @property
    def gradosTita(self):
        return self._gradosTita

    @gradosTita.setter
    def gradosTita(self, gradosTita):
        if(gradosTita < 0):
            gradosTita = 359
        if(gradosTita > 360):
            gradosTita = 1
        self._gradosTita = gradosTita

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

    def mirarA(self, Tita, fi):
        glLoadIdentity()
        self.gradosTita += Tita
        self.gradosPhi += fi
        nX, nY, nZ = self.esfericoACartesiano(self.distanciaCam,
                                              self.gradosTita,
                                              self.gradosPhi)
        self.xMira = nX
        self.yMira = nY
        self.zMira = nZ

        gluLookAt(self.xCam, self.yCam, self.zCam,
                  self.xMira, self.yMira, self.zMira,
                  0, 1, 0)
        print("gradosTita:{0} gradosPhi:{1} miraA:({2:.2f},{3:.2f},{4:.2f})".format(self.gradosTita, self.gradosPhi, self.xMira, self.yMira, self.zMira))

        glutPostRedisplay()

    def esfericoACartesiano(self, d, tita, phi):
        x = self.xCam + d * cos(radians(tita)) * cos(radians(phi))
        y = self.yCam + d * sin(radians(phi))
        z = self.zCam + d * sin(radians(tita)) * cos(radians(phi))
        return x, y, z
