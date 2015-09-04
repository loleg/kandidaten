from datetime import date
from pony.orm import *

db = Database("sqlite", "database.sqlite", create_db=True)

class Councillor(db.Entity):
    _table_ = "councillor"
    id = PrimaryKey(int, auto=True)
    adminId = Required(int)
    party = Required("Party")
    council = Required("Council")
    canton = Required("Canton")
    promises = Set("Promise")
    votes = Set("Vote")
    councillor_interests = Set("CouncillorInterest")
    firstName = Required(str)
    lastName = Required(str)


class Party(db.Entity):
    id = PrimaryKey(int, auto=True)
    councillors = Set(Councillor)
    name = Required(str)


class Council(db.Entity):
    id = PrimaryKey(int, auto=True)
    councillors = Set(Councillor)
    name = Required(str)


class Canton(db.Entity):
    id = PrimaryKey(int, auto=True)
    councillors = Set(Councillor)
    name = Required(str)


class Promise(db.Entity):
    id = PrimaryKey(int, auto=True)
    promise_source = Required("PromiseSource")
    councillor = Required(Councillor)
    promise_behaviours = Set("PromiseBehaviour")
    title = Required(str)
    text = Required(str)
    link = Required(str)


class PromiseSource(db.Entity):
    id = PrimaryKey(int, auto=True)
    promises = Set(Promise)
    name = Required(str)
    link = Required(str)


class Descriptor(db.Entity):
    id = PrimaryKey(int, auto=True)
    promise_behaviours = Set("PromiseBehaviour")
    affair_behaviours = Set("AffairBehaviour")
    interest_behaviours = Set("InterestBehaviour")
    name = Required(unicode)


class Affair(db.Entity):
    id = PrimaryKey(int, auto=True)
    votes = Set("Vote")
    affair_behaviours = Set("AffairBehaviour")


class Interest(db.Entity):
    id = PrimaryKey(int, auto=True)
    interest_behaviours = Set("InterestBehaviour")
    councillor_interests = Set("CouncillorInterest")
    name = Required(str)


class PromiseBehaviour(db.Entity):
    _table_ = "Promise_behaviour"
    id = PrimaryKey(int, auto=True)
    promise = Required(Promise)
    descriptor = Required(Descriptor)
    proCon = Required(bool)


class AffairBehaviour(db.Entity):
    id = PrimaryKey(int, auto=True)
    descriptor = Required(Descriptor)
    affair = Required(Affair)
    proCon = Required(unicode)


class InterestBehaviour(db.Entity):
    id = PrimaryKey(int, auto=True)
    descriptor = Required(Descriptor)
    interest = Required(Interest)
    proCon = Required(unicode)


class CouncillorInterest(db.Entity):
    id = PrimaryKey(int, auto=True)
    councillor = Required(Councillor)
    interest = Required(Interest)
    start = Required(date)
    end = Required(date)
    interest_connection_type = Required("InterestConnectionType")


class Vote(db.Entity):
    id = PrimaryKey(int, auto=True)
    councillor = Required(Councillor)
    affair = Required(Affair)


class InterestConnectionType(db.Entity):
    """Verwaltungsrat, Mitglied"""
    id = PrimaryKey(int, auto=True)
    councillor_interests = Set(CouncillorInterest)
    name = Required(str)


sql_debug(True)
db.generate_mapping(create_tables=True)