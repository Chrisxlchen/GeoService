import json
import logging
import traceback

import requests

from commons.config import Config
from geo_service.geocoding_base import GeocodingBase

logger = logging.getLogger(__name__)


class GoogleGeocoding(GeocodingBase):
    def __init__(self):
        super().__init__()
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.key = Config.get_gogole_key()

    def retrieve_address(self, lat: float, lng: float) -> dict:
        address = None
        try:
            api = '{}?latlng={},{}&key={}'.format(self.url, lat, lng, self.key)
            logger.debug('Sending request to {}'.format(api))
            res = json.loads(requests.get(api).text)
            address = self.get_address_from_response(res)
        except:
            logger.error(traceback.format_exc())

        return address

    def get_address_from_response(self, ret: dict) -> dict:
        """Translate google format to following format
            {
                "Label": "425 W Randolph St, Chicago, IL 60606, USA",
                "HouseNumber": "425",
                "Street": "W Randolph St",
                "District": "West Loop",
                "City": "Chicago",
                "County": "Cook County",
                "State": "IL",
                "Country": "US",
                "PostalCode": "60606"
            }
        """
        address = {}
        result = ret.get('results')
        if result:
            address['Label'] = result[0].get('formatted_address')
            address_components = result[0].get('address_components')
            if address_components:
                for comp in address_components:
                    types = comp.get('types')
                    if types[0] == 'street_number':
                        address['HouseNumber'] = comp.get('short_name')
                    elif types[0] == 'route':
                        address['Street'] = comp.get('short_name')
                    elif types[0] == 'neighborhood':
                        address['District'] = comp.get('short_name')
                    elif types[0] == 'locality':
                        address['City'] = comp.get('short_name')
                    elif types[0] == 'administrative_area_level_2':
                        address['County'] = comp.get('short_name')
                    elif types[0] == 'administrative_area_level_1':
                        address['State'] = comp.get('short_name')
                    elif types[0] == 'country':
                        address['Country'] = comp.get('short_name')
                    elif types[0] == 'postal_code':
                        address['PostalCode'] = comp.get('short_name')

        return address

