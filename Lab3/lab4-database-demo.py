
import sqlite3

dbconnect = sqlite3.connect("mydatabase.db");




cursor = dbconnect.cursor();

cursor.execute('''CREATE TABLE sensors (sensorID NUMERIC, type TEXT, zone TEXT)''');
dbconnect.commit();

cursor.execute('SELECT * FROM sensors');
cursor.execute('INSERT INTO sensors values(1, "door","kitchen");');
cursor.execute('INSERT INTO sensors values(2, "temperature","kitchen");');
cursor.execute('INSERT INTO sensors values(3, "door","garage");');
cursor.execute('INSERT INTO sensors values(4, "motion","garage");');
cursor.execute('INSERT INTO sensors values(4, "temperature","garage");');

cursor.execute('SELECT * FROM sensors');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );

dbconnect.close();
