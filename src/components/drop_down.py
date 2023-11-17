from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
from dash import Input, Output
from .. import ids
from ..data_utils import json_to_df

def render(app: Dash) -> dcc.Dropdown:
    
    return dcc.Dropdown(
                id = ids.ID_DROPDOWN,
                placeholder='Select Marker',
                value=None,
                )
