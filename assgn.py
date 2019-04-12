from flask import Flask,jsonify, request, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class hello(Resource):
	def get(self):
		helloStrip = 'Hello, world!'.rstrip()
		if(len(request.args) == 0): 
			return make_response('Hello, world!', 200)
		else:
			return make_response('Not Found',404)
	def post(self):
			return make_response('This method is unsupported', 405)

class test(Resource):
	def get(self):
		if(len(request.args) == 0):
			return make_response('GET message received',200)
		else:
			return('Not Found',404)
	def post(self):
		if(len(request.args)==0):
			return make_response('POST requests must be done with msg=',405)
		else:
			msg = request.args.get('msg')
			if not msg:
				return make_response('POST requests must be done with msg=',406)
			else:
				return make_response('POST message received: ' + msg, 200)


api.add_resource(hello, '/hello')
api.add_resource(test, "/test")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)