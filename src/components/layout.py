from dash import Dash, html, dcc
from . import umap_plot, drop_down, upload, example_button
from .. import ids
import pandas as pd

def create_layout(app: Dash, data=None) -> html.Div:
    return html.Div(
    children=[
        dcc.Store(id=ids.ID_UMAP_DATA, data=data),
        html.H1("Interactive UMAP", className="title"),
        html.Hr(),
        html.Div(
            className="main-block",
            children = [
                html.Div(
                    className="umap-container",
                    id = ids.ID_UMAP,
                    children=[
                        umap_plot.render(app)
                        ]
                ),
                html.Div(
                    className="dropdown-container",
                    children=[
                        drop_down.render(app)
                        ]
                ),
                html.Div(
                    className="upload-div",
                    children=[
                            html.Button(
                                className="dropdown-button",
                                id = ids.ID_DROPDOWN_BUTTON,
                                children=["Reset"]
                            ),
                        ]
                ),
                html.Div(
                    className="upload-div",
                    children=[
                        upload.render(app),
                        ]
                ),
                html.Div(
                    className="upload-div",
                    children=[
                        example_button.render(app),
                        ]
                )
                
            ]           
        )
    ]
)