from turtle import speed
from math import sin, cos
from graphicsAI.base.baseApp import BaseApp
from graphicsAI.base.openGLUtils import OpenGLUtils
from OpenGL.GL import *
from graphicsAI.base.attribute import Attribute
from graphicsAI.base.uniformVar import UniformVar

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
    
        glClearColor(0.0,0.0,0.0,1.0)

        glPointSize(30)
        glLineWidth(10)

        vertexPos = [0.0,0.0,0.0]
        self.vertexPosAttr = Attribute('vec3',vertexPos)
        self.vertexPosAttr.associateVariable(self.programRef, 'position')

        vertexColor = [1.0, 0.0, 0.0]
        self.vertexColorAttr = Attribute('vec3', vertexColor)
        self.vertexColorAttr.associateVariable(self.programRef, 'vertexColor')

        translationData = [0.0, 0.0, 0.0]
        self.uniTranslation = UniformVar('vec3', translationData)
        self.uniTranslation.setVariableReference(self.programRef, 'translation')

        print('System Info:', OpenGLUtils.getSystemInfo())


    def update(self):
        # x=rcos(t)+a, y=rsin(t)+b
        self.uniTranslation.data[0] = 0.75 * cos(self.timeElapsed)
        self.uniTranslation.data[1] = 0.75 * sin(self.timeElapsed)
        
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.programRef)
        
        self.uniTranslation.uploadData()
        self.vertexColorAttr.uploadDataToBuffer()

        glDrawArrays(GL_POINTS, 0, 1)
        

        

TestApp('Test App').run()
