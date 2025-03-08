import pygame
from colors import *

class Menu():
    def __init__(self, screen_size, OFFSET):
        self.screen_size=screen_size
        self.OFFSET=OFFSET
        self.reset_button=pygame.Rect(screen_size[0]-OFFSET-screen_size[0]*1/8,OFFSET,screen_size[0]*1/8,screen_size[1]*1/16)
        self.font=pygame.font.SysFont("Zen Maru Gothic Black",size=24)
        self.text=self.font.render("RESET",True,WHITE)
    
    def draw(self, screen):
        pygame.draw.rect(screen, BROWN, self.reset_button)
        screen.blit(self.text,(self.screen_size[0]-self.OFFSET-self.screen_size[0]*1/8,self.OFFSET))
        return 0
    
    def get_button(self, id):
        match id:
            case 0:
                return self.reset_button
            case _:
                return None