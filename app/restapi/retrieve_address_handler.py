import logging
import traceback
from geo_service.geocoding_service import GeoService

logger = logging.getLogger(__name__)


class RetrieveAddressHandler:
    def __init__(self):
        pass

    def get(self, lat, lng):
        try:
            logger.info('Receive lat {}, lng {}'.format(lat, lng))

            if lat < -90 or lat > 90 or lng < -180 or lng > 180:
                return 'Invalid input or gps location, lat (-90, 90), lng (-180, 180)', 400

            geo_coding = GeoService()
            address = geo_coding.retrieve_address(lat, lng)
            if address:
                return address
            else:
                return 'The Geo service is not available', 500
        except:
            logger.error(traceback.format_exc())
            return 'Internal Error', 400

