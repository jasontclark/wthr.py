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

def fetch_data():
	global JSON
	if JSON == None:
		KEY = (CONFIG_INFO['key'])	#personal API key
		LOC = (CONFIG_INFO['zip'])	#zip code
		JSON = json.loads(urllib2.urlopen("http://api.wunderground.com/api/%s/conditions/forecast/q/%s.json" % (KEY, LOC)).read())

def sky():
	W = (JSON['current_observation']['weather'])
	if SHORT != True:
		print "Sky Conditions: "+W
	else: print W

def temp_actual():
	if SHORT != True:
		return "Temperature: "+JSON['current_observation']['temperature_string']
	else:
		return JSON['current_observation']['temp_f']

# def temp_feels_like():
# 	UNITS = (CONFIG_INFO['units'])	#imperial/metric
# 	if SHORT != True:
# 		return "Feels like: "+JSON['current_observation']['feelslike_string']
# 	else:
# 		if UNITS=="imperial":
# 			return JSON['current_observation']['feelslike_f']
# 		elif UNITS=="metric":
# 			return JSON['current_observation']['feelslike_c']
# 		else: return "invalid units value in config file"

def location():
	STATE = (JSON['current_observation']['display_location']['state'])
	CITY = (JSON['current_observation']['display_location']['city'])
	ZIP = (JSON['current_observation']['display_location']['zip'])
	if SHORT != True:
		return "Specified Location: "+CITY+", "+STATE+" "+ZIP
	else: return CITY

#def forecast():

#def help():

def main(argv):
	global SHORT

	try:
		opts, args = getopt.getopt(argv,"s",["help","sky","temperature","location"])
	except getopt.GetoptError:
		print "command usage error; review README file"
	
	if not argv:
		fetch_data()
		sky()
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-s":
			SHORT=True
		elif opt == "--help":
			#help()
			print "wthr.py" 
			sys.exit(0)
		elif opt == "--sky":
			fetch_data()
			sky()
		elif opt == "--temperature":
			fetch_data()
			temp_actual()
		elif opt == "--location":
			fetch_data()
			location()

if __name__ == "__main__":
	main(sys.argv[1:])