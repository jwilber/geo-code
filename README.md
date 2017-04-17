# geo_code

[![Build Status](https://travis-ci.org/jwilber/geo-code.svg?branch=master)](https://travis-ci.org/jwilber/geo-code)

Lightweight Python package for geocoding addresses using the Google Geocoding API.


For an input string address, `Geocoder` will return the longitude, latitude, postcode, and formatted_address.


{'status': u'OK', 'input_string': '10920 Sunset Trail', 'postcode': u'55441', 'latitude': 44.9850985, 'type': u'street_address', 'formatted_address': u'11100-11298 Sunset Trail, Plymouth, MN 55441, USA', 'longitude': -93.4207907, 'accuracy': u'RANGE_INTERPOLATED'}

***

# Getting Started: Using the Geocoder Class

The core functionality provided by geo_code, geocoding, is provided by the `geocode` method of the `Geocoder` class. 
The **Geocoder** class can be initialized with an API-key (provided at [here](https://console.developers.google.com/apis/)), or without an argument (for free-tier service/rates).

```Python
from geo_code import Geocoder

# init with free tier service
g = Geocoder()

# init with API-key
g = Geocoder('thisIsNotARealAPIKey')
```

To geocode an Address, simply input the address as a string into the `Geocoder.geocode` method.

To geocode an Address, simply input the address as a string into the **Geocoder.geocode** method.

```Python
address = '190 Doe Library, Berkeley CA'
g.geocode(address)

# another example
g.geocode('1600 Pennsylvania Ave NW, Washington, DC 20500')
```