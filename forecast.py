import requests
import json
import pprint

class WeatherForcast:
    def __init__(self, cityCodeMap):
        self.cityCodeMap = cityCodeMap
        
    def getTheData(self, place, forcast):
        cityCode = self.cityCodeMap[place]
        url = "https://weather.com/en-IN/weather/" + forcast + "/l/" + cityCode
        output = requests.get(url)
        pprint.pprint(out.text)
        
if __name__ == '__main__':
    cityCodeMap = {
        
        "hyd": "d7f5a4af529e40b0a82d339e5467e89458e5ad5e2cf0ffdd05c853ed3e98fd38",
        "mumbai": "03343c09f067e51a168a3b28e5a26f73d9592bf6e527ea139c4651e7c33d5429",
        "delhi": "7eece8ea75e09132257779f0aabd74ccf33ee6b6556bdd9ddc9753220cbe9845",
        "bangalore": "072e7110ccda5a2b786e1b942f4946d382bdd6ff315f63682bfc14827786c271"
    }
    obj = WeatherForcast(cityCodeMap)
    place = input("Enter the place: ")
    forcast = "today"
    obj.getTheData(place, forcast)
