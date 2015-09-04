from flask import Flask

from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)

def create_tables():
    Councillor.create_table()
    Party.create_table()
    Council.create_table()
    Canton.create_table()
    Promise.create_table()
    Decision.create_table()
    Opinion.create_table()
