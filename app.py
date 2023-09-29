# ChatBot-SaaS

# Author: Edgar Rodriguez

# ChatBot example using an OpenAI SaaS API using a trained gpt-3.5-turbo model

# The author generated this text in part using GPT-3, OpenAI's large-scale language generation model.
# After generating the draft of the text, the author reviewed, edited, revised and tested it.
# This project is licensed under the terms of the MIT License

from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# API key at https://platform.openai.com/account/api-keys
openai.api_key = 'YOUR-API-KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input},
        ],
        temperature=0,
    )
    chatbot_response = response['choices'][0]['message']['content']
   
    return chatbot_response

if __name__ == '__main__':
    app.run(debug=True)
