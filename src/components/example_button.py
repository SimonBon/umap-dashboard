from dash import Dash, html
from .. import ids
# from .. import callbacks

def render(app: Dash) -> html.Button:
    
    button = html.Button(
            className="dropdown-button",
            id = ids.ID_EXAMPLE_BUTTON,
            children=["Example Data"]
    )
     
    return button

