from flask_peewee.rest import RestAPI, RestResource, UserAuthentication, AdminAuthentication, RestrictOwnerResource

from app import app
# from auth import auth
from models import Councillor, Promise, Decision, Opinion

api = RestAPI(app)

class CouncillorResource(RestResource):
    exclude = ()

class PromiseResource(RestResource):
    exclude = ()
    # include_resources = {'user': UserResource}

class DecisionResource(RestResource):
    exclude = ()

class OpinionResource(RestResource):
    include_resources = {
        'promise': PromiseResource,
        'decision': DecisionResource,
    }
    paginate_by = None

# register our models so they are exposed via /api/<model>/
api.register(Councillor, CouncillorResource)
api.register(Promise, PromiseResource)
api.register(Decision, DecisionResource)
api.register(Opinion, OpinionResource)
