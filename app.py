import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Create sample data
data = pd.DataFrame({
    "State": ["Kentucky", "Kentucky", "Tennessee", "Tennessee"],
    "Year": [2018, 2019, 2018, 2019],
    "Prevalence Rate": [15, 16, 20, 22]
})

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Public Health Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Public Health Data Dashboard", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in data['State'].unique()],
        value=None,
        placeholder="Select a state",
    ),
    dcc.Graph(id='line-chart')
])

# Callback to update chart
@app.callback(
    Output('line-chart', 'figure'),
    [Input('state-dropdown', 'value')]
)
def update_chart(selected_state):
    filtered_data = data[data['State'] == selected_state] if selected_state else data
    fig = px.line(filtered_data, x="Year", y="Prevalence Rate", color="State",
                  title="HIV Prevalence Over Time")
    return fig

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
