from dash import Dash, html, dcc
from src.components.layout import create_layout
from src.dataloader import load_data
from src.variables import DATA_FOLDER
from dash_bootstrap_components.themes import BOOTSTRAP

app = app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
server = app.server

umap_data = load_data("umap_data.feather")
expr_data = load_data("expression_data.feather")
print(umap_data.shape, expr_data.shape)

app.title = "Interactive UMAP"
app.layout = create_layout(app, umap_data, expr_data)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)