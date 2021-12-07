from pandas_datareader import data as web
import datetime
import numpy as np

WEEK_DAYS = 40


def getStockDetails():
    startDate = (datetime.datetime.now() -
                 datetime.timedelta(days=WEEK_DAYS)).strftime("%m-%d-%Y")
    endDate = datetime.datetime.now().strftime("%m-%d-%Y")

    df = web.DataReader(f'^BVSP', data_source='yahoo',
                        start=startDate, end=endDate)
    opens = np.array(df['Open'])
    closes = np.array(df['Close'])

    variations = []
    for i in range(len(opens)):
        variations.append((closes[i] - opens[i]) / opens[i])

    return(opens[len(opens)-7:len(opens)], closes[len(closes)-7:len(closes)], variations[len(closes)-20:len(closes)])


opens, closes, variations = getStockDetails()
print(opens)
print(closes)
print(variations, len(variations))
