import numpy
from OpenGL.GL import *
from .glDataType import GL_DATA_TYPE

class Attribute:

    def __init__(self, dataType, data):
        self.dataType = dataType
        self.data = data
        self.bufferRef = glGenBuffers(1)
        self.uploadDataToBuffer()

    def uploadDataToBuffer(self):
        data = numpy.array(self.data).astype(numpy.float32).ravel()
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        glBufferData(GL_ARRAY_BUFFER, data, GL_STATIC_DRAW)
        
    def associateVariable(self, progRef, varName):
        variableRef = glGetAttribLocation(progRef, varName)
        if variableRef == -1:
            return
        
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        try:
            glVertexAttribPointer(variableRef, *GL_DATA_TYPE[self.dataType], False, 0, None)
        except:
            raise Exception('Invalid dataType('+self.dataType+') for attribute('+varName+')')
        glEnableVertexAttribArray(variableRef)
