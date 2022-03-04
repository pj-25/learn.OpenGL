import pygame

class InputHandler:

    def __init__(self):
        self.quit = False

        self.keyDownList = [] 
        self.keyPressedList = [] 
        self.keyUpList = []
    
    def update(self):
        self.keyDownList = [] 
        self.keyUpList = []

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name( event.key )
                self.keyDownList.append( keyName )
                self.keyPressedList.append( keyName ) 
            if event.type == pygame.KEYUP:
                keyName = pygame.key.name( event.key ) 
                self.keyPressedList.remove( keyName ) 
                self.keyUpList.append( keyName )

            if event.type == pygame.QUIT:
                self.quit = True
        
    # functions to check key states 
    def isKeyDown(self, keyCode): 
        return keyCode in self.keyDownList 
    def isKeyPressed(self, keyCode): 
        return keyCode in self.keyPressedList 
    def isKeyUp(self, keyCode): 
        return keyCode in self.keyUpList