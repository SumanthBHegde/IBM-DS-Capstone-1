# Import required libraries
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'All Sites'},
                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                 ],
                 placeholder='Select a Launch Site Here',
                 value='All Sites',
                 searchable=True),
    html.Br(),
    
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    
    html.P("Payload range (Kg):"),
    
    dcc.RangeSlider(id='payload-slider',
                    min=0,
                    max=10000,
                    step=1000,
                    marks={i: f'{i}' for i in range(0, 10001, 1000)},
                    value=[min_payload, max_payload]),
    
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

@app.callback(Output('success-pie-chart', 'figure'),
              Input('site-dropdown', 'value'))
def get_pie_chart(launch_site):
    if launch_site == 'All Sites':
        fig = px.pie(values=spacex_df.groupby('Launch Site')['class'].mean(),
                     names=spacex_df.groupby('Launch Site')['Launch Site'].first(),
                     title='Total Success Launches by Site')
    else:
        site_df = spacex_df[spacex_df['Launch Site'] == launch_site]
        fig = px.pie(values=site_df['class'].value_counts(normalize=True),
                     names=site_df['class'].unique(),
                     title=f'Total Success Launches for Site {launch_site}')
    return fig

@app.callback(Output('success-payload-scatter-chart', 'figure'),
              [Input('site-dropdown', 'value'),
               Input('payload-slider', 'value')])
def get_payload_chart(launch_site, payload_mass):
    filtered_df = spacex_df[spacex_df['Payload Mass (kg)'].between(payload_mass[0], payload_mass[1])]
    
    if launch_site != 'All Sites':
        filtered_df = filtered_df[filtered_df['Launch Site'] == launch_site]
    
    fig = px.scatter(filtered_df,
                     x="Payload Mass (kg)",
                     y="class",
                     color="Booster Version Category",
                     hover_data=['Launch Site'],
                     title=f'Correlation Between Payload and Success for {launch_site}')
    return fig

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
