from app import app, db

from auth import *
from admin import admin
from api import api
from models import *
# from views import *

admin.setup()
api.setup()

def create_tables():
    auth.User.create_table(fail_silently=True)
    Councillor.create_table(fail_silently=True)
    Party.create_table(fail_silently=True)
    Council.create_table(fail_silently=True)
    Canton.create_table(fail_silently=True)
    Promise.create_table(fail_silently=True)
    Decision.create_table(fail_silently=True)
    Comment.create_table(fail_silently=True)

if __name__ == '__main__':
    app.run()
