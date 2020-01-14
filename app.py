import requests
from flask import Flask, render_template, request
from flask_restful import Api, Resource

from resources import Authorization, Chatbot, Contexta

app = Flask(__name__, template_folder="templates")

# Web section begins here
@app.route("/", methods=["GET", "POST"])
def get_access_token():
    """
    Renders the page for the user to place his client_id and client_secret
    Calls the authentication system and stores the access token
    """
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        # Authenticate
        auth = Authorization()
        response = auth.post()
        return render_template("index.html", data=response[0])


@app.route("/contexta/intents", methods=["GET"])
def get_intents():
    """
    Gets the intent for the example transcription
    """
    contexta = Contexta()
    response = contexta.get()
    normal_dict = {
        key: value for key, value in response[0].items()
    }  # Default dict has an error key that we don't want
    return render_template("contexta.html", data=normal_dict)


# API section begins here
api = Api(app)
api.add_resource(Authorization, "/v1/auth")
api.add_resource(Chatbot, "/v1/receive-sms")
api.add_resource(Contexta, "/v1/contexta")

if __name__ == "__main__":
    app.run(port="5003", debug=True)
