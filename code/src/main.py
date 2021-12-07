import requests
import numpy as np
import datetime
import graphs
import constants
from correlation import generateCorrelationForStocks
from deep_translator import (GoogleTranslator)
from stockPrice import getStockDetails
from textblob.classifiers import NaiveBayesClassifier
from csvConverter import converterCSVToTextBlob


def getArticles():
    startDate = (datetime.datetime.now() -
                 datetime.timedelta(days=constants.WEEK_DAYS)).strftime("%Y-%m-%d")
    endDate = datetime.datetime.now().strftime("%Y-%m-%d")

    url = ('https://newsapi.org/v2/everything?'
           'q=ibovespa&'
           'language=pt&'
           'sortBy=popularity&'
           'from='+startDate+'&'
           'to='+endDate+'&'
           'apiKey=04f7c388507549e0984bf138d88af82e')

    response = requests.get(url)
    page1 = response.json()['articles']

    return np.concatenate((page1, []))


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

positiveProbabilityNews = np.float32(sortedArticles[:, 3])
variations = getStockDetails()

graphs.createGraph('Variações das ações', 'Dia da ação',
                   'Variação(%)', np.array(variations) * 100)
graphs.createGraph('Variações das notícias', 'Dia da notícia',
                   'Probabilidade da notícia ser positiva(%)', np.array(positiveProbabilityNews) * 100)
graphs.createGraph('Gráfico de Correlação', 'Correlação', 'Valor obtido da correlação',
                   np.array(generateCorrelationForStocks(variations, positiveProbabilityNews)) * 100)
