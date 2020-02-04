# Wizkid Song Lyrics Predictor


## Data Collection
- 50 of wizkid song were scraped from Genius API useing this [scraper](https://github.com/geewynn/nlp_projects/blob/master/Wizkid%20Lyrics%20Generator/wizkid_lyrics_scraper.py)
- The scraped data was saved in a text file called wizkid.txt.

## Feature Engineering
- A corpus of all words were created.
- Create a dictionary of words (Key reperesents the word and Value reperesents the token)
- Create an input sequence list from the tokens.
- Create a pad sequence so the input sequences all have the same length, this length is dictated by the sequnce with the largest length.
- Split into data and label.
- The label is the last character in the sequence-
- One hot encot the label.

## Deeplearning Model
- This is a sequential model from tensorflow.
- Add an Embedding layer, 2 LSTM layers with the first passing through a biderectional function (this helps to produce predictions that go in both directions).
- Drop 20% of the training data on each iteration.
- 2 Dense output layer. The first has a relu activaation function, the second which is the output layer contains a softmax activation function.
- Compile the model on a categorical crossentropy loss, adam optimizer.
- Train the model on 70 epochs.(approximately 5 hours to train with gpu on google colab)

## Model Evaluation
![acc](https://github.com/geewynn/nlp_projects/blob/master/Wizkid%20Lyrics%20Generator/images/training.png)

- The image aboce shows us the training accuracy steadily increases on each training epoch.

![loss](https://github.com/geewynn/nlp_projects/blob/master/Wizkid%20Lyrics%20Generator/images/loss.png)

- From above image we can see that the training loss also decsreases on each epoch.

- This is an indication that our training is good and the model will perform better on higher number of training epochs.

## Prediction
- Tried the model on this seed words "come closer"
- The number of predicted words given was 50.

- The output was 

```
come closer make me sing high note ay by the world when me drop it unfolds before the boat yeah yeah yeah yeah 

yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah 

yeah yeah yeah yeah yeah yeah yeah
```

- After the first 10 words we notice a repition of the word 'yeah'
- This happens because 
    - The training data used was small, a larger dataset will perform better.
    - Increase the number of training epochs, maybe 100, 200 500, 1000.
    - The data doesn't contain enough words, most music lyrics contain mainly word repitions.
    
## Future Works
- Train the model on a higher number of epochs (I didn't do this because it took more time to train and google colab kept shutting down).
- Get more lyrics data. Scrape 100 songs and above.
- Try removing stopwords (Might reduce the performance of the model)
