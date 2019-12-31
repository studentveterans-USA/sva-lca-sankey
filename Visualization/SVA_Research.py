import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
from Visualization import (
    Overview,
    Sankey,
    SVA_Research
)
#from utils import Header, get_header, get_menu, make_dash_table


def create_layout(app):
    return html.Div(
        [
            html.Div([Header(app)]),
            html.Br([]),
            html.Br([]),

            #Home Page
            html.Div(
                [
                    # html.Div(
                    #     [
                    #         html.Img(
                    #             src='https://studentveterans.org/media/com_workforce/employees/chriscate_1569001412.png',
                    #             className='Me_img'
                    #         ),
                    #
                    #     ],
                    #     className='row'
                    # ),
                    # html.Br([]),
                    # html.Br([]),
                    html.Div(
                        [
                            html.P(
                                [
                                    "Led by ",
                                    html.A("Dr. Chris Cate", href='https://studentveterans.org/aboutus/sva-team-leadership-student-veterans-of-america?view=employee&id=4'),
                                    ", the Student Veterans of America Research Department is highly regarded"
                                    " within the industry. Frequently referenced in the United States Congress, SVA"
                                    " works to inform the public, stake holders, policy makers, and others on student"
                                    " veteran and military connected students topics and concerns through emperical research. "
                                    "In addition to the Life Cycle Atlas, SVA has completed research projects such as ",
                                    html.A("National Veteran Education Success Tracker (NVEST)", href='https://nvest.studentveterans.org/'),
                                    ', ',
                                    html.A("SVA Spotlight", href='https://studentveterans.org/aboutus/research/sva-spotlight'),
                                    ' ,',
                                    ' and ',
                                    html.A("SVA Census", href='https://studentveterans.org/images/pdf/2016-SVA-Census-Survey-Student-Veteran-General-Breakdowns-120716.pdf'),
                                    ", please take a look!",
                                    html.Br([]),
                                    html.Br([]),
                                    "Dr. Cate is supported by a tenacious team of researchers "
                                    "committed to impacting the lives of student veterans. ",
                                    html.A("Ryan Kinsey", href='https://studentveterans.org/aboutus/sva-team-leadership-student-veterans-of-america?view=employee&id=103'),
                                    " is SVA's Junior Data Scientist. With a "
                                    "Master's Degree in Data Science from The George Washington University, Ryan works"
                                    " to apply data science and data analytics techniques to higher education research. ",

                                    html.A('Madeline Clark', href='https://studentveterans.org/aboutus/sva-team-leadership-student-veterans-of-america?view=employee&id=115'),
                                    ' is a current graduate student studying Linguistics at Georgetown University. '
                                    'Her experience in qualitative and quantitative research as well as data '
                                    'visualization skills make her an invaluable asset to the SVA research team! ',
                                    html.A('Kameron Smith', href='https://studentveterans.org/aboutus/sva-team-leadership-student-veterans-of-america?view=employee&id=114'),
                                    ' served in the United States Air Force for over 7 years. He is'
                                    ' is currently pursuing a Journalism degree at American University. His firsthand '
                                    'experience with being a student veteran, combined with his data analytics skills'
                                    ' bring valuable insight to SVA!',
                                    html.Br([]),
                                    html.Br([]),
                                    " Each member of the team played a pivotal role in making this research available to the public! "
                                    "For inquires or to report issues with this application, please ",
                                    html.A("email",href='mailto:chris.cate@studentveterans.org'),
                                    " or visit our ",
                                    html.A('website', href='https://studentveterans.org/aboutus/research'),
                                    "."
                                ],
                                className='summary',
                                style={'font-size':'20px'}
                            )

                        ],
                        className='summary'
                    ),


                ],
                className="sub-page"
            ),
        ],
        className="page"
    )
