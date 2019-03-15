#游戏设置
class Settings(object):
    """store settings"""
    def __init__(self):
        self.screen_width=800
        self.screen_height=600
        self.bg_color=(255,255,255)
        self.fleet_drop_speed=10
        self.bullet_width=3
        self.bullet_height=6
        self.bullet_color=60,60,60
        self.bullets_allowed=5
        self.ship_limit=3
        self.speed_up_scale=1.2
        self.score_scale=1.5
        self.chargelen=10
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=2
        self.alien_speed_factor=1#也可表示方向，-为左
        self.fleet_direction=1
        self.alien_points=50
    def increase_speed(self):
        self.ship_speed_factor*=self.speed_up_scale
        self.bullet_speed_factor*=self.speed_up_scale
        self.alien_speed_factor*=self.speed_up_scale

        self.alien_points=int(self.alien_points*self.score_scale)



