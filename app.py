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
    print(data)
    answers = get_answers()
    print(answers)
    res = list(map(lambda x, y: x == y, data, answers))
    print(res)

    return jsonify(res)