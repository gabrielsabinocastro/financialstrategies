import pandas as pd
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta as rltd


def rolVol(dReturns, daywindow): #TODO Volatility Rolling
    """
    Recebe um pdDataFrame com os retornos diários e um número natural de intervalo e retorna.
    """
    temp = dReturns.rolling(window=daywindow).std()
    return temp

def clusterVol(dReturns, window, weight): #TODO Volatility Cluster
    """
    Calcula uma lista de cluster de volatlilidade.
    """
    pass


def distrReturns(dReturns): #TODO Distribuition of Returns
    """
    Calcula uma lista com a distribuição dos retornos.
    """
    pass

def maxDDown(dReturns): #TODO maximum drawdown

    pass

def benchmarkBeta(dReturns, benchmarkReturns): #TODO Linear Beta
    #devolver uma tupla com o angular da regressão linear e o r^2
    #observar a quantidade de dias, anual, mensal...

    pass

def ewmadVol(dReturns, window, lamb = 0.94):
    """
    Recebe:
        dReturns (Pandas.DataFrame / .Series): retornos diários.
        window (int): número no intervalo da série de retornos, para o range da volatilidade.
        lam (float): parâmetro do decaimento exponencial
    Devolve:
        Pandas.Series: volatilidade diária EWMA.
    """

    temp = pd.DataFrame(dReturns)
    temp = temp[len(dReturns)- window:]
    temp['Expo'] = np.arange(window-1,-1,-1)
    temp = temp.apply(lambda x: (x**2)* (1 - lamb) * (lamb) **(x['Expo']) , axis=1)
    temp.drop('Expo', axis=1, inplace=True)

    return np.sqrt(temp.sum())

def rolewmaVol(dReturns, window, lamb = 0.94):
    # (sigma^2)_t =  (1 - lambda) * (r^2)_t-1  +  lambda * (sigma^2)_t-1
    temp = 0

    pass