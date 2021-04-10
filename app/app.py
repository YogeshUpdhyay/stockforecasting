import dash
import dash_bootstrap_components as dbc

def create_app():
    # creating app instance
    app = dash.Dash(
        __name__, 
        external_stylesheets=[dbc.themes.SUPERHERO],
        title="Stock Forecasting",
        assets_folder="assets"
    )
    return app

app = create_app()