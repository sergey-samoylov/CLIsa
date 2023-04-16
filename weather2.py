import requests

def weather():
    url = 'https://wttr.in'

    weather_parameters = {
        '0': '',
        'M': '',
        'format': '4',
        'lang': 'ru',
    }

    response = requests.get(url, params=weather_parameters)

    return response.text
