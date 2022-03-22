from OpenGL.GL import *

class UniformVar:

    def __init__(self, dataType, data):
        self.dataType = dataType
        self.data = data
        self.varRef = None
        self.varName = None
    
    def associateVariableReference(self, progRef, varName):
        self.varRef = glGetUniformLocation(progRef, varName)
        self.varName = varName

    def uploadData(self):
        if self.varRef == -1:
            return

        if(self.dataType == 'int'):
            glUniform1i(self.varRef, self.data)
        elif self.dataType == 'float':
            glUniform1f(self.varRef, self.data)
        elif self.dataType == 'vec2':
            glUniform2f(self.varRef, self.data[0], self.data[1])
        elif self.dataType == 'vec3':
            glUniform3f(self.varRef, self.data[0], self.data[1], self.data[2])
        elif self.dataType == 'vec4':
            glUniform4f(self.varRef, self.data[0], self.data[1], self.data[2], self.data[3])
        elif self.dataType == 'mat4':
            glUniformMatrix4fv(self.varRef, 1, GL_TRUE, self.data)
        else:
            raise Exception('Invalid datatype({0}) for uniform variable({1})'.format(self.dataType, self.varName))