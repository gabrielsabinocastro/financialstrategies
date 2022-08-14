import yfinance as yf
import pandas as pd



class DataYFinance():
    """
    Trata e padroniza dados do Yahoo Finance, além de prover algumas métricas básicas
    """
    def __init__(self, tickers):
        """
        Parâmetro:
            tickers (array de strings): códigos para ativos bando de dados YahooFinance.

        """
        super().__init__()
        self.tickers = tickers
    
    def getAdjclose(self, startDate, endDate):
        """
        Função que recebe uma lista de tickers e retorna um dataframe com os preços 
        ajustados de cada um dos tickers, com base nos dados extraídos do YahooFinance.
        Recebe:
            startDate (objeto datetime.date ou string 'YYYY-MM-DD'): data mais antiga para a série.
            endDate (objeto datetime.date ou string 'YYYY-MM-DD'): data mais recente para a série.
        Devolve:
            Pandas.DataFrame: dataframe com os preços diários ajustados.        
        """
        
        df = yf.download(self.tickers, startDate, endDate)
        df = df["Adj Close"]
        
        return df

    def mReturns(self, adjclose): #TODO adapatar para DataFrame, funciona epanas com DataSeries
        """
        Recebe:
            adjclose (Pandas.DataFrame / .Series): preços diários ajustados.
        Devolve:
            Pandas.DataFrame / .Series: dataframe/series com os retornos mensais.        
        """
        
        adjclose = adjclose.rename('Returns')
        temp = (adjclose.pct_change().dropna()).resample("M").apply(lambda x: ((1+x).prod()) - 1)
        temp.index = pd.to_datetime(temp.index, format="%Y%m").to_period('M')
        
        return temp

    def dReturns(self, adjclose): #TODO adapatar para DataFrame, funciona epanas com DataSeries
        """
        Recebe:
            adjclose (Pandas.DataFrame / .Series): preços diários ajustados.
        Devolve:
            Pandas.DataFrame / .Series: dataframe/series com os retornos diários.
        """
        
        adjclose = adjclose.rename('Returns')
        temp = adjclose.dropna().pct_change()
        
        return temp.dropna()
    
    def mVol(self, adjclose): #TODO adapatar para DataFrame, funciona epanas com DataSeries
        """
        Recebe:
            adjclose (Pandas.DataFrame / .Series): preços diários ajustados.
        Devolve:
            numpy.float64: volatilidade (simples) mensal.
        """
        
        temp = self.mReturns(adjclose).std()
        
        return temp

    def dVol(self, adjclose): #TODO adapatar para DataFrame, funciona epanas com DataSeries
        """
        Recebe:
            adjclose (Pandas.DataFrame / .Series): preços diários ajustados.
        Devolve:
            numpy.float64: volatilidade (simples) diária.
        """
        
        temp = self.dReturns(adjclose).std()
        
        return temp

    def aVol(self, adjclose): #TODO adapatar para DataFrame, funciona epanas com DataSeries
        """
        Recebe:
            adjclose (Pandas.DataFrame / .Series): preços diários ajustados.
        Devolve:
            numpy.float64: volatilidade (simples) anualizada.
        """
        
        temp = (252 ** (1/2)) * self.dVol(adjclose)
        
        return temp
    
    
