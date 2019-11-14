import os
import logging.config
import traceback

import yaml
from commons.constants import Constants


def setup_logging(default_level=logging.INFO):
    """
        Setup logging configuration
    """
    try:
        path = Constants.LOG_SETTINGS
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
    except:
        logging.error(traceback.format_exc())
