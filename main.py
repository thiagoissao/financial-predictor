import requests
import numpy as np
from dictionary import lmdict
from classification import countWords
from textblob import TextBlob
from deep_translator import (GoogleTranslator)

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

    text = title + " " + description + " " + content

    translation = translator.translate(text=title + " " + description)
    print(title + " " + description)
    print(TextBlob(translation).sentiment)

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
