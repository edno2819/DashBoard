import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from app import app
from wordcloud import WordCloud


image_card = dbc.Card(
    [
        dbc.CardBody(
            [   
                html.H4("Filtros", className="card-title"),
                html.Br(),
                html.Hr(),
                html.H6("Selecione a palavra chave:", className="card-text"),
                html.Br(),
                html.Hr(),
                html.H6("Selecione os grupos:", className="card-text"),
                html.Br(),
                dcc.Dropdown(id='groups', options=[{'label':'A TOCA DO COELHO', "value": 'A TOCA DO COELHO'}],
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
                dcc.Graph(id='wordcloud', figure={}, config={'displayModeBar': False}),
            ]
        ),
    ],
    color="light",
)
 

# *********************************************************************************************************
cloud_words_layout = html.Div([
    dbc.Row([dbc.Col(image_card, width=4), dbc.Col(graph_card, width=8)], justify="around")
])
# *********************************************************************************************************


# Word Cloud **********************************************************************************************
@app.callback(
    [Output('wordcloud','figure')],
    [Input('groups','value'),Input('submit-filter','n_clicks')],
    [State('upload-data', 'last_modified')]
)
def update_pie(list_of_contents, start_date, end_date):
    if list_of_contents is not None:
        dff = ['teste']
        my_wordcloud = WordCloud(
            background_color='white',
            height=275
        ).generate(' '.join(dff))

        fig_wordcloud = px.imshow(my_wordcloud, template='ggplot2',
                                title="Total Connections by Position")
        fig_wordcloud.update_layout(margin=dict(l=20, r=20, t=30, b=20))
        fig_wordcloud.update_xaxes(visible=False)
        fig_wordcloud.update_yaxes(visible=False)

        return fig_wordcloud
