from sqlalchemy import Column, String, DateTime, Sequence, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from ckan.model.domain_object import DomainObject
from ckan.model.meta import metadata, mapper, Session
from ckan import model

import logging
log = logging.getLogger(__name__)

base = declarative_base()

def _get_datetime():
    return datetime.now()

class Article(base):
    __tablename__ = 'articles'

    id = Column(Integer, Sequence('articles_id_seq'), primary_key=True)
    title = Column(types.UnicodeText, nullable=False, unique=True)
    content = Column(types.UnicodeText, nullable=False)
    author = Column(types.UnicodeText, nullable=False)
    created_date = Column(Date, default = _get_date)
    update_date = Column(Date, onupdate = _get_date)

