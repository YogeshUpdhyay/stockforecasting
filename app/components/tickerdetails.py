import dash_bootstrap_components as dbc
import dash_html_components as html

# "name": info['longName'],
# "description": info["longBusinessSummary"],
# "city": info["city"],
# "state": info["state"],
# "country": info["country"],
# "logo_url": info["logo_url"]

ticker_detail = dbc.Container([
    dbc.Row([
        dbc.Col(html.Img(src="https://images.plot.ly/logo/new-branding/plotly-logomark.png", height="75px"), width=2, align="center"),
        dbc.Col(html.H1("Company Name", className="display-3"), width=10),
    ],
    no_gutters=True
    ),
    dbc.Row(
        dbc.Col(html.P("Description text"))
    ),
    dbc.Row([
        dbc.Col(html.P("Mumbai", className="text-muted")),
        dbc.Col(html.P("Maharashtra", className="text-muted")),
        dbc.Col(html.P("India", className="text-muted")),
    ])],
)