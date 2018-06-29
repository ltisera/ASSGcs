from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from auxiliares import dibujarCuadricula
from cuadrado import cuadrado
from cubo import cubo
from camara import camara
# el coso se encuentra a 129x 217y

mPosXOld = None
mPosYOld = None
lstObjetos = []


width = 800
heigth = 500

inCamX = -50
inCamY = -50
inCamZ = -50


def inicializar(cam):
    global eyeX
    global eyeY
    global eyeZ
    global gradosTita
    global gradosPhi
    global mx
    global my
    global mz
    global distanciaCam

    cam.inicializar(width, heigth, 1, 2000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPolygonMode(GL_FRONT, GL_LINE)

    glDepthMask(GL_TRUE)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glDepthRange(0, 1)

    cam.mirarA(0, 0)
    cam.xCam = inCamX
    cam.yCam = inCamY
    cam.zCam = inCamZ

    glClearColor(0, 0, 0, 0)


def dibujar():
    global lstObjetos
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    colBlanc = (1, 0, 1)
    glColor(colBlanc)
    for i in lstObjetos:
        i.dibujar()
    dibujarCuadricula()

    glutSwapBuffers()
    glFlush()


def mouseClickEvent(mouse, state, x, y):
    global mPosXOld
    global mPosYOld
    if(mouse == GLUT_LEFT_BUTTON and state == GLUT_DOWN):
        mPosXOld = x
        mPosYOld = y
    if(mouse == GLUT_LEFT_BUTTON and state == GLUT_UP):
        mPosXOld = x
        mPosYOld = y
    print("B")


def mouseEvent(x, y):
    global mPosXOld
    global mPosYOld
    centerX = 800 / 2
    centerY = 500 / 2

    dx = 0
    dy = 0
    if(mPosXOld is not None and mPosYOld is not None):
        dx = x - centerX
        dy = -(y - centerY)

    mPosXOld = x
    mPosYOld = y
    cam.mirarA(dx * 0.1, dy * 0.1)

    if (x != centerX or y != centerY):
        glutWarpPointer(int(centerX), int(centerY))


def keyboarEvent(key, x, y):
    global lstObjetos

    if(key == GLUT_KEY_UP):
        cam.gradosPhi += 1

    if(key == GLUT_KEY_DOWN):
        cam.gradosPhi -= 1

    if(key == GLUT_KEY_RIGHT):
        cam.gradosTita += 1

    if(key == GLUT_KEY_LEFT):
        cam.gradosTita -= 1

    if(key == b'w'):
        vdir = cam.vecUDireccion()
        cam.mover(vdir[0], vdir[1], vdir[2])

    if(key == b's'):
        vdir = cam.vecUDireccion()
        cam.mover(-vdir[0], -vdir[1], -vdir[2])

    cam.mirarA(0, 0)
    if(key == b'q'):
        glLoadIdentity()
        gluLookAt(-10, 5, -10, 0, 0, 0, 0, 1, 0)
    glutPostRedisplay()
    if(key == b'\x1b'):
        glutDestroyWindow(app)


if __name__ == "__main__":
    ay = 0.5
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(width, heigth)
    app = glutCreateWindow("test camara")

    cam = camara()
    inicializar(cam)

    miCuad = cuadrado(5, 1, 5, 1, (1, 1, 1))
    miCubo = cubo(0, 0, 0, 100, ((1, 0.5, 0.5), (0.5, 1, 0.5), (0.5, 0.5, 1)))

    lstObjetos.append(miCuad)
    lstObjetos.append(miCubo)
    glutDisplayFunc(dibujar)
    glutKeyboardFunc(keyboarEvent)
    glutSpecialFunc(keyboarEvent)
    glutMouseFunc(mouseClickEvent)
    glutMotionFunc(mouseEvent)
    glutPassiveMotionFunc(mouseEvent)
    glutMainLoop()
"""
v1 = eyeX-mx, eyeY-my,eyeZ-mz

vPerp = -(eyeY-my),eyeX-mx,0

v1 * v2 = (vx,vy,vz) * (ux,uy,uz)

vx*ux+vy*uy+vz*uz = 0

(eyeX-mx )x + (eyeY-my)y + (eyeZ-mz)z = 0


-Bx+Ay


"""
