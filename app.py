import dash
import dash_core_components as dcc
import pandas as pd
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from Visualization import (
    Overview,
    Sankey,
    SVA_Research,
    utils
)

layout=dict(
        height='800',
        #width='1000',
        #pad='200',
        font=dict(
        size=10
        ),
        )

################################ App ##################################
app = dash.Dash(__name__,meta_tags=[{"name": "viewport", "content": "width=device-width"}])
server = app.server

app.layout = html.Div(
    [dcc.Location(id='url', refresh=False), html.Div(id='page_content')]
)
app.config['suppress_callback_exceptions']=True


################################ Update App ##################################
@app.callback(Output('page_content', 'children'),
              [Input('url', 'pathname')])
def update_app(pathname):
    if pathname == "/Heroku_Deployment_v2/Visualization/Sankey":
        return Sankey.create_layout(app)
    elif pathname == "/Heroku_Deployment_v2/Visualization/SVA_Research":
        return SVA_Research.create_layout(app)
    else:
        return Overview.create_layout(app)


################################ Clear Filter- Dash Table##################
@app.callback(
    Output('LCA_Datatable', 'filter_query'),
    [Input('clear', 'n_clicks')],
    [State('LCA_Datatable', 'filter_query')],
)
def clearFilter(n_clicks, state):
    if n_clicks is None:
        return '' if state is None else state

    return ''


############################## Sankey Callbacks ############################
@app.callback(
    Output('LCA_Sankey', 'figure'),
    [Input('LCA_Datatable', "derived_virtual_data"),
     Input('LCA_Datatable', "derived_virtual_selected_rows")])
def update_graphs(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []
    dff = df if rows is None else pd.DataFrame(rows)


    data_trace = dict(
        type='sankey',
        domain=dict(
            x=[0, 1],
            y=[0, 1]
        ),
        hoverlabel=dict(
            bgcolor='rgba(255, 255, 230, 1.0)',
            align='auto',
            bordercolor='#000000',
            namelength=-1,
            font=dict(
                family='Helvetica',
                size=15,
                color='#000000'
            )),
        orientation="h",
        valueformat=".0f",
        textfont=dict(
            family="Arial Black",
            size=15,
            color='black'
        ),
        node=dict(
            pad=30,
            thickness=30,
            color=["#1F1B1B",
                   "#CA0000", "#FFFFF0", "#002147", "#e7f5fe", "#FFFAFA", "#660000", "#ffdd1a", "#156eb7", "#6115b7",
                   "#CA0000", "#FFFFF0", "#002147", "#e7f5fe", "#FFFAFA", "#660000", "#ffdd1a", "#156eb7", "#6115b7",
                   "#CA0000", "#FFFFF0", "#002147", "#e7f5fe", "#FFFAFA", "#660000", "#ffdd1a", "#156eb7", "#6115b7",
                   "#CA0000", "#FFFFF0", "#002147", "#e7f5fe", "#FFFAFA", "#660000", "#ffdd1a", "#156eb7", "#6115b7",
                   "#CA0000", "#FFFFF0", "#002147", "#e7f5fe", "#FFFAFA", "#660000", "#ffdd1a", "#156eb7", "#6115b7",
                   "#CA0000", "#FFFFF0", "#002147", "#e7f5fe", "#FFFAFA", "#660000", "#ffdd1a", "#156eb7", "#6115b7",
                   "#CA0000", "#FFFFF0", "#002147", "#e7f5fe", "#FFFAFA", "#660000", "#ffdd1a", "#156eb7", "#6115b7",
                   "#CA0000", "#FFFFF0", "#002147", "#e7f5fe", "#FFFAFA", "#660000", "#ffdd1a", "#156eb7", "#6115b7"],
            line=dict(
                width=0.5
            ),
            label=["High School",
                   "Enlisted", "School", "Work", "Work & School", "Work & Reserves", "School & Reserves",
                   "Retirement", "ROTC or Mil. Acad.", "Transfer Schools",
                   "Enlisted", "School", "Work", "Work & School", "Work & Reserves", "School & Reserves",
                   "Retirement", "ROTC or Mil. Acad.", "Transfer Schools",
                   "Enlisted", "School", "Work", "Work & School", "Work & Reserves", "School & Reserves",
                   "Retirement", "ROTC or Mil. Acad.", "Transfer Schools",
                   "Enlisted", "School", "Work", "Work & School", "Work & Reserves", "School & Reserves",
                   "Retirement", "ROTC or Mil. Acad.", "Transfer Schools",
                   "Enlisted", "School", "Work", "Work & School", "Work & Reserves", "School & Reserves",
                   "Retirement", "ROTC or Mil. Acad.", "Transfer Schools",
                   "Enlisted", "School", "Work", "Work & School", "Work & Reserves", "School & Reserves",
                   "Retirement", "ROTC or Mil. Acad.", "Transfer Schools",
                   "Enlisted", "School", "Work", "Work & School", "Work & Reserves", "School & Reserves",
                   "Retirement", "ROTC or Mil. Acad.", "Transfer Schools",
                   "Enlisted", "School", "Work", "Work & School", "Work & Reserves", "School & Reserves",
                   "Retirement", "ROTC or Mil. Acad.", "Transfer Schools"],
        ),
        link=dict(
            source=dff['source'].dropna(axis=0, how='any'),
            target=dff['target'].dropna(axis=0, how='any'),
            value=dff['value'].dropna(axis=0, how='any'),
            color="rgba(140, 140, 140, .1)",
            label=dff['label'].dropna(axis=0, how='any'),
        )
    ),
    figure = {
        'data': data_trace,
        'layout': layout
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)