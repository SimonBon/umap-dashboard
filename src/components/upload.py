from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
from dash import Input, Output, State
from .. import ids
from ..data_utils import parse_content
from pathlib import Path
import base64
import io  

def render(app: Dash) -> html.Div:

    return html.Div(
        children=[
            dcc.Upload(
                id=ids.ID_UPLOAD,
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=False
            ),
            html.Div(id=ids.ID_UPLOAD_OUTPUT),
        ])
        

