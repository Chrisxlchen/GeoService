import logging
import tornado.ioloop
import tornado.web
from commons.constants import Constants
from commons.log import setup_logging
from restapi.retrieve_address_handler import RetrieveAddressHandler

setup_logging()
logger = logging.getLogger(__name__)


def make_app():
    return tornado.web.Application([
        (r"/api/v1/geocoding/retrieveaddress/(.*)", RetrieveAddressHandler),
    ])


def main():
    app = make_app()
    app.listen(Constants.PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
