from flask import Flask, render_template, request, jsonify
from transformers import pipeline, set_seed
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Set up the text generation pipeline with GPT-2
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    return get_Chat_response(msg)

def get_Chat_response(text):
    # Generate a response using GPT-2
    response = generator(text, max_length=30, num_return_sequences=1)
    return response[0]['generated_text']

if __name__ == '__main__':
    app.run()
