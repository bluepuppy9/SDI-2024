from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama  # Ensure this is installed and properly configured

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()
    
    # Dictionary to store predefined responses
    predefined_responses = {
        "exit": "Goodbye!",
        "hi": "Hi there!",
        "bye": "Bye!",
        "how are you": "I'm doing well, thank you!"
    }
    
    # Check for predefined responses
    response = predefined_responses.get(user_input, "Your response here")
    
    # If no predefined response, call the ollama function # Replace with your chatbot's response function

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
