import dash_core_components as dcc
import dash_html_components as html

from .components.navbar import navbar


index = html.Div([
    navbar,
    html.Div(id='my-output')
])