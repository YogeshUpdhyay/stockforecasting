import dash_bootstrap_components as dbc

forecast_form = dbc.Container(
    dbc.Col(
        [
            dbc.Row(dbc.Input(id="forecast-days", placeholder=5, className="mr-auto")),
            dbc.Row(dbc.Button("Forecast", id="forecast-submit", className="btn btn-info"))
        ],
        className="mt-auto"
    )
)