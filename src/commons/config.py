""""This file updates app.config with info from config.ini."""
import logging
import threading
import traceback
import yaml

from src.commons.constants import Constants

logger = logging.getLogger(__name__)


class Config:
    # Here will be the instance stored.
    __singleton_lock = threading.Lock()
    __instance = None
    __config = None
    __run_time = None

    @classmethod
    def get_instance(cls):
        """ Static access method. """
        if cls.__instance is None:
            with cls.__singleton_lock:
                if not cls.__instance:
                    cls.__instance = Config()
        return cls.__instance

    def __init__(self):
        Config.__config = Config.load_config()

    @classmethod
    def get_config(cls):
        return cls.__config

    @staticmethod
    def load_config():
        """
            Setup logging configuration
        """
        config = None
        path = Constants.SERVER_CONFIGS
        try:
            with open(path, 'r') as f:
                config = yaml.safe_load(f.read())
        except:
            logger.error(traceback.format_exc())

        return config

    @staticmethod
    def get_here_info():
        try:
            ins = Config.get_instance().get_config()
            return ins.get("here_geocoding").get('app_id'), ins.get("here_geocoding").get('app_code')
        except:
            logger.error('can not find the appid for here geo service')
            logger.error(traceback.format_exc())
            return None, None


    @staticmethod
    def get_gogole_key():
        try:
            ins = Config.get_instance().get_config()
            return ins.get("google_geocoding").get('key')
        except:
            logger.error('can not find the key for google geo service')
            logger.error(traceback.format_exc())
            return None