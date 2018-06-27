from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from auxiliares import dibujarCuadricula
from mira import mira
from cuadrado import cuadrado
from camara import camara
# el coso se encuentra a 129x 217y
mPosXOld = None
mPosYOld = None
lstObjetos = []
width = 800
heigth = 500

eyeX = 0.0
eyeY = 0.0
eyeZ = 0.0
mx = 0.0
my = 0.0
mz = 0.0
gradosTheta = 0
gradosFi = 0
distanciaCam = 0
avanceDeGrados = 1


def esfericoACartesiano(r, theta, fi):
    x = r * sin(radians(theta)) * cos(radians(fi))
    y = r * cos(radians(theta))
    z = r * sin(radians(theta)) * sin(radians(fi))
    return x, y, z


def inicializar(cam):
    global eyeX
    global eyeY
    global eyeZ
    global gradosTheta
    global gradosFi
    global mx
    global my
    global mz
    global distanciaCam

    cam.inicializar(width, heigth, 1, 200)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPolygonMode(GL_FRONT, GL_LINE)

    glDepthMask(GL_TRUE)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glDepthRange(0, 1)

    eyeX = 30.0
    eyeY = 30.0
    eyeZ = 30.0
    distanciaCam = 52
    gradosTheta = 56
    gradosFi = 45
    cam.mirarA(29, 29, 29)
    """
    if (gradosTheta <= 180):
        gluLookAt(eyeX, eyeY, eyeZ, mx, my, mz, 0, 1, 0)
    else:
        gluLookAt(eyeX, eyeY, eyeZ, mx, my, mz, 0, -1, 0)
    glTranslatef(0.0, 0.0, 0.0)
    """
    glClearColor(0, 0, 0, 0)


def dibujar():
    global lstObjetos
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    colBlanc = (1, 0, 1)
    glColor(colBlanc)
    for i in lstObjetos:
        i.dibujar()
    dibujarCuadricula()

    # Mira
    glLineWidth(2.5)
    glColor3f(1, 0.5, 1)
    glBegin(GL_LINES)
    glVertex3f(mx - 2, my, mz)
    glVertex3f(mx + 2, my, mz)
    glVertex3f(mx, my - 2, mz)
    glVertex3f(mx, my + 2, mz)
    glVertex3f(mx, my, mz - 2)
    glVertex3f(mx, my, mz + 2)
    glEnd()

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


def mouseEvent(x, y):
    global mPosXOld
    global mPosYOld
    global gradosTheta
    global gradosFi
    global distanciaCam
    global eyeX
    global eyeY
    global eyeZ
    global mx
    global my
    global mz

    dx = 0
    dy = 0
    if(mPosXOld is not None and mPosYOld is not None):
        dx = x - mPosXOld
        dy = -(y - mPosYOld)
    else:
        mPosXOld = x
        mPosYOld = y
    gradosTheta += dy * 0.5
    gradosFi += dx * 0.5

    if(gradosTheta >= 360):
        gradosTheta = 0.1
    if(gradosTheta <= 0):
        gradosTheta = 360
    """
    if(gradosFi >= 360):
        gradosFi = 0
    if(gradosFi <= 0):
        gradosFi = 360
    """
    eyeX, eyeY, eyeZ = esfericoACartesiano(distanciaCam, gradosTheta, gradosFi)

    glLoadIdentity()

    if(gradosTheta <= 180):
        gluLookAt(eyeX + mx, eyeY + my, eyeZ + mz, mx, my, mz, 0, 1, 0)
    else:
        gluLookAt(eyeX + mx, eyeY + my, eyeZ + mz, mx, my, mz, 0, -1, 0)
    glutPostRedisplay()
    mPosXOld = x
    mPosYOld = y


def keyboarEvent(key, x, y):
    global lstObjetos
    global eyeX
    global eyeY
    global eyeZ
    global gradosTheta
    global gradosFi
    global mx
    global my
    global mz
    global distanciaCam
    if(key == b'-'):
        distanciaCam = distanciaCam + 0.2
    if(key == b'+'):
        distanciaCam = distanciaCam - 0.2

    if(key == GLUT_KEY_UP):
        gradosTheta = gradosTheta - avanceDeGrados
        if(gradosTheta <= 0):
            gradosTheta = 360

    if(key == GLUT_KEY_DOWN):
        gradosTheta = gradosTheta + avanceDeGrados
        if(gradosTheta >= 360):
            gradosTheta = 0

    if(key == GLUT_KEY_RIGHT):
        gradosFi = gradosFi - avanceDeGrados
        if(gradosFi <= 0):
            gradosFi = 360

    if(key == GLUT_KEY_LEFT):
        gradosFi = gradosFi + avanceDeGrados
        if(gradosFi >= 360):
            gradosFi = 0
    if(key == b'a'):
        for i in lstObjetos:
            (x, y, z) = i.getTrans()
            i.mover(x - 0.1, y, z)

    if(key == b'd'):
        for i in lstObjetos:
            (x, y, z) = i.getTrans()
            i.mover(x + 0.1, y, z)

    if(key == b'w'):
        for i in lstObjetos:
            (x, y, z) = i.getTrans()
            i.mover(x, y + 0.1, z)

    if(key == b's'):
        for i in lstObjetos:
            (x, y, z) = i.getTrans()
            i.mover(x, y - 0.1, z)

    if(gradosTheta == 0):
        gradosTheta = 0.01

    eyeX, eyeY, eyeZ = esfericoACartesiano(distanciaCam, gradosTheta, gradosFi)

    if (key == b'x'):
        eyeX += 1
        mx += 1

    if (key == b'z'):
        eyeX -= 1
        mx -= 1
    """
    if(gradosTheta <= 180):
        gluLookAt(eyeX + mx, eyeY + my, eyeZ + mz, mx, my, mz, 0, 1, 0)
    else:
        gluLookAt(eyeX + mx, eyeY + my, eyeZ + mz, mx, my, mz, 0, -1, 0)
    """
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

    miraTest = mira(0, 0, 0)
    miraTest.xPos = 2
    miraTest.yPos = 3
    miraTest.zPos = -1

    print("Ves que cambia: ", miraTest.getPos())
    miCuad = cuadrado(1, 1, 1, 1, (1, 1, 1))

    lstObjetos.append(miCuad)
    lstObjetos.append(miraTest)
    glutDisplayFunc(dibujar)
    glutKeyboardFunc(keyboarEvent)
    glutSpecialFunc(keyboarEvent)
    glutMouseFunc(mouseClickEvent)
    glutMotionFunc(mouseEvent)
    glutMainLoop()
"""
v1 = eyeX-mx, eyeY-my,eyeZ-mz

vPerp = -(eyeY-my),eyeX-mx,0

v1 * v2 = (vx,vy,vz) * (ux,uy,uz)

vx*ux+vy*uy+vz*uz = 0

(eyeX-mx )x + (eyeY-my)y + (eyeZ-mz)z = 0


-Bx+Ay


"""
