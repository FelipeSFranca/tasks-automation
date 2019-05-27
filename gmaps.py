# -*- coding: utf-8 -*-
import requests

__doc__ = """
Simplest way to get the lat, long of any address.
Using Python requests and the Google Maps Geocoding API.

params = {
    'address': 'oshiwara industerial center goregaon west mumbai',
    'sensor': 'false',
    'region': 'india'
}
"""

API_KEY = 'AIzaSyC9laIvz69kPc1QZlUQmbIl4hglZOA7O7w'
GOOGLE_MAPS_API_URL = f'https://maps.googleapis.com/maps/api/geocode/json?key={API_KEY}'


class GoogleException(Exception):
    pass


def get_address(params):
    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    if res.get('error_message'):
        raise GoogleException(res.get('error_message'))

    if not len(res['results']):
        return

    # Use the first result
    result = res['results'][0]

    geodata = dict()
    geodata['latitude'] = result['geometry']['location']['lat']
    geodata['longitude'] = result['geometry']['location']['lng']
    geodata['address'] = result['formatted_address']

    return geodata
