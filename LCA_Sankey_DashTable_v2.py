import dash_table
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly
import pandas as pd



df = pd.read_csv("LSA_Sankey_Working.csv")
df.rename(columns={
    'Last_Loop_Name':'Current Decision Point',
    'Last_Loop_Number':'Number of Decision Points',
    'Highest_Rank_Earned': 'Highest Rank Earned',
    'Age_at_Military_Separation':'Age at Military Separation',
    'Age_at_Enlistment':'Age at Enlistment',
    'Current_Age':'Current Age',
    'Current_Military':'Current Military',
    'Q63':'Ethnicity',
    'Q65':'Gender',
    'Q67_3':'Edu lvl earned or planned',
    'Q71':'Current Income',
    'Q79':'Education Debt',
    'Branch_of_Service':'Branch of Service'}, inplace=True)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

layout =  dict(
        #title = "LCA",
        height = '600',
        width = '1850',
        pad= '200',
        font = dict(
          size = 10
        ),
        )
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#ffffff',
    'text': '#000000'
}

app.layout = html.Div([
    #Title Row
    html.Div(
        [
            html.H1(
                children="Student Veterans of America -- Life Cycle Atlas",
                    style={
                        'textAlign': 'center'
                    },
                className='twelve columns',
            )

        ],
        className='row'
    ),
    #Images Row
    html.Div([
        html.Div([
            html.Img(
                src="https://www.stripes.com/polopoly_fs/1.175627.1335454273!/image/3107706660.jpg_gen/derivatives/landscape_900/3107706660.jpg",
                style={
                    'height': '45%',
                    'width': '45%',
                    'marginLeft':'auto',
                    'marginRight':'auto'
                },
            ),
        ],style={'textAlign':'center'},
        className='six columns'),
        html.Div([
            html.Img(
                src="https://www.usveteransmagazine.com/wp-content/uploads/2017/04/pwc_charitablefoundation_logo.png",
                style={
                    'height': '25%',
                    'width': '20%',
                    'marginLeft': 'auto',
                    'marginRight': 'auto'
                },
            ),
        ],style={'textAlign':'center'},
        className='six columns')
    ],
    className='row'),
    html.Div([
    html.Button(id='clear', children='Clear filter'),
    ],className='row', style={'textAlign': 'left', 'padding-left': '275px', 'padding-bottom':'5px'}),
    #DashTable
    html.Div([
         dash_table.DataTable(
            id='LCA_Datatable',
            columns=[
                {"name":i, "id": i, 'presentation': 'dropdown'} for i in df.columns
                            ],
                style_cell={
                    'fontFamily':'Arial',
                    'whiteSpace':'normal',
                    'textAlign':'center',
                    'minWidth':'10px', 'width':'100px','maxWidth':'100px',
                    'whiteSPace':'no-wrap',
                    'overflow':'hidden',
                    'textOverflow':'ellipsis'
                },
                data=df.to_dict('records'),
                hidden_columns=['Source', 'Target', 'Value', 'Color', 'Label'],
                fixed_rows={'headers':True, 'data':0},
                editable=False,
                #filtering=True,
                filter_action='native',
                sort_action='native',
                sort_mode='multi',
                #column_selectable='single',
                row_selectable=False,
                css=[{"selector": ".show-hide", "rule": "display: none"}],
                row_deletable=False,
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=[
                 {
                     'if': {'row_index': 'odd'},
                     'backgroundColor': 'rgb(255, 227, 227)'
                 },

                 {
                     'if': {'row_index':'even'},
                     'backgroundColor': 'rgb(253, 253, 255)'

                 }
                 ],
                # style_data_conditional=[
                #      {'if': {'column_id': 'Last_Loop_Name'},
                #          'width': '20px'},
                #      {'if': {'column_id': 'Last_Loop_Number'},'width': '20px'},
                #      {'if': {'column_id': 'Highest_Rank_Earned'},
                #          'width': '20px'},
                #      {'if': {'column_id': 'Age_at_Military_Separation'},
                #          'width': '20px'},
                #      {'if': {'column_id': 'Age_at_Enlistment'},
                #          'width': '25px'},
                #      {'if': {'column_id': 'Current_Age'},
                #          'width': '75px'},
                #      {'if': {'column_id': 'Current_Military'},
                #          'width': '75px'},
                #      {'if': {'column_id': 'Q63'},
                #          'width': '75px'},
                #      {'if': {'column_id': 'Q65'},
                #          'width': '75px'},
                #      {'if': {'column_id': 'Q67_3'},
                #          'width': '75px'},
                #      {'if': {'column_id': 'Branch_of_Service'},
                #          'width': '75px'},
                # ],
                virtualization=True,
                page_action='none',
                style_table={'maxHeight': '200px','overflfowY': 'scroll'},
                style_header={
                    'backgroundColor': 'rgb(227, 237, 255)',
                    'fontWeight': 'bold'
                }
            )
            ], className="six columns", style={'width':'100%', 'display':'flex', 'align-items':'center', 'justify-content':'center', 'padding-right':'10%'}),
         html.Br(),
         html.P(['NOTE: When filtering for numbers, please encase in quotation marks. (ex: "2" or "35,000") '], style={'padding-left':'275px', 'padding-top':'5px'}),

    # Graph
    html.Div(
        [
            html.Div([
                dcc.Graph(id='LCA_Sankey')
                # figure={'data': data_trace, 'layout': layout})

            ], className="twelve columns"),
        ]
    )
])

@app.callback(
    Output('LCA_Datatable', 'filter_query'),
    [Input('clear', 'n_clicks')],
    [State('LCA_Datatable', 'filter_query')],
)
def clearFilter(n_clicks, state):
    if n_clicks is None:
        return '' if state is None else state

    return ''

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
                # color = "black",
                width=0.5
            ),
            label=["High School or GED",
                   "Enlisted", "School", "Work", "Work and School", "Work and Reserves", "School and Reserves",
                   "Retirement", "ROTC or Mil. Academy", "Transferred Schools",
                   "Enlisted", "School", "Work", "Work and School", "Work and Reserves", "School and Reserves",
                   "Retirement", "ROTC or Mil. Academy", "Transferred Schools",
                   "Enlisted", "School", "Work", "Work and School", "Work and Reserves", "School and Reserves",
                   "Retirement", "ROTC or Mil. Academy", "Transferred Schools",
                   "Enlisted", "School", "Work", "Work and School", "Work and Reserves", "School and Reserves",
                   "Retirement", "ROTC or Mil. Academy", "Transferred Schools",
                   "Enlisted", "School", "Work", "Work and School", "Work and Reserves", "School and Reserves",
                   "Retirement", "ROTC or Mil. Academy", "Transferred Schools",
                   "Enlisted", "School", "Work", "Work and School", "Work and Reserves", "School and Reserves",
                   "Retirement", "ROTC or Mil. Academy", "Transferred Schools",
                   "Enlisted", "School", "Work", "Work and School", "Work and Reserves", "School and Reserves",
                   "Retirement", "ROTC or Mil. Academy", "Transferred Schools",
                   "Enlisted", "School", "Work", "Work and School", "Work and Reserves", "School and Reserves",
                   "Retirement", "ROTC or Mil. Academy", "Transferred Schools"],
        ),
        link=dict(
            source=dff['Source'].dropna(axis=0, how='any'),
            target=dff['Target'].dropna(axis=0, how='any'),
            value=dff['Value'].dropna(axis=0, how='any'),
            color="rgba(140, 140, 140, .025)",
            label=dff['Label'].dropna(axis=0, how='any'),
        )
    ),
    figure = {
        'data': data_trace,
        'layout': layout
    }
    return figure





if __name__ == '__main__':
    app.run_server(debug=True)

