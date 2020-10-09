
import urllib.request
import requests
import threading
import json

def thingspeak_post():
    valField1='L1-f-3'
    valField2='c'
    valField3='MoonisMohammad@cmail.carleton.ca'
    URl='https://api.thingspeak.com/update?api_key='
    KEY='7481QW0APO2BO2BU'
    HEADER='&field1={}&field2={}&field3={}'.format(valField1,valField2,valField3)
    NEW_URL=URl+KEY+HEADER

    print(NEW_URL)

    data=urllib.request.urlopen(NEW_URL)
    print(data)


thingspeak_post()