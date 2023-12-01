from flask import Flask, render_template, jsonify
from brain import get_json
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", data=jsonify(get_json()))