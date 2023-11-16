from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd
from .. import ids

def create_plot(umap_df, expr_df, color=None):
    
    fig = go.Figure(go.Scatter(
            x=umap_df["V1"], 
            y=umap_df["V2"], 
            mode="markers",
            marker=dict(
                color=expr_df[color] if color is not None else None,  # Use the 'color' column for marker colors
                size=8,
                line=dict(width=0.5, color='DarkSlateGrey'),
            ),
            # customdata=pd.DataFrame({"idx": filtered_df.index, "celltype": filtered_df["celltype"]}),  # Adding the index of the DataFrame as custom data
            # hovertemplate='Celltype: %{customdata[1]}' # This will show the 'celltype' when you hover over a marker
        ))
    
    fig.update_layout(
        margin=dict(
            l=20,
            r=20,
            b=20,
            t=100,
            pad=0
        )
    )
    
    return dcc.Graph(className="umap-object",
                     figure=fig,
        style=dict(height="100%", width="100%")
    )

def render(app: Dash, umap_df: pd.DataFrame, expr_df: pd.DataFrame) -> dcc.Graph:
    
    @app.callback(
        Output(ids.ID_UMAP, 'children'),
        Input(ids.ID_DROPDOWN, 'value')
    )
    def change_coloring(color):
        
        plot = create_plot(umap_df, expr_df, color)
        
        return plot
    
    return create_plot(umap_df, expr_df)
    