import re
from dictionary import negate
from unidecode import unidecode


def isNot(word):
    if word.lower() in negate:
        return True
    else:
        return False


def countWords(dictionary, text):
    positiveCount = 0
    negativeCount = 0

    positiveWords = []
    negativeWords = []

    input_words = re.findall(
        r'\b([a-zA-Z]+n\'t|[a-zA-Z]+\'s|[a-zA-Z]+)\b', unidecode(text).lower())

    word_count = len(input_words)

    for i in range(0, word_count):
        if unidecode(input_words[i]) in dictionary['Negative']:
            negativeCount += 1
            negativeWords.append(input_words[i])
        if unidecode(input_words[i]) in dictionary['Positive']:
            if i >= 3:
                if isNot(input_words[i - 1]) or isNot(input_words[i - 2]) or isNot(input_words[i - 3]):
                    negativeCount += 1
                    negativeWords.append(input_words[i] + ' (with negation)')
                else:
                    positiveCount += 1
                    positiveWords.append(input_words[i])
            elif i == 2:
                if isNot(input_words[i - 1]) or isNot(input_words[i - 2]):
                    negativeCount += 1
                    negativeWords.append(input_words[i] + ' (with negation)')
                else:
                    positiveCount += 1
                    positiveWords.append(input_words[i])
            elif i == 1:
                if isNot(input_words[i - 1]):
                    negativeCount += 1
                    negativeWords.append(input_words[i] + ' (with negation)')
                else:
                    positiveCount += 1
                    positiveWords.append(input_words[i])
            elif i == 0:
                positiveCount += 1
                positiveWords.append(input_words[i])

    return (positiveCount, negativeCount, positiveWords, negativeWords)
