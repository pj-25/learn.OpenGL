from graphicsAI.base.baseApp import BaseApp
from graphicsAI.base.openGLUtils import OpenGLUtils
from OpenGL.GL import *

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

        glPointSize(10)

        print('System Info:', OpenGLUtils.getSystemInfo())


    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_POINTS, 0, 1)

TestApp('Test App').run()
