from flask import Flask, jsonify
from scripts.min import Min
from scripts.range import Range
import json

app = Flask(__name__)

@app.route("/")
@app.route("/help")
def landing_page():
    return "<p>Welcome to Hotel API</p>"

@app.route('/<string:address>')
def min_distance(address):
    result = Min(address)
    j = json.dumps(result.__dict__,indent=4)
    return j

@app.route('/<string:address>/<int:distance>')
def range_distance(address,distance):
    result = Range(address,distance)
    j = json.dumps(result.__dict__,indent=4)
    return j

if __name__ == '__main__':
    app.run(debug=True)