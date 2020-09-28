from urllib import request
import requests
import json

URL = 'https://api.thingspeak.com/channels/1161029/feeds.json?api_key=LWLR0NMR9Y5NZTIY&results=2'
print(URL)
get_data = requests.get(URL).json()
print(get_data)
channelid = get_data['channel']['id']
print( channelid)
data = get_data['feeds']
print( data)