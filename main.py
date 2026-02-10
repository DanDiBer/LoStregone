from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Simple test: takes two numbers and does basic math
    """
    # Get the data from Squarespace
    data = request.json

    # Get the two numbers
    number1 = float(data.get('number1', 0))
    number2 = float(data.get('number2', 0))

    # Do simple calculations
    sum_result = number1 + number2
    difference = number1 - number2
    product = number1 * number2

    # Avoid division by zero
    if number2 != 0:
        division = number1 / number2
    else:
        division = "Cannot divide by zero"

    # Return all results
    return jsonify({
        'number1': number1,
        'number2': number2,
        'sum': sum_result,
        'difference': difference,
        'product': product,
        'division': division
    })


@app.route('/')
def home():
    return "Simple Test Calculator API is running! ✅"


if __name__ == '__main__':
    app.run()