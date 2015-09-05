import datetime
from flask import request, redirect

from flask_peewee.admin import Admin, ModelAdmin #, AdminPanel
from flask_peewee.filters import QueryFilter

from app import app, db
from auth import auth
from models import Councillor, Promise, Decision, Opinion

admin = Admin(app, auth, branding='KandiDaten Backend')

class CouncillorAdmin(ModelAdmin):
    columns = ('council', 'first_name', 'last_name', 'party', 'canton')
    # foreign_key_lookups = {'party': 'name', 'canton': 'initials'}
    # filter_fields = ('name', 'active_date', 'party__name', 'canton__initials')

class PromiseAdmin(ModelAdmin):
    columns = ('date', 'text', 'councillor',)
    foreign_key_lookups = {'councillor': 'last_name'}
    exclude = ('created_date',)

class DecisionAdmin(ModelAdmin):
    columns = ('date', 'text', 'councillor',)
    foreign_key_lookups = {'councillor': 'last_name'}
    exclude = ('created_date',)

class OpinionAdmin(ModelAdmin):
    columns = ('created_date', 'valid', 'quote_promise', 'quote_decision')

auth.register_admin(admin)
admin.register(Councillor, CouncillorAdmin)
admin.register(Promise, PromiseAdmin)
admin.register(Decision, DecisionAdmin)
admin.register(Opinion, OpinionAdmin)
