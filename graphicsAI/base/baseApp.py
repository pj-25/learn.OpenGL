import pygame
import sys

from graphicsAI.base.inputHandler import InputHandler

class BaseApp:

    def __init__(self, title, displaySize=[512, 512]):
        '''
        BaseApp Constructor: 
            initializing display properties/attributes; 
            creating and displaying window
        '''
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        renderingOptions = pygame.GL_DOUBLEBUFFER | pygame.OPENGL

        pygame.display.set_mode(displaySize, renderingOptions)
        pygame.display.set_caption(title)

        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.inputHandler = InputHandler()

        self.timeElapsed = 0

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()
        
        while self.isRunning:
            self.inputHandler.update()
            self.isRunning = not self.inputHandler.quit
            
            self.deltaTime = self.clock.get_time() / 1000
            self.timeElapsed += self.deltaTime

            self.update()
        
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
        sys.exit()
    

