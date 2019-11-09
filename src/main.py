import logging
import tornado.ioloop
import tornado.web
from commons.constants import Constants
from commons.log import setup_logging
from restapi.gps_coord_handler import GpsCoordHandler

setup_logging()
logger = logging.getLogger(__name__)


def make_app():
    return tornado.web.Application([
        (r"/api/v1/gps_coord", GpsCoordHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(Constants.PORT)
    tornado.ioloop.IOLoop.current().start()
