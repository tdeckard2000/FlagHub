import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "You are connected to a server! -- Test"

if os.getenv("ENV") == "dev" :
    app.run(debug=True)