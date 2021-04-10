import datetime
from datetime import date
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from ..app import app
from .stockform import stock_form

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# navbar component
navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Stock Forecasting", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/"
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(stock_form, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

