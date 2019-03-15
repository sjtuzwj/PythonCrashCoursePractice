#飞船的抽象
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """description of class"""
    def __init__(self,aoa_settings,screen):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp')#返回表示飞船的surface
        self.image=pygame.transform.scale(self.image,(60,40))#缩放
        self.rect=self.image.get_rect()#用矩形来处理游戏元素
        self.screen_rect=screen.get_rect()
        self.aoa_settings=aoa_settings
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)
        #移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.hit=0
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx+=self.aoa_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.centerx-=self.aoa_settings.ship_speed_factor
        if self.moving_up and self.rect.top>0:
            self.centery-=self.aoa_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.centery+=self.aoa_settings.ship_speed_factor
        self.rect.centerx=self.centerx
        self.rect.centery=self.centery

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.centerx=self.screen_rect.centerx
        self.centery=self.screen_rect.bottom

