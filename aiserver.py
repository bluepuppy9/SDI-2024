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
    #return jsonify({'response': "the mitocondira is actually the powerhouse of the cell"})
    #return jsonify({'response': f"{user_input} for real"})
    return jsonify({'response': message})
if __name__ == '__main__':
    app.run(debug=True)
#import os
#import google.generativeai as genai
#
#genai.configure(api_key=os.environ[''])
#
#model = genai.GenerativeModel(
#    model_name='gemini-1.5-pro',
#    tools='code_execution')
#
#response = model.generate_content((
#    'What is the sum of the first 50 prime numbers? '
#    'Generate and run code for the calculation, and make sure you get all 50.'))
#
#print(response.text)