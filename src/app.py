import dash
import dash_html_components as html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1("Simple Dash Application"),
        html.P("This is a basic example of a Dash application."),
        html.Div("Hello, Dash!")
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)