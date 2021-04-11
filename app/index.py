import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .components.navbar import navbar
from .components.tickerdetails import generate_ticker_details
from .components.forecastform import forecast_form


index = html.Div([
    navbar,
    dbc.Row([
        dbc.Col(
            html.Div(id="ticker-detail"),
            width=5,
            align="center"
        ),
        dbc.Col(
            html.Div(id="ticker-graph"),
            width=7
        )
    ],
    align="center")
])