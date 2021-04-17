import dash_bootstrap_components as dbc
import dash_core_components as dcc


def generate_ticker_graph(graph):
    ticker_graph = dbc.Col(
        dcc.Graph(figure=graph),
        width=7,
        align="center"
    )
    return ticker_graph

def generate_forecast_graph(graph):
    forecast_graph = dbc.Col(
        dcc.Graph(figure=graph),
        width=7,
        align="center"
    )
    return forecast_graph
