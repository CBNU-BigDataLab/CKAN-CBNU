import ckan.plugins as plugins
import ckan.lib.base as base

class PageController(base.BaseController):

    def sitemap(self):
	return plugins.toolkit.render('sitemap.html')
    def usingInformation(self):
	return plugins.toolkit.render('using-information.html')
