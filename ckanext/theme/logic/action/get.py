# coding: utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

import sqlalchemy

import ckan.plugins.toolkit as toolkit
import ckan.lib.dictization.model_dictize as model_dictize
from ckan.logic import NotAuthorized

import logging
log = logging.getLogger(__name__)

from sqlalchemy import Column, String, DateTime, Sequence, Integer, types
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from ckan.model.domain_object import DomainObject
from ckan.model.meta import metadata, mapper, Session
from ckan import model

import logging
log = logging.getLogger(__name__)

import json
import uuid

base = declarative_base()

def _get_datetime():
    return datetime.now()

def make_uuid():
    return unicode(uuid.uuid4())

class Article(base):
    __tablename__ = 'articles'

    id = Column(types.UnicodeText, primary_key=True, default=make_uuid)
    title = Column(types.UnicodeText, nullable=False, unique=True)
    content = Column(types.UnicodeText, nullable=False)
    author = Column(types.UnicodeText, nullable=False)
    created_date = Column(DateTime, default = _get_datetime)
    update_date = Column(DateTime, onupdate = _get_datetime)


@toolkit.side_effect_free
def get_all_articles(context, data_dict):
    toolkit.check_access('ckanext_theme_list', context, data_dict)
    model = context['model']
    articles = model.Session.query(Article).all()
    article_list = []
    for article in articles:
        print(str(article.id) + " =============  " + article.title)
       #article_list.append(model_dictize(article, context))
    
    return articles

def get_article_by_id(context, data_dict):
    model = context['model']
    print(data_dict['id'])
    article = model.Session.query(Article).filter(Article.id == data_dict['id']).one()

    print(article.title) 
    return article 
    
