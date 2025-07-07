import pygame
from pygame._sdl2 import Window

class UIManager():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.create_window()

    def create_window(self):
        pygame.init()
        win = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
        Window.from_display_module().maximize()
        
        running = True
        while running:
            self.clock.tick(60) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            win.fill((120, 50, 75))

            # refresh frame
            pygame.display.flip()



