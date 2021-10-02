import dash
from flask import Flask
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

server = Flask(__name__)
app = dash.Dash(server=server,external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)
colors = {'background': '#02000d','text': '#f2f7f7','text2': '#180599','error':'#a83240'}

app.layout = html.Div([

    dbc.Row(dbc.Col(html.H1(children='Life Expectancy Vs GDP per Capita Income',
            style={
            'textAlign': 'center',
            'color': colors['text'],
            'font_size':'50px',
            'backgroundColor':colors['background']
             }))),
    
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0',port = 8050,debug=False) #FOR DOCKER IMAGE
    #app.run_server(port = 8050,debug=False)
