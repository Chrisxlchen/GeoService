import logging
import traceback

import tornado.web

from geo_service.geocoding_service import GeoService
from restapi.base import BaseHandler

logger = logging.getLogger(__name__)


class RetrieveAddressHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            logger.debug(self.get_arguments("lat"))
            logger.debug(self.get_arguments("lng"))
            lat = float(self.get_arguments("lat")[0])
            lng = float(self.get_arguments("lng")[0])

            if lat < -90 or lat > 90 or lng < -180 or lng > 180:
                raise tornado.web.HTTPError(400, 'Invalid input or gps location, lat (-90, 90), lng (-180, 180)')

            geo_coding = GeoService()
            address = geo_coding.retrieve_address(lat, lng)
            if address:
                self.write(address)
            else:
                raise tornado.web.HTTPError(500, 'The Geo service is not available')
        except:
            logger.error(traceback.format_exc())
            raise tornado.web.HTTPError(400, 'Code bugs, fix me')

