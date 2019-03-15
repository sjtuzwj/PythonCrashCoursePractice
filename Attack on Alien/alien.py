import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,aoa_settings,screen):
        super().__init__()
        self.screen=screen
        self.aoa_settings=aoa_settings
        self.image=pygame.image.load('images/alien.bmp')
        self.image=pygame.transform.scale(self.image,(45,45))
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.x+=self.aoa_settings.alien_speed_factor*self.aoa_settings.fleet_direction
        self.rect.x=self.x
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right or self.rect.left<=0:
            return True



