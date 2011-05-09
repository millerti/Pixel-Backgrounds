import pixelWall
import os, sys
from multiprocessing import Pool,cpu_count
import itertools

def makeImages((pixelimg,wNew,hNew,radius,wCircle,hCircle,out)):
	pixelWall.spotlight(pixelimg,wNew,hNew,radius,wCircle,hCircle,out)

if __name__ == "__main__":
	width = int(sys.argv[1])
	height = int(sys.argv[2])
	cWidth = int(sys.argv[3])
	cHeight = int(sys.argv[4])
	cRadius = int(sys.argv[5])

	wallPath = os.getcwd() + "/Wallpaper/"
	imgPath = os.getcwd() + "/Patterns/"

	imageNames = []
	saves = []

	if not os.path.exists(wallPath):
		os.mkdir(wallPath)

	for image in os.listdir(imgPath):
		imageNames.append(imgPath + image)
		saves.append(wallPath + image)

	pool = Pool(processes=cpu_count())
	pool.map(makeImages,itertools.izip(imageNames,itertools.repeat(width),itertools.repeat(height),itertools.repeat(cRadius),itertools.repeat(cWidth),itertools.repeat(cHeight),saves))