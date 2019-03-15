import json
class   GameStats(object):
    def __init__(self,aoa_settings):
        filename='Highscore.json'
        with open(filename)as f_obj:
            self.high_score=int(json.load(f_obj))
        self.aoa_settings=aoa_settings
        self.game_active=False
        self.reset_stats()
    def reset_stats(self):
        self.ships_left=self.aoa_settings.ship_limit
        self.score=0
        self.level=1

