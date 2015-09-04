from datetime import datetime
from flask import Markup
from peewee import *

from app import db

class Party(db.Model):
    name = TextField()

class Council(db.Model):
    name = TextField()

class Canton(db.Model):
    name = TextField()

class Councillor(db.Model):
    id_admin = IntegerField()
    id_politnetz = IntegerField()
    name = CharField()
    active_since = DateTimeField()
    active_until = DateTimeField()
    photo = CharField()
    party = ForeignKeyField(Party)
    council = ForeignKeyField(Council)
    canton = ForeignKeyField(Canton)
    class Meta:
        order_by = ('party', 'name')

class Promise(db.Model):
    created_date = DateTimeField(default=datetime.now)
    date = DateTimeField(default=datetime.now)
    text = TextField()
    url = CharField()
    councillor = ForeignKeyField(Councillor, null=False, related_name='promises')

class Decision(db.Model):
    created_date = DateTimeField(default=datetime.now)
    date = DateTimeField(default=datetime.now)
    text = TextField()
    url = CharField()
    councillor = ForeignKeyField(Councillor, null=False, related_name='decisions')

class Opinion(db.Model):
    created_date = DateTimeField(default=datetime.now)
    valid = BooleanField()
    comment = TextField()
    quote_promise = CharField()
    quote_decision = CharField()
    promise = ForeignKeyField(Promise, null=False, related_name='opinions')
    decision = ForeignKeyField(Decision, null=False, related_name='opinions')
    class Meta:
        indexes = (('promise', 'decision'), False)
