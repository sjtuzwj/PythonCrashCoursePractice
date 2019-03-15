#主程序
import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    #初始化背景设置
    pygame.init()
    aoa_settings=Settings()
    screen=pygame.display.set_mode(
        (aoa_settings.screen_width,aoa_settings.screen_height))
    pygame.display.set_caption("Attack on Alien")

    #初始化对象
    play_button=Button(aoa_settings,screen,'PLAY')
    stats=GameStats(aoa_settings)
    sb=Scoreboard(aoa_settings,screen,stats)
    ship=Ship(aoa_settings,screen)
    bullets=Group()
    alien=Alien(aoa_settings,screen)
    aliens=Group()
    gf.create_fleet(aoa_settings,screen,ship,aliens)

    #游戏界面刷新
    while True:
        gf.check_events(aoa_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aoa_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(aoa_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(aoa_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()