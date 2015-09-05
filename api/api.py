from flask_peewee.rest import RestAPI, RestResource, UserAuthentication, AdminAuthentication, RestrictOwnerResource

from app import app
from auth import auth
from models import Councillor, Promise, Decision, Comment

api = RestAPI(app)
admin_auth = AdminAuthentication(auth)

class CouncillorResource(RestResource):
    exclude = ()

class PromiseResource(RestResource):
    exclude = ()
    include_resources = {
        'councillor': CouncillorResource
    }

class DecisionResource(RestResource):
    exclude = ('councillor')

class CommentResource(RestResource):
    include_resources = {
        'promise': PromiseResource,
        'decision': DecisionResource
    }
    paginate_by = None

class UserResource(RestResource):
    exclude = ('password', 'email',)

# register our models so they are exposed via /api/<model>/
api.register(Councillor, CouncillorResource)
api.register(Promise, PromiseResource)
api.register(Decision, DecisionResource)
api.register(Comment, CommentResource)
api.register(auth.User, UserResource, auth=admin_auth)
