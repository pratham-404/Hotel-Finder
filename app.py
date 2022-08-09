from flask import Flask, jsonify, render_template, request
from scripts.min import Min
from scripts.range import Range
import json

app = Flask(__name__, static_url_path='/static')

@app.route("/")
@app.route("/help")
def home():
    return render_template('index.html', title="Home")

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    address = args.get("location", default="", type=str)
    distance = args.get("radius", default=0, type=int)

    if distance == 0: result = Min(address)
    else: result = Range(address, distance)
    
    return json.dumps(result.__dict__,indent=4)

if __name__ == '__main__':
    app.run(debug=True)