import dash
from datetime import date, timedelta
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from ..app import app
from .tickerdetails import generate_ticker_details
from .plot import generate_ticker_graph
from .forecastform import forecast_form
from ..controller.stock import Stock

stock_form = dbc.Row(
    [
        dbc.Col(dbc.Input(placeholder="TICKR", id="tickr-input", className="mr-3"), align="center", width=3),

        dbc.Col(dcc.DatePickerRange(
            id='stock-date-picker-range',
            min_date_allowed=(date.today() - timedelta(days = 3*365)),
            max_date_allowed=date.today(),
            initial_visible_month=date.today()
        )),
        
        dbc.Col(dbc.Button("Filter", color="primary", id="form-submit"), width="3", align="center"),
    ],
    no_gutters=False,
    className="ml-auto flex-nowrap mt-md-0",
    align="end",
)

@app.callback(
    Output("main-view", "children"),
    [
        Input("form-submit", "n_clicks"),
        Input("forecast-submit", "n_clicks")
    ],
    [
        State("tickr-input", "value"),
        State("stock-date-picker-range", "start_date"),
        State("stock-date-picker-range", "end_date")
    ],
)
def form_submit(stock_click, forecast_click, tickr, start_date, end_date):

    # fetching context to determine which button triggered callback
    ctx = dash.callback_context
    trigger = ctx.triggered[0]['prop_id'].split('.')[0]

    if stock_click:
        if tickr:
            if start_date and end_date:
                stock = Stock(tickr, start_date, end_date)
            elif start_date:
                stock = Stock(tickr, start_date)
            else:
                stock = Stock(tickr)
            
            info = stock.get_info()
            ticker_detail = generate_ticker_details(info)

            open_close_graph, moving_avg_graph = stock.get_graphs()
            ticker_graph = generate_ticker_graph(open_close_graph)

            return dbc.Row([ticker_detail, ticker_graph], align="center", no_gutters=True)
        else:
            return dbc.Alert("No TICKER found!!", color="primary", dismissable=True)
    else:
        raise PreventUpdate

    if forecast_click:
        if tickr:
            if start_date and end_date:
                stock = Stock(tickr, start_date, end_date)
            elif start_date:
                stock = Stock(tickr, start_date)
            else:
                stock = Stock(tickr)
            
            info = stock.get_info()
            ticker_detail = generate_ticker_details(info)

            open_close_graph, moving_avg_graph = stock.get_graphs()
            ticker_graph = generate_ticker_graph(open_close_graph)

            return dbc.Row([ticker_detail, ticker_graph], align="center", no_gutters=True)
        else:
            return dbc.Alert("No TICKER found!!", color="primary", dismissable=True)
    else:
        raise PreventUpdate




