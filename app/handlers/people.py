from tornado_sqlalchemy import SessionMixin
from ..config.meta import BaseHandler
from abc import ABC
import json
from ..models.people import People


class PeopleGetHandler(BaseHandler, SessionMixin, ABC):
    def get(self):
        try:
            with self.make_session() as session:
                people = session.query(People).all()
                data = [{
                    'id': c.id,
                    'name': c.name
                } for c in people]

                self.set_status(200)
                self.write({'Success To Get People list': 200, 'data': data})

        except Exception as e:
            print(e)
            self.set_status(500)
            self.write({'Error To Get People List': 500})


class PeoplePostHandler(BaseHandler, SessionMixin, ABC):
    def post(self):
        try:
            body = (json.loads(self.request.body))
            name = body.get('name')

            with self.make_session() as session:
                people = People()
                people.name = name
                session.add(people)
                session.commit()

                self.set_status(200)
                self.write({'Success To Add New People': 200})

        except Exception as e:
            print(e)
            self.set_status(500)
            self.write({'Error To Add New People': 500})


class PeopleUpdHandler(BaseHandler, SessionMixin, ABC):
    def put(self, **matchdict):
        try:
            body = (json.loads(self.request.body))
            id = matchdict.get('id')
            name = body.get('name')

            with self.make_session() as session:
                people = session.query(People).filter(
                    People.id == int(id)
                ).first()

                people.name = name
                session.add(people)
                session.commit()

                self.set_status(200)
                self.write({'Success To Edit People': 200})

        except Exception as e:
            print(e)
            self.set_status(500)
            self.write({'Error To Edit People': 500})


class PeopleDelHandler(BaseHandler, SessionMixin, ABC):
    def delete(self, **matchdict):
        try:
            id = matchdict.get('id')

            with self.make_session() as session:
                session.query(People).filter(
                    People.id == int(id)
                ).delete(synchronize_session=False)

                session.commit()

                self.set_status(200)
                self.write({'Success To Delete People': 200})

        except Exception as e:
            print(e)
            self.set_status(500)
            self.write({'Error To Delete People': 500})
