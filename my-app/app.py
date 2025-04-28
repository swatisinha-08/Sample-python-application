from flask import Flask, request, jsonify
from app import calculator  # Import your logic

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Calculator API"

@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calculator.add(a, b)
    return jsonify(result=result)

@app.route('/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calculator.subtract(a, b)
    return jsonify(result=result)

@app.route('/multiply', methods=['GET'])
def multiply():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calculator.multiply(a, b)
    return jsonify(result=result)

@app.route('/divide', methods=['GET'])
def divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = calculator.divide(a, b)
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
