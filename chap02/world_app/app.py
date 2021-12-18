from dash import html, dcc
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash
from dash.dependencies import Output, Input
import pandas as pd

poverty_data = pd.read_csv('./data/PovStatsData.csv')

app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    html.H1('Poverty and Equity Database'),
    html.H2('The World Bank'),
    html.Div([
    html.Div([
        html.P('Country'),
        dcc.Dropdown(
            id='country',
            options=[
                {'label':country, 'value':country} for country in \
                    poverty_data['Country Name'].unique()
        ]
        ),
    ],
    style = {'padding':'10px','width' : '90%'}),
    html.Div([
        html.P('Year'),
        dcc.Dropdown(
            id='year',
            options=[
                {'label':year, 'value':year} for year in range(1974, 2020)
            ]
        ),
    ],
    style = {'padding':'10px','width' : '90%'}),
    ],
    style = {
        'padding': '10px',
        'width' : '75%',
        'border-radius': '5px',
        'background-color': 'gray'
    }),


    html.Br(),
    html.Div([
        html.P(id='report')
    ])
])

@app.callback(Output('report', 'children'), Input('country', 'value'), Input('year', 'value'))
def display_country_report(country, year):
    if country is None or year is None:
        return ''
    filtered_df = poverty_data[
        (poverty_data['Country Name'] == country) & (poverty_data['Indicator Name']=='Population, total')
    ]
    population = filtered_df.loc[:, str(year)].values[0]
    return f'The population of {country} in {year} was {population:,.0f}.'

if __name__=="__main__":
    app.run_server(mode='inline', debug=True)