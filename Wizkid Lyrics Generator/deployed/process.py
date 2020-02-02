from tensorflow import keras
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import numpy as np


model = tf.keras.models.load_model('first_model.h5')
#model._make_predict_function()
tokenizer = Tokenizer()

def get_input():
    print('Enter your text')
    text = input()
    print('How many tags do you want')
    length = input()
    return text, length


def tokenize_text():
    data = open('wizkid.txt').read()
    corpus = data.lower().split('\n')
    tokenizer.fit_on_texts(corpus)
    input_sequences = []
    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i + 1]
            input_sequences.append(n_gram_sequence)
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
    return max_sequence_len, input_sequences


def preprocess_text(text, length, max_sequence_len):
    for _ in range(length):
        token_list = tokenizer.texts_to_sequences([text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)
        output_word = ''
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        text = text + " " + output_word
    return text


if __name__ == '__main__':
    print('Enter start word here')
    text = input()
    length = int(input('number of words to predict: '))
    max_sequence_len, input_sequences = tokenize_text()
    words = preprocess_text(text=text, length=length, max_sequence_len=max_sequence_len)
    print(words)