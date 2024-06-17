import json
from pprint import pprint

class UserData:

    def __init__(self, user_name, text, num_mistake, middle_time_pressed, middle_speed, middle_speed_without_big_pauses, dict_symbols, dict_pauses):

        self.user_name = user_name
        self.text = text
        self.num_mistake = num_mistake
        self.middle_time_pressed = middle_time_pressed
        self.middle_speed = middle_speed
        self.middle_speed_without_big_pauses = middle_speed_without_big_pauses
        self.dict_symbols = dict_symbols
        self.dict_pauses = dict_pauses




