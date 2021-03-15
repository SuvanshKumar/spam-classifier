# Email Spam Classifier

Classifying an email as spam or ham, using Naive Bayes and Logistic Regression Algorithms

This project aims to develop a reliable and accurate classifier that marks an email as a spam or ham (non-spam) using only a small dataset (containing 948 labeled emails).

Here, I implemented the multinomial Naive Bayes algorithm for text classification, for which more description can be found [here](http://nlp.stanford.edu/IR-book/pdf/13bayes.pdf "NLP Stanford IR book, Text classification and Naive Bayes").

## Results and further improvements

An accuracy of 96.65% is achieved on the test dataset. 

In an attempt to improve the results further, the commonly occurring words (called _stopwords_, like 'the', 'do', 'each', 'for', etc.) are removed. This is because they don't add much context to the emails (both spams and hams contain a lot of them, so they don't provide much useful information). Some good common stopwords can be found [here](https://www.ranks.nl/stopwords "Stopwords"), and have been included in [stopwords.txt](data/stopwords.txt).

> Stopwords for other languages can also be found on [that link](https://www.ranks.nl/stopwords "Stopwords").

The removal of stopwords lead to a slightly increased accuracy of 96.86%.

## Instructions of use

To train your Naive Bayes Classifier:

- Clone this repository

```bash
$ git clone https://github.com/SuvanshKumar/spam-classifier.git
```

or

```bash
$ git clone git@github.com:SuvanshKumar/spam-classifier.git
```

- Change to inside the cloned directory

```bash
$ cd spam-classifier
```

- Go to the src folder

```bash
$ cd src
```

- Run [main.py](src/main.py) file.

```
$ python3 main.py

Naive Baye's classifier:
Including stop words, the accuracy is: 0.9665271966527197
After removing stop words, the accuracy is: 0.9686192468619247
```

There it is. You have successfully run a classifier that gives 96%+ accuracy on classifying an email as spam.

## (Optional) Adding your own data for testing/training

The dataset consists of emails, stored as `.txt` files. The initial training and testing data are stored in the [data](data/) folder, sorted into hams and spams. You can add your own email text files for training or testing, in the appropriate folders. The [stopwords.txt](data/stopwords.txt) may be edited to suit your needs.

> Tip: You can also classify emails in other languages (French? Hindi? Spanish?) using the same classifier. Add your email text file into the dataset and run [main.py](src/main.py). The more data you have in the language of your choice, the better the results.

> You can also add stopwords of your language to [stopwords.txt](data/stopwords.txt).
