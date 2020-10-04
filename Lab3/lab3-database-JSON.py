
from urllib.request import *
from urllib.parse import *
import json
import sqlite3


apiKey = "6bf648b968eb7105fc80b971eab54c4a" 

city = input("Enter the name of a city whose weather you want: ")

params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')

webData.close()
print (results)

data = json.loads(results)


current = data["main"]
degreeSym = chr(176)

print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
print ("Humidity: %d%%" % current["humidity"])
print ("Pressure: %d" % current["pressure"] )

current = data["wind"]
print ("Wind : %d" % current["speed"])

windspeed = current["speed"]

print("TSET",windspeed)


dbconnect = sqlite3.connect("mydatabase.db");

cursor = dbconnect.cursor();

#cursor.execute('''CREATE TABLE meteomatics (city TEXT, WindSpeed NUMERIC)''');
dbconnect.commit();

cursor.execute('SELECT * FROM meteomatics');
cursor.execute('INSERT INTO meteomatics values("'+ str(city) +'",'+ str(windspeed) + ');');

cursor.execute('SELECT * FROM meteomatics');
for row in cursor:
    #print(row['city'],row['WindSpeed'] );
    print(row)
dbconnect.close();
