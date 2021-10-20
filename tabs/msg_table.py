import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')


graph_card = dbc.Card(
    [   html.Hr(),
        dbc.CardBody(
            [
                html.H4("Gráfico de recorrência de temas", className="card-title", style={"text-align": "center"}),
                dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                page_current= 0,
                page_size= 10,
                page_action="native",
                filter_action="native",
                style_cell={
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                },

                #legenda das linhas
                tooltip_data=[
                    {
                        column: {'value': str(value), 'type': 'markdown'}
                        for column, value in row.items()
                    } for row in df.to_dict('records')
                ],
                tooltip_duration=None,
                #Width of columns
                style_cell_conditional=[
                    {'if': {'column_id': 'STATE'},
                    'width': '30%'},
                    {'if': {'column_id': 'Region'},
                    'width': '30%'},
                ]
                )


            ]
        ),
    ],
    color="light",
)
 

# *********************************************************************************************************
datatable_layout = html.Div([
    dbc.Row([dbc.Col(graph_card, width=12)], justify="around")
])
# *********************************************************************************************************


    
