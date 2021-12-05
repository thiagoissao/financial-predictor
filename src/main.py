import requests
import numpy as np
from dictionary import lmdict
from classification import countWords
from deep_translator import (GoogleTranslator)
from textblob.classifiers import NaiveBayesClassifier
from csvConverter import converterCSVToTextBlob

train = converterCSVToTextBlob()
classifier = NaiveBayesClassifier(train)

translator = GoogleTranslator(source='pt', target='en')


url = ('https://newsapi.org/v2/everything?'
       'q=ibovespa&'
       'language=pt&'
       'sortBy=popularity&'
       'apiKey=04f7c388507549e0984bf138d88af82e')


response = requests.get(url)
page1 = response.json()['articles']

response = requests.get(url + '&page=2')
page2 = response.json()['articles']

articles = np.concatenate((page1, page2))

posTotals = 0
negTotals = 0

for article in articles:
    print('\n\n')
    title = article['title']
    description = article['description']
    content = article['content']

    text = title + " " + description
    translation = translator.translate(text=text)
    print(text)
    prob_dist = classifier.prob_classify(translation)
    pos_prob = round(prob_dist.prob("pos"), 2)
    neg_prob = round(prob_dist.prob("neg"), 2)
    print(prob_dist.max(), "pos_prob: ", pos_prob, "neg_prob: ", neg_prob)

    positiveCount, negativeCount, positiveWords, negativeWords = countWords(
        lmdict, text)

    # print("Palavras positivas => ", positiveWords)
    print("Quantidade de palavras positivas => ",
          positiveCount)

    # print("\nPalavras negativas => ", negativeWords)
    print("Quantidade de palavras negativas => ",
          negativeCount)

    posTotals += positiveCount
    negTotals += negativeCount

print("Total de palavras positivas: ", posTotals)
print("Total de palavras negativas: ", negTotals)
