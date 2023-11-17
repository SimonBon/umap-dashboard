from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd
from .. import ids
import json
from ..data_utils import json_to_df

def create_plot(data, color=None):
    
    if data is None:
        
        fig = go.Figure()
        
    else:
        
        try:
    
            fig = go.Figure(go.Scatter(
                    x=data["V1"], 
                    y=data["V2"], 
                    mode="markers",
                    marker=dict(
                        color=data[color] if color is not None else None,  # Use the 'color' column for marker colors
                        size=8,
                        line=dict(width=0.5, color='DarkSlateGrey'),
                    ),
                    # customdata=pd.DataFrame({"idx": filtered_df.index, "celltype": filtered_df["celltype"]}),  # Adding the index of the DataFrame as custom data
                    # hovertemplate='Celltype: %{customdata[1]}' # This will show the 'celltype' when you hover over a marker
                ))
        
        except Exception as e:
            print(e)
            return html.Div('There was an error processing this file.', className="error-message")
        
    fig.update_layout(
        margin=dict(
            l=20,
            r=20,
            b=20,
            t=40,
            pad=0
        )
    )
    
    return dcc.Graph(className="umap-object",
                     figure=fig,
        style=dict(height="100%", width="100%")
    )

def render(app: Dash) -> dcc.Graph:
    
    return create_plot(None)
    