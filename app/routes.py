from tornado.web import Application
from tornado_sqlalchemy import SQLAlchemy
from .config.meta import db_url
from .handlers.people import PeopleGetHandler,PeoplePostHandler, PeopleUpdHandler, PeopleDelHandler


def route():
    routes = [
        (r"/people", PeopleGetHandler),
        (r"/people/add", PeoplePostHandler),
        (r"/people/update/(?P<id>\w+)", PeopleUpdHandler),
        (r"/people/delete/(?P<id>\w+)", PeopleDelHandler)
    ]

    return Application(routes, db=SQLAlchemy(db_url), debug=True)
