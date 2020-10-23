from sqlalchemy import Column, BigInteger, String
from sqlalchemy.schema import Sequence
from ..config.meta import Base


class People(Base):
    __tablename__ = 'people'

    id = Column(BigInteger, Sequence('people_id_seq', increment=1), primary_key=True)
    name = Column(String(255))
