from graphicsAI.base import inputHandler
from graphicsAI.base.baseApp import BaseApp
from OpenGL.GL import *
from graphicsAI.base.matrixUtils import MatrixUtils
from graphicsAI.base.openGLUtils import OpenGLUtils
from graphicsAI.base.attribute import Attribute
from graphicsAI.base.uniformVar import UniformVar
from math import pi

class TestApp3(BaseApp):

    def initialize(self):
        
        # set default gl properties
        glClearColor(0.0,0.0,0.0,1.0)
        glEnable(GL_DEPTH_TEST)
        glPointSize(30)

        #load vertex shader and fragment shader 
        vertexShaderCode = ''
        with open('shaders/vertexShader3.vs', 'r') as vertexShaderFile:
            vertexShaderCode = vertexShaderFile.read()
        
        fragmentShaderCode = ''
        with open('shaders/fragmentShader3.fs', 'r') as fragmentShaderFile:
            fragmentShaderCode = fragmentShaderFile.read()
        
        #compile shaders 
        vertexShaderRef = OpenGLUtils.initShader(vertexShaderCode)
        fragmentShaderRef = OpenGLUtils.initShader(fragmentShaderCode, GL_FRAGMENT_SHADER)
        self.programRef = OpenGLUtils.initProgram(vertexShaderRef, fragmentShaderRef)

        #generate and bind vertex arrays
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        #bind and upload vertex attributes
        position = [[0.0,0.2,0.0],
                    [0.1,-0.2,0.0],
                    [-0.1,-0.2,0.0]]
        self.posAttribute = Attribute('vec3', position)
        self.posAttribute.associateVariable(self.programRef, 'position')
        self.posAttribute.uploadDataToBuffer()

        #bind uniform variables
        modelData = MatrixUtils.createTranslation(0,0,-1)
        self.modelMatrix = UniformVar('mat4', modelData)
        self.modelMatrix.associateVariableReference(self.programRef, 'modelMatrix')

        angleOfView = 60
        aspectRatio = 1.0
        projectionData = MatrixUtils.createPerspective(0.1, 1000, angleOfView, aspectRatio)
        self.projectionMatrix = UniformVar('mat4', projectionData)
        self.projectionMatrix.associateVariableReference(self.programRef, 'projectionMatrix')

        self.moveSpeed = 0.5
        self.turnSpeed = pi/2
        

    def update(self):
        moveAmount = self.moveSpeed * self.deltaTime
        turnAmount = self.turnSpeed * self.deltaTime
        ##onKeyPress Events
        #global Transformation
        if(self.inputHandler.isKeyPressed('w')):
            m = MatrixUtils.createTranslation(0,moveAmount,0)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if(self.inputHandler.isKeyPressed('s')):
            m = MatrixUtils.createTranslation(0,-moveAmount,0)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if(self.inputHandler.isKeyPressed('a')):
            m = MatrixUtils.createTranslation(-moveAmount,0,0)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if(self.inputHandler.isKeyPressed('d')):
            m = MatrixUtils.createTranslation(moveAmount,0,0)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if(self.inputHandler.isKeyPressed('z')):
            m = MatrixUtils.createTranslation(0,0,moveAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if(self.inputHandler.isKeyPressed('x')):
            m = MatrixUtils.createTranslation(0,0,-moveAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data
    
        if(self.inputHandler.isKeyPressed('q')):
            m = MatrixUtils.createRotationZ(turnAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data
        if(self.inputHandler.isKeyPressed('e')):
            m = MatrixUtils.createRotationZ(-turnAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data
        
        #local transformation
        if(self.inputHandler.isKeyPressed('i')):
            m = MatrixUtils.createTranslation(0,moveAmount,0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if(self.inputHandler.isKeyPressed('k')):
            m = MatrixUtils.createTranslation(0,-moveAmount,0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if(self.inputHandler.isKeyPressed('j')):
            m = MatrixUtils.createTranslation(-moveAmount,0,0)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if(self.inputHandler.isKeyPressed('l')):
            m = MatrixUtils.createTranslation(moveAmount,0,0)
            self.modelMatrix.data = self.modelMatrix.data @ m
    
        if(self.inputHandler.isKeyPressed('u')):
            m = MatrixUtils.createRotationZ(turnAmount)
            self.modelMatrix.data = self.modelMatrix.data @ m
        if(self.inputHandler.isKeyPressed('o')):
            m = MatrixUtils.createRotationZ(-turnAmount)
            self.modelMatrix.data = self.modelMatrix.data @ m
        
        #render scene
        glUseProgram(self.programRef)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.modelMatrix.uploadData()
        self.projectionMatrix.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, 3)


TestApp3('Test App 3').run()


