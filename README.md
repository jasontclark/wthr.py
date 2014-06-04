wthr.py
=======

Version 0.0.3

_wthr.py_ is a command-line application that pulls weather data from [Weather Underground](http://www.wunderground.com).  _wthr.py_ was intended to be used for piping weather information directly into other applications, specifically system-monitoring programs (ex. conky).

Description
-----------
_wthr.py_ requires an API key from Weather Underground: [http://www.wunderground.com/weather/api](http://www.wunderground.com/weather/api). The functionality of _wthr.py_ does not require a paid API key, however each call of the script that _does not_ include the `-h` switch _will use one call_ to the API. 

The API key should be added to `$HOME/.wthrrc`, along with the desired zip code and units type for the weather data:

	{
		"key": "YOUR_API_KEY",
		"zip": "20004",
		"units": "imperial"
	}
_The above template in `/wthrrc` can be used to create the .wthrrc config file._

_wthr.py_ has complete functionality of the following options:

* `--sky` gives the current sky condition

* `--temperature` gives the current temperature

* `--feels-like` gives the current perceivable temperature

* `--location` reports the configured location, based on the .wthrrc

The previous report-based options can be accompanied by `-s`, which trims the output of the reports to the raw API data from Weather Underground. The `-s` functionality is extremely useful for programs that process weather info.

_wthr.py_ also includes the `-h` and `--help` switches that provide information about the script. By default, running simply `wthr.py` will show print the program name.

Installation
------------
_wthr.py_ can be run as-is from the command line, however it is recommended to place it in a location specified in `$PATH`, so it can be easily run by other programs.

To obtain the source for _wthr.py_ run:

	git clone git://github.com/travis-g/wthr.py.git

Remember to edit, move and rename the `/wthrrc` file, adding your API key and changing the zip code/units type as desired.

If `$HOME/bin/` is included in $PATH (check by running `echo $PATH|grep "$HOME/bin:"`) it is suggested to move _wthr.py_ there for convenience.

To-do
-----
- optimize the optargs processing
- add more data pulling functionality
- complete coding

License(s)
----------
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).

Data courtesy of Weather Underground, Inc. (WUI) is subject to the [Weather Underground API Terms and Conditions of Use](http://www.wunderground.com/weather/api/d/terms.html).  The author of this software is not affiliated with WUI, and the software is neither sponsored nor endorsed by WUI.
