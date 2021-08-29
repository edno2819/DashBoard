import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from app import app, api

image_card = dbc.Card(
    [
        dbc.CardBody(
            [   
                html.H4("Filtros", className="card-title"),
                html.Hr(),
                html.H6("Periodo:", className="card-text"),
                html.Div(id="the_alert", children=[]),
                html.B(),
                dcc.RangeSlider(
                                        min=0,
                                        max=10,
                                        step=None,
                                        marks={
                                            0: '26/05',
                                            3: '05/06',
                                            5: '07/06',
                                            7.65: '16/06',
                                            10: '29/06'
                                        },
                                        value=[3, 7.65],
                                        id='slider'
                                    ),
                html.Br(),
                html.Hr(),
                html.H6("Selecione a palavra chave:", className="card-text"),
                html.Br(),
                dcc.Input(id='input_palavra_chave'),

                html.Br(),
                html.Hr(),
                html.H6("Selecione os grupos:", className="card-text"),
                html.Br(),
                dcc.Dropdown(id='district_chosen', options=[{'label':'A TOCA DO COELHO', "value": 'A TOCA DO COELHO'}],
                             value=["A TOCA DO COELHO", "Pankow", "Spandau"], multi=True, style={"color": "#000000"}),

                html.Br(),
                html.Hr(),
                html.Button('Submit', id='submit-filter', n_clicks=0)
            ]
        ),
    ],
    color="light",
)

graph_card = dbc.Card(
    [   html.Hr(),
        dbc.CardBody(
            [
                html.H4("Gráfico de recorrência de temas", className="card-title", style={"text-align": "center"}),
                dcc.Graph(id='line_chart', figure={}),

            ]
        ),
    ],
    color="light",
)
 

# *********************************************************************************************************
frequencia_layout = html.Div([
    dbc.Row([dbc.Col(image_card, width=4), dbc.Col(graph_card, width=8)], justify="around")
])
# *********************************************************************************************************

@app.callback(
    [Output("line_chart", "figure"), Output("the_alert", "children")],
    [Input("submit-filter", "n_clicks"), Input("district_chosen", "value"), Input('slider', 'value')],
    [State("input_palavra_chave", "value")]
)
def update_graph_card(n_clicks, values, data, palavra):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'n_clicks' in changed_id:
        data = [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],

        figure={
            'data': data,
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
        return figure, dash.no_update
    return {}

    
