# Import the required packages using their usual aliases:
import dash
import dash_html_components as html

# Create (instantiate) the app:
app = dash.Dash(__name__)

# Create the app's layout:
app.layout = html.Div([
    html.H1('Hello World!')
])

# Run the app:
if __name__=="__main__":
    app.run_server(debug=True)