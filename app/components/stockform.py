from datetime import date, timedelta
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from ..app import app
from .tickerdetails import generate_ticker_details
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
    # Output("ticker-detail", "children"),
    [
        Output("ticker-detail", "children"),
        Output("ticker-graph", "children")
    ],
    [Input("form-submit", "n_clicks")],
    [
        State("tickr-input", "value"),
        State("stock-date-picker-range", "start_date"),
        State("stock-date-picker-range", "end_date")
    ],
)
def form_submit(clicks, tickr, start_date, end_date):
    if clicks:
        if tickr:
            if start_date and end_date:
                stock = Stock(tickr, start_date, end_date)
                info = stock.get_info()
                # moving average graph to be implemented later with forecasting form
                close_graph, moving_avg_graph = stock.get_graphs()
                return [generate_ticker_details(info), forecast_form], [dcc.Graph(figure=close_graph)]
            elif start_date:
                stock = Stock(tickr, start_date)
                info = stock.get_info()
                close_graph, moving_avg_graph = stock.get_graphs()
                return [generate_ticker_details(info), forecast_form], [dcc.Graph(figure=close_graph)]
            else:
                stock = Stock(tickr)
                info = stock.get_info()
                close_graph, moving_avg_graph = stock.get_graphs()
                return [generate_ticker_details(info), forecast_form], [dcc.Graph(figure=close_graph)]
        else:
            return dbc.Alert("No TICKER found!!", color="primary", dismissable=True), None
    else:
        raise PreventUpdate



