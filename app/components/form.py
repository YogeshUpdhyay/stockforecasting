import datetime
from datetime import date
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from ..app import app
from .plot import alerts

stock_form = dbc.Row(
    [
        dbc.Col(dbc.Input(placeholder="TICKR", id="tickr-input"), align="center"),

        dbc.Col(dcc.DatePickerRange(
            id='stock-date-picker-range',
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date.today(),
            initial_visible_month=date.today()
        )),
        
        dbc.Col(
            dbc.Button("Filter", color="primary", className="ml-2", id="form-submit"),
            width="auto",
            align="center"
        ),
    ],
    no_gutters=False,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="end"
)

@app.callback(
    Output("my-output", "children"),
    [Input("form-submit", "n_clicks")],
    [
        State("tickr-input", "value"),
        State("stock-date-picker-range", "start_date"),
        State("stock-date-picker-range", "end_date")
    ],
)
def form_submit(clicks, tickr, start_date, end_date):
    if clicks:
        return alerts

