from flask_restful import Resource, Api, reqparse
from flask.json import jsonify
from flask import request
from utils import pickanswer
class Chatbot(Resource):

    def post(self):
        print("here")
        arguments = ["msisdn", "to", "messageId", "text", "type"]
        parser = reqparse.RequestParser()
        print("parser>>",parser)
        for item in arguments:
            parser.add_argument(item)
        args = parser.parse_args()

        msisdn = args['msisdn']
        to = args["to"]
        messageId = args["messageId"]
        text = args["text"]
        category = args["type"]

        print(msisdn)
        pickanswer(text,msisdn)

        return "ok", 200