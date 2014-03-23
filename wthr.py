#!/usr/bin/python2
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

def weather():
	W = (JSON['current_observation']['weather'])
	if SHORT != True:
		print "Sky Conditions: "+W
	else: print W

def temp_actual():
	UNITS = (CONFIG_INFO['units'])	#imperial/metric
	if SHORT != True:
		return "Temperature: "+JSON['current_observation']['temperature_string']
	else:
		if UNITS=="imperial":
			return JSON['current_observation']['temp_f']
		elif UNITS=="metric":
			return JSON['current_observation']['temp_c']
		else: return "invalid units value in config file"

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

def heat_index():
	UNITS = (CONFIG_INFO['units'])	#imperial/metric
	if SHORT != True:
		return "Heat Index: "+JSON['current_observation']['heat_index_string']
	else:
		if UNITS=="imperial":
			return JSON['current_observation']['heat_index_f']
		elif UNITS=="metric":
			return JSON['current_observation']['heat_index_c']
		else: return "invalid units value in config file"	

def location():
	STATE = (JSON['current_observation']['display_location']['state'])
	CITY = (JSON['current_observation']['display_location']['city'])
	ZIP = (JSON['current_observation']['display_location']['zip'])
	if SHORT != True:
		return "Specified Location: "+CITY+", "+STATE+" "+ZIP
	else: return CITY

def detailed():
	print "Current conditions at "+JSON['current_observation']['observation_location']['full']
	print JSON['current_observation']['observation_time']
	print "   %s" % temp_actual()
	if JSON['current_observation']['heat_index_string']!="NA":
		print "   %s" % heat_index()
	print "   %s" % weather()


#def help():

def main(argv):
	global SHORT

	try:
		opts, args = getopt.getopt(argv,"shwtld",["SHORT","help","weather","temperature","location","all"])
	except getopt.GetoptError:
		print "command usage error; review README file"
	
	if not argv:
		fetch_data()
		weather()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-s","--short"):
			SHORT=True
		elif opt in ("-h", "--help"):
			#help()
			print "wthr.py" 
			sys.exit(0)
		elif opt in ("-w", "--weather"):
			fetch_data()
			weather()
		elif opt in ("-t", "--temperature"):
			fetch_data()
			temp_actual()
		elif opt in ("-l", "--location"):
			fetch_data()
			location()
		elif opt in ("-d", "--detailed"):
			fetch_data()
			detailed()

if __name__ == "__main__":
	main(sys.argv[1:])