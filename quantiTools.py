import pandas as pd
import numpy as np


def movVol(dReturns, window):
    """
    Recebe um pdDataFrame com os retornos diários e um número natural de intervalo e retorna.
    """
    temp = dReturns.rolling(window=window).std()
    return temp