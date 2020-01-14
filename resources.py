import json
from collections import defaultdict

import requests
from flask import request
from flask_restful import Api, Resource


class Authorization(Resource):
    def post(self):
        url = "https://api-prd.kpn.com/oauth/client_credential/accesstoken"

        payload = dict(
            client_id=request.form["clientid"],
            client_secret=request.form["clientsecret"],
        )
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        data = requests.post(
            url,
            params=dict(grant_type="client_credentials"),
            data=payload,
            headers=headers,
        )
        message = data.json()
        message["input"] = payload
        return message, data.status_code


class Chatbot(Resource):
    def __init__(self):
        self.msisdn = ""
        self.text = ""
        self.access_token = ""

    def get(self):
        return "I am alive", 200

    def post(self):
        """
        Processes the message, picks and answer and sends it back
        """
        args = request.json
        if "Authorization" in request.headers:  # remove this condition XDD
            self.access_token = request.headers["Authorization"]
        self.tonumber = args["msisdn"]
        # to = args["to"]
        # messageId = args["messageId"]
        self.text = args["text"].lower()
        # category = args["type"]
        intent = self.pickanswer()
        return self.sendSMS(intent)

    def pickanswer(self):
        with open("chatbot_sample_intents.csv", "r") as f:
            content = f.readlines()

        text_fields = self.text.split(" ")
        predict_answer = {}
        for line in content:
            fields = line.strip().split(",")
            target = fields[0]
            count = sum([1 for word in text_fields if word in fields[1:]])
            predict_answer[target] = count

        answer = max(predict_answer, key=predict_answer.get)
        return answer

    def sendSMS(self, text):
        url = "https://api-prd.kpn.com/communication/nexmo/sms/send"

        payload = f"from=3197010240299&to={self.tonumber}&text={text}"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate",
        }

        response = requests.post(url, data=payload, headers=headers)
        return response.json(), response.status_code


class Contexta(Resource):
    def __init__(self):
        self.load_data()
        # load knowledge
        self.load_knowledge()

    def get(self):
        text = self.extract_text()
        intentions = self.extract_intentions(text)
        return intentions, 200

    def extract_text(self):
        """
        Retrieves the intention per speaker
        """
        speech = defaultdict(list)
        for segmentList in self.data["SegmentList"]:
            words = [word["text"] for word in segmentList["words"]]
            speech[segmentList["spkid"]] += words
        return speech

    def extract_intentions(self, speech):
        intention = defaultdict(str)
        for speaker, speech in speech.items():
            intention[speaker] = self.pickanswer(speech)
        return intention

    def pickanswer(self, text):
        predict_answer = defaultdict(int)
        for word in text:
            if word in self.vocabulary.keys():
                meanings = self.vocabulary[word]
                for meaning in meanings:
                    predict_answer[meaning] += 1
        if predict_answer:
            answer = max(predict_answer, key=predict_answer.get)
            return answer

    def load_data(self):
        with open("contexta_speech_sample.json") as json_file:
            self.data = json.load(json_file)

    def load_knowledge(self):
        """
        Returns a dictionaty where each word points to a meaning
        """
        with open("contexta_vocab.csv", "r") as file:
            content = file.readlines()

        self.vocabulary = defaultdict(list)
        for line in content:
            fields = line.strip().split(",")
            target = fields[0]
            words = fields[1:]
            for word in words:
                self.vocabulary[word].append(target)
