#库函数
import sys
import pygame
import json
from bullet import Bullet
from alien import Alien
from time import sleep

def fire_bullet(aoa_settings,screen,ship,bullets):
          if ship.hit>=10:
              burning_love(aoa_settings,screen,ship,bullets)
              ship.hit-=10
          elif len(bullets)<aoa_settings.bullets_allowed:
                new_bullet=Bullet(aoa_settings,screen,ship,False)
                bullets.add(new_bullet)
          
def burning_love(aoa_settings,screen,ship,bullets):
    for x in range(0,aoa_settings.bullets_allowed):
        new_bullet=Bullet(aoa_settings,screen,ship,True)
        bullets.add(new_bullet)

def check_keydown_events(event,aoa_settings,screen,stats,ship,bullets):
    if event.key==pygame.K_RIGHT:
                    ship.moving_right=True
    elif event.key==pygame.K_LEFT:
                    ship.moving_left=True
    elif event.key==pygame.K_UP:
                    ship.moving_up=True
    elif event.key==pygame.K_DOWN:
                    ship.moving_down=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(aoa_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        filename='Highscore.json'
        with open(filename,'w')as f_obj:
                    json.dump(stats.high_score,f_obj)
        sys.exit()

def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
                    ship.moving_right=False
    elif event.key==pygame.K_LEFT:
                    ship.moving_left=False
    elif event.key==pygame.K_UP:
                    ship.moving_up=False
    elif event.key==pygame.K_DOWN:
                    ship.moving_down=False


def check_events(aoa_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    #响应按键和鼠标事件
    for event in pygame.event.get():#侦测输入设备
            if event.type==pygame.QUIT:#点击关闭窗口时触发QUIT事件
                filename='Highscore.json'
                with open(filename,'w')as f_obj:
                    json.dump(stats.high_score,f_obj)
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                check_keydown_events(event,aoa_settings,screen,stats,ship,bullets)
            elif event.type==pygame.KEYUP:
                check_keyup_events(event,ship)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                check_play_button(aoa_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(aoa_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        start_new_game(aoa_settings,screen,stats,sb,play_button,ship,aliens,bullets)

def start_new_game(aoa_settings,screen,stats,sb,play_button,ship,aliens,bullets):
        aoa_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active=True

        sb.prep_images()

        aliens.empty()
        bullets.empty()

        create_fleet(aoa_settings,screen,ship,aliens)
        ship.center_ship()

def update_screen(aoa_settings,screen,stats,sb,ship,aliens,bullets,play_button):
        screen.fill(aoa_settings.bg_color)#设置背景颜色
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        sb.show_score()
        if not stats.game_active:
           play_button.draw_button()
        pygame.display.flip()#更新屏幕

def update_bullets(aoa_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)
    check_bullet_alien_collisions(aoa_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(aoa_settings,screen,stats,sb,ship,aliens,bullets):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)#第一个True消灭前者，第二个True消灭后者
    if collisions:
        for aliens in collisions.values():
            ship.hit+=len(aliens)
            stats.score+=aoa_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens)==0:
        start_new_level(aoa_settings,screen,stats,sb,ship,aliens,bullets)

def start_new_level(aoa_settings,screen,stats,sb,ship,aliens,bullets):
        bullets.empty()
        aoa_settings.increase_speed()
        stats.level+=1
        sb.prep_level()
        create_fleet(aoa_settings,screen,ship,aliens)

def get_number_aliens_x(aoa_settings,alien_width):
    avaiable_space_x=aoa_settings.screen_width-2*alien_width
    number_aliens_x=int(avaiable_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(aoa_settings,ship_height,alien_height):
    available_space_y=(aoa_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(aoa_settings,screen,aliens,alien_number,row_number):
        alien=Alien(aoa_settings,screen)
        alien_width=alien.rect.width
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        aliens.add(alien)

def create_fleet(aoa_settings,screen,ship,aliens):
    alien=Alien(aoa_settings,screen)
    number_aliens_x=get_number_aliens_x(aoa_settings,alien.rect.width)
    number_rows=get_number_rows(aoa_settings,ship.rect.height,alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(aoa_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(aoa_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aoa_settings,aliens)
            break

def change_fleet_direction(aoa_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=aoa_settings.fleet_drop_speed
    aoa_settings.fleet_direction*=-1

def ship_hit(aoa_settings,screen,stats,sb,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1

        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(aoa_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def update_aliens(aoa_settings,screen,stats,sb,ship,aliens,bullets):
    check_fleet_edges(aoa_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(aoa_settings,screen,stats,sb,ship,aliens,bullets)
    check_aliens_bottom(aoa_settings,screen,stats,sb,ship,aliens,bullets)

def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()

def check_aliens_bottom(aoa_settings,screen,stats,sb,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(aoa_settings,screen,stats,sb,ship,aliens,bullets)
            break