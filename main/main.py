from weatherapp.model.forecast import Forecast
from weatherapp.web.crawler import Crawler
from weatherapp.text.parser import Parser

crawler = Crawler()
text = crawler.crawl_forecast()
parser = Parser("hko_daily_forecast", text)
parser.parse_to_today_forecast()
