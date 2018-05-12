"""
Source of information:
===============================================================================
9 day Weather forecast: http://www.hko.gov.hk/textonly/v2/forecast/nday.htm

Could obtain - Date
             - Wind
               - Direction
               - Level
             - Weather
             - Temperature Range ( Unit: Degree Celsius )
               - Lowest
               - Highest 
             - R.H Range ( Unit: Percent )
               - Lowest
               - Highest

Class Design:
    - date : String
    - wind_direction : String
    - wind_level_min: int
    - wind_level_max: int
    - temperature_min: int
    - temperature_max: int
    - relative_humidity_min: int
    - relative_humidity_max: int
"""
class Forecast():
    def __init__(self, date, wind_direction, wind_level_min, wind_level_max, temperature_min, temperature_max, relative_humidity_min, relative_humidity_max):
        self.date = date
        self.wind_direction = wind_direction
        self.wind_level_min = wind_level_min
        self.wind_level_max = wind_level_max
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.relative_humidity_min = relative_humidity_min
        self.relative_humidity_max = relative_humidity_max
        
