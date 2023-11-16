from dash import Dash, html
from . import umap_plot, drop_down
from .. import ids
import pandas as pd


def create_layout(app: Dash, umap_df: pd.DataFrame, expr_df: pd.DataFrame) -> html.Div:
    return html.Div(
    children=[
        html.H1("Interactive UMAP", className="title"),
        html.Hr(),
        html.Div(
            className="main-block",
            children = [
                html.Div(
                    className="umap-container",
                    id = ids.ID_UMAP,
                    children=[
                        umap_plot.render(app, umap_df, expr_df)
                        ]
                ),
                html.Div(
                    className="dropdown-container",
                    children=[
                        drop_down.render(app, expr_df)
                        ]
                ),
                html.Button(
                    className="dropdown-button",
                    id = ids.ID_DROPDOWN_BUTTON,
                    children=["Reset"]
                ),
            ]           
        )
    ]
)