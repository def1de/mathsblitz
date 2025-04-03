from flask import Flask, render_template, jsonify, request
from mathsapi import get_questions, get_answers

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", data=get_questions())

@app.route("/validate", methods=["POST"])
def validate():
    req = request.get_json()
    data = req["answers"]
    answers = get_answers()
    res = list(map(lambda x, y: x == y, data, answers))

    return jsonify(res)