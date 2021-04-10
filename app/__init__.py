from .app import app
from .index import index

def make_app():
    app.layout = index
    return app

