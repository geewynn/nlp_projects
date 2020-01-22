# Tag Generator
This is a simple Natural Language Project created to generate tags from a given set of word. This can be an article, question or anything etc.

## Concepts Used
For this project I used
- 1. Non-matrix Factorization(NMF)
- 2. Tfidf Vectorizer(TFIDF)
- 3. Singular Value Decomposition(SVD).

## Project Walkthrough

## Data Processing

### Stop Words
- Stop words are common words that appear or a commonly used in a specific language. eg.'the', 'a', 'an' etc.
- Stop words are library dependent.
- These stop words where removed from the text, removing stop words sometime varies, they might negatively 
affect the performance of your model or not, It all depends on your use case. 
- In this scenario I chose to remove to avoid the model returning a stop word as a suggested tag.

### Vectorization
- Vectorization is the process of converting words into numbers. This is the numeric representation of a specific word into a number.
- I used CountVectorizer a method in sklearn to create seperate vectors for the text.
- After I created vocabularies of each vectorized text from the count vectorizer.

The above two methods are the main preprocessing steps taken to clean up the data set. Moving on to Modelling.

### Modelling
- For the model building I experimented on 3 different NLP concepts,
- 1. SVD
- 2. NMF
- 3. TFIDF

#### SVD
- SVD means singular value decomposition, It is used to reduce the dimensional representaton of our matrix and helps remove noises in our text.
- SVD finds the least possible text used to represent the whole information.
- SVD takes in the vectorized words and returns the words and returns the word that it thinks can correctly represents the other words.
- Used the scipy linalg.svd function here.

#### NMF
Linear-algeabreic model, that factors high-dimensional vectors into a low-dimensionality representation. 
Similar to Principal component analysis (PCA), NMF takes advantage of the fact that the vectors are non-negative.

### TFIDF
- Term frequency inverse document frequency returns the most important word in a documents.

- For the final model I used the term NMF model to generate tags from a collection of text/content.
