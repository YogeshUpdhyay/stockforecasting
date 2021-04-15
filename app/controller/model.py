import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.svm import SVR
import plotly.express as px
from datetime import date, timedelta, datetime
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split, GridSearchCV

from .stock import Stock

class Forecasting:
    def __init__(self, ticker):
        # fetching stock data
        stock = Stock(ticker)
        if not stock.get_data():
            raise ConnectionError
        self.data = stock.df

    def preprocess(self):
        self.data["Date"] = pd.to_datetime(self.data["Date"], format='%d%b%Y:%H:%M:%S.%f')
        start_date = self.data["Date"][0].date()
        X = np.array([(curr_date.date() - start_date).days for curr_date in self.data["Date"]])
        X = X.reshape(-1, 1)

        Y = self.data['Close']

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, shuffle=False)
        return X_train, X_test, Y_train, Y_test

    def tune_hyperparamters(self, x, y):
        gsc = GridSearchCV(
            estimator=SVR(kernel='rbf'),
            param_grid={
                'C': [0.001, 0.01, 0.1, 1, 100, 1000],
                'epsilon': [
                    0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10,
                    50, 100, 150, 1000
                ],
                'gamma': [0.0001, 0.001, 0.005, 0.1, 1, 3, 5, 8, 40, 100, 1000]
            },
            cv=5,
            scoring='neg_mean_absolute_error',
            verbose=0,
            n_jobs=-1
        )

        grid_result = gsc.fit(x, y)
        best_params = grid_result.best_params_
        return best_params

    def train(self):
        print("Preprocessing Data")
        x_train, x_test, y_train, y_test = self.preprocess()

        print("Tuning Parameters")
        best_params = self.tune_hyperparamters(x_train, y_train)

        model = SVR(
            kernel='rbf',
            C=best_params["C"],
            epsilon=best_params["epsilon"],
            gamma=best_params["gamma"],
            max_iter=-1
        )

        print("Training Model")
        model.fit(x_train, y_train)

        accuracy = self.validate(x_test, y_test, model)

        return model, accuracy

    def validate(self, x_test, y_test, model):
        y_pred = model.predict(x_test)
        accuracy = mean_absolute_error(y_test, y_pred)
        return accuracy

    def forecast(self, n_days):
        # training and validating a model
        model, accuracy = self.train()

        # predicting the prices for the upcoming days
        x_test = np.arange(90, 90 + int(n_days), 1)
        dates = [(date.today() + timedelta(day)) for day in x_test.tolist()]
        x_test = x_test.reshape(-1, 1)
        y_pred = model.predict(x_test)

        return dates, y_pred, accuracy








def prediction(stock, n_days):

    df = yf.download(stock, period='60d')
    df.reset_index(inplace=True)
    df['Day'] = df.index
    print(df)

    # days = list()
    # for i in range(len(df.Day)):
    #     days.append([i])

    # # Splitting the dataset

    # X = days
    # Y = df[['Close']]

    # x_train, x_test, y_train, y_test = train_test_split(X,
    #                                                     Y,
    #                                                     test_size=0.1,
    #                                                     shuffle=False)

    # gsc = GridSearchCV(
    #     estimator=SVR(kernel='rbf'),
    #     param_grid={
    #         'C': [0.001, 0.01, 0.1, 1, 100, 1000],
    #         'epsilon': [
    #             0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10,
    #             50, 100, 150, 1000
    #         ],
    #         'gamma': [0.0001, 0.001, 0.005, 0.1, 1, 3, 5, 8, 40, 100, 1000]
    #     },
    #     cv=5,
    #     scoring='neg_mean_absolute_error',
    #     verbose=0,
    #     n_jobs=-1)

    # y_train = y_train.values.ravel()
    # y_train
    # grid_result = gsc.fit(x_train, y_train)
    # best_params = grid_result.best_params_
    # best_svr = SVR(kernel='rbf',
    #                C=best_params["C"],
    #                epsilon=best_params["epsilon"],
    #                gamma=best_params["gamma"],
    #                max_iter=-1)

    # rbf_svr = best_svr

    # rbf_svr.fit(x_train, y_train)

    # output_days = list()
    # for i in range(1, n_days):
    #     output_days.append([i + x_test[-1][0]])

    # dates = []
    # current = date.today()
    # for i in range(n_days):
    #     current += timedelta(days=1)
    #     dates.append(current)

    # fig = go.Figure()
    # fig.add_trace(
    #     go.Scatter(
    #         x=dates,  # np.array(ten_days).flatten(), 
    #         y=rbf_svr.predict(output_days),
    #         mode='lines+markers',
    #         name='data'))
    # fig.update_layout(
    #     title="Predicted Close Price of next " + str(n_days - 1) + " days",
    #     xaxis_title="Date",
    #     yaxis_title="Closed Price",
    #     # legend_title="Legend Title",
    # )

    # return fig

# prediction("AAPL", 5)