import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ThemePlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer),
    plugins.implements(plugins.IRoutes, inherit=True)

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
	return m
