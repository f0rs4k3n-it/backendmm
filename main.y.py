import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    resp = jsonify(success=True)
    return resp


@app.route('/info')
def info():
    return json.dumps({'name': 'matteo',
                       'surname': 'massai'})


app.run(host='127.0.0.1', port=4444, debug=True)
