import pandas as pd
import numpy as np
import json
import os
import dash
import pathlib
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import State, Input, Output
import plotly as py
from plotly import graph_objs as go
from app import app

BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("../datasets").resolve()

with open(DATA_PATH.joinpath("selected-ok-counties.json")) as geocounty:
    okgeo = json.load(geocounty)


okPPL = pd.read_csv(DATA_PATH.joinpath("ok-population.csv"))
#read tulsa area population
tuPPL = pd.read_csv(DATA_PATH.joinpath("tulsa-population.csv"))
ok_bachelorOrHigher = pd.read_csv(DATA_PATH.joinpath("ok_bachelorOrHigher.csv"))
tu_bachelorOrHigher = pd.read_csv(DATA_PATH.joinpath("tu_bachelorOrHigher.csv"))
ok_homeownership = pd.read_csv(DATA_PATH.joinpath("ok_homeownership.csv"))
tu_homeownership = pd.read_csv(DATA_PATH.joinpath("tu_homeownership.csv"))
ok_unemploy = pd.read_csv(DATA_PATH.joinpath("ok_unemploy.csv"))
tu_unemploy = pd.read_csv(DATA_PATH.joinpath("tu_unemploy.csv"))
ok_medianDaysOnMarket = pd.read_csv(DATA_PATH.joinpath("ok_medianDaysOnMarket.csv"))
tu_medianDaysOnMarket = pd.read_csv(DATA_PATH.joinpath("tu_medianDaysOnMarket.csv"))
ok_medianHouseholdIncome = pd.read_csv(DATA_PATH.joinpath("ok_medianHouseholdIncome.csv"))
tu_medianHouseholdIncome = pd.read_csv(DATA_PATH.joinpath("tu_medianHouseholdIncome.csv"))
ok_combinedCrime = pd.read_csv(DATA_PATH.joinpath("ok_combinedCrime.csv"))
tu_combinedCrime = pd.read_csv(DATA_PATH.joinpath("tu_combinedCrime.csv"))
ok_resiPop = pd.read_csv(DATA_PATH.joinpath("ok_resiPop.csv"))
tu_resiPop = pd.read_csv(DATA_PATH.joinpath("tu_resiPop.csv"))
ok_race = pd.read_csv(DATA_PATH.joinpath("ok_race.csv"))
tu_race = pd.read_csv(DATA_PATH.joinpath("tu_race.csv"))
ok_career = pd.read_csv(DATA_PATH.joinpath("ok_career.csv"))
tu_career = pd.read_csv(DATA_PATH.joinpath("tu_career.csv"))
ok_votePop = pd.read_csv(DATA_PATH.joinpath("ok_votePop.csv"))
tu_votePop = pd.read_csv(DATA_PATH.joinpath("tu_votePop.csv"))
ok_disaster  = pd.read_csv(DATA_PATH.joinpath("ok_disaster.csv"))
tu_disaster = pd.read_csv(DATA_PATH.joinpath("tu_disaster.csv"))
ok_1bed = pd.read_csv(DATA_PATH.joinpath("ok_1bed.csv"))
ok_2bed = pd.read_csv(DATA_PATH.joinpath("ok_2bed.csv"))
ok_3bed = pd.read_csv(DATA_PATH.joinpath("ok_3bed.csv"))
ok_4bed = pd.read_csv(DATA_PATH.joinpath("ok_4bed.csv"))
ok_5bed = pd.read_csv(DATA_PATH.joinpath("ok_5bed.csv"))
tu_1bed = pd.read_csv(DATA_PATH.joinpath("tu_1bed.csv"))
tu_2bed = pd.read_csv(DATA_PATH.joinpath("tu_2bed.csv"))
tu_3bed = pd.read_csv(DATA_PATH.joinpath("tu_3bed.csv"))
tu_4bed = pd.read_csv(DATA_PATH.joinpath("tu_4bed.csv"))
tu_5bed = pd.read_csv(DATA_PATH.joinpath("tu_5bed.csv"))


#ok area map
def ok_map():
    okzmin, okzmax = np.min(okPPL["POP"]), np.max(okPPL["POP"])

    ok_data = [
        go.Choropleth(
            colorbar = dict(
            tickvals = [okzmin, okzmax],
            tickformat = ".2f",
            ticks = "",
            title = "Total Population",
            titlefont = dict(family = "Roboto", color = '#2cfec1', size = 15),
            thickness = 30,
            len = 0.7,
            tickcolor = '#2cfec1',
            tickfont = dict(color = '#2cfec1')
                        ),
            colorscale = [
                     [0, "#f2fffb"],
                     [0.1, "#98ffe0"],
                     [0.2, "#79ffd6"],
                     [0.3, "#69e7c0"],
                     [0.4, "#59dab2"],
                     [0.5, "#45d0a5"],
                     [0.6, "#31c194"],
                     [0.7, "#2bb489"],
                     [0.8, "#25a27b"],
                     [0.9, "#1e906d"],
                     [1, "#188463"]],
            reversescale = False,
            geojson = okgeo,
            featureidkey = "properties.name",
            locations = ['Canadian', 'Cleveland', 'Garfield', 'Grady', 'Kingfisher', 'Lincoln', 'Logan', 'Oklahoma', 'Payne', 'Pottawatomie'],
            z = okPPL["POP"].tolist(),
            marker = dict(line = {"color": '#2cfec1'}),
            marker_line_width = 3,
            locationmode = "geojson-id",
            customdata = okPPL["CTYNAME"].tolist(),
            hoverinfo = 'location+z'
                )
        ]

    layout = dict(
            margin = dict(l=0, r=0, t=70, b=0),
            clickmode = "event+select",
            paper_bgcolor = "#252e3f",
            title = "<b>Oklahoma City Area</b>",
            font = dict(family = 'Roboto', color = '#FFFFFF',size = 15),
        )


    okfig = go.Figure(data = ok_data, layout = layout)
    okfig.update_geos(fitbounds="locations", visible=False)
    okfig.update_layout(geo=dict(bgcolor= "#252e3f"))

    return okfig

#tulsa area map
def tu_map():
    tuzmin, tuzmax = np.min(tuPPL["POP"]), np.max(tuPPL["POP"])
    tu_data = [
        go.Choropleth(
            colorbar = dict(
            tickvals = [tuzmin, tuzmax],
            tickformat = ".2f",
            ticks = "",
            title = "Total Population",
            titlefont = dict(family = "Roboto", color = '#2cfec1', size = 15),
            thickness = 30,
            len = 0.7,
            tickcolor = '#2cfec1',
            tickfont = dict(color = '#2cfec1')
                        ),
            colorscale = [
                     [0, "#f2fffb"],
                     [0.03, "#98ffe0"],
                     [0.06, "#79ffd6"],
                     [0.07, "#69e7c0"],
                     [0.08, "#59dab2"],
                     [0.09, "#45d0a5"],
                     [0.1, "#31c194"],
                     [0.105, "#2bb489"],
                     [0.11, "#25a27b"],
                     [0.13, "#1e906d"],
                     [1, "#188463"]],
            reversescale = False,
            geojson = okgeo,
            featureidkey = "properties.name",
            locations = ['Creek', 'Mayes', 'Muskogee', 'Okmulgee', 'Osage', 'Rogers', 'Tulsa', 'Wagoner', 'Washington'],
            z = tuPPL["POP"].tolist(),
            marker = dict(line = {"color": '#2cfec1'}),
            marker_line_width = 3,
            locationmode = "geojson-id",
            customdata = tuPPL["CTYNAME"].tolist(),
            hoverinfo = 'location+z'
                )
            ]

    layout = dict(
            margin = dict(l=0, r=0, t=70, b=0),
            clickmode = "event+select",
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e8f",
            title = "<b>Tulsa Area</b>",
            font = dict(family = 'Roboto', color = '#FFFFFF',size = 15),
        )


    tufig = go.Figure(data = tu_data, layout = layout)
    tufig.update_geos(fitbounds="locations", visible=False)
    tufig.update_layout(geo=dict(bgcolor= "#252e3f"))


    return tufig

layout = html.Div(id = 'app-body',
    children = [
        html.Div(
            style = {'backgroundColor': '#1f2330', 'margin-top': '0px'},
            className = "Row",
            children = [
                html.Div(
                    style = {'width': '47%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft': '1%', 'marginTop': '1%', 'marginBottom': '1%'},
                    id = "map-outer1",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "ok-choropleth", figure = ok_map())]
                            )
                        ]
                    ),
                html.Div(
                    className = 'vertical'
                ),
                html.Div(
                    style = {'width': '47%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft': '1%', 'marginTop': '1%', 'marginBottom': '1%'},
                    id = "map-outer2",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tu-choropleth", figure = tu_map())]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft': '1%', 'marginBottom': '1%'},
                    id = "ok-bedroom-outer",
                    children = [
                        html.Div(style = {'width' : '200px', 'padding': '3px', 'border': '10px solid #252e3f', 'border-radius': '15px', 'backgroundColor': '#252e3f'},
                            children = [
                                dcc.Dropdown(style = {'color': '#252e3f', 'border-radius': '15px', 'content': '#FFFFFF'},
                                id = "ok-dropdown",
                                options = [{'label': 'One Bedroom', 'value': 'bed1'}, {'label': 'Two Bedroom', 'value': 'bed2'},
                                    {'label': 'Three Bedroom', 'value': 'bed3'}, {'label': 'Four Bedroom', 'value': 'bed4'},
                                    {'label': 'Five or more', 'value': 'bed5'}],
                                value = 'bed1'

                            )
                        ]
                    ),
                        html.Div(
                            children = [dcc.Graph(id = "okHousingPrice")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%'},
                    id = "okHomeownership-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okHomeownership")]
                        )
                    ]
                ),
                html.Div(
                    className = 'vertical'
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft': '1%', 'marginBottom': '1%'},
                    id = "tu-bedroom-outer",
                    children = [
                        html.Div(style = {'width' : '200px', 'padding': '3px', 'border': '10px solid #252e3f', 'border-radius': '15px', 'backgroundColor': '#252e3f'},
                            children = [
                                dcc.Dropdown(style = {'color': '#252e3f', 'border-radius': '15px', 'content': '#FFFFFF'},
                                id = "tu-dropdown",
                                options = [{'label': 'One Bedroom', 'value': 'bed1'}, {'label': 'Two Bedroom', 'value': 'bed2'},
                                        {'label': 'Three Bedroom', 'value': 'bed3'}, {'label': 'Four Bedroom', 'value': 'bed4'},
                                        {'label': 'Five or more', 'value': 'bed5'}],
                                value = 'bed1'

                                )
                            ]
                        ),
                            html.Div(
                                children = [dcc.Graph(id = "tuHousingPrice")]
                            )
                        ]
                    ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%'},
                    id = "tuHomeownership-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuHomeownership")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginLeft': '1%', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okMedianDays-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okMedianDays")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okUnemployRate-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okUnemployRate")]
                        )
                    ]
                ),
                html.Div(
                    className = 'vertical'
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft' : '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuMedianDays-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuMedianDays")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuUnemployRate-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuUnemployRate")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '18%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft' : '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okRace-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okRace")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '28%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okDisaster-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okDisaster")]
                        )
                    ]
                ),
                html.Div(
                    className = 'vertical'
                ),
                html.Div(
                    style = {'width': '18%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft' : '1%','marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuRace-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuRace")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '28%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuDisaster-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuDisaster")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okResidentPop-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okResiPop")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okBachelorOrHigher-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okBachelorOrHigher")]
                        )
                    ]
                ),
                html.Div(
                    className = 'vertical'
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%','marginLeft' : '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuResidentPop-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuResiPop")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuBachelorOrHigher-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuBachelorOrHigher")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '18%', 'display': 'inline-block', 'marginRight': '1%','marginLeft' : '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okAge-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okAge")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '28%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okCareer-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okCareer")]
                        )
                    ]
                ),
                html.Div(
                    className = 'vertical'
                ),
                html.Div(
                    style = {'width': '18%', 'display': 'inline-block', 'marginRight': '1%','marginLeft' : '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuAge-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuAge")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '28%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuCareer-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuCareer")]
                            )
                        ]
                    ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft' : '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okCombinedCrime-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okCombinedCrime")]
                            )
                        ]
                    ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "okMedianHouseholdIncome-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "okMedianHouseholdIncome")]
                        )
                    ]
                ),
                html.Div(
                    className = 'vertical'
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginLeft' : '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuCombinedCrime-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuCombinedCrime")]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '23%', 'display': 'inline-block', 'marginRight': '1%', 'marginBottom': '1%', 'marginTop': '1%'},
                    id = "tuMedianHouseholdIncome-outer",
                    children = [
                        html.Div(
                            children = [dcc.Graph(id = "tuMedianHouseholdIncome")]
                        )
                    ]
                ),
            ]
        )
    ]
)
def generate_ok_unemploy(county):
    filter = ["DATE", county]
    filter_df = ok_unemploy[(filter)]
    filter_col = filter_df.iloc[:,1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),
                )
        ],
        'layout': go.Layout(
            title = "Unemployment Rate in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Percent', 'color': '#2cfec1'},
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_tu_unemploy(county):
    filter = ["DATE", county]
    filter_df = tu_unemploy[(filter)]
    filter_col = filter_df.iloc[:,1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),
                )
        ],
        'layout': go.Layout(
            title = "Unemployment Rate in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Percent', 'color': '#2cfec1'},
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_ok_age(county):
    filter_df = okPPL[okPPL['CTYNAME'].str.contains(county)]
    pct = filter_df.iloc[:,2:6].values.tolist()
    groups = filter_df.columns[2:6].tolist()
    colors = ['#e98074', '9fcbdf']
    return{
        'data': [
            go.Pie(
                labels = groups,
                values = pct[0],
                textfont = dict(size = 15),
                marker = dict(colors = colors,
                line = dict(color = '#2cfec1', width = 2)),
                hole = 0.3
            )
        ],
        'layout': go.Layout(
            title = "Population by Age Group in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f",
            margin = dict(t=90, l=30, r=1, b=10)
            )
    }

def generate_tu_age(county):
    filter_df = tuPPL[tuPPL['CTYNAME'].str.contains(county)]
    pct = filter_df.iloc[:,2:6].values.tolist()
    groups = filter_df.columns[2:6].tolist()
    colors = ['#e98074', '9fcbdf']
    return{
        'data': [
            go.Pie(
                labels = groups,
                values = pct[0],
                textfont = dict(size = 15),
                marker = dict(colors = colors,
                line = dict(color = '#2cfec1', width = 2)),
                hole = 0.3
            )
        ],
        'layout': go.Layout(
            title = "Population by Age Group in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f",
            margin = dict(t=90, l=30, r=1, b=10)
            )
    }

def generate_ok_resiPop(county):
    filter = ["DATE", county]
    filter_df = ok_resiPop[(filter)]
    filter_col = filter_df.iloc[:, 1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),

            )
        ],
        'layout': go.Layout(
            title = "Resident Population in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            yaxis = {'title': 'Thousands of Persons', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_tu_resiPop(county):
    filter = ["DATE", county]
    filter_df = tu_resiPop[(filter)]
    filter_col = filter_df.iloc[:, 1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),

            )
        ],
        'layout': go.Layout(
            title = "Resident Population in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            yaxis = {'title': 'Thousands of Persons', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_ok_bachelorOrHigher(county):
    filter = ["DATE", county]
    filter_df = ok_bachelorOrHigher[(filter)]
    filter_col = filter_df.iloc[:, 1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),

            )
        ],
        'layout': go.Layout(
            title = "Bachelor Degree or Higher in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            yaxis = {'title': 'Thousands of Persons', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_tu_bachelorOrHigher(county):
    filter = ["DATE", county]
    filter_df = tu_bachelorOrHigher[(filter)]
    filter_col = filter_df.iloc[:, 1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),

            )
        ],
        'layout': go.Layout(
            title = "Bachelor Degree or Higher in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            yaxis = {'title': 'Thousands of Persons', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_ok_career(county):
    filter_df = ok_career[ok_career['County'].str.contains(county)]
    pct = filter_df.iloc[:,2:7].values.tolist()
    groups = filter_df.columns[2:7].tolist()
    colors = ['#e98074', '9fcbdf']
    return{
        'data': [
            go.Bar(
                x = groups,
                y = pct[0],
                marker_color = '#9fcbdf',
                opacity = 0.7,
                marker_line_width = 1.5
                )
        ],
        'layout': go.Layout(
            title = "Career Type in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Percent %'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_tu_career(county):
    filter_df = tu_career[tu_career['County'].str.contains(county)]
    pct = filter_df.iloc[:,2:7].values.tolist()
    groups = filter_df.columns[2:7].tolist()
    colors = ['#e98074', '9fcbdf']
    return{
        'data': [
            go.Bar(
                x = groups,
                y = pct[0],
                marker_color = '#9fcbdf',
                opacity = 0.7,
                marker_line_width = 1.5
                )
        ],
        'layout': go.Layout(
            title = "Career Type in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Percent %'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_ok_combinedCrime(county):
    filter = ["DATE", county]
    filter_df = ok_combinedCrime[(filter)]
    filter_col = filter_df.iloc[:, 1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),

            )
        ],
        'layout': go.Layout(
            title = "Violent and Property Crime in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            yaxis = {'title': 'Incidents', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_tu_combinedCrime(county):
    filter = ["DATE", county]
    filter_df = tu_combinedCrime[(filter)]
    filter_col = filter_df.iloc[:, 1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),

            )
        ],
        'layout': go.Layout(
            title = "Violent and Property Crime in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            yaxis = {'title': 'Incidents', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_ok_homeownership(county):
    filter = ["DATE", county]
    filter_df = ok_homeownership[(filter)]
    filter_col = filter_df.iloc[:,1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),
                )
        ],
        'layout': go.Layout(
            title = "Homeownership Rate in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Percent', 'color': '#2cfec1'},
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_tu_homeownership(county):
    filter = ["DATE", county]
    filter_df = tu_homeownership[(filter)]
    filter_col = filter_df.iloc[:,1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),
                )
        ],
        'layout': go.Layout(
            title = "Homeownership Rate in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Percent', 'color': '#2cfec1'},
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_ok_medianDays(county):
    filter = ["DATE", county]
    filter_df = ok_medianDaysOnMarket[(filter)]
    filter_col = filter_df.iloc[:,1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),
                )
        ],
        'layout': go.Layout(
            title = "Median Days On Market in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Days', 'color': '#2cfec1'},
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_tu_medianDays(county):
    filter = ["DATE", county]
    filter_df = tu_medianDaysOnMarket[(filter)]
    filter_col = filter_df.iloc[:,1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),
                )
        ],
        'layout': go.Layout(
            title = "Median Days on Market in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Days', 'color': '#2cfec1'},
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_ok_medianHouseholdIncome(county):
    filter = ["DATE", county]
    filter_df = ok_medianHouseholdIncome[(filter)]
    filter_col = filter_df.iloc[:,1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),
                )
        ],
        'layout': go.Layout(
            title = "Median Household Income in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Dollars', 'color': '#2cfec1'},
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_tu_medianHouseholdIncome(county):
    filter = ["DATE", county]
    filter_df = tu_medianHouseholdIncome[(filter)]
    filter_col = filter_df.iloc[:,1]
    return{
        'data': [
            go.Scatter(
                x = filter_df.DATE,
                y = filter_col,
                line = dict(color = '#2cfec1', width = 3),
                )
        ],
        'layout': go.Layout(
            title = "Median Household Income in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Dollas', 'color': '#2cfec1'},
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_ok_race(county):
    filter_df = ok_race[ok_race['County'].str.contains(county)]
    pct = filter_df.iloc[:,1:7].values.tolist()
    groups = filter_df.columns[1:7].tolist()
    colors = ['#e98074', '9fcbdf']
    return{
        'data': [
            go.Pie(
                labels = groups,
                values = pct[0],
                textfont = dict(size = 15),
                marker = dict(colors = colors,
                line = dict(color = '#2cfec1', width = 2)),
                hole = 0.3
            )
        ],
        'layout': go.Layout(
            title = "Population by Race in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f",
            margin = dict(t=90, l=30, r=1, b=10)
            )
    }

def generate_tu_race(county):
    filter_df = tu_race[tu_race['County'].str.contains(county)]
    pct = filter_df.iloc[:,1:7].values.tolist()
    groups = filter_df.columns[1:7].tolist()
    colors = ['#e98074', '9fcbdf']
    return{
        'data': [
            go.Pie(
                labels = groups,
                values = pct[0],
                textfont = dict(size = 15),
                marker = dict(colors = colors,
                line = dict(color = '#2cfec1', width = 2)),
                hole = 0.3
            )
        ],
        'layout': go.Layout(
            title = "Population by Race in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f",
            margin = dict(t=90, l=30, r=1, b=10)
            )
    }

def generate_ok_disaster_histogram(county):
    filter_df = ok_disaster[ok_disaster['designatedArea'].str.contains(county)]
    return{
        'data': [
            go.Histogram(
                x = filter_df['incidentType'],
                marker_color = '#9fcbdf',
                opacity = 0.7,
                marker_line_width = 1.5
                )
        ],
        'layout': go.Layout(
            title = "Histogram of Disaster in <b>{0}</b>, <b>{1}</b> -- since 1966 to 2020".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Count'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_tu_disaster_histogram(county):
    filter_df = tu_disaster[tu_disaster['designatedArea'].str.contains(county)]
    return{
        'data': [
            go.Histogram(
                x = filter_df['incidentType'],
                marker_color = '#9fcbdf',
                opacity = 0.7,
                marker_line_width = 1.5
                )
        ],
        'layout': go.Layout(
            title = "Histogram of Disaster in <b>{0}</b>, <b>{1}</b> -- since 1966 to 2020".format(county, "OK"),
            font = dict(family = 'Roboto', color = '#2cfec1'),
            yaxis = {'title': 'Count'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"
        )
    }

def generate_ok_housingPrice(county, dd_select):

    if dd_select == "bed1":
        housedata = ok_1bed
        print(housedata)
    elif dd_select == "bed2":
        housedata = ok_2bed
        print(housedata)
    elif dd_select == "bed3":
        housedata = ok_3bed
        print(housedata)
    elif dd_select == "bed4":
        housedata = ok_4bed
        print(housedata)
    else:
        housedata = ok_5bed
        print(housedata)
    date = housedata.columns[2:52].tolist()
    filter_df = housedata[housedata['RegionName'].str.contains(county)]
    prices = filter_df.iloc[:, 2:52].values

    return{
        'data': [
            go.Scatter(
                x = date,
                y = prices[0],
                line = dict(color = '#2cfec1', width = 3),

            )
        ],
        'layout': go.Layout(
            title = "Home Values in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            yaxis = {'title': 'Dollars'},
            font = dict(family = 'Roboto', color = '#2cfec1'),
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"

        )
    }

def generate_tu_housingPrice(county, dd_select):

    if dd_select == "bed1":
        housedata = tu_1bed
        print(housedata)
    elif dd_select == "bed2":
        housedata = tu_2bed
        print(housedata)
    elif dd_select == "bed3":
        housedata = tu_3bed
        print(housedata)
    elif dd_select == "bed4":
        housedata = tu_4bed
        print(housedata)
    else:
        housedata = tu_5bed
        print(housedata)
    date = housedata.columns[2:52].tolist()
    filter_df = housedata[housedata['RegionName'].str.contains(county)]
    prices = filter_df.iloc[:, 2:52].values

    return{
        'data': [
            go.Scatter(
                x = date,
                y = prices[0],
                line = dict(color = '#2cfec1', width = 3),

            )
        ],
        'layout': go.Layout(
            title = "Home Values in <b>{0}</b>, <b>{1}</b>".format(county, "OK"),
            yaxis = {'title': 'Dollars'},
            font = dict(family = 'Roboto', color = '#2cfec1'),
            xaxis = {'title': 'Time', 'color': '#2cfec1'},
            paper_bgcolor = "#252e3f",
            plot_bgcolor = "#252e3f"

        )
    }
@app.callback(Output("okUnemployRate", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okUnemploy_rate(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_unemploy(county[0])
    else:
        return generate_ok_unemploy("Oklahoma")

@app.callback(Output("tuUnemployRate", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuUnemploy_rate(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_unemploy(county[0])
    else:
        return generate_tu_unemploy("Tulsa")

@app.callback(Output("okAge", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okAge_pie(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_age(county[0])
    else:
        return generate_ok_age("Oklahoma")

@app.callback(Output("tuAge", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuAge_pie(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_age(county[0])
    else:
        return generate_tu_age("Tulsa")

@app.callback(Output("okResiPop", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okResiPop(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_resiPop(county[0])
    else:
        return generate_ok_resiPop("Oklahoma")

@app.callback(Output("tuResiPop", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuResiPop(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_resiPop(county[0])
    else:
        return generate_tu_resiPop("Tulsa")

@app.callback(Output("okBachelorOrHigher", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okBachelorOrHigher(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_bachelorOrHigher(county[0])
    else:
        return generate_ok_bachelorOrHigher("Oklahoma")

@app.callback(Output("tuBachelorOrHigher", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_turesiPop(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_bachelorOrHigher(county[0])
    else:
        return generate_tu_bachelorOrHigher("Tulsa")

@app.callback(Output("okCareer", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okCareer(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_career(county[0])
    else:
        return generate_ok_career("Oklahoma")

@app.callback(Output("tuCareer", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuCareer(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_career(county[0])
    else:
        return generate_tu_career("Tulsa")

@app.callback(Output("okCombinedCrime", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okCombinedCrime(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_combinedCrime(county[0])
    else:
        return generate_ok_combinedCrime("Oklahoma")

@app.callback(Output("tuCombinedCrime", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuCombinedCrime(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_combinedCrime(county[0])
    else:
        return generate_tu_combinedCrime("Tulsa")

@app.callback(Output("okHomeownership", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okHomeownership(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_homeownership(county[0])
    else:
        return generate_ok_homeownership("Oklahoma")

@app.callback(Output("tuHomeownership", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuHomeownership(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_homeownership(county[0])
    else:
        return generate_tu_homeownership("Tulsa")

@app.callback(Output("okMedianDays", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okMedianDays(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_medianDays(county[0])
    else:
        return generate_ok_medianDays("Oklahoma")

@app.callback(Output("tuMedianDays", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuMedianDays(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_medianDays(county[0])
    else:
        return generate_tu_medianDays("Tulsa")

@app.callback(Output("okMedianHouseholdIncome", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okMedianHouseholdIncome(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_medianHouseholdIncome(county[0])
    else:
        return generate_ok_medianHouseholdIncome("Oklahoma")

@app.callback(Output("tuMedianHouseholdIncome", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuMedianHouseholdIncome(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_medianHouseholdIncome(county[0])
    else:
        return generate_tu_medianHouseholdIncome("Tulsa")

@app.callback(Output("okRace", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okRace(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_race(county[0])
    else:
        return generate_ok_race("Oklahoma")

@app.callback(Output("tuRace", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuRace(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_race(county[0])
    else:
        return generate_tu_race("Tulsa")

@app.callback(Output("okDisaster", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure")])
def update_okDisaster(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_disaster_histogram(county[0])
    else:
        return generate_ok_disaster_histogram("Oklahoma")

@app.callback(Output("tuDisaster", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure")])
def update_tuDisaster(choro_click, choro_figure):
    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_disaster_histogram(county[0])
    else:
        return generate_tu_disaster_histogram("Tulsa")

@app.callback(Output("okHousingPrice", "figure"),
    [Input("ok-choropleth", "clickData"), Input("ok-choropleth", "figure"),Input("ok-dropdown", "value")])
def update_ok_house_price(choro_click, choro_figure, dd_select):
    if dd_select is None:
        dd_select = "bed1"

    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_ok_housingPrice(county[0], dd_select)
    else:
        return generate_ok_housingPrice("Oklahoma", dd_select)

@app.callback(Output("tuHousingPrice", "figure"),
    [Input("tu-choropleth", "clickData"), Input("tu-choropleth", "figure"),Input("tu-dropdown", "value")])
def update_tu_house_price(choro_click, choro_figure, dd_select):
    if dd_select is None:
        dd_select = "bed1"

    if choro_click is not None:
        county = []
        for point in choro_click["points"]:
            county.append(point["location"])
        return generate_tu_housingPrice(county[0], dd_select)
    else:
        return generate_tu_housingPrice("Tulsa", dd_select)
