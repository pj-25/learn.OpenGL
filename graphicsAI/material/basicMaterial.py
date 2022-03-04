from graphicsAI.material.material import Material 
from graphicsAI.base.uniformVar import UniformVar

class BasicMaterial(Material):
    def __init__(self, vertexShaderCode=None, fragmentShaderCode=None):
        if vertexShaderCode is None:
            vertexShaderCode = ''
            with open('shaders/simpleVertexShader.vs', 'r') as shaderFile:
                vertexShaderCode = shaderFile.read()
        if fragmentShaderCode is None:
            fragmentShaderCode = ''
            with open('shaders/simpleFragmentShader.fs', 'r') as shaderFile:
                fragmentShaderCode = shaderFile.read()

        super().__init__(vertexShaderCode, fragmentShaderCode) 
        self.addUniform("vec3", "baseColor", [1.0, 1.0, 1.0]) 
        self.addUniform("bool", "useVertexColors", False) 
        self.locateUniforms()