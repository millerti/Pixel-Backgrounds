import math

# non-square-rooted 2D distance
def dist(a,b,x,y):
	return ((x-a)**2 + (y-b)**2)

# non-square-rooted 2D distance but with POINTS
def pointDist(a,b):
	return ((b.x-a.x)**2 + (b.y-a.y)**2)
	
def toDec(x):
	return(float(x)/255)
	
def toInt(x):
	return(x*255)