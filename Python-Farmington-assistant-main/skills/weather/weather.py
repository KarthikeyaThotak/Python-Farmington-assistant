import requests as request
import xml.etree.ElementTree as ET
import jxmlease

# For alerts get the headline in XML data

class weatherapi:
    def __init__(self,zip_code, day):
        self.day = day
        self.zip_code = zip_code
        self.api = "64a9a52aa44441a4946200751212508"
        self.base_url = "http://api.weatherapi.com/v1"
        self.Current_weather = "/forecast.xml?key="
        self.response = request.get(self.base_url+self.Current_weather+self.api+"&q="+str(self.zip_code)+"&days="+str(self.day)+"aqi=no&alerts=no")
        self.response_xml_as_string = self.response.content.decode()
        self.root = jxmlease.parse(self.response_xml_as_string)

    def current_weather(self):
        text = self.root['root']['current']['temp_f'].get_cdata()
        text_2 = self.root['root']['current']['feelslike_f'].get_cdata()

        mini = self.root['root']['forecast']['forecastday']['day']['mintemp_f']
        maxi = self.root['root']['forecast']['forecastday']['day']['maxtemp_f']
        result_min_and_max = " and also currently peak temperature is "+str(maxi)+" fahrenheit also the minimum is around "+str(mini)+ " fahrenheit"
        result = "the current temperature is "+str(text)+" fahrenheit"+" but it feels like "+str(text_2) + " fahrenheit. "+result_min_and_max
        return result

    def conditions(self):
        text = self.root['root']['current']['condition']['text'].get_cdata()
        text = "currently we have "+str(text)
        return text
    def wind_mile(self):
        text = self.root['root']['current']['wind_mph'].get_cdata()
        text = "the Wind speed is "+str(text)+" miles"
        return text

    def wind_direction(self):
        text = self.root['root']['current']['wind_dir'].get_cdata()
        result = ''
        if text == 'S':
            result = "The direction of the wind is south"
        elif text == 'SW':
            result = "The direction of wind is south west"
        elif text == 'W':
            result = "The direction of wind is west"
        elif text == 'NW':
            result = "The direction of wind is north west"
        elif text  == 'NE':
            result = "The direction of wind is north east"
        elif text  == 'N':
            result = "The direction of wind is north"
        elif text  == 'E':
            result = "The direction of wind is East"
        elif text  == 'SE':
            result = "The direction of wind is south east"

        return result

    def rain(self):
        text = self.root['root']['forecast']['forecastday']['day']['condition']['text'].get_cdata()
        rain = self.root['root']['forecast']['forecastday']['day']['totalprecip_in'].get_cdata()
        text = "currently it will be "+str(text)+" and the total percipitation is "+str(rain)+" percent"
        return text

    def snow(self):
        text = self.root['root']['forecast']['forecastday']['day']['daily_will_it_snow'].get_cdata()
        text = "currently we have "+str(text)+" percent of snow"
        return text

    def sunraise(self):
        sunraise = self.root['root']['forecast']['forecastday']['astro']['sunrise'].get_cdata()
        sunset = self.root['root']['forecast']['forecastday']['astro']['sunset'].get_cdata()
        text = "currently the sunraise is at "+str(sunraise)+" and sunset is at "+str(sunset)
        return text




weatherapi = weatherapi(48336, 1)
