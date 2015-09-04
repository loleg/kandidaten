# config

class Configuration(object):
    DATABASE = {
        'name': 'local.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    DEBUG = True
