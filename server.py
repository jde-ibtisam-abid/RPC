# server.py
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

def get_xy_from_json():
    data = request.get_json(silent=True)
    if data is None:
        return None, ("Invalid JSON body", 400)
    if 'x' not in data or 'y' not in data:
        return None, ("Missing 'x' or 'y' in JSON body", 400)
    try:
        x = float(data['x'])
        y = float(data['y'])
    except (ValueError, TypeError):
        return None, ("'x' and 'y' must be numbers", 400)
    return (x, y), None

def maybe_int(n):
    # If n is whole number, convert to int for nicer JSON
    if float(n).is_integer():
        return int(n)
    return n

@app.route('/add', methods=['POST'])
def add():
    xy, err = get_xy_from_json()
    if err:
        msg, code = err
        return jsonify({"error": msg}), code
    x, y = xy
    result = x + y
    return jsonify({"result": maybe_int(result)}), 200

@app.route('/multiply', methods=['POST'])
def multiply():
    xy, err = get_xy_from_json()
    if err:
        msg, code = err
        return jsonify({"error": msg}), code
    x, y = xy
    result = x * y
    return jsonify({"result": maybe_int(result)}), 200

# Optional: helper endpoint to simulate a slow server (for timeout testing)
@app.route('/delay', methods=['POST'])
def delay():
    data = request.get_json(silent=True) or {}
    seconds = data.get('seconds', 5)
    try:
        secs = float(seconds)
    except (ValueError, TypeError):
        return jsonify({"error": "seconds must be a number"}), 400
    time.sleep(secs)
    return jsonify({"slept": maybe_int(secs)}), 200

if __name__ == '__main__':
    # Dev server (bind to 0.0.0.0 and port 8080 as required)
    app.run(host='0.0.0.0', port=8080)
