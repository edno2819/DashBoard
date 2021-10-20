import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app

from tabs.frequencia import frequencia_layout
from tabs.cloud_words import cloud_words_layout
from tabs.msg_table import datatable_layout
import webbrowser


webbrowser.open("http://127.0.0.1:8050/")


#analy = Analytics()

# our app's Tabs *********************************************************
app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Mentions", tab_id="cloud_words_layout", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="Trends", tab_id="frequencia_layout", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="Frequencia", tab_id="datatable_layout", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
            ],
            id="tabs",
            active_tab="tab-mentions",
        ),
    ], className="mt-3"
)

app.layout = dbc.Container([
    html.Hr(),
    dbc.Row(dbc.Col(html.H1("ANALISE TELEGRAM DASHBOARD",
                            style={"textAlign": "center"}), width=12)),
    html.Hr(),
    dbc.Row(dbc.Col(app_tabs, width=16), className="mb-3"),
    html.Div(id='content', children=[])

])

@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")]
)
def switch_tab(tab_chosen):
    if tab_chosen == "cloud_words_layout":
        return cloud_words_layout
    elif tab_chosen == "frequencia_layout":
        return frequencia_layout
    elif tab_chosen == "datatable_layout":
        return datatable_layout

    return frequencia_layout



if __name__=='__main__':
    app.run_server(debug=True)