from Point import point
import GraphUtils as gu

class circle:
	center = 0
	radius = 0
	
	# distance from point p. Not square rooted.
	def distFrom(self,p):
		return gu.dist(self,p)
	
	
	# --- Boring stuff ---------------------------------------------------------
	
	def __init__(self,c,r):
		self.center = c
		self.radius = r
		
	def setCenter(self,c):
		self.center = c
		
	def setRadius(self,r):
		self.radius = r
	
	def getCenter(self):
		return self.center
	
	def getRadius(self):
		return self.radius
		
	def __str__(self):
		rtn = " Center: " + self.center + "\n"
		rtn += " Radius: " + self.radius
		
		return(rtn)
