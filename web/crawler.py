"""
This module is used to digest static web page into python object
"""
import weatherapp.model.forecast
from bs4 import BeautifulSoup
from urllib import request

class Crawler():
    forecast_link = "http://www.hko.gov.hk/textonly/v2/forecast/nday.htm"

    def crawl_forecast(self):
        with request.urlopen(Crawler.forecast_link) as response:
            html = response.read()
            if ( bool(BeautifulSoup(html, "html.parser").find()) ):
                return html
            else:
                raise ValueError("Invalid html crawled from crawler.")
            


"""
Example

9-day Weather Forecast
Bulletin updated at 16:30 HKT 01/May/2018

9-Day Weather Forecast

General Situation:
Under the influence of an anticyclone aloft, it will be
mainly fine and hot over the coast of southeastern China
tomorrow. An easterly airstream is expected to bring a few
showers to the coast of Guangdong in the following couple of
days. With the anticyclone aloft strengthening again over
the weekend, the weather will improve over the south China
coast.

Date/Month 2/5 (Wednesday)
Wind: South force 2 to 3.
Weather: Mainly fine and hot. Coastal fog in the morning.
Temp Range: 25 - 31 C
R.H. Range: 65 - 95 Per Cent

"""