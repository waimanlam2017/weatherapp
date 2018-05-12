from bs4 import BeautifulSoup
import datetime
import re

class Parser():
    def __init__(self, site_name, text_to_parse):
        self.site_name = site_name
        self.text_to_parse = text_to_parse
    
    def parse_to_today_forecast(self):
        soup = BeautifulSoup(self.text_to_parse, 'html.parser')
        daily_forecast_text = soup.body.link.pre.string
        list_of_lines = daily_forecast_text.splitlines()

        """
            Forecast Example
            ================================
            Date/Month 16/5(Wednesday)
            Wind: South force 3.
            Weather: Mainly fine and hot.
            Temp Range: 27 - 32 C
            R.H. Range: 60 - 85 Per Cent
        """

        #Calculate the year of forecast because the forecast does not contain year component
        today = datetime.datetime.now()
        if ( today.month == "12" and today.day == "31" ):
            next_day_year = today.year+1
        else:
            next_day_year = today.year

        for i in range(0 , len(list_of_lines)):
            #If the line starts with Date/Month, process the next four lines together
            if ( list_of_lines[i].startswith("Date") and "Month" in list_of_lines[i] ):                
                idx = i
                
                #print(list_of_lines[idx])
                #print(list_of_lines[idx+1])
                #print(list_of_lines[idx+2])
                #print(list_of_lines[idx+3])
                #print(list_of_lines[idx+4])

                date = list_of_lines[i]
                date_list = [int(s) for s in re.findall(r"[+-]?\d+(?:\.\d+)?", date)]
                forecast_day = date_list[0]
                forecast_month = date_list[1]
                idx+=1

                wind = list_of_lines[idx]
                wind_list = [int(s) for s in re.findall(r"[+-]?\d+(?:\.\d+)?", wind)]
                if ( len(wind_list) > 1 ):
                    min_wind_speed = wind_list[0]
                    max_wind_speed = wind_list[1]
                else:
                    min_wind_speed = wind_list[0]
                    max_wind_speed = wind_list[0]
                idx+=1

                #weather is ignored here for processing later
                flag_weather_section_not_done = True
                weather_list = []
                while(flag_weather_section_not_done):
                    weather_list.append(list_of_lines[idx])
                    if (list_of_lines[idx+1].startswith("Temp")):
                        flag_weather_section_not_done = False
                    idx+=1

                temperature = list_of_lines[idx]
                temperature_list = [int(s) for s in re.findall(r"[+-]?\d+(?:\.\d+)?", temperature)]  
                min_temperature = temperature_list[0]
                max_temperature = temperature_list[1]
                idx+=1

                relative_humidity = list_of_lines[idx]
                relative_humidity_list = [int(s) for s in re.findall(r"[+-]?\d+(?:\.\d+)?", relative_humidity)]  
                min_relative_humidity = relative_humidity_list[0]
                max_relative_humidity = relative_humidity_list[1]

                forecast_date = datetime.datetime(next_day_year, forecast_month, forecast_day,0,0,0,0)
                date_diff = forecast_date - today
                if ( date_diff.total_seconds() < 86400 ):                
                    print("Tomorrow is the forecast date!")
                    print("Date:", next_day_year, forecast_month, forecast_day)
                    print("Wind Speed: ", min_wind_speed, max_wind_speed)
                    print("Weather:", weather_list)
                    print("Temperature:", min_temperature, max_temperature)
                    print("Relative Humidity:", min_relative_humidity, max_relative_humidity)


        

"""
http://www.hko.gov.hk/textonly/v2/forecast/nday.htm

Forecast located by body->link->pre tag

<html lang="zh-hk">
 <head>
  <title>
   9-day Weather Forecast
  </title>
  <meta content="text/html; CHARSET=UTF-8" http-equiv="Content-Type">
   <meta content="WCAG2.0_Verified" name="Comments"/>
   <meta content="9-day Weather Forecast" name="Description"/>
   <meta content="9-day Weather Forecast" name="Keywords"/>
  </meta>
 </head>
 <body>
  <script src="/js/jquery/jquery-1.6.4.min.js" type="text/javascript">
  </script>
  <script src="/js/clf_textonly.js" type="text/javascript">
  </script>
  <style type="text/css">
   #wcag_logo_area{
        display:inline;
        text-align: center;
}
#wcag_logo_area a img{
        border: 0px;
        position:relative;
        top:12px;
}
  </style>
  <link href="/Logo.ico" rel="SHORTCUT ICON">
   <p align="center">
    <img alt="Hong Kong Observatory Logo" height="65" src="../../images_e/logo_dblue.gif" width="333">
    </img>
   </p>
   <h1 align="center">
    9-day Weather Forecast
   </h1>
   <p>
    <span style="font-style:italic;">
     Bulletin updated at 11:30 HKT 12/May/2018
    </span>
   </p>
   <!--9-day Weather Forecast-->
   <pre>
9-Day Weather Forecast

General Situation:
An anticyclone aloft over the northern part of the South
China Sea is expected to strengthen. The weather will be
mainly fine and hot over the south China coastal areas next
week.

Date/Month 13/5 (Sunday)
Wind: South force 3.
Weather: Sunny periods.
Temp Range: 26 - 30 C
R.H. Range: 70 - 90 Per Cent

Date/Month 14/5(Monday)
Wind: South force 3.
Weather: Mainly fine.
Temp Range: 26 - 31 C
R.H. Range: 65 - 85 Per Cent

Date/Month 15/5(Tuesday)
Wind: South force 3.
Weather: Fine and hot.
Temp Range: 27 - 32 C
R.H. Range: 60 - 85 Per Cent

Date/Month 16/5(Wednesday)
Wind: South force 3.
Weather: Mainly fine and hot.
Temp Range: 27 - 32 C
R.H. Range: 60 - 85 Per Cent

Date/Month 17/5(Thursday)
Wind: South to southwest force 3.
Weather: Mainly fine and hot. Isolated showers in the
morning.
Temp Range: 27 - 32 C
R.H. Range: 65 - 90 Per Cent

Date/Month 18/5(Friday)
Wind: South to southwest force 3.
Weather: Mainly fine and hot. Isolated showers in the
morning.
Temp Range: 27 - 32 C
R.H. Range: 65 - 90 Per Cent

Date/Month 19/5(Saturday)
Wind: South force 3.
Weather: Sunny periods and one or two showers.
Temp Range: 26 - 31 C
R.H. Range: 65 - 95 Per Cent

Date/Month 20/5(Sunday)
Wind: South force 3.
Weather: Sunny periods and a few showers.
Temp Range: 26 - 31 C
R.H. Range: 65 - 95 Per Cent

Date/Month 21/5(Monday)
Wind: South force 3.
Weather: Sunny periods and one or two showers.
Temp Range: 26 - 31 C
R.H. Range: 65 - 95 Per Cent

Sea surface temperature at 7 a.m.12/5/2018 at North Point
was 25 degrees C.

Soil temperatures at 7 a.m.12/5/2018 at the Hong Kong
Observatory:
0.5 M below surface was 25.8 degrees C.
1.0 M below surface was 26.0 degrees C.

Weather Cartoons for 9-day weather forecast
Day 1 cartoon no. 51 - SUNNY PERIODS
Day 2 cartoon no. 51 - SUNNY PERIODS
Day 3 cartoon no. 50 - SUNNY
Day 4 cartoon no. 51 - SUNNY PERIODS
Day 5 cartoon no. 51 - SUNNY PERIODS
Day 6 cartoon no. 51 - SUNNY PERIODS
Day 7 cartoon no. 53 - Sunny Periods with A Few Showers
Day 8 cartoon no. 53 - Sunny Periods with A Few Showers
Day 9 cartoon no. 53 - Sunny Periods with A Few Showers
</pre>
   <!--/9-day Weather Forecast-->
   <hr>
    |
    <a href="../readme.htm">
     Copyright and Disclaimer
    </a>
    |
    <a href="../index.htm">
     Home
    </a>
    |
    <a href="ndayc.htm">
     Chinese Version / 中文版本
    </a>
    |
    <a href="http://rss.weather.gov.hk/rss/SeveralDaysWeatherForecast.xml">
     <img alt="9-day Weather Forecast RSS" border="0" src="/img/rss3.gif"/>
    </a>
    |
    <br/>
    <div id="wcag_logo_area">
    </div>
    <link href="http://rss.weather.gov.hk/rss/SeveralDaysWeatherForecast.xml" rel="alternate" title="9-day Weather Forecast" type="application/rss+xml">
    </link>
   </hr>
  </link>
 </body>
</html>

"""