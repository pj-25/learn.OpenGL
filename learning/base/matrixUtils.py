import numpy
from math import sin, cos, pi, tan

class MatrixUtils:

    @staticmethod
    def createIdentity():
        return numpy.array([[1,0,0,0],
                            [0,1,0,0],
                            [0,0,1,0],
                            [0,0,0,1]], dtype=float)
    
    @staticmethod
    def createScale(p,q,r):
        return numpy.array([[p,0,0,0],
                            [0,q,0,0],
                            [0,0,r,0],
                            [0,0,0,1]], dtype=float)
    
    @staticmethod
    def createTranslation(a,b,c):
        return numpy.array([[1,0,0,a],
                            [0,1,0,b],
                            [0,0,1,c],
                            [0,0,0,1]], dtype=float)

    @staticmethod
    def createRoationX(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[1,0,0,0],
                            [0,c,-s,0],
                            [0,s,c,0],
                            [0,0,0,1]], dtype=float)
    
    @staticmethod
    def createRotationY(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c,0,-s,0],
                            [0,1,0,0],
                            [s,0,c,0],
                            [0,0,0,1]], dtype=float)
    
    @staticmethod
    def createRotationZ(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c,-s,0,0],
                            [-s,c,0,0],
                            [0,0,1,0],
                            [0,0,0,1]], dtype=float)

    @staticmethod
    def createPerspective(near, far, angleOfView, aspectRatio):
        a = angleOfView*pi/180.0
        d = 1.0/tan(a/2)
        b = (far+near)/(near-far)
        c = 2*far*near/(near-far)
        return numpy.array([[d/aspectRatio,0,0,0],
                            [0,d,0,0],
                            [0,0,b,c],
                            [0,0,-1,0]], dtype=float)
        
