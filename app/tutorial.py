import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os
from pylsd.lsd import lsd
from flask import Flask

app = Flask(__name__)

@app.route("/")
class Steps:
    def __init__(self, image):
        self.img = image
        self.edges = None

    def lineArt(self, image):
        fullName = image
        src = cv.imread(image, cv.IMREAD_COLOR)
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        lines = lsd(gray)
        img = np.zeros([1080,1200,3],dtype=np.uint8)
        img.fill(255)
        os.mkdir('./lineart')
        for i in range(lines.shape[0]):
            pt1 = (int(lines[i, 0]), int(lines[i, 1]))
            pt2 = (int(lines[i, 2]), int(lines[i, 3]))
            width = lines[i, 4]
            cv.line(img, pt1, pt2, (0, 0, 0), int(np.ceil(width / 2)))
            if i%10==0 or i==lines.shape[0]-1:
                cv.imshow('Step', img)
                cv.waitKey(0)
                cv.destroyAllWindows()
                cv.imwrite('./gallery/new' + i + '.jpg', img)

    def contours3(self):
        #Start shading your image
        im = cv.imread(self.img, cv.IMREAD_COLOR)
        cv.imshow("Contours", im)
        imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(imgray, 127, 255, 0)
        im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cnt = contours[4]
        cv.drawContours(im, [cnt], -1, (0,255,0), 3)
        cv.imshow("Contours", im)

def main():
    new = Steps('fruit.jpg')
    new.lineArt('asparagus')
    new.contours3()

if __name__=='__main__':
    app.run(debug=T)
