import os


class Constants:
    PORT = 12632
    HOST = '127.0.0.1'
    API_VERSION = '/api/v1/'
    # The follow path should be hardcoded to the application installation dir when deploy in production
    LOG_SETTINGS = "configuration/logging.yaml"
    SERVER_CONFIGS = "configuration/secret.yaml"

