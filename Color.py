import math

class color:
	RGB = [0,0,0]
	RGBdirty = False
	
	HSV = [0.0, 0.0, 0.0]
	HSVdirty = False
	
	minRGB, maxRGB, delta = [0.0, 0.0, 0.0]

	def getR(self):
		if self.RGBdirty:
			self.makeRGB()
		
		return self.RGB[0]
	
	def setR(self,r):
		self.HSVdirty = True

		self.RGB[0] = range(r,0,255)

	def getG(self):
		if self.RGBdirty:
			self.makeRGB()

		return self.RGB[1]

	def setG(self,g):
		self.HSVdirty = True

		self.RGB[1] = range(g,0,255)

	def getB(self):
		if self.RGBdirty:
			self.makeRGB()

		return self.RGB[2]

	def setB(self,b):
		self.HSVdirty = True

		self.RGB[2] = range(b,0,255)

	def getH(self):
		if self.HSVdirty:
			self.makeHSV()

		return self.HSV[0]

	def setH(self,h):
		self.RGBdirty = True

		self.HSV[0] = h

	def getS(self):
		if self.HSVdirty:
			self.makeHSV()

		return self.HSV[1]

	def setS(self,s):
		self.RGBdirty = True

		self.HSV[1] = range(s,0.0,100.0)

	def getV(self):
		if self.HSVdirty:
			self.makeHSV()

		return self.HSV[2]

	def setV(self,v):
		self.RGBdirty = True

		self.HSV[2] = range(v,0.0,100.0)
		
	def makeHSV(self):
		self.HSV[2] = float(self.maxRGB)
		
		if (self.maxRGB != 0.0):
			self.HSV[1] = 255.0 * self.delta / self.maxRGB
		else:
			self.HSV[1] = 0.0
		
		if (self.HSV[1] != 0.0):
			if self.RGB[0] == self.maxRGB:
				self.HSV[0] = (self.RGB[1] - self.RGB[2]) / self.delta
			elif self.RGB[1] == self.maxRGB:
				self.HSV[0] = 2.0 + (self.RGB[2] - self.RGB[0]) / self.delta
			elif self.RGB[2] == self.maxRGB:
				self.HSV[0] = 4.0 + (self.RGB[0] - self.RGB[1]) / self.delta
		    
		else:
			self.HSV[0] = -1.0
			
		self.HSV[0] *= 60.0
		
		if self.HSV[0] < 0.0:
			self.HSV[0] += 360.0
			
		self.HSV[1] *= (100.0/255.0)
		self.HSV[2] *= (100.0/255.0)
		
		self.madeHSV, self.madeH, self.madeS, self.madeV = [True, True, True, True]
		
	def makeRGB(self):
		f, p, q, t = [0.0, 0.0, 0.0, 0.0]
		h = (self.HSV[0] % 360.0) / 360.0
		s = self.HSV[1] / 100.0
		v = self.HSV[2] / 100.0
		
		if( self.HSV[1] == 0 ):
			# achromatic (grey)
			self.RGB[0] = self.RGB[1] = self.RGB[2] = v * 255.0
			return
			
		h *= 6		# sector 0 to 5
		i = math.floor(h)
		f = h - i			# factorial part of h
		p = v * ( 1.0 - s )
		q = v * ( 1.0 - s * f )
		t = v * ( 1.0 - s * ( 1.0 - f ) )
		
		if i == 0:
			print "Case 0"
			self.RGB[0] = v
			self.RGB[1] = t
			self.RGB[2] = p

		elif i == 1:
			print "Case 1"
			self.RGB[0] = q
			self.RGB[1] = v
			self.RGB[2] = p

		elif i == 2:
			print "Case 2"
			self.RGB[0] = p
			self.RGB[1] = v
			self.RGB[2] = t

		elif i == 3:
			print "Case 3"
			self.RGB[0] = p
			self.RGB[1] = q
			self.RGB[2] = v

		elif i == 4:
			print "Case 4"
			self.RGB[0] = t
			self.RGB[1] = p
			self.RGB[2] = v

		else:		# case 5:
			print "Case 5"
			self.RGB[0] = v
			self.RGB[1] = p
			self.RGB[2] = q
		
		self.RGB[0] = math.floor(self.RGB[0] * 255)
		self.RGB[1] = math.floor(self.RGB[1] * 255)
		self.RGB[2] = math.floor(self.RGB[2] * 255)
	
	
	def range(self,val,mini,maxi):
		if val < mini:
			val = mini
		elif val > maxi:
			val = maxi

		return val
			
	def __init__(self,tup,rgb = True):
		if rgb:
			self.RGB = list(tup)
			self.makeHSV()
			
		else:
			self.HSV = list(tup)			
			self.makeRGB()
		
		self.HSV[0] = 0.0
		self.minRGB = float(min(self.RGB[0], self.RGB[1], self.RGB[2]))
		self.maxRGB = float(max(self.RGB[0], self.RGB[1], self.RGB[2]))
		self.delta = float(self.maxRGB - self.minRGB)
		