import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1("Dummy Dash App"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 5], 'y': [4, 1, 2, 6], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3, 4], 'y': [2, 4, 5, 7], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
