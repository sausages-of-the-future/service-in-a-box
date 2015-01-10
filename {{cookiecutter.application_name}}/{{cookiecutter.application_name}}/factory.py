# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
from flask import Flask, render_template

from {{cookiecutter.application_name}}.extensions import (
    oauth
    #add others as needed
)

# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
import os
from flask import Flask, render_template

from {{cookiecutter.application_name}}.extensions import (
    oauth
    #add others as needed
)

def create_app(config_filename):
    ''' An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/
    '''
    app = Flask(__name__)
    app.config.from_object(config_filename)
    register_oauth(app)
    register_errorhandlers(app)
    register_blueprints(app)
    return app

def register_oauth(app):
    oauth.init_app(app)
    #TODO maybe make the scope params more configurable?
    registry = oauth.remote_app(
        'registry',
        consumer_key = app.config['REGISTRY_CONSUMER_KEY'],
        consumer_secret = app.config['REGISTRY_CONSUMER_SECRET'],
        request_token_params = {'scope': '{{cookiecutter.oauth_scopes}}' },
        base_url = app.config['REGISTRY_BASE_URL'],
        request_token_url = None,
        access_token_method = 'POST',
        access_token_url = '%s/oauth/token' % app.config['REGISTRY_BASE_URL'],
        authorize_url = '%s/oauth/authorize' % app.config['REGISTRY_BASE_URL']
    )
    app.registry = registry

def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

def register_blueprints(app):
    from {{cookiecutter.application_name}}.frontend.views import frontend
    app.register_blueprint(frontend)

def register_extensions(app):
    pass
