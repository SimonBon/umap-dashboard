from dash import Dash, html, dcc, ctx, callback
import plotly.graph_objects as go
import pandas as pd
from dash import Input, Output, State
from . import ids
from .data_utils import json_to_df
from .variables import DATA_FOLDER
import os
from .data_utils import parse_content
from .custom_errors import UnexpectedError
from .components.umap_plot import create_plot

@callback(
    Output(ids.ID_UMAP_DATA, 'data'),
    Output(ids.ID_UPLOAD_OUTPUT, 'children'),
    Input(ids.ID_EXAMPLE_BUTTON, 'n_clicks'),
    Input(ids.ID_UPLOAD, 'contents'),
    State(ids.ID_UPLOAD, 'filename'),
    prevent_initial_call=True)
def define_data(a: int, content, filename):
    
    trigger = ctx.triggered_id
  
    if trigger == ids.ID_EXAMPLE_BUTTON:
        
        data = pd.read_feather(os.path.join(DATA_FOLDER, "example.feather"))
        data = data.to_json(orient='split', date_format='iso')
        
        return data, None
        
    elif trigger == ids.ID_UPLOAD:
        
        if filename:

            data =  parse_content(content, filename)
            
            if isinstance(data, str):
                return None, data
            

            data = data.to_json(orient='split', date_format='iso')
            
            return data, f"Successfully loaded {filename}"
            
    else:
        raise UnexpectedError()
   
    
@callback(
    Output(ids.ID_DROPDOWN, "value"),
    Output(ids.ID_DROPDOWN, "placeholder"),
    Output(ids.ID_DROPDOWN, "options"),
    Input(ids.ID_DROPDOWN_BUTTON, "n_clicks"),
    Input(ids.ID_UMAP_DATA, "data"))
def reset_dropdown(_: int, data):
    
    if data is None:
    
        return None, 'Select Marker', {}
    
    data = json_to_df(data)
    
    columns = [x for x in data.columns if not x == "V1" and not x == "V2"]
    
    return None, 'Select Marker', [{"label": col, "value": col} for col in columns]

@callback(
    Output(ids.ID_UMAP, 'children'),
    Input(ids.ID_DROPDOWN, 'value'),
    Input(ids.ID_UMAP_DATA, 'data')
)
def change_plot(color, data):

    if data is not None:

        data = json_to_df(data)

    plot = create_plot(data, color)

    return plot