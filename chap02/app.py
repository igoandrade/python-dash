<<<<<<< HEAD
# Uso de notebooks Jupyter para rodar aplicativos Dash

## Inportação dos pacotes requeridos
import dash_html_components as html
import dash_core_components as dcc
from jupyter_dash import JupyterDash
from dash.dependencies import Output, Input

## Instanciação do 'app'
app = JupyterDash(__name__)

## Layout do 'app'
app.layout = html.Div([
    html.H1('OI'),
    dcc.Dropdown(
        id='color_dropdown',
        options=[
            {'label': color, 'value': color} for color in ['red', 'green', 'yellow']
        ]
    ),
    html.Br(),
    html.Div(id='color_output')
])


# Especificando a função de callback
@app.callback(Output(component_id='color_output', component_property='children'),\
              Input(component_id='color_dropdown', component_property='value'))
def display_selected_color(color):
    if color is None:
        color = 'nothing'
    return f'You selected {color}.'

## Rodar o 'app'
## app.run_server(mode='inline', height=600, width='80%')
if __name__=="__main__":
    app.run_server(mode='inline')
=======
# Uso de notebooks Jupyter para rodar aplicativos Dash

## Inportação dos pacotes requeridos
from dash import dcc, html
from jupyter_dash import JupyterDash
from dash.dependencies import Output, Input

## Instanciação do 'app'
app = JupyterDash(__name__)

## Layout do 'app'
app.layout = html.Div([
    html.H1('OI'),
    dcc.Dropdown(
        id='color_dropdown',
        options=[
            {'label': color, 'value': color} for color in ['red', 'green', 'yellow']
        ]
    ),
    html.Br(),
    html.Div(id='color_output')
])


# Especificando a função de callback
@app.callback(Output(component_id='color_output', component_property='children'),\
              Input(component_id='color_dropdown', component_property='value'))
def display_selected_color(color):
    if color is None:
        color = 'nothing'
    return f'You selected {color}.'

## Rodar o 'app'
## app.run_server(mode='inline', height=600, width='80%')
if __name__=="__main__":
    app.run_server(mode='inline')
>>>>>>> 6ebcfdb5871ded669bc417360e2bb327b40f9f9a
