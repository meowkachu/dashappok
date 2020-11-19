import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os
import pathlib
import joblib
import sklearn
from sklearn.linear_model import Lasso
import numpy as np
import pandas as pd
from app import app

BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("../datasets").resolve()

model = joblib.load(DATA_PATH.joinpath("lassoModel.pkl"))

# Div for age
input_age = dcc.Input(
    id='age',
    type='number',
    value=30)

div_age = html.Div(
        children=[html.H3('Age:'), input_age],
        className="Row"
        )

# Div for work hours
input_wkhp = dcc.Input(
    id='wkhp',
    type='number',
    value=40)

div_wkhp = html.Div(
        children=[html.H3('Work Hours Per Week:'), input_wkhp],
        className="Row"
        )


# Div for onlyEnglish
onlyEnglish_values = ['Yes', 'No']
onlyEnglish_options = [{'label': x, 'value': x} for x in onlyEnglish_values]
input_onlyEnglish = dcc.Dropdown(
    id='onlyEnglish',
    options = onlyEnglish_options,
    value = 'Yes'
    )

div_onlyEnglish = html.Div(
        children=[html.H3('Only Speaks English:'), input_onlyEnglish],
        className="Row"
        )

# Div for degree
degree_values = ['NoDiploma', 'HighSchool', 'Associate', 'Bachelor', 'Master', 'Professional', 'Doctorate']
degree_options = [{'label': x, 'value': x} for x in degree_values]
input_degree = dcc.Dropdown(
    id='degree',
    options = degree_options,
    value = 'Bachelor'
    )

div_degree = html.Div(
        children=[html.H3('Degree:'), input_degree],
        className="Row"
        )

# Div for race
race_values = ['White', 'Black', 'Asian', 'Native', 'Other']
race_options = [{'label': x, 'value': x} for x in race_values]
input_race = dcc.Dropdown(
    id='race',
    options = race_options,
    value = 'White'
    )

div_race = html.Div(
        children=[html.H3('Race:'), input_race],
        className="Row"
        )

# Div for Citizenship
citizen_values = ['Yes', 'No']
citizen_options = [{'label': x, 'value': x} for x in citizen_values]
input_citizen = dcc.Dropdown(
    id='citizen',
    options = citizen_options,
    value = 'Yes'
    )

div_citizen = html.Div(
        children=[html.H3('Citizenship:'), input_citizen],
        className="Row"
        )

# Div for industry
ind_values = ['BUS', 'CMM', 'ENG', 'FIN', 'MGR', 'SAL', 'SCI']
ind_options = [{'label': x, 'value': x} for x in ind_values]
input_ind = dcc.Dropdown(
    id='ind',
    options = ind_options,
    value = 'BUS'
    )

div_ind = html.Div(
        children=[html.H3('Occupation:'), input_ind],
        className="Row"
        )

# Div for Gender
gender_values = ['Male', 'Female']
gender_options = [{'label': x, 'value': x} for x in gender_values]
input_gender = dcc.Dropdown(
    id='gender',
    options = gender_options,
    value = 'Male'
    )

div_gender = html.Div(
        children=[html.H3('Gender:'), input_gender],
        className="Row"
        )

# Div for Stem
stem_values = ['Yes', 'No']
stem_options = [{'label': x, 'value': x} for x in stem_values]
input_stem = dcc.Dropdown(
    id='stem',
    options = stem_options,
    value = 'Yes'
    )

div_stem = html.Div(
        children=[html.H3('S.T.E.M. Degree:'), input_stem],
        className="Row"
        )

# Div for weeksWorked in the past 12 months
wkw_values = ['lessThan14', 'from50to52', 'from48to49', 'from40to47', 'from27to39', 'from14to26']
wkw_options = [{'label': x, 'value': x} for x in wkw_values]
input_wkw = dcc.Dropdown(
    id='wkw',
    options = wkw_options,
    value = 'from50to52'
    )

div_wkw = html.Div(
        children=[html.H3('Weeks Worked in the Past 12 Months:'), input_wkw],
        className="Row"
        )

# Div for class of worker
cow_values = ['Private_forProfit', 'Prvate_nonforProfit', 'Local_gov', 'State_gov', 'Federal_gov']
cow_options = [{'label': x, 'value': x} for x in cow_values]
input_cow = dcc.Dropdown(
    id='cow',
    options = cow_options,
    value = 'Private_forProfit'
    )

div_cow = html.Div(
        children=[html.H3('Class of Worker:'), input_cow],
        className="Row"
        )

def get_prediction(age, wkhp, onlyEnglish, degree, race, citizen, gender, stem, ind, wkw, cow):

    cols = ['AGEP', 'WKHP', 'onlyEnglish_No',
           'onlyEnglish_Yes', 'schLev_Associate', 'schLev_Bachelor',
           'schLev_Doctorate', 'schLev_HighSchool', 'schLev_Master',
           'schLev_NoDiploma', 'schLev_Professional', 'gender_Female',
           'gender_Male', 'citizen_No', 'citizen_Yes',
           'race_Asian', 'race_Black', 'race_Native', 'race_Other', 'race_White',
           'stem_No', 'stem_Yes', 'industry_BUS',
           'industry_CMM', 'industry_ENG', 'industry_FIN', 'industry_MGR',
           'industry_SAL', 'industry_SCI', 'weeksWorked_from14to26',
           'weeksWorked_from27to39', 'weeksWorked_from40to47',
           'weeksWorked_from48to49', 'weeksWorked_from50to52',
           'weeksWorked_lessThan14', 'cow_Federal_gov', 'cow_Local_gov',
           'cow_Private_forProfit', 'cow_Prvate_nonforProfit', 'cow_State_gov']

    onlyEnglish_dict = {x: 'onlyEnglish_' + x for x in onlyEnglish_values[1:]}
    schLev_dict = {x: 'schLev_' + x for x in degree_values[1:]}
    citizen_dict = {x: 'citizen_' + x for x in citizen_values[1:]}
    race_dict = {x: 'race_' + x for x in race_values[1:]}
    stem_dict = {x: 'stem_' + x for x in stem_values[1:]}
    gender_dict = {x: 'gender_' + x for x in gender_values[1:]}
    ind_dict = {x: 'industry_' + x for x in ind_values[1:]}
    wkw_dict = {x: 'weeksWorked_' + x for x in wkw_values[1:]}
    cow_dict = {x: 'cow_' + x for x in cow_values[1:]}

    df = pd.DataFrame(data = np.zeros((1,len(cols))), columns = cols)

    df.loc[0,'AGEP'] = age
    df.loc[0,'WKHP'] = wkhp

#onlyEnglish_No, schLev_Associate, race_Asian, citizen_No,
#gender_Female, stem_No, IND_BUS, weeksWorked_from14to26,
#cow_Federal_gov
    if onlyEnglish!='Yes':
        df.loc[0, onlyEnglish_dict[onlyEnglish]] = 1

    if degree!='Associate':
        df.loc[0, schLev_dict[degree]] = 1

    if race!='White':
        df.loc[0, race_dict[race]] = 1

    if gender!='Male':
        df.loc[0, gender_dict[gender]] = 1

    if citizen!='Yes':
        df.loc[0, citizen_dict[citizen]] = 1

    if stem!='Yes':
        df.loc[0, stem_dict[stem]] = 1

    if ind!='BUS':
        df.loc[0, ind_dict[ind]] = 1

    if wkw!='from14to26':
        df.loc[0, wkw_dict[wkw]] = 1

    if cow!='Private_forProfit':
        df.loc[0, cow_dict[cow]] = 1


    prediction = model.predict(df.values).flatten()[0]

    return int(prediction)

layout = html.Div(className = "container", children = [
        html.Div(id = 'income-title', children = dcc.Markdown('''
                                            >
                                            >Enter the Personal Characteristics to Get the Predicted Income
                                            >
                                            '''
                                            )),
        html.Div(id = 'input-1num',
                children=[div_age]
                ),
        html.Div(id = 'input-2num',
                children=[div_wkhp]
                ),
        html.Div(id = 'input-1cal',
                children=[div_onlyEnglish]
                ),
        html.Div(id = 'input-2cal',
                children=[div_citizen]
                ),
        html.Div(id = 'input-3cal',
                children=[div_cow]
                ),
        html.Div(id = 'input-4cal',
                children=[div_degree]
                ),
        html.Div(id = 'input-5cal',
                children=[div_gender]
                ),
        html.Div(id = 'input-6cal',
                children=[div_ind]
                ),
        html.Div(id = 'input-7cal',
                children=[div_stem]
                ),
        html.Div(id = 'input-8cal',
                children=[div_wkw]
                ),
        html.Div(id = 'input-9cal',
                children=[div_race]
                ),
        html.H1(id='output',
                style={'margin-top': '50px', 'text-align': 'center'}),
        html.Div(className = 'instruction', children = [
                html.P(["*BUS - Business Administration Related",
                html.Br(),
                "CMM - Computer Science Related" ,
                html.Br(),
                "ENG - Engineering Related",
                html.Br(),
                "FIN - Finanace Related",
                html.Br(),
                "MGR - Manager Related",
                html.Br(),
                "SAL - Sales Related",
                html.Br(),
                "SCI - Scientist Related"])])


        ])

predictors = ['age', 'wkhp', 'onlyEnglish', 'degree', 'race', 'citizen', 'gender', 'stem', 'ind', 'wkw', 'cow']
@app.callback(Output('output', 'children'),
    [Input(x, 'value') for x in predictors])
def show_prediction(age, wkhp, onlyEnglish, degree, race, citizen, gender, stem, ind, wkw, cow):
    pred = get_prediction(age, wkhp, onlyEnglish, degree, race, citizen, gender, stem, ind, wkw, cow)
    return str("Predicted Income: {:,}".format(pred))
