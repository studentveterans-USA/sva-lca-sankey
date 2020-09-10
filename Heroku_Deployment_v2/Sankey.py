import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go

####################################################### Data ###########################################################
df = pd.read_csv("LCA_Sankey_Processed_Data.csv")
df = df.dropna(subset=['Last_Loop_Name', 'Last_Loop_Number', 'Branch_of_Service', 'Highest_Rank_Earned','Age_At_Separation','Age_At_Enlistment','Q4','Current_Military', 'First_Gen_College',
                       'Q63', 'Q65', 'Q67_3', 'Q71', 'Q79'])
df['Last_Loop_Name'] = df['Last_Loop_Name'].astype('category')
df['Last_Loop_Number'] = df['Last_Loop_Number'].astype('int')
df['Branch_of_Service'] = df['Branch_of_Service'].astype('category')
df['Highest_Rank_Earned'] = df['Highest_Rank_Earned'].astype('category')
df['Age_At_Separation'] = df['Age_At_Separation'].astype('int')
df['Age_At_Enlistment'] = df['Age_At_Enlistment'].astype('int')
df['Q4'] = df['Q4'].astype('int')
df['Current_Military'] = df['Current_Military'].astype('category')
df['First_Gen_College'] = df['First_Gen_College'].astype('category')
df['Q63'] = df['Q63'].astype('category')
df['Q65'] = df['Q65'].astype('category')
df['Q67_3'] = df['Q67_3'].astype('category')
df['Q71'] = df['Q71'].astype('category')
df['Q79'] = df['Q79'].astype('category')

df.rename(columns={
    'Last_Loop_Name':'Final Decision Point',
    'Last_Loop_Number':'Number of Decision Points',
    'Highest_Rank_Earned': 'Highest Rank Earned',
    'Age_At_Separation':'Age at Military Separation',
    'Age_At_Enlistment':'Age at Enlistment',
    'Q4':'Current Age',
    'Current_Military':'Current Military',
    'First_Gen_College':'First Generation College',
    'Q63':'Ethnicity',
    'Q65':'Gender',
    'Q67_3':'Edu lvl earned or planned',
    'Q71':'Current Income',
    'Q79':'Education Debt',
    'Branch_of_Service':'Branch of Service'}, inplace=True)



df_cols_to_filter = df[['Final Decision Point', 'Number of Decision Points','Highest Rank Earned','Age at Military Separation',
                        'Age at Enlistment','Current Age','Current Military','First Generation College','Ethnicity','Gender',
                        'Edu lvl earned or planned','Current Income','Education Debt','Branch of Service']]
############################################# Dtype Function for Dropdown ##############################################
def get_dtype(df, col):
    dtypes = ['datetime', 'bool', 'int', 'float', 'object', 'category']
    for d in dtypes:
        try:
            if d in str(df_cols_to_filter.dtypes.loc[col]).lower():
                return d
        except KeyError:
            return None


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


layout=dict(
        height='600',
        pad='200',
        font=dict(
        size=10
        ),
        )

colors = {
    'background': '#ffffff',
    'text': '#000000'}



#LAYOUT

def create_layout(app):
    return html.Div(
        [
            html.Div([Header(app)]),

            #Home Page
            html.Div(
                [
                    #Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5('Explore The Data'),
                                    html.Br([]),
                                    html.P([
                                        html.A('Sankey Diagrams', href='https://towardsdatascience.com/the-what-why-and-how-of-sankey-diagrams-430cbd4980b5'),
                                        " are designed to show the flow of information from beginning to end."                                        
                                        " Given the complex and sequential nature of the Life Cycle Atlas data, it is"
                                        " most appropriate to visualize the data using this type of diagram."
                                        " In this particular example, the beginning starts at the left-most node"
                                        " titled 'High School'."
                                        " The size of flow to the next node, "
                                        "as well as the size of the node itself, represents"
                                        " the number of veterans that chose that particular path."
                                        " The flow between nodes is a collection of individuals and as such, "
                                        "please feel free to hover and get more information about the person's journey!",
                                    html.Br([]),
                                    html.Br([]),
                                        "The power of this visualization is its ability to answer anyone's questions by exploring different educational journeys using data filters. "
                                        "To do so, simply use the table below by"
                                        " typing in your specific filtering criteria. The user has the ability to add as many or as few filters as they want and can start over by simply clicking 'CLEAR FILTER'!",
                                    html.Br([]),
                                    html.Br([]),
                                        " For example, if you are interested in "
                                        " understanding the educational journeys of Male, Hispanic, Navy veterans who enlisted"
                                        " in the military before 22 years of age (< 22), simply type that information"
                                        " into the appropriate columns of the table, and click 'enter' on your keyboard"
                                        " and watch the visualization change!",
                                    html.Br([]),
                                    html.Br([]),
                                        " Or, for example, if you are a 23 year old Female thinking about enlisting"
                                        " in the Marine Corps, filter the 'Branch of Service' column using 'Marine', "
                                        "the 'Age at Enlistment' column using '>23', and the 'Gender' column using 'Female'."
                                        " Doing so, will filter the visualization to a much more manageable size where"
                                        " you can then see the journey of someone exactly like you who has already "
                                        "been there, done that!"


                                        ],
                                        className='row',
                                        style={'font-size':'20px'}
                                    ),

                                ],
                                className='summary'
                            )

                        ],
                        className='row'
                    ),
                    #Row 4 - Clear filter button
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Button(id='clear', children='Clear filter'),
                                    html.P("    NOTE: When filtering for integers, please encase in quotation marks. (ex: '2' or '35,000')")

                                ],
                                className='row'

                            ),

                        ],
                        className='row'
                    ),
                    #Row 5 - Dash Table
                    html.Div(
                        [
                            html.Div([
                                dash_table.DataTable(
                                    id='LCA_Datatable',
                                    columns=[
                                        {"name": i, "id": i, 'presentation': 'dropdown'} for i in df.columns],
                                    style_cell={
                                        'fontFamily': 'Arial',
                                        'whiteSpace': 'normal',
                                        'textAlign': 'center',
                                        'minWidth': '10px', 'width': '100px', 'maxWidth': '100px',
                                        'whiteSPace': 'no-wrap',
                                        'overflow': 'hidden',
                                        'textOverflow': 'ellipsis'
                                    },
                                    data=df.to_dict('records'),
                                    hidden_columns=['source', 'target', 'value', 'color', 'label'],
                                    filter_action='native',
                                    fixed_rows={'headers': True, 'data': 0},
                                    css=[{"selector": ".show-hide", "rule": "display: none"}],
                                    style_data_conditional=[
                                        {
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(255, 227, 227)'
                                        },

                                        {
                                            'if': {'row_index': 'even'},
                                            'backgroundColor': 'rgb(253, 253, 255)'

                                        }
                                    ],
                                    virtualization=True,
                                    page_action='none',
                                    style_table={'maxHeight': '200px', 'overflfowY': 'scroll'},
                                    style_header={
                                        'backgroundColor': 'rgb(227, 237, 255)',
                                        'fontWeight': 'bold'
                                    }
                                )
                            ], className="twelve columns"
                            ),
                        ],
                        className='row'
                    ),
                    #Row 5 - Sankey Graph
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            dcc.Graph(id='LCA_Sankey')

                                        ],
                                        className='Sankey'
                                        #,style={'width':'97%','padding-left':'1.5%','padding-right':'1.5%', 'align-items':'center', 'justify-content':'center'}
                                    )
                                ],
                                className='twelve columns'
                            )

                        ],
                        className='row'

                    ),


                ],
                className="sub-page"
            ),
        ],
        className="page"
    )