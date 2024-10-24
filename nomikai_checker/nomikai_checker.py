import datetime as dt
import random
from dataclasses import dataclass


@dataclass
class DayInfo:
    chance: float
    time_modifier: float


class NomikaiChecker():
    def __init__(self):
        """ Initialize with probabilities and time modifiers for each day"""
        self.day_data = {
            'Monday': DayInfo(chance=0.001, time_modifier=0.02),
            'Tuesday': DayInfo(chance=0.002, time_modifier=0.02),
            'Wednesday': DayInfo(chance=0.01, time_modifier=0.001),
            'Thursday': DayInfo(chance=0.003, time_modifier=0.02),
            'Friday': DayInfo(chance=0.05, time_modifier=0.5),
            'Saturday': DayInfo(chance=0.99, time_modifier=1.0),
            'Sunday': DayInfo(chance=0.5, time_modifier=1.8)
        }
        self.today = self.get_day_info()

    def get_datetime(self):
        """ Return date time object for current time. """
        return dt.datetime.today()

    def get_day_info(self):
        """ Get today's name and related probability/modifiers. """
        today_name = self.get_datetime().strftime('%A')
        # Default if day not found
        return self.day_data.get(today_name, DayInfo(chance=0.01, time_modifier=0.5))

    def is_before_4pm(self):
        """Check if the current time is before 4 PM."""
        return self.get_datetime().hour < 16

    def calculate_probability(self):
        """Calculate the final probability based on the day's chance and the time modifier."""
        day_info = self.today
        if self.is_before_4pm():
            return day_info.chance * day_info.time_modifier
        return day_info.chance

    def check_probability(self):
        """Determine if the user can go for nomikai based on the calculated probability."""
        return random.random() < self.calculate_probability()


def test():
    checker = NomikaiChecker()
    print(checker.check_probability())


if __name__ == '__main__':
    test()
