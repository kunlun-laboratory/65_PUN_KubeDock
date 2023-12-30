from flask import Flask
from flask import jsonify
import os
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def api():
    return jsonify(
        status=200,
        message='Hello Python!'
    )

@app.route('/get/<name>', methods=['GET'])
def api_name(name):    
    return jsonify(
        status=200,
        message=f"Hello {name}!"
    )

@app.route('/list', methods=['GET'])
def json_return():
    try:
        with open(os.path.join(os.getcwd(), "src/assets/exampleList.json"), encoding='utf-8') as json_data:
            json_string = json.load(json_data)
        return jsonify(
            status=200,
            message=json_string
        )
    except Exception as e:
        print(e)
        return jsonify(
            status=500,
            message='Internal Server Error'
        )

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=8000)