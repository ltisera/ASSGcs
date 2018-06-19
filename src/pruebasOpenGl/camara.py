from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

#el coso se encuentra a 129x 217y

width = 500
heigth = 800
ax= 0.0
ay= 0.0
az = 0.0
eyeX = 30.0
eyeY = 10.0
eyeZ = 30.0
gradosCamX = 1.0
gradosCamY = 1.0
distanciaCam = 50
avanceDeGrados=3

px =0.0
py =0.0
pz =0.0

class cuadrado:
	def __init__(self):
		self.cx = 0
		self.cy = 0
		self.cz = 0
	def __init__(self, x, y, z):
		self.cx = x
		self.cy = y
		self.cz = z
	
	def getCoordX(self):
		return self.cx
	def getCoordY(self):
		return self.cy
	def getCoordZ(self):
		return self.cz
	def setCoordX(self,x)
		self.cx=x
	def setCoordY(self,y)
		self.cy=y
	def setCoordZ(self,z)
		self.cz=z

def inicializar():
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60.0,width/heigth,1.0,100.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glPolygonMode ( GL_FRONT, GL_LINE ) 

	
	gluLookAt(eyeX,eyeY,eyeZ,0,0,0, 0,1,0);
	glTranslatef(0.0,0.0,0.0);
	glClearColor(0, 0, 0, 0)
	

def dibujar():
	glClear (GL_COLOR_BUFFER_BIT)
	glLineWidth(2.5); 
	glColor3f(1, 0, 0)
	glBegin(GL_LINES)
	glVertex3f(0.0, 0.0, 0.0)
	glVertex3f(10, 0, 0)
	glEnd()
	
	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_LINES)
	glVertex3f(0.0, 0.0, 0.0)
	glVertex3f(0, 10, 0)
	glEnd()
	
	glColor3f(0,0,1)
	glBegin(GL_LINES)
	glVertex3f(0.0, 0, 0.0)
	glVertex3f(0, 0, 10)
	glEnd()
	
	glColor3f(1,1,1)
	glBegin(GL_POINTS)
	glVertex3f(px, py, pz)
	glEnd()
	glLineWidth(1); 
	
	glutWireSphere(3,10,10)
	
	glFlush()

def mouseEvent(x, y):
	print("X: ",x, " Y:", y)
def keyboarEvent(key, x, y):
	global eyeX
	global eyeY
	global eyeZ
	global gradosCamX
	global gradosCamY
	global px
	global py
	global pz
	global distanciaCam

	if(key == b'y'):
		distanciaCam = distanciaCam + 0.1
	if(key == b'h'):
		distanciaCam = distanciaCam - 0.1
	if(key == b'u'):
		py = py + 0.1
	if(key == b'j'):
		py = py - 0.1
	if(key == b'i'):
		pz = pz + 0.1
	if(key == b'k'):
		pz = pz - 0.1

	if(key == b'w'):
		if(gradosCamX <= 0):
			gradosCamX = 360
		gradosCamX = gradosCamX - avanceDeGrados
		
	if(key == b's'):
		if(gradosCamX >= 360):
			gradosCamX = 0
		gradosCamX = gradosCamX +avanceDeGrados
	
	if(key == b'd'):
		if(gradosCamY <= 0):
			gradosCamY = 360
		gradosCamY = gradosCamY -avanceDeGrados
		
	if(key == b'a'):
		if(gradosCamY >= 360):
			gradosCamY = 0
		gradosCamY = gradosCamY +avanceDeGrados
	if(gradosCamX == 0):
		gradosCamX = 1
	eyeX = distanciaCam*sin(radians(gradosCamX))*cos(radians(gradosCamY))
	eyeY = distanciaCam*cos(radians(gradosCamX))
	eyeZ = distanciaCam*sin(radians(gradosCamX))*sin(radians(gradosCamY))
	
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	if(gradosCamX <=180):

		gluLookAt(30,10,30,eyeX,eyeY,eyeZ,0,1,0);
	else:
		gluLookAt(30,10,30,eyeX,eyeY,eyeZ,0,1,0);
	print("grados X: ", gradosCamX," grados Y: ", gradosCamY)
	glutPostRedisplay();



if __name__ == "__main__":
	ay=0.5;
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowPosition(0, 0)
	glutInitWindowSize(width, heigth)
	glutCreateWindow("test camara")
	inicializar()
	glutDisplayFunc(dibujar)
	glutKeyboardFunc(keyboarEvent)
	glutMotionFunc(mouseEvent)
	glutMainLoop()
	