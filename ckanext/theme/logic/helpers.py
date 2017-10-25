import ckan.lib.helpers as h
from ckan.plugins import toolkit

def get_top_articles():

    articles = toolkit.get_action('ckanext_theme_get_all_articles')({},{})

    return articles
