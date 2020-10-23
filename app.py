import asyncio

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
import tornado.autoreload

from app.routes import route

define('port', default=4000, help='port to listen on')


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = route()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('========================================')
    print('App listening at: http://localhost:%i/' % options.port)
    tornado.autoreload.start()
    IOLoop.current().start()

# pipenv run python app.py
