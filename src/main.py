import requests
import numpy as np
from deep_translator import (GoogleTranslator)
from textblob.classifiers import NaiveBayesClassifier
from csvConverter import converterCSVToTextBlob
import datetime


def getArticles():
    WEEK_DAYS = 7
    startDate = (datetime.datetime.now() -
                 datetime.timedelta(days=WEEK_DAYS)).strftime("%Y-%m-%d")
    endDate = datetime.datetime.now().strftime("%Y-%m-%d")

    url = ('https://newsapi.org/v2/everything?'
           'q=ibovespa&'
           'language=pt&'
           'sortBy=popularity&'
           'from='+startDate+'&'
           'to='+endDate+'&'
           'apiKey=04f7c388507549e0984bf138d88af82e')
    print(url)

    response = requests.get(url)
    page1 = response.json()['articles']

    response = requests.get(url + '&page=2')
    page2 = response.json()['articles']

    return np.concatenate((page1, page2))


def formatArticles(articles):
    formattedArticles = []
    for article in articles:
        print('\n\n')
        title = article['title']
        description = article['description']
        publishedAt = article['publishedAt']
        print(publishedAt)
        text = ''

        if(title):
            text = title

        if(description):
            text = text + " " + description

        translation = translator.translate(text=text)
        print(text)
        prob_dist = classifier.prob_classify(translation)
        pos_prob = round(prob_dist.prob("pos"), 2)
        neg_prob = round(prob_dist.prob("neg"), 2)
        print(prob_dist.max(), "pos_prob: ", pos_prob, "neg_prob: ", neg_prob)
        formattedArticles.append(
            (publishedAt, text, prob_dist.max(), pos_prob, neg_prob))
    return formattedArticles


train = converterCSVToTextBlob()
classifier = NaiveBayesClassifier(train)
translator = GoogleTranslator(source='pt', target='en')
articles = getArticles()
formattedArticles = formatArticles(articles)
sortedArticles = np.array(sorted(formattedArticles))

pos_probs = sortedArticles[:, 3]
print(pos_probs)
