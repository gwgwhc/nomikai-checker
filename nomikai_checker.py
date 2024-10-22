import datetime as dt
import random
from dataclasses import dataclass

img_paths = {
    'nekochan': 'images/nekochan.png',
    'isogashii': 'images/isogashii_woman.png',
    'gaman': 'images/gaman_osake_woman.png',
    'energy': 'images/energy_drink.png'
}


@dataclass
class DayInfo:
    chance: float
    time_modifier: float


class NomikaiChecker(self):
    def __init__(self):
        self.day_data = {
            'Monday': DayInfo(chance=0.001, time_modifier=0.01),
            'Tuesday': DayInfo(chance=0.002, time_modifier=0.01),
            'Wednesday': DayInfo(chance=0.01, time_modifier=0.2),
            'Thursday': DayInfo(chance=0.003, time_modifier=0.01),
            'Friday': DayInfo(chance=0.50, time_modifier=0.5),
            'Saturday': DayInfo(chance=0.99, time_modifier=1.0),
            'Sunday': DayInfo(chance=0.9, time_modifier=1.0)
        }

    def check_probability(self):
        today = dt.datetime.today()
        day_info = self.day_data.get(today.strftime('%A'), DayInfo(chance=0.01, time_modifier=0.5))
        
        if today.hour < 16:
            chance_final = day_info.chance * day_info.time_modifier
        else:
            chance_final = day_info.chance

        return random.random() < chance_final

# def nomikai_kakunin():
#     today = dt.datetime.today()
#     if today.strftime('%A') in nomikai_days and today.hour < 18:
#         message = 'Be patient, the nomikai will come...'
#         image = 'gaman'
#     elif today.strftime('%A') in nomikai_days and today.hour >= 18:
#         message = 'Leave the office ASAP. Nomikai time.'
#         image = 'energy'
#     elif today.strftime('%A') == 'Sunday':
#         message = 'What are you doing? Go and drink!'
#         image = 'energy'
#     else:
#         message = 'Today you must work harder...'
#         image = 'isogashii'
#     return message, image
