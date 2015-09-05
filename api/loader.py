# -*- coding: utf-8 -*-
"""
    kandidaten.loader
    ~~~~~~~~~~~~~~~~~

    This module collects data from different sources.

    :license: MIT, see LICENSE for more details.
"""
from app import app
from models import *
import csv

def import_cantons(filename):
    count = 0
    with open('../data/%s.csv' % filename, 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            c = Canton.create_or_get(name=row['name-de'], initials=row['abbr'])
            count = count + 1
    print "%d cantons loaded" % count

def import_parties(filename):
    count = 0
    with open('../data/%s.csv' % filename, 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            p = Party.create_or_get(name=row['name-de'], shortname=row['abbr'].upper())
            count = count + 1
    print "%d parties loaded" % count

def import_councillors(filename, council):
    count = 0
    with open('../data/%s.csv' % filename, 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            party = Party.by_shortname(row['party_short'])
            canton = Canton.by_name(row['district'])
            c = Councillor.create_or_get(
                id_smartvote=row['ID_Candidate'],
                first_name=row['firstname'],
                last_name=row['lastname'],
                photo = row['LINK_photo'],
                party = party,
                council = council,
                canton = canton
            )
            count = count + 1
    print "%d councillors loaded into %s" % (count, council.name)




def import_json(file):
    filedata = file.read()
    jsondata = json.loads(filedata)
    count = 0
    for p in jsondata['votes']:
        if save_vote(p): count = count + 1
    print "%d votes counted" % count

def run():
    import_cantons('cantons')
    import_parties('parties')
    nr = Council(name="Nationalrat")
    nr.save()
    import_councillors('NR-Kandidierende', nr)
    sr = Council(name="Ständerat")
    sr.save()
    import_councillors('SR-Kandidierende', sr)
