from OpenGL.GL import *

from graphicsAI.base.openGLUtils import OpenGLUtils
from graphicsAI.base.uniformVar import UniformVar

class Material(object):
    def __init__(self, vertexShaderCode, fragmentShaderCode):
        self.programRef = OpenGLUtils. initProgram(vertexShaderCode, fragmentShaderCode)
        self.uniforms = {} 
        
        self.uniforms["modelMatrix"] = UniformVar("mat4", None) 
        self.uniforms["viewMatrix"] = UniformVar("mat4", None) 
        self.uniforms["projectionMatrix"] = UniformVar("mat4", None) 
        
        self.settings = {} 
        self.settings["drawStyle"] = GL_TRIANGLES

    def addUniform(self, dataType, variableName, data): 
        self.uniforms[variableName] = UniformVar(dataType, data)
    
    # initialize all uniform variable references 
    def locateUniforms(self): 
        for variableName, uniformObject in self. uniforms.items(): 
            uniformObject.setVariableReference( self.programRef, variableName )
        
    # configure OpenGL with render settings 
    def updateRenderSettings(self): pass
    
    # convenience method for setting multiple material "properties" 
    # (uniform and render setting values) from a dictionary 
    def setProperties(self, properties):
        for name, data in properties.items(): 
            if name in self.uniforms.keys():
                self.uniforms[name].data = data 
            elif name in self.settings.keys():
                self.settings[name] = data 
            else:
                raise Exception( "Material has no property named: " + name)
