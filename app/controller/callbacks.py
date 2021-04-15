import dash
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from ..app import app
from ..components.tickerdetails import generate_ticker_details
from ..components.plot import generate_ticker_graph
from .stock import Stock
from .model import Forecasting


def get_ticker_details(tickr, start_date, end_date):
    if start_date and end_date:
        stock = Stock(tickr, start_date, end_date)
    elif start_date:
        stock = Stock(tickr, start_date)
    else:
        stock = Stock(tickr)
    
    info = stock.get_info()
    ticker_detail = generate_ticker_details(info)

    return ticker_detail

@app.callback(
    Output("main-view", "children"),
    [
        Input("form-submit", "n_clicks"),
        Input("forecast-submit", "n_clicks")
    ],
    [
        State("tickr-input", "value"),
        State("stock-date-picker-range", "start_date"),
        State("stock-date-picker-range", "end_date"),
        State("forecast-days", "value")
    ],
)
def form_submit(stock_click, forecast_click, tickr, start_date, end_date, forecast_days):

    # fetching context to determine which button triggered callback
    ctx = dash.callback_context
    trigger = ctx.triggered[0]['prop_id'].split('.')[0]

    if stock_click and trigger == "form-submit":
        if tickr:
            ticker_detail = get_ticker_details(tickr, start_date, end_date)

            open_close_graph, moving_avg_graph = stock.get_graphs()
            ticker_graph = generate_ticker_graph(open_close_graph)

            return dbc.Row([ticker_detail, ticker_graph], align="center", no_gutters=True)
        else:
            return dbc.Alert("No TICKER found!!", color="primary", dismissable=True)
    elif forecast_click and trigger == "forecast-submit":
        print("here")
        if tickr:
            ticker_detail = get_ticker_details(tickr, start_date, end_date)

            forecaster = Forecasting(tickr)
            dates, y_pred, accuracy = forecaster.forecast(forecast_days)

            return dbc.Row([ticker_detail, ticker_graph], align="center", no_gutters=True)
        else:
            return dbc.Alert("No TICKER found!!", color="primary", dismissable=True)
    else:
        raise PreventUpdate
