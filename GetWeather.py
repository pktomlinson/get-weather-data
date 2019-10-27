# python class for obtaining weather data from darksky.net
# requires darksky.net account and developer API key

# import require libraries / modules
import urllib3
import json
import datetime


class GetWeather:
    """
        GetWeather: A class that takes 4 inputs to consolidate a weather forecast from darksky.net
        It generates and returns a JSON object

        Requires:
        1) api_key, which can be obtained at https://darksky.net
        2) lat, your decimal coordinate for latitude, such as 43.01234
        3) lon, your decimal coordinate for longitude, such as -81.0123
        4) wunits, ypecification for units. See https:/darksky.net for acceptable values (default is si, or celcius)

    """
    
    def __init__(self, api_key, lat, lon ,wunits):
        # create connection to api
        self.http = urllib3.PoolManager()
        # create get request and return data to self.weather_data
        self.weather_data = self.http.request('GET', 'https://api.darksky.net/forecast/' + api_key + '/' + lat + ', ' + lon + '/?units=' + wunits)
        # convert returned data to JSON string (UTF-8 encoded)
        self.weather_dict = json.loads(self.weather_data.data.decode('UTF-8'))

    def CurrentConditions(self):
        self.current = self.weather_dict['currently']
        self.currentTime = self.current['time']
        self.theTime = datetime.datetime.fromtimestamp(self.currentTime).strftime('%Y-%m-%d %H:%M:%S')
        return(self.current)

    def HourlyForecast(self):
        self.hourly = self.weather_dict['hourly']
        self.hourly_data = self.hourly['data']
        return(self.hourly_data)

    def MinutelyForecast(self):
        self.minutely = self.weather_dict['minutely']
        self.minutely_data = self.minutely['data']
        return(self.minutely_data)
    
    def DailyForecast(self):
        self.daily = self.weather_dict['daily']
        self.daily_data = self.daily['data']
        return(self.daily_data)
    




    

    
