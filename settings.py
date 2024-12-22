
class Settings:
    """ class to keep all settings"""
    def __init__(self):
        """ initialize settings """
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 10
        self.ship_limit = 3
        #bullet settings
        self.bullet_speed = 10
        self.bullet_width = 400
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 30
        #alien settings
        self.alien_speed = 12.0
        self.fleet_drop_speed = 30
        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        # game speed up rate
        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()
        self.alien_points = 50

    def initialize_dynamic_settings(self):
            self.ship_speed = 1.5
            self.bullet_speed = 2.5
            self.alien_speed = 1
            self.fleet_direction = 1
        
    def increase_speed(self):
            self.ship_speed *= self.speedup_scale
            self.bullet_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale