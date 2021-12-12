# Import the required packages using their usual aliases:
import dash
import dash_html_components as html

# Create (instantiate) the app:
app = dash.Dash(__name__)

# Create the app's layout:
app.layout = html.Div([
    html.H1(
        children='Poverty And Equity Database',
        style={
            'color': 'blue',
            'fontSize': '32px',
            'marginLeft': '20%'
        }
    ),
    html.H2('The World Bank'),
    html.P('Key Facts:'),
    html.Ul([
        html.Li('Number of Economies: 170'),
        html.Li('Temporal Coverage: 1974 - 2019'),
        html.Li('Update Frequency: Quarterly'),
        html.Li('Last Update: March 18, 2020'),
        html.Li([
            'Source: ',
            html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database', href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
        ])
    ])
])

# Run the app:
if __name__=="__main__":
    app.run_server(debug=True)