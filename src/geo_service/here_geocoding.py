import json
import logging
import requests
from geo_service.geocoding_base import GeocodingBase

logger = logging.getLogger(__name__)


class HereGeocoding(GeocodingBase):
    def __init__(self):
        super().__init__()
        self.url = 'https://reverse.geocoder.api.here.com/6.2/'
        self.app_id = 'zA1C3SxTGHdz7mi7glta'
        self.app_code = '7nHBdtNyW_sDLQU2UNg0PA'
        self.radius = 10

    def retrieve_address(self, lat: float, lng: float) -> dict:
        address = None
        try:
            api = '{}reversegeocode.json?app_id={}&app_code={}&mode=retrieveAddresses&prox={},{},{}'.\
                   format(self.url, self.app_id, self.app_code, lat, lng, self.radius)
            logger.debug(api)
            ret = json.loads(requests.get(api).text)
            logger.debug(ret)
            address = self.get_address_from_response(ret)
        except:
            logger.error('Failed to get address')

        return address

    def get_address_from_response(self, ret: dict) -> dict:
        """Get only the first matched and get rid of AdditionalData
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
        resp = ret.get('Response')
        address = {}
        if resp:
            view = resp.get('View')
            if view:
                view_obj = view[0]
                result = view_obj.get('Result')
                if result:
                    location = result[0].get('Location')
                    logger.debug(location)
                    if location:
                        address = location.get('Address')
                        del address['AdditionalData']

        return address

