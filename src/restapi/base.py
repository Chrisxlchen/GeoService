import logging
from typing import Optional, Awaitable
import tornado.web
import tornado.escape

logger = logging.getLogger(__name__)


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Authorization, X-File-Size, X-File-Name")
        self.set_header('Access-Control-Allow-Methods', 'POST, PUT, GET, OPTIONS, DELETE')

    def options(self, *args, **kwargs):
        # no body
        self.set_status(204)
        self.finish()

