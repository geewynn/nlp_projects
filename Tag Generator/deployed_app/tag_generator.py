import numpy as np
from sklearn import decomposition
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy import linalg
import nltk

nltk.download('wordnet')


def get_input():
    print('Enter your text')

    text = input()
    print('How many tags do you want')
    length = input()
    return text, length


def vectorize_words(text):
    vectorizer = CountVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(text).todense()
    vocabs = np.array(vectorizer.get_feature_names())
    return vocabs, vectors


def nmf(vectors):
    d = 5
    clf = decomposition.NMF(n_components=d, random_state=1)
    nm = clf.fit_transform(vectors)
    nmf_comp = clf.components_
    return nmf_comp


def tfidf(vectors, text):
    d = 4
    clf = decomposition.NMF(n_components=d, random_state=1)
    vectorizer_tfidf = TfidfVectorizer(stop_words='english')
    vectors_tfidf = vectorizer_tfidf.fit_transform(text)
    tfid = clf.fit_transform(vectors_tfidf)
    tfid_comp = clf.components_
    return tfid_comp


def svd(vectors):
    U, s, Vh = linalg.svd(vectors, full_matrices=False)

    return Vh


def show_words(Vh, length, vocabs):
    top_words = lambda t: [vocabs[i] for i in np.argsort(t)[:-length - 1:-1]]
    topic_words = ([top_words(t) for t in Vh])
    return [" ".join(t) for t in topic_words]


if __name__ == '__main__':
    print('Paste your text here')
    text = [input()]
    length = int(input('number of words: '))
    vocabs, vectors = vectorize_words(text=text)
    Vh = svd(vectors)
    nmf_comp = nmf(vectors)
    tfid_comp = tfidf(vectors, text)
    words = show_words(nmf_comp, length, vocabs)
    print(words)
