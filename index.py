import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to app pages
from apps import dashboard, incomemodel


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className= 'browser-banner',
        children = [
            html.H2(children=html.Div([
                dcc.Link(id="h2-title1", children = 'Oklahoma v.s. Tulsa Overview          |', href='/apps/dashboard'),
                dcc.Link(id="h2-title2", children = '          |     Income Prediction Model', href='/apps/incomemodel'),
            ]),
        )
        ]
    ),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/dashboard':
        return dashboard.layout
    if pathname == '/apps/incomemodel':
        return incomemodel.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)
