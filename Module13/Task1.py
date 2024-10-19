from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/primenumber/<int:number>', methods=['GET'])

def primenumber(number):
    if number % 2 != 0:
        response = {
            "Number": number,
            "isPrime": "true"
        }

        return json.dumps(response, indent=4)



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
