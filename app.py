from unittest import result
from flask import Flask, jsonify
import scripts.run as run

app = Flask(__name__)

@app.route("/")
@app.route("/help")
def landing_page():
    return "<p>Welcome to Hotel API</p>"


@app.route('/<string:address>')
def min_distance(address):
    result = run.distance(address)
    return jsonify(result)

@app.route('/<string:address>/<int:distance>')
def range_distance(address,distance):
    result = run.distance(address,distance)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)