class Settings():
    #'''存储《外星人入侵》的所有设置的类'''

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船的设置
        self.ship_limit = 3

        #子弹设置
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 15

        #外星人设置
        self.fleet_drop_speed = 15

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 1
        # 积分
        self.alien_points = 50

        #flee_direction 为1表示向右移动，-1表示向左移动
        self.fleet_direction = 1

    def increase_speed(self):
        """ 提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)