#!/usr/bin/env python
"""
wthr.py -- Weather Underground command-line client, written in python
"""

"""
Imports
"""
# for fetching & parsing WU JSONs
import urllib2, json
# for reading parameters
import os, sys, getopt


"""
Global vars
"""
# read user configs
USR_HOME_DIR = os.path.expanduser("~")
CONFIG_PATH = "%s/.wthrrc" % USR_HOME_DIR
CONFIG_INFO = json.loads(open(CONFIG_PATH, 'r').read())

global JSON
global SHORT
global UNITS

# Global vars initialization
JSON = None
SHORT = False
UNITS = None


"""
Function definitions
"""
def fetch_data(req):
    """
    fetch_data(req) -- pull the requested JSON data from WU using the API
    """
    global JSON, UNITS

	# metric/imperial
    UNITS = CONFIG_INFO['units']

    if JSON == None:
		# load info from config file
		key = CONFIG_INFO['key']
		loc = CONFIG_INFO['zip']

		# feed key, loc, and req (requested API data) into JSON URL
		wu_url = 'http://api.wunderground.com/api/%s/%s/q/%s.json' % (key, req, loc)
		
		# assign var JSON to returned JSON file
		JSON = json.loads(urllib2.urlopen(wu_url).read())

def sky():
	"""
	sky() -- prints the current sky conditions
	"""
	fetch_data("conditions")
	sky_cond = JSON['current_observation']['weather']
	if SHORT != True:
		print "Sky Conditions: " + sky_cond
	else:
		print sky_cond

def temp_actual():
	"""
	temp_actual() -- prints the current temperature
	"""
	fetch_data("conditions")

	if SHORT != True:
	    print "Temperature: " + JSON['current_observation']['temperature_string']
	elif UNITS == "imperial":
	    print JSON['current_observation']['temp_f']
	elif UNITS == "metric":
		print JSON['current_observation']['temp_c']
	else:
		print "invalid units string in config file."

def temp_feels_like():
	"""
	temp_feels_like() -- prints the 'feels-like' temperature
	"""
	fetch_data("conditions")
	UNITS = (CONFIG_INFO['units'])	#imperial/metric

	if SHORT != True:
	    print "Feels like: " + JSON['current_observation']['feelslike_string']
	elif UNITS == "imperial":
	    print JSON['current_observation']['feelslike_f']
	elif UNITS == "metric":
		print JSON['current_observation']['feelslike_c']
	else:
		print "invalid units string in config file"

def location():
	"""
	location() -- prints the specified location
	"""
	fetch_data("conditions")
	state = (JSON['current_observation']['display_location']['state'])
	city = (JSON['current_observation']['display_location']['city'])
	zipcode = (JSON['current_observation']['display_location']['zip'])

	if SHORT != True:
		print "Specified Location: " + city + ", " + state + " " + zipcode
	else:
		print city

def forecast():
	"""
	forecast() -- prints current forecast
	"""
	pass

def help():
	"""
	help() -- prints help info
	"""
	pass

def main(argv):
	global SHORT

	try:
		opts, args = getopt.getopt(argv, "s", ["help", "sky", "temperature", "feels-like", "location"])
		except getopt.GetoptError:
			print "command usage error; review README file."

		if not argv:
			print "wthr.py"
			sys.exit(2)
		for opt, arg in opts:
			if opt == "-s":
				SHORT = True
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
