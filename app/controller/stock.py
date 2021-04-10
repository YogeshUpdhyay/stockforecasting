import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from datetime import date, timedelta

class Stock:
    def __init__(self, ticker, end_date: str = str(date.today()), start_date: str = str(date.today() - timedelta(days = 90))):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def get_info(self):
        try:
            info = yf.Ticker(self.ticker)
            info = {
                "name": info['longName'],
                "description": info["longBusinessSummary"],
                "city": info["city"],
                "state": info["state"],
                "country": info["country"],
                "logo_url": info["logo_url"]
            }
            return info
        except Exception as e:
            raise ConnectionError

    def get_graphs(self):
        if self.get_data():
            close_graph = self.close_graph()
            moving_avg_graph = self.moving_average_graph()
            return close_graph, moving_avg_graph
        else:
            raise ConnectionError

    def get_data(self):
        try:
            df = yf.download(
                tickers = self.ticker,
                start = self.start_date,
                end = self.end_date
            )
            df.reset_index(inplace=True)
            self.df = df
            return True

    def close_graph(self):
        fig = px.line(
            x=self.df['Date'],
            y=self.df['Close'],
            title="Close Price"
        )
        return fig

    def moving_average_graph(self):
        self.df['EWA_20'] = self.df['Close'].ewm(span=20, adjust=False).mean()
        fig = px.scatter(
            x=self.df['Date'],
            y=self.df['EWA_20'],
            title="Moving Averages"
        )
        return fig
    




stock = Stock("AAPL")
# stock.get_info()
print(stock.moving_average_graph())
