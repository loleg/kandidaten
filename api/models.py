from datetime import datetime
from flask import Markup
from peewee import *

from app import db

class Party(db.Model):
    name = CharField()
    shortname = CharField(unique=True, null=True)
    def __unicode__(self):
        return self.name
    @staticmethod
    def by_shortname(shortname):
        try:
            return Party.get(Party.shortname==shortname.upper())
        except Party.DoesNotExist:
            print "Party %s not found" % shortname
            return None

class Canton(db.Model):
    name = CharField()
    initials = CharField(unique=True)
    def __unicode__(self):
        return self.name
    @staticmethod
    def by_name(name):
        try:
            return Canton.get(Canton.name==name)
        except Canton.DoesNotExist:
            print "Canton %s not found" % name
            return None

class Council(db.Model):
    name = CharField(unique=True)
    def __unicode__(self):
        return self.name

class Councillor(db.Model):
    last_name = CharField()
    first_name = CharField()
    id_admin = IntegerField(unique=True, null=True)
    id_politnetz = IntegerField(unique=True, null=True)
    id_smartvote = IntegerField(unique=True, null=True)
    photo = CharField(null=True)
    occupation = CharField(null=True)
    party = ForeignKeyField(Party, null=True)
    canton = ForeignKeyField(Canton, null=True)
    council = ForeignKeyField(Council, null=True)
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Promise(db.Model):
    created_date = DateTimeField(default=datetime.now)
    date = DateTimeField(default=datetime.now)
    text = TextField()
    url = CharField(null=True)
    councillor = ForeignKeyField(Councillor, null=False, related_name='promises')
    def __unicode__(self):
        return "%s: %s" % (self.councillor.last_name, self.text[0:25])

class Decision(db.Model):
    created_date = DateTimeField(default=datetime.now)
    date = DateTimeField(default=datetime.now)
    text = TextField()
    url = CharField(null=True)
    councillor = ForeignKeyField(Councillor, null=False, related_name='decisions')
    def __unicode__(self):
        return "%s: %s" % (self.councillor.last_name, self.text[0:25])

class Comment(db.Model):
    created_date = DateTimeField(default=datetime.now)
    valid = BooleanField()
    comment = TextField(null=True)
    quote_promise = CharField(null=True)
    quote_decision = CharField(null=True)
    promise = ForeignKeyField(Promise, null=False, related_name='comments')
    decision = ForeignKeyField(Decision, null=False, related_name='comments')
