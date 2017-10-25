import ckan.plugins as plugins
import ckan.lib.base as base
import ckan.model as model
import ckan.lib.helpers as helper
from ckan.plugins import toolkit
#import ckanext.theme.model


import logging
log = logging.getLogger(__name__)

class PageController(base.BaseController):

    def sitemap(self):
	return plugins.toolkit.render('sitemap.html')
    def usingInformation(self):
	return plugins.toolkit.render('using-information.html')
 

    def get_all_articles(self):
        context = {'model': model, 'session': model.Session,
                   'user': toolkit.c.user or toolkit.c.author, 'for_view': True,
                   'auth_user_obj': toolkit.c.userobj}
        data_dict = {}  

        articles = toolkit.get_action('ckanext_theme_get_all_articles')(context, data_dict)
  
	for article in articles:
            log.debug(article.title)

        return articles

    def get_article_by_id(self, id):
        context = {'model': model, 'session': model.Session,
                   'user': toolkit.c.user or toolkit.c.author, 'for_view': True,
                   'auth_user_obj': toolkit.c.userobj}
        data_dict = {'id': id}

	print(id)
        try:
            article = toolkit.get_action('ckanext_theme_get_article_by_id')(context, data_dict)
        except NotFound:
            abort(404, 'Article Not Found')
        except NotAuthorized:
            abort(401, 'Unauthorized to read article')

        return toolkit.render('article/show.html', extra_vars={'article': article})

