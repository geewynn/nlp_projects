from flask import Flask, request, render_template
import os
from tag_generator import vectorize_words, nmf, show_words

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/modelling', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        text = request.form['text']
        return render_template('model.html', result=request.form['text']), text
    if request.method == 'GET':
        return render_template('model.html')


@app.route('/text', methods=['POST'])
def texts():
    text = request.form['text']
    text = [text]
    length = request.form['length']
    length = int(length)
    vocabs, vectors = vectorize_words(text=text)
    nmf_comp = nmf(vectors)
    words = show_words(nmf_comp, length, vocabs)
    return render_template('text.html', words=words)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
