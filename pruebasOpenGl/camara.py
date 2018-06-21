from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from functools import partial
from auxiliares import dibujarCuadricula
#el coso se encuentra a 129x 217y

width = 800
heigth = 500
ax= 0.0
ay= 0.0
az = 0.0
eyeX = 30.0
eyeY = 10.0
eyeZ = 30.0
gradosCamX = 45.0
gradosCamY = 45.0
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
		glColor3f(1, 1, 1)
		glBegin(GL_POLYGON)
		glVertex3f(self.cx - self.size, self.cy + self.size,self.cz)
		glVertex3f(self.cx + self.size, self.cy + self.size,self.cz)
		glVertex3f(self.cx + self.size, self.cy - self.size,self.cz)
		glVertex3f(self.cx - self.size, self.cy - self.size,self.cz)
		glEnd()

def inicializar():
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0,width/heigth,1,200)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glPolygonMode ( GL_FRONT, GL_LINE ) 

	glDepthMask(GL_TRUE);
	glClearDepth(1.0);
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
	glDepthRange(0, 1)
	
	gluLookAt(eyeX,eyeY,eyeZ,0,0,0, 0,1,0);
	glTranslatef(0.0,0.0,0.0);
	glClearColor(0, 0, 0, 0)
	
	
	
def dibujar(asd):
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	colBlanc = (1,0,1)
	glColor(colBlanc)
	#glutSolidSphere(3,10,10)
	for i in asd:
		glPushMatrix()
		glTranslatef(2, 0, 0)
		i.dibujar()
		
		glPopMatrix()

	
	dibujarCuadricula()

	glutSwapBuffers();
	
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
		distanciaCam = distanciaCam + 0.2
	if(key == b'h'):
		distanciaCam = distanciaCam - 0.2
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
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowPosition(0, 0)
	glutInitWindowSize(width, heigth)
	app = glutCreateWindow("test camara")
	inicializar()

	miCuad=cuadrado(1,1,1,1,(1,1,1))
	lstObjetos=[]
	
	lstObjetos.append(miCuad)
	glutDisplayFunc(partial(dibujar,lstObjetos))
	#glutIdleFunc(partial(dibujar,lstObjetos))
	
	glutKeyboardFunc(keyboarEvent)
	glutMotionFunc(mouseEvent)
	glutMainLoop()
	
