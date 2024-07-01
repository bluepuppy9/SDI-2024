from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()
    #response = ollama.respond(user_input)  # Replace with your chatbot's response function
    response = "Your response here"
    if user_input == "exit":
        response = "Goodbye!"
    elif user_input == "hello":
        response = "Hi there!"
    elif user_input == "bye":
        response = "Bye!"
    elif user_input == "how are you?":
        response = "I'm doing well, thank you!"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)