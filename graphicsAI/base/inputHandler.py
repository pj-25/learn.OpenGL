import pygame

class InputHandler:

    def __init__(self):
        self.quit = False
        self.hasEventOccurred=False

    def update(self):
        self.downKeys = []
        self.upKeys = []
        self.pressedKeys = []
        self.hasEventOccurred = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                downKey = pygame.key.name(event.key)
                self.downKeys.append(downKey)
                self.pressedKeys.append(downKey)
                self.hasEventOccurred = True

            if event.type == pygame.KEYUP:
                upKey = pygame.key.name(event.key)
                self.upKeys.append(upKey)
                self.pressedKeys.remove(upKey)
                self.hasEventOccurred = True

            if event.type == pygame.QUIT:
                self.quit = True
                self.hasEventOccurred = True
            
            