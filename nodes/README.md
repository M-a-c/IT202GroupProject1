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

 1. Install Python 2.7 from your preferred distribution package manager.
 2. Install Pip or easy_install for easy Python package management.
 3. Install python_dev & python_openssl via your distribution's package manager or pip/easy_install.
 4. Clone Adafruit_Python_DHT library (See github link in requirement section above)
 5. Change directory into the Adafruit_Python_DHT library and run the following: `sudo python setup.py install`
    Make sure you follow any prompts that the install may give you.
 6. In the /nodes directory, download the clients secret json file from the Google Developer Console.
 7. Copy .env_example to .env and change the values in that configuration file.


Running
-------

`sudo python2 server.py --noauth_local_webserver`

On the first run, the Google API will prompt you to verify the use of the Google Fusions Table API via OAuth2 protocols.
You will need to copy the URL that it outputs and login with your credentials that have write access to the Google Fusion Table ID referenced in the .env file.


Setting Up a repeating job
--------------------------

On Archlinux, you can use Systemd/Timers:


 1. Copy ambientReport.timer and ambientReport.service into /usr/lib/systemd/system/. (This will install a service to run the server every minute)
 2. Adjust and verify the paths referenced in ambientReport.service.
 
