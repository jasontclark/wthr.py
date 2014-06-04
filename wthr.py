#!/usr/bin/python2
"""
wthr.py -- Weather Underground command-line client, written in python
"""

import urllib2, json 				#fetching weather
import os, sys, getopt, subprocess	#reading parameters

USR_HOME_DIR = os.path.expanduser("~")
CONFIG_PATH = "%s/.wthrrc" % USR_HOME_DIR
CONFIG_INFO = json.loads(open(CONFIG_PATH,'r').read())

global JSON; JSON=None
global SHORT; SHORT=False
global UNITS; UNITS=None;

def fetch_data(dataType):
	global JSON, UNITS
	UNITS=(CONFIG_INFO['units'])	#metric/imperial
	if JSON == None:
		# load info from config file
		KEY = (CONFIG_INFO['key'])	#personal API key
		LOC = (CONFIG_INFO['zip'])	#zip code
		# feed KEY, LOC, and dataType (requested API data) into JSON URL
		JSON = json.loads(urllib2.urlopen("http://api.wunderground.com/api/%s/%s/q/%s.json" % (KEY, dataType, LOC)).read())
		# verbose
		# print "http://api.wunderground.com/api/%s/%s/q/%s.json" % (KEY, dataType, LOC)

def sky():
	fetch_data("conditions")
	W = (JSON['current_observation']['weather'])
	if SHORT != True:
		print "Sky Conditions: "+W
	else: print W

def temp_actual():
	fetch_data("conditions")
	if SHORT != True:
		print "Temperature: "+JSON['current_observation']['temperature_string']
	else:
		if UNITS=="imperial":
			print JSON['current_observation']['temp_f']
		elif UNITS=="metric":
			print JSON['current_observation']['temp_c']
		else: print "invalid units string in config file"

def temp_feels_like():
	fetch_data("conditions")
	UNITS = (CONFIG_INFO['units'])	#imperial/metric
	if SHORT != True:
		print "Feels like: "+JSON['current_observation']['feelslike_string']
	else:
		if UNITS=="imperial":
			print JSON['current_observation']['feelslike_f']
		elif UNITS=="metric":
			print JSON['current_observation']['feelslike_c']
		else: print "invalid units string in config file"

def location():
	fetch_data("conditions")
	STATE = (JSON['current_observation']['display_location']['state'])
	CITY = (JSON['current_observation']['display_location']['city'])
	ZIP = (JSON['current_observation']['display_location']['zip'])
	print CITY+STATE+ZIP
	if SHORT != True:
		print "Specified Location: "+CITY+", "+STATE+" "+ZIP
	else: print CITY

#def forecast():

#def help():

def main(argv):
	global SHORT

	try:
		opts, args = getopt.getopt(argv,"s",["help","sky","temperature","feels-like","location"])
	except getopt.GetoptError:
		print "command usage error; review README file"
	
	if not argv:
		print "wthr.py"
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-s":
			SHORT=True
		elif opt == "-h":
			#help()
			print "wthr.py" 
			sys.exit(0)
		elif opt == "--help":
			#help()
			print "wthr.py"
			sys.exit(0)
		elif opt == "--sky":
			sky()
		elif opt == "--temperature":
			temp_actual()
		elif opt == "--feels-like":
			temp_feels_like()
		elif opt == "--location":
			location()

if __name__ == "__main__":
	main(sys.argv[1:])