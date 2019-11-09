import logging
from restapi.base import BaseHandler

logger = logging.getLogger(__name__)


class GpsCoordHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.debug('get request')
        self.write('success')
