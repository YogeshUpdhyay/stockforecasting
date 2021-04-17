import dash_bootstrap_components as dbc
import dash_html_components as html

from .plot import generate_forecast_graph

def get_forecast_detail(accuracy, graph):
    forecast_detail = dbc.Col(
        dbc.Container([
            dbc.Row(html.H3("Error Margin: {}".format(accuracy)), align='center', no_gutters=True),
            generate_forecast_graph(graph)
        ]),
        align="center"
    )
    return forecast_detail