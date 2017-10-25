import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import urllib2
import json

# SQL Alchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Date, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

db = create_engine('postgresql://ckan_healthcare:Dbnis32581234@localhost/ckan_healthcare')

base = declarative_base()

def _get_date():
    return datetime.now()

class Article(base):
    __tablename__ = 'articles'
    id = Column(Integer, Sequence('articles_id_seq'), primary_key=True)
    title = Column(String)
    content = Column(String)
    author = Column(String)
    created_date = Column(Date, default = _get_date)
    update_date = Column(Date, onupdate = _get_date)

Session = sessionmaker(db)
session = Session()

def get_all_articles():
    articles = session.query(Article) 
    session.close()
    return articles

def most_popular_groups():
    groups = toolkit.get_action('group_list')(data_dict={'sort':'package_count desc', 'all_fields': True})
    groups = groups[:10]
    print(groups)
    return groups

def get_organization_count():
    #organizations = toolkit.get_action('group_list')
    #return len(organizations)
    return format(46346,'0,d')

def get_dataset_count():
    request = urllib2.Request('http://localhost/api/3/action/package_search?rows=25&start=0')
    request.add_header('Authorization', '7abc032e-dee4-46a9-88d0-616d4a3dfb8b')
    response = urllib2.urlopen(request)
    response_dict = json.loads(response.read())
    return format(response_dict['result']['count'],'0,d')
    #return format(44806, '0,d')

def get_agency_dataset_count():
    return format(2460,'0,d')

class ThemePlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer),
    plugins.implements(plugins.IRoutes, inherit=True),
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'theme')
    
    def before_map(self, m):
        # Sitemap Page Routing
        m.connect('sitemap', 
		'/sitemap',
		controller='ckanext.theme.controller:PageController',
		action='sitemap')
        m.connect('usingInformation',
                '/usage',
                controller='ckanext.theme.controller:PageController',
                action='usingInformation')
	return m

    def get_helpers(self):
        return {'theme_most_popular_groups': most_popular_groups,
                'theme_get_all_articles'   : get_all_articles,
                'theme_organization_count' : get_organization_count,
		'theme_dataset_count' : get_dataset_count,
                'theme_agency_dataset_count': get_agency_dataset_count}
