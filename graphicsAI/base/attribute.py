import numpy
from OpenGL.GL import *

class Attribute:

    ATTR_TYPE = {"int": (1, GL_INT), 
                "float": (1, GL_FLOAT), 
                "vec2": (2, GL_FLOAT),
                "vec3": (3, GL_FLOAT),
                "vec4": (4, GL_FLOAT)}

    def __init__(self, dataType, data):
        self.dataType = dataType
        self.data = data
        self.bufferRef = glGenBuffers(1)
        self.uploadDataToBuffer()

    def uploadDataToBuffer(self):
        data = numpy.array(self.data).astype(numpy.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
        
    def associateVariable(self, progRef, varName):
        variableRef = glGetAttribLocation(progRef, varName)
        if variableRef == -1:
            return
        
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        try:
            glVertexAttribPointer(variableRef, *Attribute.ATTR_TYPE[self.dataType], False, 0, None)
        except:
            raise Exception('Invalid dataType('+self.dataType+') for attribute('+varName+')')
        glEnableVertexAttribArray(variableRef)
