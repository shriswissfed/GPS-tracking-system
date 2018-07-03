# -*- coding: utf-8 -*-

import serial

from pynmea import nmea

import string

import webbrowser

 

#####Global Variables######################################

#be sure to declare the variable as 'global var' in the fxn

ser = 0

#####FUNCTIONS#############################################

def scan():

 #scan for available ports. return a list of tuples (num, name)

 available = []

 for i in range(256):

 try:

 s = serial.Serial(i)

 available.append( (i, s.name))

 s.close() # explicit close 'cause of delayed GC in java

 except serial.SerialException:

 pass

 return available

 

#initialize serial connection

def init_serial():

 print "Found Ports:"

 for n,s in scan():

 print "%s" % s

 print " "

 

 COMNUM = 5 #set you COM port # here

 global ser #must be declared in each fxn used

 ser = serial.Serial()

 ser.baudrate = 4800

 ser.port = COMNUM -1#starts at 0, so subtract 1

 

 ser.timeout = 1 #you must specify a timeout (in seconds) so that the serial port doesn't hang

 ser.open() #open the serial port

 ser.isOpen()

 

 # print port open or closed

 if ser.isOpen():

 print 'Open: ' + ser.portstr

 

def to_degrees(lats, longs):

 lat_deg = lats[0:2]

 lat_mins = lats[2:4]

 lat_secs = round(float(lats[5:])*60/10000, 2)

 lat_str = lat_deg + u'°'+ lat_mins + string.printable[68] + str(lat_secs) + string.printable[63]

 

 lon_deg = longs[0:3]

 lon_mins = longs[3:5]

 lon_secs = round(float(longs[6:])*60/10000, 2)

 lon_str = lon_deg + u'°'+ lon_mins + string.printable[68] + str(lon_secs) + string.printable[63]

 

 return [lat_str, lon_str]

 

def open_google_maps(GPS_coordinates):

 gmaps = 'http://www.google.com/maps/place/'

 webbrowser.open(gmaps+GPS_coordinates)

 

def display_time(time):

 hours = time[0:2]

 mins = time[2:4]

 sec = time[4:6]

 print 'UTC Time: ' + hours + ':' + mins + ':' + sec

 

init_serial()

 

#####MAIN LOOP############################################

while 1:

 

 # read what is on serial port

 data = ser.readline() #read4s in bytes followed by a newline

 if data[0:6] == '$GPGGA':

 print data#print to the console

 gpgga = nmea.GPGGA()

 gpgga.parse(data)

 lats = gpgga.latitude

 lat_dir = gpgga.lat_direction

 longs = gpgga.longitude

 long_dir = gpgga.lon_direction

 time = gpgga.timestamp

 alt = gpgga.antenna_altitude

 display_time(time)

 if lats == '':

 print 'GPS coordinates not available'

 else:

 display_time(time)

 print 'Your altitude is ' + alt + 'm'

 lat_lon = to_degrees(lats, longs)

 print lat_lon[0]+lat_dir

 print lat_lon[1]+long_dir

 open_google_maps(lat_lon[0]+lat_dir+lat_lon[1]+long_dir)

 break
