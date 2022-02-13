from OpenGL.GL import * 

class OpenGLUtils:

    @staticmethod
    def initShader(shaderSourceCode, shaderType=GL_VERTEX_SHADER):
        shaderRef = glCreateShader(shaderType)
        shaderSourceCode = '#version 330\n'+shaderSourceCode
        glShaderSource(shaderRef, shaderSourceCode)
        glCompileShader(shaderRef)

        isCompiled = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)
        if not isCompiled:
            compileErrorInfo = glGetShaderInfoLog(shaderRef)
            glDeleteShader(shaderRef)
            compileErrorInfo = '\n'+compileErrorInfo.decode('utf-8')
            raise Exception(compileErrorInfo)
        return shaderRef

    @staticmethod
    def initProgram(vertexShaderRef, fragmentShaderRef):
        progRef = glCreateProgram()
        glAttachShader(progRef, vertexShaderRef)
        glAttachShader(progRef, fragmentShaderRef)
        glLinkProgram(progRef)

        isLinked = glGetProgramiv(progRef, GL_LINK_STATUS)
        if not isLinked:
            linkErrorInfo = glGetProgramInfoLog(progRef)
            glDeleteProgram(progRef)
            linkErrorInfo = '\n'+linkErrorInfo.decode('utf-8')
            raise Exception(linkErrorInfo)
        
        return progRef

    @staticmethod
    def getSystemInfo():
        return {"Vendor":glGetString(GL_VENDOR).decode('utf-8'), 
                "Renderer":glGetString(GL_RENDERER).decode('utf-8'),
                "OpenGL_Version_Supported":glGetString(GL_VERSION).decode('utf-8'),
                "GLSL_Version_Supported:":glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8')
                }