from flask import Flask, render_template, jsonify
from mathsapi import get_result
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", data=get_result())