from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

PROMISES = {
    'p1': {'who': 'Major Laser', 'what': 'Save the world!', 'when': '2014-04-01j'}
}

def abort_if_doesnt_exist(_id):
    if _id not in PROMISES:
        abort(404, message="Promise with ID {} doesn't exist".format(_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class Promise(Resource):
    def get(self, promise_id):
        abort_if_doesnt_exist(promise_id)
        return PROMISE[promise_id]

    def delete(self, promise_id):
        abort_if_doesnt_exist(promise_id)
        del PROMISE[promise_id]
        return '', 204

    def put(self, promise_id):
        args = parser.parse_args()
        p = {'who': args['who'], 'what': args['what'], 'when': args['when']}
        PROMISES[promise_id] = task
        return p, 201

class PromiseList(Resource):
    def get(self):
        return PROMISES

    def post(self):
        args = parser.parse_args()
        promise_id = int(max(PROMISES.keys()).lstrip('promise')) + 1
        promise_id = 'p%i' % promise_id
        PROMISES[promise_id] = {'who': args['who'], 'what': args['what'], 'when': args['when']}
        return PROMISES[promise_id], 201

# setup resource routing
api.add_resource(PromiseList, '/promises')
api.add_resource(Promise, '/promises/<promise_id>')

if __name__ == '__main__':
    app.run(debug=True)
