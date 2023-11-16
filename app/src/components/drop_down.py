from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
from dash import Input, Output
from .. import ids

def render(app: Dash, df: pd.DataFrame) -> dcc.Dropdown:
    
    @app.callback(
        Output(ids.ID_DROPDOWN, "value"),
        Output(ids.ID_DROPDOWN, "placeholder"),
        Input(ids.ID_DROPDOWN_BUTTON, "n_clicks")
    )
    def reset_dropdown(_: int):
        return [None, 'Select Marker']
     
    print({col: col for col in df.columns})
     
    return dcc.Dropdown(
                id = ids.ID_DROPDOWN,
                    options=[
                        {"label": col, "value": col} for col in df.columns
                    ],
                placeholder='Select Marker',
                value=None,
                )