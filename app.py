from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Ava")
ASSISTANT_STYLE = os.getenv("ASSISTANT_STYLE",
                            "Be concise, practical, friendly and respond in preferred language.")

if not API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY in .env file")

client = OpenAI(api_key=API_KEY)

# Load instructions at server startup
try:
    with open("prompt-sample.txt", "r", encoding="utf-8") as f:
        INSTRUCTIONS = f.read()
except FileNotFoundError:
    INSTRUCTIONS = f"SYSTEM: {ASSISTANT_NAME}. {ASSISTANT_STYLE}"


@app.route('/')
def home():
    # Redirect to chat-widget.html
    return '''
    <html>
    <head>
        <meta http-equiv="refresh" content="0; url=/chat-widget.html">
    </head>
    <body>
        <p>Redirecting to chatbot... <a href="/chat-widget.html">Click here</a></p>
    </body>
    </html>
    '''


@app.route('/chat-widget.html')
def chat_widget():
    try:
        with open('chat-widget.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return '<h1>Error: chat-widget.html not found</h1>', 404


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'error': 'Missing message'}), 400

    try:
        response = client.responses.create(
            model="gpt-5",
            instructions=INSTRUCTIONS,
            input=user_message
        )

        assistant_text = getattr(response, "output_text", None)
        if not assistant_text:
            assistant_text = ""
            if hasattr(response, "output"):
                parts = response.output if isinstance(response.output, list) else [response.output]
                assistant_text = " ".join(p.get("content", "") if isinstance(p, dict) else str(p) for p in parts)

        return jsonify({
            'response': assistant_text,
            'status': 'success'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)