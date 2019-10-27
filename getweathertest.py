# a test script
# input your values for api_key, lat, lon, and wunits (si = Celcius)
#
import GetWeather as GetWeather


api_key = '<your api key>'
lat = '43.0575'
lon = '-81.0212'
wunits = 'si'

# create WeatherObject
Weather = GetWeather.GetWeather(api_key, lat, lon, wunits)

# get all forecast info

CurrentConditions = Weather.CurrentConditions()
DailyForecast = Weather.DailyForecast()
HourlyForecast = Weather.HourlyForecast()
MinutelyForecast = Weather.MinutelyForecast()

# print for fun and profit!
print(CurrentConditions)
print(HourlyForecast)
print(DailyForecast)
print(MinutelyForecast)
