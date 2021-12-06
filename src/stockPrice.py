from pandas_datareader import data as web
import datetime
import numpy as np

WEEK_DAYS = 7


def getLastStockPrice():
    startDate = (datetime.datetime.now() -
                 datetime.timedelta(days=WEEK_DAYS)).strftime("%m-%d-%Y")
    endDate = datetime.datetime.now().strftime("%m-%d-%Y")

    print(startDate, endDate)
    # vamos pegar cotação do Indice e de Petrobras

    df = web.DataReader(f'^BVSP', data_source='yahoo',
                        start=startDate, end=endDate)
    opens = np.array(df['Open'])
    closes = np.array(df['Close'])

    lastOpen = opens[len(opens) - 1]
    lastClose = closes[len(closes) - 1]
    return(lastOpen, lastClose)


print(getLastStockPrice())
