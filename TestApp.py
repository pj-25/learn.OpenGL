from graphicsAI.base.baseApp import BaseApp
from OpenGL.GL import *
from graphicsAI.base.openGLUtils import OpenGLUtils
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

        #vaoRef = glGenVertexArrays(1)
        #glBindVertexArray(vaoRef)
    
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
        self.uniTranslation.associateVariableReference(self.programRef, 'translation')

        print('System Info:', OpenGLUtils.getSystemInfo())

        self.step = 0.02
        self.slope = 0.6


    def update(self):
        glUseProgram(self.programRef)
        glClear(GL_COLOR_BUFFER_BIT)
 
        if not (-0.97< self.uniTranslation.data[0] < 0.97):
            self.step = -self.step
            self.slope = -self.slope
        elif not (-0.97 < self.uniTranslation.data[1] < 0.97):
            self.slope = -self.slope

        self.uniTranslation.data[0] += self.step
        self.uniTranslation.data[1] += self.slope*self.step
        self.uniTranslation.uploadData()

        glDrawArrays(GL_POINTS, 0, 1)
        if(self.inputHandler.hasEventOccurred):
            print('pressed keys:', self.inputHandler.pressedKeys)
            print('up keys:', self.inputHandler.upKeys)
            print('down keys:', self.inputHandler.downKeys)
        

TestApp('Test App').run()
