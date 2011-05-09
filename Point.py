import GraphUtils as gu
import math

class point:
	x, y = 0, 0
	
	# distance from other point p. Not square rooted.
	def distFrom(self,p):
		return gu.dist(self.x,self.y,p.x,p.y)
	
	# distance from cartesian coordinates. Not square rooted.
	def dist(self,x,y):
		return math.sqrt(gu.dist(self.x,self.y,x,y))
	
	# --- Boring stuff -------------------------------------------------------
	
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def __str__(self):
		rtn = "( " + self.x + " , " + self.y + " )\n"
		return(rtn)

class circle(point):
	radius = 0
		
	# True when p is <= radius away
	def encompasses(self,p):
		return(self.radius >= self.distFrom(p))
		
	# True when this circle overlaps the passed circle
	def overlaps(self,c):
		return((self.radius + c.radius) >= self.distFrom(c))

	# function that returns a float -- 1 when outside circle, 0 when at center.
	def featherPoint(self,p):
		d = self.distFrom(p)
		
		if d > self.radius:
			return(1)
		else:
			return(float(d) / float(self.radius))
	
	# returns float 1 outside, 0 at center, from cartesian coords
	def feather(self,x,y):
		d = self.dist(x,y)
				
		if d > self.radius:
			mul = 1
		else:
			mul = (float(d) / float(self.radius))
		
		mul = math.radians(mul*90) # now we have a number between 0 and pi/2
		
		return(1-math.sin(mul))
		
		

	# --- Boring shit ---------------------------------------------------------

	def __init__(self,x,y,r):
		point.__init__(self,x,y)
		self.radius = r

	def setRadius(self,r):
		self.radius = r

	def getCenter(self):
		return self.point

	def getRadius(self):
		return self.radius

	def __str__(self):
		rtn = " Center: " + self.point + "\n"
		rtn += " Radius: " + self.radius

		return(rtn)