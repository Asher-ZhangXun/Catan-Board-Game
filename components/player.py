"""
Player class

"""


class Player:
    def __init__(self, super_surface_object, color):
        self.super_surface_object = super_surface_object
        self.color = color
        self.settlement = 0
        self.city = 0
        self.road = 0
        self.resources = {
            "brick": 0,
            "ore": 0,
            "grain": 0,
            "lumber": 0,
            "wool": 0
        }
        self.chooseable_settlement_buttons = self.super_surface_object.main_board.settlement_buttons.copy()
        self.chooseable_road_buttons = []

    def get_total_points(self):
        return self.settlement * 1 + self.city * 2 #TODO: Check the rule that if roads should be counted to points

