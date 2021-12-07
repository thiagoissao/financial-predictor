from pandas_datareader import data as web
import datetime
import numpy as np
import constants


def getStockDetails():
    startDate = (datetime.datetime.now() -
                 datetime.timedelta(days=constants.STOCK_QUANTITY_DAYS)).strftime("%m-%d-%Y")
    endDate = datetime.datetime.now().strftime("%m-%d-%Y")

    df = web.DataReader(f'^BVSP', data_source='yahoo',
                        start=startDate, end=endDate)
    opens = np.array(df['Open'])
    closes = np.array(df['Close'])

    variations = []
    for i in range(len(opens)):
        variations.append((closes[i] - opens[i]) / opens[i])

    return variations[len(closes)-constants.NUMBER_OF_VARIATIONS:len(closes)]
