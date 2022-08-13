import yfinance as yf
import pandas as pd



class DataYFinance():
    """
    Trata e padroniza dados do Yahoo Finance, além de prover algumas métricas básicas
    """
    def __init__(self, tickers):
        """
        Parâmetros:
            tickers (array de strings): ativos 
        """
        super().__init__()
        self.tickers = tickers
    
    def getAdjclose(self, startDate, endDate):
        """
        Função que recebe uma lista de tickers e retorna um dataframe com os preços 
        ajustados de cada um dos tickers, com base nos dados extraídos do YahooFinance.
        startDate: data mais antiga
        endDate: data mais recente
        """
        df = yf.download(self.tickers, startDate, endDate)
        df = df["Adj Close"]
        return df

    def mReturns(self, adjclose):
        """
        para dataframe com retornos mensais.
        """
        temp = (adjclose.pct_change().dropna()).resample("M").apply(lambda x: ((1+x).prod()) - 1)
        temp.index = pd.to_datetime(temp.index, format="%Y%m").to_period('M')
        return temp

    def dReturns(self, adjclose):
        """
        para retornos diários.
        """
        temp = adjclose.dropna().pct_change()
        return temp.dropna()
    
    def mVol(self, adjclose):
        temp = self.mReturns(adjclose).std()
        return temp

    def dVol(self, adjclose):
        temp = self.dReturns(adjclose).std()
        return temp

    def aVol(self, adjclose):
        temp = (252 ** (1/2)) * self.dVol(adjclose)
        return temp
    
    
