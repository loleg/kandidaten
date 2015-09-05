# config

class Configuration(object):
    DATABASE = {
        'name': '../data/local.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    DEBUG = True
    SECRET_KEY = 'asdfghjkl'
