from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from functools import partial
from auxiliares import dibujarCuadricula
#el coso se encuentra a 129x 217y
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
avanceDeGrados= 1

"""def cartesianoAEsferico(x,y,z):
	No funca
	if (y!=0):
		theta = degrees(atan(sqrt((pow(x,2)+pow(z,2))/y)))
	else:
		theta = 90
	if(x!=0):
		fi = degrees(atan(z/x))
	else:
		fi = 90
	r = sqrt((x*x)+(y*y)+(z*z))
	#r = distaciaCam ; theta = gradosTheta ; fi = gradosFi
	return r, theta, fi"""

def esfericoACartesiano(r,theta,fi):
	x = r*sin(radians(theta))*cos(radians(fi))
	y = r*cos(radians(theta))
	z = r*sin(radians(theta))*sin(radians(fi))
	return x, y, z

class camara:
	def __init__(self):
		self.xCam = 0.0
		self.yCam = 0.0
		self.zCam = 0.0
		self.xPOI = 0.0
		self.yPOI = 0.0
		self.zPOI = 0.0
		self.anguloApertura = 45.0


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
		self.tx = 0
		self.ty = 0
		self.tz = 0
	def getTrans(self):
		#print("devuelvo {0},{1},{2}".format(self.tx,self.ty,self.tz))
		return self.tx,self.ty,self.tz
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

	def mover(self,x, y, z):
		#print("value")
		#print("Guardo: {},{},{}",x,y,z)
		self.tx = x
		self.ty = y
		self.tz = z
	def dibujar(self):
		glPushMatrix()
		glTranslatef(self.tx, self.ty, self.tz)
		glColor3f(1, 1, 1)
		glBegin(GL_POLYGON)
		glVertex3f(self.cx - self.size, self.cy + self.size,self.cz)
		glVertex3f(self.cx + self.size, self.cy + self.size,self.cz)
		glVertex3f(self.cx + self.size, self.cy - self.size,self.cz)
		glVertex3f(self.cx - self.size, self.cy - self.size,self.cz)
		
		glEnd()
		glPopMatrix()

def inicializar():
	global eyeX
	global eyeY
	global eyeZ
	global gradosTheta
	global gradosFi
	global mx
	global my
	global mz
	global distanciaCam

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
	
	eyeX = 30.0
	eyeY = 30.0
	eyeZ = 30.0
	distanciaCam = 52
	gradosTheta = 56
	gradosFi = 45
	if (gradosTheta <= 180):
		gluLookAt(eyeX,eyeY,eyeZ,mx,my,mz, 0,1,0)
	else:
		gluLookAt(eyeX,eyeY,eyeZ,mx,my,mz, 0,-1,0)
	print("INICIO {0:.6f};{1:.6f};{2:.6f} dist {3:.6f}; Theta {4:.6f}; Fi {5:.6f}".format(eyeX,eyeY,eyeZ,distanciaCam,gradosTheta,gradosFi))
	
	glTranslatef(0.0,0.0,0.0);
	glClearColor(0, 0, 0, 0)
	
	
	
def dibujar():
	global lstObjetos
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	colBlanc = (1,0,1)
	glColor(colBlanc)
	#glutSolidSphere(3,10,10)
	for i in lstObjetos:
		i.dibujar()
	
	dibujarCuadricula()

	#Mira
	glLineWidth(2.5); 
	glColor3f(1, 0.5, 1)
	glBegin(GL_LINES)
	glVertex3f(mx-2, my, mz)
	glVertex3f(mx+2, my, mz)
	glVertex3f(mx, my-2, mz)
	glVertex3f(mx, my+2, mz)
	glVertex3f(mx, my, mz-2)
	glVertex3f(mx, my, mz+2)
	glEnd()

	glutSwapBuffers();
	
	glFlush()

def mouseClickEvent(mouse, state, x ,y):
	global mPosXOld 
	global mPosYOld 
	if(mouse == GLUT_LEFT_BUTTON and state == GLUT_DOWN):
		print ("apreto")
		mPosXOld = x
		mPosYOld = y
	if(mouse == GLUT_LEFT_BUTTON and state == GLUT_UP):
		mPosXOld = x
		mPosYOld = y
		print ("solto")

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
	if(mPosXOld != None and mPosYOld != None):
		dx = x - mPosXOld
		dy = -(y - mPosYOld)
	else:
		mPosXOld = x
		mPosYOld = y
	#print("X: {} D: {} y las Anteriores X: {} Y:{}".format(x,y,mPosXOld,mPosYOld))
	
	gradosTheta += dy*0.5
	gradosFi += dx*0.5
	eyeX,eyeY,eyeZ = esfericoACartesiano(distanciaCam,gradosTheta,gradosFi)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(eyeX+mx,eyeY+my,eyeZ+mz,mx,my,mz,0,1,0);
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
		#print("eyeX:", eyeX, "eyeY:", eyeY, "eyeZ:", eyeZ )
		gradosTheta = gradosTheta +avanceDeGrados
		if(gradosTheta >= 360):
			gradosTheta = 0
		
	
	if(key == GLUT_KEY_RIGHT):
		gradosFi = gradosFi -avanceDeGrados
		if(gradosFi <= 0):
			gradosFi = 360
		
		
	if(key == GLUT_KEY_LEFT):
		gradosFi = gradosFi +avanceDeGrados
		if(gradosFi >= 360):
			gradosFi = 0
	if(key == b'a'):
		for i in lstObjetos:
			(x,y,z) = i.getTrans()
			i.mover(x-0.1,y,z)

	if(key == b'd'):
		for i in lstObjetos:
			(x,y,z) = i.getTrans()
			i.mover(x+0.1,y,z)

	if(key == b'w'):
		for i in lstObjetos:
			(x,y,z) = i.getTrans()
			i.mover(x,y+0.1,z)

	if(key == b's'):
		for i in lstObjetos:
			(x,y,z) = i.getTrans()
			i.mover(x,y-0.1,z)

	if(gradosTheta == 0):
		gradosTheta = 0.01

	#print("DX:{}, DY:{}".format(gradosTheta,gradosFi))
	
	eyeX,eyeY,eyeZ = esfericoACartesiano(distanciaCam,gradosTheta,gradosFi)
	print("{0:.6f};{1:.6f};{2:.6f} dist {3:.6f}; Theta {4:.6f}; Fi {5:.6f}".format(eyeX,eyeY,eyeZ,distanciaCam,gradosTheta,gradosFi))
	
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()


	if (key == b'x'):
		eyeX += 1
		mx += 1

	if (key == b'z'):
		eyeX -= 1
		mx -= 1

	if(gradosTheta<=180):
		gluLookAt(eyeX+mx,eyeY+my,eyeZ+mz,mx,my,mz,0,1,0);
	else:
		gluLookAt(eyeX+mx,eyeY+my,eyeZ+mz,mx,my,mz,0,-1,0);
	
	glutPostRedisplay()
	if(key == b'\x1b'):
		glutDestroyWindow(app)



if __name__ == "__main__":
	ay=0.5;
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowPosition(0, 0)
	glutInitWindowSize(width, heigth)
	app = glutCreateWindow("test camara")
	inicializar()

	miCuad=cuadrado(1,1,1,1,(1,1,1))
	
	
	lstObjetos.append(miCuad)
	glutDisplayFunc(dibujar)
	#glutIdleFunc(dibujar)
	
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