from dash import Dash
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP

app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
server = app.server

data = None

app.title = "Interactive UMAP"
app.layout = create_layout(app)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
