import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from ..app import app

forecast_form = dbc.Container(
    dbc.Col(
        [
            dbc.Row(dbc.Input(id="forecast-days", placeholder=5, className="mr-auto")),
            dbc.Row(dbc.Button("Forecast", id="forecast-submit", className="btn btn-info"))
        ],
        className="mt-auto"
    )
)