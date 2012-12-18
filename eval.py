import cv
from math import pi,atan
from numpy import var, mean
import sys
def slope(p1,p2):
    a = [p1,p2]
    a.sort()
    p1 = a[0]
    p2 = a[1]
    if p2[0] == p1[0]:
        return pi/2
    else:
        return atan((p2[1]-p1[1]) / float(p2[0]-p1[0])) 

def evaluateFiles(files):
    results = []
    cv.NamedWindow("Source", 1)
    cv.NamedWindow("Hough", 1)
    for filename in files:
        src = cv.LoadImage(filename, cv.CV_LOAD_IMAGE_GRAYSCALE)
        new_size = map(lambda d : d/2,cv.GetSize(src))
        src_thumb = cv.CreateImage(new_size, src.depth, src.nChannels)
        cv.Resize(src,src_thumb)
        src = src_thumb
        dst = cv.CreateImage(cv.GetSize(src), 8, 1)
        color_dst = cv.CreateImage(cv.GetSize(src), 8, 3)
        storage = cv.CreateMemStorage(0)
        cv.Canny(src, dst, 50, 200, 3)
        cv.CvtColor(dst, color_dst, cv.CV_GRAY2BGR)
        lines = cv.HoughLines2(dst, storage, cv.CV_HOUGH_PROBABILISTIC, 1, pi / 180, 40, 15, 2)
        angles = []
        for line in lines:
            angles.append(slope(line[0],line[1]))
        score = mean(map(lambda a : a**2, angles))
        for line in lines:
            cv.Line(color_dst, line[0], line[1], cv.CV_RGB(255, 0, 0), 3, 8)
        #cv.ShowImage("Hough", color_dst)
        #k = cv.WaitKey(0)
        results.append((score,int(filename.split('.')[0])))
    results.sort()
    print "Best guess: " + str(results[0][1]) +".jpeg"
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python eval.py *.jpeg"
    evaluateFiles(sys.argv[1:])
