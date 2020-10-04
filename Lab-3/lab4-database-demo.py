


#!/usr/bin/env python3

	
import sqlite3
	
#connect to database file

dbconnect = sqlite3.connect("mydatabase.db");

#If we want to access columns by name we need to set

#row_factory to sqlite3.Row class

dbconnect.row_factory = sqlite3.Row;

#now we create a cursor to work with db

cursor = dbconnect.cursor();

#execute simple select statement

cursor.execute('SELECT * FROM sensors WHERE zone = "kitchen"');

#print data

for row in cursor:

    print(" sensors in kitchen "+ row['type']);

#execute simple select statement  

cursor.execute('SELECT * FROM sensors WHERE type = "door"');

#print data

for row in cursor:

    print(" door sensors: ",row['sensorID'],row['zone']);

#close the connection

dbconnect.close();


