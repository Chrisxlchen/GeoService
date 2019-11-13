import logging
import traceback
from re import match

import tornado.web

from geo_service.geocoding_service import GeoService
from restapi.base import BaseHandler

logger = logging.getLogger(__name__)


class RetrieveAddressHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            para = match(r"/api/v1/geocoding/retrieveaddress/(.*)", self.request.uri).groups()[0]
            if not para:
                raise tornado.web.HTTPError(400)

            gps = para.split('/')
            lat = float(gps[0])
            lng = float(gps[1])
            logger.info('Receive lat {}, lng {}'.format(lat, lng))

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

