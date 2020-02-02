from flask import Flask, request, render_template
from process import preprocess_text, tokenize_text


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/predictor', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        return render_template('predictor.html', result=request.form['text']), text

    if request.method == 'GET':
        return render_template('predictor.html')


@app.route('/prediction', methods=['POST'])
def predictions():
    text = request.form['text']
    length = request.form['length']
    length = int(length)
    max_sequence_len, input_sequences = tokenize_text()
    words = preprocess_text(text=text, length=length, max_sequence_len=max_sequence_len)
    return render_template('predictions.html', words=words)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
