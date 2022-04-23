import os
from os import environ

class Config(object):

    DEBUG = False
    Testing = False


    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'planalytix'

    UPLOADS = "Users\MSI\PycharmProjects\pythonProject\Assignment\Pan card Tempering\app\static"

    SESSION_COOKIE_SECURE = True

    DEFAULT_THEME = None

class DevelopmentConfig(Config):


    DEBUG = True

    SESSION_COOKIE_SECURE = False

class DebugConfig(Config):

    DEBUG = False



eey