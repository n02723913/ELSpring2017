#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys
""" Log Current Time, Temperature in Celsius and Fahrenheit
 To an Sqlite3 database """
def readTemp():
	 currentTime=time.strftime('%Y-%m-%d %H:%M')
	 return currentTime
def logTemp():
	 con = mydb.connect('/home/pi/myPi/Tests/testTime.db')
	 with con:
		try:
			 [C,F]=readTemp()
			 print "Current temperature is: %s F" %F
			 cur = con.cursor()
			 #sql = "insert into testTime values(?,?,)"
			 cur.execute('insert into testTime values(?,?)', (C,F))
			 print "Temperature logged"
		except:
			print "Error!!"


#print readTemp()
logTemp()