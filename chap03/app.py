#  Uso de notebooks jupyter para rodar aplicativos Dash

## Importção dos pacotes requeridos
import dash_html_components as html
import dash_core_components as dcc
from jupyter_dash import JupyterDash
from dash.dependencies import Output, Input 

## Importação dos elementos gráficos
import plotly.graph_objects as go

##  Instanciação do 'app'
app = JupyterDash(__name)

## Layout do 'app'
app.layout = html.Div([
    html.H1('Criação dos primeiros gráficos')
])

## Rodar o 'app'
if __name__=='__main__':
    app.run_server(mode='inline')
