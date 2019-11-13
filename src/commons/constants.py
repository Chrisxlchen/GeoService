import os


class Constants:
    parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    PORT = 12632
    HOST = '127.0.0.1'
    API_VERSION = '/api/v1/'
    # The follow path should be hardcoded to the application installation dir when deploy in production
    LOG_SETTINGS = os.path.join(parent_path, "deploy/logging.yaml")
    SERVER_CONFIGS = os.path.join(parent_path, "deploy/secret.yaml")

