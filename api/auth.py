from flask_peewee.auth import Auth, BaseUser
from peewee import CharField, DateTimeField, BooleanField
from app import app, db
from datetime import datetime

class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=True)
    def __unicode__(self):
        return self.username

auth = Auth(app, db, user_model=User)
