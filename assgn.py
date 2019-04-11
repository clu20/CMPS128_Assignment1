from flask import Flask, abort,jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class hello(Resource):
	def get(self):
		helloStrip = 'Hello, world!'.rstrip()
		if(len(request.args) == 0): 
			return helloStrip
		else:
			raise InvalidUsage('Cannot GET request with string query', status_code = 406)
	def post(self):
		raise InvalidUsage('This method is unsupported', status_code = 405)

class test(Resource):
	def get(self):
		if(len(request.args) == 0):
			return 'GET message received'
		else:
			raise InvalidUsage('Cannot GET request with string query', status_code = 406)
	def post(self):
		if(len(request.args)==0):
			raise InvalidUsage('This method is unsupported', status_code = 405)
		else:
			msg = request.args.get('msg')
			if not msg:
				raise InvalidUsage('POST requests must be done with msg=', status_code = 406)
			else:
				return 'POST message received: ' + msg

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


api.add_resource(hello, '/hello')

api.add_resource(test, "/test")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8081)