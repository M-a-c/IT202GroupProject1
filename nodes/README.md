Temperature Sensor and Fusion Table Interface
=============================================

Author: Mackenzie Carter & Chase Lee

Additional resources by:
 * Adafruit
 * Python


Requirements / Dependencies
---------------------------

 * Python 2.7
 * Adafruit_Python_DHT (https://github.com/adafruit/Adafruit_Python_DHT.git)
 * Python-dev
 * Python-openssl
 * Google API Python Client (https://pypi.python.org/pypi/google-api-python-client/)


Installation
------------

 - Install Python 2.7 from your preferred distribution package manager.
 - Install Pip or easy_install for easy Python package management.
 - Install python_dev & python_openssl via your distribution's package manager or pip/easy_install.
 - Clone Adafruit_Python_DHT library
 - Change directory into the Adafruit_Python_DHT library and run the following: `sudo python setup.py install`


Running
-------

`sudo python2 server.py --noauth_local_webserver`


Setting Up a repeating job
--------------------------

On Archlinux, you can use Systemd/Timers:


