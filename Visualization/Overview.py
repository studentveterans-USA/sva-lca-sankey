import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
from Visualization import (
    Overview,
    Sankey,
    SVA_Research,
)
from utils import Header, get_header, get_menu, make_dash_table

decision_points = {'Options':["A) Enlisted", "B) Military and Enrolled in School", "C) School & Reserves/Nat. Guard", "D) School", "E) Transferred", "F) Work", "G) Work & Reserves/Nat. Guard", "H) Work & School", "I) Retirement"], 'Descriptions':["Active duty military service", "ROTC, Military Academy, etc.", "Military reservist or National Guard while enrolled in school", "Enrolled in post-secondary education", "Transferred to a different post-secondary institution", "Worked full-time non-military job", "Worked full-time non-military job and joined Reserves or National Gueard", "Worked full-time non-military job and enrolled in post-secondary education", "No longer working, going to school, or in military"]}
decision_points_df = pd.DataFrame(decision_points)
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
                                    html.H5('Project Overview'),
                                    html.Br([]),
                                    html.Br([]),
                                    html.P([
                                        html.A("Student Veterans of America", href="https://studentveterans.org/"),
                                        ", in partnership with ",
                                        html.A("PwC Charitable Foundation",href="http://www.pwccharitablefoundation.org/"),
                                        ", are working to better understand the student veteran population. Specifically designed "
                                        "to address a gap in research, the Life Cycle Atlas project was launched in 2017. "
                                        "The research focuses on the educational life cycle of student veterans in order to provide "
                                        "policy makers, stakeholders, current or future student veterans, and the public alike with "
                                        "accurate information to make data driven decisions.",
                                    html.Br([]),
                                    html.Br([]),

                                        "The data were collected through an online survey. "
                                        "During the two years of data collection, nearly 4,000 current and former service members that pursued post-secondary education "
                                        "at some point in their career completed the survey. Key 'decision points' in a student veteran's post-high school life are captured "
                                        "in the data, resulting in a sequential summary of student veteran's life events. ",
                                    html.Br([]),
                                    html.Br([]),

                                        "Respondants were given nine different options (see table below) to describe their key decisions."
                                        "These decisions were analyzed in-depth for insight. Common first decisions after high school are represented in the graphs below. For more detailed analysis about complete paths, please see the ",
                                        html.A("Data Visualization section.", href="/Visualization/Sankey")
                                    ]
                                        ,
                                        className="row",
                                        style={'font-size':'20px'}
                                    ),
                                ],
                                className="summary"
                            )
                        ],
                        className='row'
                    ),
                    #Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        'Description of Decisions',
                                        className='subtitle padded'
                                    ),
                                    html.Table(make_dash_table(decision_points_df)),
                                ],
                                className='six columns',
                                style={'font-size': '16px'}
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        '1st decision after High school or GED',
                                        className='subtitle padded'
                                    ),
                                    dcc.Graph(
                                        id='graph-1',
                                        figure={
                                            'data':[
                                                go.Bar(
                                                    x=[
                                                        'Enlisted',
                                                        'School',
                                                        'Work',
                                                        'Work & School',
                                                        'School & Reserves/NG',
                                                        'Work & Reserves/NG',
                                                        'ROTC or Mil. Acad.'
                                                    ],
                                                    y=[
                                                        '51.6',
                                                        '21.5',
                                                        '10.9',
                                                        '5.8',
                                                        '4.5',
                                                        '1.8',
                                                        '3.7'
                                                    ],
                                                    text=['51.6%','21.5%','10.9%','5.8%','4.5%','1.8%','3.7%'],
                                                    textposition='auto',
                                                    marker={
                                                        #'text':['51.6%','21.5%','10.9%','5.8%','4.5%','1.8%','3.7%'],
                                                        'color':'#A0001F',
                                                        'line':{
                                                            'color':'rgb(255,255,255)',
                                                            'width':2,
                                                        }
                                                    }
                                                )
                                            ],
                                            'layout':go.Layout(
                                                autosize=False,
                                                #text=['51.6%','21.5%','10.9%','5.8%','4.5%','1.8%','3.7%'],
                                                bargap=0.35,
                                                hovermode='closest',
                                                title='',
                                                yaxis={
                                                    'range':[0,55],
                                                    'showgrid':True,
                                                    'showline':True,
                                                    'type':'linear',
                                                    'title':'Percentage'
                                                },
                                            ),
                                        },
                                        config={'displayModeBar':False}
                                    ),
                                ],
                                className='six columns'
                            )

                        ],
                        className='row'
                    ),
                    html.Br([]),
                    html.Br([]),
                    #Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        'Gender Differences in 1st Decision',
                                        className='subtitle padded'
                                    ),
                                    dcc.Graph(
                                        id='graph-2',
                                        figure={
                                            'data':[
                                                go.Bar(
                                                    x=[
                                                        'Enlisted',
                                                        'School',
                                                        'Work',
                                                        'Work & School',
                                                        'School & Reserves/NG',
                                                        'Work & Reserves/NG',
                                                        'ROTC or Mil. Acad.'
                                                    ],
                                                    y=[
                                                        "54.1",
                                                        "20.4",
                                                        "10.9",
                                                        "5.1",
                                                        "4.2",
                                                        "1.7",
                                                        "3.5"

                                                    ],
                                                    text=["54.1%","20.4%","10.9%","5.1%","4.2%","1.7%","3.5%"],
                                                    textposition='auto',
                                                    marker={
                                                        'color':'#002760',
                                                        'line':{
                                                            'color': 'rgb(255,255,255)',
                                                            'width': 2,
                                                        },

                                                    },
                                                    name='Men'
                                                ),
                                                go.Bar(
                                                    x=[
                                                        'Enlisted',
                                                        'School',
                                                        'Work',
                                                        'Work & School',
                                                        'School & Reserves/NG',
                                                        'Work & Reserves/NG',
                                                        'ROTC or Mil. Acad.'
                                                    ],
                                                    y=[
                                                        "43.4",
                                                        "23.5",
                                                        "9.7",
                                                        "7.6",
                                                        "5.1",
                                                        "2.3",
                                                        "3.7"



                                                    ],
                                                    text=['43.4%','23.5%','9.7%','7.6%','5.1%','2.3%','3.7%'],
                                                    textposition='auto',
                                                    marker={
                                                        'color':'#A0001F',
                                                        'line':{
                                                            'color': 'rgb(255,255,255)',
                                                            'width': 2,
                                                        },
                                                    },
                                                    name='Women'
                                                ),
                                            ],
                                            'layout': go.Layout(
                                                autosize=False,
                                                # text=['51.6%','21.5%','10.9%','5.8%','4.5%','1.8%','3.7%'],
                                                bargap=0.35,
                                                hovermode='closest',
                                                title='',
                                                yaxis={
                                                    'range': [0, 55],
                                                    'showgrid': True,
                                                    'showline': True,
                                                    'type': 'linear',
                                                    'title': 'Percentage'
                                                },
                                            ),
                                        },
                                        config={'displayModeBar': False}

                                    ),

                                ],
                                className='six columns'
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        'Branch of Service Differences in 1st Decision',
                                        className='subtitle padded'
                                    ),
                                    dcc.Graph(
                                        id='graph-3',
                                        figure={
                                            'data':[
                                                go.Bar(
                                                    x=[
                                                        'Enlisted',
                                                        'School',
                                                        'Work',
                                                        'Work & School',
                                                        'School & Reserves/NG',
                                                        'Work & Reserves/NG',
                                                        'ROTC or Mil. Acad.'
                                                    ],
                                                    y=[
                                                        "52.6",
                                                        "16.1",
                                                        "8.6",
                                                        "4.9",
                                                        "8.7",
                                                        "3.7",
                                                        "5.4"

                                                    ],
                                                    #text=['52.6%','16.1%','8.6%','4.9%','8.7%','3.7%','5.4%'],
                                                    #textposition='auto',
                                                    marker={
                                                        'color': '#313640',
                                                        'line': {
                                                            'color': 'rgb(255,255,255)',
                                                            'width': 2,
                                                        },

                                                    },
                                                    name='Army'
                                                ),

                                                go.Bar(
                                                    x=[
                                                        'Enlisted',
                                                        'School',
                                                        'Work',
                                                        'Work & School',
                                                        'School & Reserves/NG',
                                                        'Work & Reserves/NG',
                                                        'ROTC or Mil. Acad.'
                                                    ],
                                                    y=[
                                                        "55.6",
                                                        "20.0",
                                                        "10.7",
                                                        "5.7",
                                                        "2.2",
                                                        "1.2",
                                                        "4.8"
                                                    ],
                                                    #text=['55.6%', '20.0%','10.7%','5.7%','2.2%','1.2%','4.8%'],
                                                    #textposition='auto',
                                                    marker={
                                                        'color': 'rgb(0, 144, 216)',
                                                        'line': {
                                                            'color': 'rgb(255,255,255)',
                                                            'width': 2,
                                                        },

                                                    },
                                                    name='Air Force'
                                                ),
                                                go.Bar(
                                                    x=[
                                                        'Enlisted',
                                                        'School',
                                                        'Work',
                                                        'Work & School',
                                                        'School & Reserves/NG',
                                                        'Work & Reserves/NG',
                                                        'ROTC or Mil. Acad.'
                                                    ],
                                                    y=[
                                                        '69.6',
                                                        '12.1',
                                                        '7.9',
                                                        '3.2',
                                                        '3.8',
                                                        '1.5',
                                                        '1.9'
                                                    ],
                                                    #text=['69.6%','12.1%','7.9%','3.2%','3.8%','1.5%','1.9%'],
                                                    #textposition='auto',
                                                    marker={
                                                        'color': '#A0001F',
                                                        'line': {
                                                            'color': 'rgb(255,255,255)',
                                                            'width': 2,
                                                        },

                                                    },
                                                    name='Marine Corps'
                                                ),
                                                go.Bar(
                                                    x=[
                                                        'Enlisted',
                                                        'School',
                                                        'Work',
                                                        'Work & School',
                                                        'School & Reserves/NG',
                                                        'Work & Reserves/NG',
                                                        'ROTC or Mil. Acad.'
                                                    ],
                                                    y=[
                                                        '63.3',
                                                        '18.3',
                                                        '8.0',
                                                        '4.3',
                                                        '2.2',
                                                        '0.7',
                                                        '3.0'

                                                    ],
                                                    #text=['63.3%','18.3%','8.0%','4.3%''2.2%','0.7%','3.0%'],
                                                    #textposition='auto',
                                                    marker={
                                                        'color': '#002760',
                                                        'line': {
                                                            'color': 'rgb(255,255,255)',
                                                            'width': 2,
                                                        },

                                                    },
                                                    name='Navy'
                                                ),
                                                go.Bar(
                                                    x=[
                                                        'Enlisted',
                                                        'School',
                                                        'Work',
                                                        'Work & School',
                                                        'School & Reserves/NG',
                                                        'Work & Reserves/NG',
                                                        'ROTC or Mil. Acad.'
                                                    ],
                                                    y=[
                                                        '50.0',
                                                        '14.3',
                                                        '19.6',
                                                        '5.3',
                                                        '3.6',
                                                        '3.6',
                                                        '3.6'

                                                    ],
                                                    #text=['50.0%','14.3%','19.6%','5.3%','3.6%','3.6%','3.6%'],
                                                    #textposition='auto',
                                                    marker={
                                                        'color': '#CCBA74',
                                                        'line': {
                                                            'color': 'rgb(255,255,255)',
                                                            'width': 2,
                                                        },

                                                    },
                                                    name='Coast Guard'
                                                ),

                                            ],
                                            'layout':go.Layout(
                                                autosize=False,
                                                #text=['51.6%','21.5%','10.9%','5.8%','4.5%','1.8%','3.7%'],
                                                bargap=0.35,
                                                hovermode='closest',
                                                title='',
                                                yaxis={
                                                    'range':[0,70],
                                                    'showgrid':True,
                                                    'showline':True,
                                                    'type':'linear',
                                                    'title':'Percentage'
                                                },


                                            ),
                                        },
                                        config={'displayModeBar': False}
                                    ),

                                ],
                                className='six columns'
                            )

                        ],
                        className='row'
                    ),
                    html.Br([]),
                    html.Br([]),
                ],
                className="sub-page"
            ),
        ],
        className="page"
    )
