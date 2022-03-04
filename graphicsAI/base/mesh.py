from OpenGL.GL import *
from graphicsAI.base.object3D import Object3D

class Mesh(Object3D):
    def __init__(self, geometry, material): 
        super().__init__()
        self.geometry = geometry 
        self.material = material
        self.isVisible = True
       
        self.vaoRef = glGenVertexArrays(1) 
        glBindVertexArray(self.vaoRef) 
        for varName, attrObject in geometry.attributes.items(): 
            attrObject.associateVariable(material.programRef, varName) 
        
        glBindVertexArray(0)