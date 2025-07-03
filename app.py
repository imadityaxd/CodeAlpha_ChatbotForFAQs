from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os 
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# Make sure the environment variable name is correct
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')  # corrected spelling from GEMENI
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
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT environment variable
    app.run(host="0.0.0.0", port=port)
