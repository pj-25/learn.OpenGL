from graphicsAI.base.baseApp import BaseApp
from graphicsAI.base.openGLUtils import OpenGLUtils
from OpenGL.GL import *
from graphicsAI.base.attribute import Attribute

class TestApp(BaseApp):

    def initialize(self):
        print('Initializing the app.......')

        vertexShaderSource = ''
        with open('shaders/simpleVertexShader.vs', 'r') as shaderFile:
            vertexShaderSource = shaderFile.read()

        fragmentShaderSource = ''
        with open('shaders/simpleFragmentShader.fs', 'r') as shaderFile:
            fragmentShaderSource = shaderFile.read()
        
        vertexShaderRef = OpenGLUtils.initShader(vertexShaderSource)
        fragmentShaderRef = OpenGLUtils.initShader(fragmentShaderSource, GL_FRAGMENT_SHADER)
        self.programRef = OpenGLUtils.initProgram(vertexShaderRef, fragmentShaderRef)

        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        glPointSize(30)
        glLineWidth(10)

        vertexPos = [[0.8, 0.0, 0.0], 
                        [0.4, 0.6, 0.0],
                        [-0.4, 0.6, 0.0],
                        [-0.8, 0.0, 0.0],
                        [-0.4, -0.6, 0.0],
                        [0.4, -0.6, 0.0]]
        self.vertexPosAttr = Attribute('vec3',vertexPos)
        self.vertexPosAttr.associateVariable(self.programRef, 'position')

        vertexColor = [[1.0, 0.0, 0.0],
                        [1.0, 0.5, 0.0],
                        [1.0, 1.0, 0.0],
                        [0.0, 1.0, 0.0],
                        [0.0, 0.0, 1.0],
                        [0.5, 0.0, 1.0]]
        self.vertexColorAttr = Attribute('vec3', vertexColor)
        self.vertexColorAttr.associateVariable(self.programRef, 'vertexColor')

        print('System Info:', OpenGLUtils.getSystemInfo())


    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_TRIANGLE_FAN, 0, len(self.vertexPosAttr.data))
        glDrawArrays(GL_POINTS, 0, len(self.vertexPosAttr.data))

TestApp('Test App').run()
