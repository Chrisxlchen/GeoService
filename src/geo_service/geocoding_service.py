import logging

from geo_service.google_geocoding import GoogleGeocoding
from geo_service.here_geocoding import HereGeocoding
logger = logging.getLogger(__name__)


class GeoService:
    def __init__(self):
        # Add Geocoding service to the list if there is more.
        self.geocoding_services = [GoogleGeocoding, HereGeocoding]

    def retrieve_address(self, lat: float, lng: float) -> dict:
        """
            Return Address format
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
        for service in self.geocoding_services:
            service_obj = service()
            address = service_obj.retrieve_address(lat, lng)
            logger.debug(address)
            if address is not None:
                return address

        return {}
