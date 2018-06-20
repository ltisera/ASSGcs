from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

#el coso se encuentra a 129x 217y

width = 800
heigth = 500
ax= 0.0
ay= 0.0
az = 0.0
eyeX = 30.0
eyeY = 10.0
eyeZ = 30.0
gradosCamX = 1.0
gradosCamY = 1.0
distanciaCam = 50
avanceDeGrados=1

px =0.0
py =0.0
pz =0.0

class cuadrado:
	def __init__(self):
		self.cx = 0
		self.cy = 0
		self.cz = 0
		self.size = 1
		self.color = (1,0,1)

	def __init__(self, x, y, z, size, color):
		self.cx = x
		self.cy = y
		self.cz = z
		self.size = size
		self.color = color
	def getCoordX(self):
		return self.cx
	def getCoordY(self):
		return self.cy
	def getCoordZ(self):
		return self.cz
	def setCoordX(self,x):
		self.cx=x
	def setCoordY(self,y):
		self.cy=y
	def setCoordZ(self,z):
		self.cz=z


	def dibujar(self):
		glBegin(GL_POLYGON)
		glVertex3f(self.size-cx, self.size+self.cy,cz)
		glVertex3f(self.size+cx, self.size+self.cy,cz)
		glVertex3f(self.size+cx, self.size-self.cy,cz)
		glVertex3f(self.size-cx, self.size-self.cy,cz)
		glEnd()

def inicializar():
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60.0,width/heigth,1.0,1000.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glPolygonMode ( GL_FRONT, GL_LINE ) 

	
	gluLookAt(eyeX,eyeY,eyeZ,0,0,0, 0,1,0);
	glTranslatef(0.0,0.0,0.0);
	glClearColor(0, 0, 0, 0)
	
def dibujarCuadricula():
	glLineWidth(2.5); 
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
	
	glColor3f(0,0,1)
	glBegin(GL_LINES)
	glVertex3f(0.0, 0, 0.0)
	glVertex3f(0, 0, 100)
	glEnd()
	
	
	glColor3f(1,1,1)
	glLineWidth(1); 

	for i in range (-10,10):
		glBegin(GL_LINES)
		glVertex3f( (i*10), 0, -100)
		glVertex3f( (i*10), 0, 100)
		glVertex3f( -100, 0, (i*10))
		glVertex3f(100, 0,  (i*10))
		glEnd()
	
	
def dibujar():
	glClear (GL_COLOR_BUFFER_BIT)

	dibujarCuadricula()
	colBlanc = (1,0,1)
	glColor(colBlanc)
	glutSolidSphere(1,10,10)
	
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
		distanciaCam = distanciaCam + 1
	if(key == b'h'):
		distanciaCam = distanciaCam - 1
	if(key == b'u'):
		py = py + 0.1
	if(key == b'j'):
		py = py - 0.1
	if(key == b'i'):
		pz = pz + 0.1
	if(key == b'k'):
		pz = pz - 0.1

	if(key == b'w'):
		gradosCamX = gradosCamX - avanceDeGrados
		if(gradosCamX <= 0):
			gradosCamX = 360
		
		
	if(key == b's'):
		gradosCamX = gradosCamX +avanceDeGrados
		if(gradosCamX >= 360):
			gradosCamX = 0
		
	
	if(key == b'd'):
		gradosCamY = gradosCamY -avanceDeGrados
		if(gradosCamY <= 0):
			gradosCamY = 360
		
		
	if(key == b'a'):
		gradosCamY = gradosCamY +avanceDeGrados
		if(gradosCamY >= 360):
			gradosCamY = 0
		
	if(gradosCamX == 0):
		gradosCamX = 0.01
	
	eyeX = distanciaCam*sin(radians(gradosCamX))*cos(radians(gradosCamY))
	eyeY = distanciaCam*cos(radians(gradosCamX))
	eyeZ = distanciaCam*sin(radians(gradosCamX))*sin(radians(gradosCamY))
	
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	if(gradosCamX <=180):

		gluLookAt(eyeX,eyeY,eyeZ,0,0,0,0,1,0);
	else:
		gluLookAt(eyeX,eyeY,eyeZ,0,0,0,0,-1,0);
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

	miCuad=cuadrado(0,0,0,1,(1,1,1))
	lstObjetos=[]
	
	lstObjetos.append(miCuad)
	glutDisplayFunc(dibujar)
	glutKeyboardFunc(keyboarEvent)
	glutMotionFunc(mouseEvent)
	glutMainLoop()
	
