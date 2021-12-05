from textblob import TextBlob
from translate import Translator
translator = Translator(from_lang='pt', to_lang='en')
# train = [
#     ('ibovespa fecha em queda', 'neg'),
#     ('ibovespa fecha em forte queda', 'neg'),
#     ('ibovespa renova mínima histórica', 'neg'),
#     ('Ibovespa cai e renova menor fechamento do ano com receios sobre Ômicron', 'neg'),

#     ('ibovespa fecha em alta', 'pos'),
#     ('ibovespa fecha em forte alta', 'pos'),
#     ('ibovespa renova máxima histórica', 'pos'),
# ]

# test = [
#     ('Ibovespa tem forte queda com temor global por nova variante do coronavírus', 'neg')
# ]

# cl = NaiveBayesClassifier(train)

# print(cl.classify(
#     'Ibovespa sobe e renova alta fechamento do ano com receios sobre Ômicron '))

translation = translator.translate(
    "Ibovespa sobe e renova alta fechamento do ano com receios sobre Ômicron ")
test = TextBlob(translation)
print(test.sentiment)
