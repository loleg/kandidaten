from app import app
from models import Councillor, Party, Canton, Promise, Decision, Opinion
import csv

def onlyascii(char):
    if ord(char) < 48 or ord(char) > 127: return ''
    else: return char

def import_cantons(filename):
    count = 0
    with open('../data/%s.csv' % filename, 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            c = Canton(name=row['name-de'], initials=row['abbr'])
            c.save()
            count = count + 1
    print "%d cantons loaded" % count

def import_councillors(filename):
    data = []
    for item in [filter(onlyascii, line).lower()
                 for line in open("../data/%s" % filename)]:
        data.append(item)
    print "%d items loaded" % len(data)

def import_json(file):
    filedata = file.read()
    jsondata = json.loads(filedata)
    count = 0
    for p in jsondata['votes']:
        if save_vote(p): count = count + 1
    print "%d votes counted" % count

def run():
    import_cantons('cantons')
    # import_parties('parties')
    # import_councillors('NR-Kandidierende')
