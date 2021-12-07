import csv


def converterCSVToTextBlob():
    path = '../data/dataset.csv'
    with open(path, 'r') as file:
        reader = csv.reader(file)
        train = []
        for row in reader:
            phrase = row[1]
            status = row[0]  # negative, neutral, positive
            if(status == 'negative'):
                train.append((phrase, 'neg'))
            if(status == 'positive'):
                train.append((phrase, 'pos'))
    return train
