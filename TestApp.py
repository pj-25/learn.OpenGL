from turtle import speed
from math import sin, cos
from graphicsAI.base.baseApp import BaseApp
from graphicsAI.base.matrix import Matrix
from graphicsAI.base.openGLUtils import OpenGLUtils
from OpenGL.GL import *
from graphicsAI.base.attribute import Attribute
from graphicsAI.base.uniformVar import UniformVar
from math import pi

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

        vertexPos = [ [0.0, 0.2, 0.0], 
                      [0.1, -0.2, 0.0],
                      [-0.1, -0.2, 0.0] ] 
        self.vertexCount = len(vertexPos) 
        self.vertexPosAttr = Attribute('vec3',vertexPos)
        self.vertexPosAttr.associateVariable(self.programRef, 'position')

        vertexColor = [1.0, 0.0, 0.0]
        self.vertexColorAttr = Attribute('vec3', vertexColor)
        self.vertexColorAttr.associateVariable(self.programRef, 'vertexColor')

        mMatrix = Matrix.makeTranslation(0, 0, -1) 
        self.modelMatrix = UniformVar("mat4", mMatrix) 
        self.modelMatrix.setVariableReference( self.programRef,"modelMatrix" )
        
        pMatrix = Matrix.makePerspective() 
        self.projectionMatrix = UniformVar("mat4", pMatrix) 
        self.projectionMatrix.setVariableReference( self.programRef,"projectionMatrix" )

        self.moveSpeed = 0.5 
        self.turnSpeed = 90 * (pi / 180)

        print('System Info:', OpenGLUtils.getSystemInfo())


    def update(self):
        moveAmount = self.moveSpeed * self.deltaTime 
        turnAmount = self.turnSpeed * self.deltaTime

        # global translation
        if self.inputHandler.isKeyPressed("w"): 
            m = Matrix.makeTranslation(0, moveAmount, 0) 
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.inputHandler.isKeyPressed("s"): 
            m = Matrix.makeTranslation(0, -moveAmount, 0) 
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.inputHandler.isKeyPressed("a"): 
            m = Matrix.makeTranslation(-moveAmount, 0, 0) 
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.inputHandler.isKeyPressed("d"): 
            m = Matrix.makeTranslation(moveAmount, 0, 0) 
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.inputHandler.isKeyPressed("z"): 
            m = Matrix.makeTranslation(0, 0, moveAmount) 
            self.modelMatrix.data = m @ self.modelMatrix.data
        if self.inputHandler.isKeyPressed("x"): 
            m = Matrix.makeTranslation(0, 0, -moveAmount) 
            self.modelMatrix.data = m @ self.modelMatrix.data

        # global rotation (around the origin)
        if self.inputHandler.isKeyPressed("q"):
            m = Matrix.makeRotationZ(turnAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data 
        if self.inputHandler.isKeyPressed("e"):
            m = Matrix.makeRotationZ(-turnAmount)
            self.modelMatrix.data = m @ self.modelMatrix.data

        # local translation
        if self.inputHandler.isKeyPressed("i"):
            m = Matrix.makeTranslation(0, moveAmount, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m 
        if self.inputHandler.isKeyPressed("k"):
            m = Matrix.makeTranslation(0, -moveAmount, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m 
        if self.inputHandler.isKeyPressed("j"):
            m = Matrix.makeTranslation(-moveAmount, 0, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m 
        if self.inputHandler.isKeyPressed("l"):
            m = Matrix.makeTranslation(moveAmount, 0, 0)
            self.modelMatrix.data = self.modelMatrix.data @ m

        # local rotation (around object center)
        if self.inputHandler.isKeyPressed("u"):
            m = Matrix.makeRotationZ(turnAmount)
            self.modelMatrix.data = self.modelMatrix.data @ m 
        if self.inputHandler.isKeyPressed("o"):
            m = Matrix.makeRotationZ(-turnAmount)
            self.modelMatrix.data = self.modelMatrix.data @ m
        
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.programRef)
        
        self.projectionMatrix.uploadData() 
        self.modelMatrix.uploadData() 

        glDrawArrays( GL_TRIANGLES , 0 , self.vertexCount )        

        

TestApp('Test App').run()
