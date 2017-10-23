import ckan.plugins as plugins
from ckan.lib.base import BaseController

class PageController(BaseController):

    def sitemap(self):
	return plugins.toolkit.render('sitemap.html')
