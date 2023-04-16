import requests

def weather():
    url = 'http://wttr.in/Королёв?format=4'
    response = requests.get(url)
    return response.text
