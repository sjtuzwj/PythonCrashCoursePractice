#子弹的抽象
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """子弹管理"""
    def __init__(self,aoa_settings,screen,ship,mode):
        super().__init__()
        self.screen=screen
        self.mode=mode
        if self.mode:
            self.rect=pygame.Rect(0,0,aoa_settings.bullet_width,aoa_settings.screen_height)
            self.speed_factor=aoa_settings.bullet_speed_factor*15
            self.color=(255,0,0)
        else:
            self.rect=pygame.Rect(0,0,aoa_settings.bullet_width,aoa_settings.bullet_height)
            self.speed_factor=aoa_settings.bullet_speed_factor
            self.color=aoa_settings.bullet_color

        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        
        self.y=float(self.rect.y)
    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)#颜色填充屏幕

