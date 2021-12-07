import numpy as np
import constants

news = [
    1.00,
    0.74,
    0.55,
    0.04,
    1.00,
    0.02,
    1.00,
    0.00,
    0.00,
    0.44,
    0.02,
    0.68,
    1.00,
    0.99,
    1.00,
    0.57,
    0.88,
    0.89,
    1.00,
    0.98
]

variations = [
    -0.000410,
    0.007177,
    0.004103,
    0.016389,
    -0.011750,
    -0.017191,
    -0.013984,
    -0.004119,
    0.005946,
    -0.008871,
    0.015070,
    0.008316,
    0.012410,
    -0.033891,
    0.005742,
    -0.008744,
    -0.011195,
    0.036523,
    0.000000,
    0.017798,
    -0.011195,
    0.036523,
    0.000000,
    0.017798
]


def generateCorrelationForStocks(variations, news):
    corrs = []
    for i in np.arange(constants.NUMBER_OF_CORRELATIONS):
        start = i
        end = i + constants.NUMBER_OF_NEWS
        range = np.arange(start, end)
        corr = np.corrcoef(news, np.take(variations, range))
        corrs.append(corr[0][1])
    return corrs
