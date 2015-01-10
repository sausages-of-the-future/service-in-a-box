# -*- coding: utf-8 -*-
import os

class Config(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    APP_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BASE_URL = os.environ['BASE_URL']
    REGISTRY_BASE_URL = os.environ['REGISTRY_BASE_URL']
    WWW_BASE_URL = os.environ['WWW_BASE_URL']
    REGISTRY_CONSUMER_KEY = os.environ['REGISTRY_CONSUMER_KEY']
    REGISTRY_CONSUMER_SECRET = os.environ['REGISTRY_CONSUMER_SECRET']

class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False

class TestConfig(Config):
    TESTING = True
