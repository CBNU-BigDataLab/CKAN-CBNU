import ckan.plugins as plugins
import ckan.lib.base as base
import ckan.model as model
import ckan.lib.helpers as helper
from ckan.plugins import toolkit
#import ckanext.theme.model
from ckan.common import request, c, config


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
        currentPage = request.params.get('page', u'1')
        data_dict = {'page': int(currentPage)}  

        # unicode format (decoded from utf8)
        q = c.q = request.params.get('q', u'')

        c.query_error = False

        page = helper.get_page_number(request.params)

        limit = int(config.get('ckan.datasets_per_page', 20))

        # most search operations should reset the page counter:
        params_nopage = [(k, v) for k, v in request.params.items()
                         if k != 'page']

        articles = toolkit.get_action('ckanext_theme_get_all_articles')(context, data_dict)
        c.page = helper.Page(
                collection=articles,
                page=page,
                url= None,
                item_count= toolkit.get_action('ckanext_theme_get_count_all_articles')(context, data_dict),
                items_per_page=limit
            )
  
	for article in articles:
            log.debug(article.title)
       
        return toolkit.render('article/list.html', extra_vars={'articles': articles, 'total': 50, 'current': int(currentPage), 'index': 1})

    def get_article_by_id(self, id):
        context = {'model': model, 'session': model.Session,
                   'user': toolkit.c.user or toolkit.c.author, 'for_view': True,
                   'auth_user_obj': toolkit.c.userobj}
        data_dict = {'id': id}

	print(id)
        try:
            article = toolkit.get_action('ckanext_theme_get_article_by_id')(context, data_dict)
        except toolkit.ObjectNotFound:
            abort(404, 'Article Not Found')
        except toolkit.NotAuthorized:
            abort(401, 'Unauthorized to read article')

        return toolkit.render('article/show.html', extra_vars={'article': article})
    def new(self):
	return plugins.toolkit.render('article/new.html')

    def save_new(self):
        if request.method == 'POST':
            context = {'model': model, 'session': model.Session,
                   'user': toolkit.c.user or toolkit.c.author, 'for_view': True,
                   'auth_user_obj': toolkit.c.userobj}
            new_title = request.POST.get('title')
            new_content = request.POST.get('notes')
	    data_dict = {'title': new_title, 'content': new_content}
	    try:
	        toolkit.get_action('ckanext_theme_save_new_article')(context, data_dict)
                helper.flash_success('The new blog has been added')
            except toolkit.ObjectNotFound:
		abort(404, 'Blog cannot save')

	return plugins.toolkit.render('article/new.html')


