import logging

from flask import Flask
from commons.constants import Constants
from commons.log import setup_logging
from restapi.retrieve_address_handler import RetrieveAddressHandler

setup_logging()
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load default config
app.config.update(dict(
    DEBUG=False,
))


@app.route(Constants.API_VERSION + 'geocoding/retrieveaddress/<lat>/<lng>', methods=['GET'])
def retrieve_address(lat, lng):
    handler = RetrieveAddressHandler()
    return handler.get(float(lat), float(lng))


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000, threaded=True)