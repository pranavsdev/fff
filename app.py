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


# API section begins here
api = Api(app)
api.add_resource(Authorization, "/auth")
api.add_resource(Chatbot, "/receive-sms")
api.add_resource(Contexta, "/contexta")

if __name__ == "__main__":
    app.run(port="5003", debug=True)
