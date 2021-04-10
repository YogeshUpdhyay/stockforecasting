import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .components.navbar import navbar
from .components.tickerdetails import ticker_detail
from .components.forecastform import forecast_form


index = html.Div([
    navbar,
    dbc.Row([
        dbc.Col([
            ticker_detail,
            forecast_form
        ],
        width=5),
        dbc.Col(
            html.Div(),
            width=7
        )
    ],
    align="center")
])