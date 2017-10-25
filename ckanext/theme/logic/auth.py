import ckan.plugins.toolkit as toolkit
import ckan.model as model

import logging
log = logging.getLogger(__name__)


@toolkit.auth_allow_anonymous_access
def show(context, data_dict):
    '''All users can access a articles show'''
    return {'success': True}


@toolkit.auth_allow_anonymous_access
def list(context, data_dict):
    '''All users can access a articles list'''
    return {'success': True}
