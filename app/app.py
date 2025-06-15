from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    op = data['operation']
    n1, n2 = data['num1'], data['num2']

    try:
        result = {
            'add': n1 + n2,
            'subtract': n1 - n2,
            'multiply': n1 * n2,
            'divide': n1 / n2 if n2 else 'Divide by zero error'
        }.get(op, 'Invalid operation')
    except Exception as e:
        result = str(e)

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
