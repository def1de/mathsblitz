from flask import Flask, render_template, jsonify
from mathsapi import get_json
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", data=get_json())