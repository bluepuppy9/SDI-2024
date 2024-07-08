from flask import Flask, request, jsonify
from flask_cors import CORS
from time import sleep

from ollama import generate

app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()
    message = ''
    for part in generate('llama3', user_input, stream=True):
        message += part['response']
    #return jsonify({'response': f"{user_input} for real"})
    return jsonify({'response': message})
if __name__ == '__main__':
    app.run(debug=True)