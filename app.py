from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os 
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMENI_API_KEY')
# Configure your Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.get_json().get('message', '')
    response = model.generate_content(user_input)
    return jsonify({"response": response.text.strip()})

if __name__ == "__main__":
    app.run(debug=True)
