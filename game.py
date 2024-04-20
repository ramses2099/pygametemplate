import pygame, sys
from settings import *
from state import SplashScreen

class Game:
    def __init__(self):
      pygame.init()
      self.clock = pygame.time.Clock()
      self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
      pygame.display.set_caption(TITLE)
      self.font = pygame.font.Font(FONT, TITLESIZE)
      self.running = True
      # state machine
      self.states = []
      self.splash_screen = SplashScreen(self)
      self.states.append(self.splash_screen)
    
    def render_text(self, text, color, font, pos, centrilised=True):
        surf = font.render(str(text), False, color)
        rect = None 
        if centrilised:
            rect = surf.get_rect(center = pos)
        else:
            rect = surf.get_rect(topleft = pos)
        self.screen.blit(surf, rect)
         
    def get_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    INPUTS['escape'] = True
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    INPUTS['space'] = True
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    INPUTS['left'] = True
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    INPUTS['right'] = True
                elif event.key in (pygame.K_UP, pygame.K_w):
                    INPUTS['up'] = True
                elif event.key in (pygame.K_DOWN, pygame.K_x):
                    INPUTS['down'] = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    INPUTS['space'] = False
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    INPUTS['left'] = False
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    INPUTS['right'] = False
                elif event.key in (pygame.K_UP, pygame.K_w):
                    INPUTS['up'] = False
                elif event.key in (pygame.K_DOWN, pygame.K_x):
                    INPUTS['down'] = False
                    
            if event.type == pygame.MOUSEWHEEL:
                if event.y  == 1:
                    INPUTS['scroll_up'] = True
                elif event.y == -1:
                    INPUTS['scroll_down'] = True
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button  == 1:
                    INPUTS['left_click'] = True
                if event.button  == 3:
                    INPUTS['right_click'] = True
                if event.button  == 4:
                    INPUTS['scroll_down'] = True
                if event.button  == 2:
                    INPUTS['scroll_up'] = True
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button  == 1:
                    INPUTS['left_click'] = False
                if event.button  == 3:
                    INPUTS['right_click'] = False
                if event.button  == 4:
                    INPUTS['scroll_down'] = False
                if event.button  == 2:
                    INPUTS['scroll_up'] = False

    def reset_inputs(self):
        for key in INPUTS:
            INPUTS[key] = False

    def loop(self):
        while self.running:
            dt = self.clock.tick(FPS)/1000
            self.get_inputs()
            # state machine
            # update
            self.states[-1].update(dt)
            # draw
            self.states[-1].draw(self.screen)
            # 
            pygame.display.update()
