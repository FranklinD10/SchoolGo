from flask import Flask, render_template, send_from_directory, request
import openai
import os
from config import OPENAI_API_KEY

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

def ask_gpt(text):
    prompt = f"User: {text}\n“SchoolGo is a chatbot who is an expert on various topics covered in schools and universities. The bot is very conversational and funny. SchoolGo:"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=100, stop="\nUser:", temperature=0.2, top_p=1.0,  frequency_penalty=0.0,  presence_penalty=0.0,
        )
        message = response.choices[0].text.strip()
        return message
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't understand you. Can you please rephrase your question?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def predict():
    text = request.form['text']
    response = ask_gpt(text)
    return response

@app.route('/reset', methods=['POST'])
def reset():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
