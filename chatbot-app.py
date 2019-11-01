from chatbot import Chatbot
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Chatbot, '/recieve-sms')

if __name__ == '__main__':
    app.run(port='5003')
