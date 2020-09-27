import http.client
import urllib.parse
import urllib.request
import requests
import threading
import json
import random


def read_data_thingspeak():
    URL ='https://api.thingspeak.com/channels/1158628/feeds.json?api_key='
    KEY = 'S294JENKHE5EDKIF'
    HEADER ='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)

    get_data = requests.get(NEW_URL).json() 
    #print(get_data)
    #channel_id=get_data['channel']['id']

    feild_1 = get_data['feeds']
    #print(feild_1)

    t=[]
    for x in feild_1:
        #print(x['feild1'])
        t.append(x['field1'])
    print(t)

if __name__=='__main__':
    #thingspeak_post()
    read_data_thingspeak()
