from numpy.linalg import inv
from graphicsAI.base.matrix import Matrix
from graphicsAI.base.object3D import Object3D

class Camera(Object3D):
    def __init__(self, angleOfView=60,aspectRatio=1, near=0.1, far=1000): 
        super().__init__() 
        self.projectionMatrix = Matrix.makePerspective(angleOfView, aspectRatio, near, far) 
        self.viewMatrix = Matrix.makeIdentity()
    
    def updateViewMatrix(self): 
        self.viewMatrix = inv( self.getWorldMatrix() )