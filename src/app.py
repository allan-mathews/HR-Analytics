import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the dataset (adjust path as per your directory structure)
df = pd.read_csv('src/Data/HR_Analytics.csv')

# Define quantitative and qualitative features
quantitative_features = ['Age', 'DailyRate', 'DistanceFromHome',
                         'HourlyRate', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
                         'PercentSalaryHike', 'StockOptionLevel', 'TotalWorkingYears',
                         'TrainingTimesLastYear', 'YearsAtCompany',
                         'YearsInCurrentRole', 'YearsSinceLastPromotion',
                         'YearsWithCurrManager']

qualitative_features = [
    'Attrition', 'BusinessTravel', 'Department', 'EducationField', 'Gender', 'EnvironmentSatisfaction',
    'Education', 'JobSatisfaction', 'JobInvolvement', 'JobLevel', 'JobRole', 'MaritalStatus', 'OverTime',
    'WorkLifeBalance', 'PerformanceRating', 'RelationshipSatisfaction',
]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("IBM HR Analytics Dashboard"),
    
    # Dropdown for selecting analysis
    dcc.Dropdown(
        id='analysis-dropdown',
        options=[
            {'label': 'Attrition Overview', 'value': 'attrition_overview'},
            {'label': 'Monthly Income by Education', 'value': 'monthly_income_education'},
            {'label': 'Distance from Home by Job Role and Attrition', 'value': 'distance_from_home'},
            {'label': 'Job Satisfaction Overview', 'value': 'job_satisfaction'},
            {'label': 'Years at Company Distribution', 'value': 'years_at_company'},
            # Add more options as needed
        ],
        value='attrition_overview',
        style={'width': '50%'}
    ),
    
    # Placeholder for graph or table
    html.Div(id='output-container', children=[]),
])

# Callback to update output based on dropdown selection
@app.callback(
    Output('output-container', 'children'),
    [Input('analysis-dropdown', 'value')]
)
def update_output(selected_analysis):
    if selected_analysis == 'attrition_overview':
        # Create a bar chart of Attrition counts
        fig = px.histogram(df, x='Attrition', title='Attrition Overview')
        return dcc.Graph(figure=fig)
    
    elif selected_analysis == 'monthly_income_education':
        # Create a box plot of Monthly Income by Education
        fig = px.box(df, x='Education', y='MonthlyIncome', points='all', title='Monthly Income by Education')
        return dcc.Graph(figure=fig)
    
    elif selected_analysis == 'distance_from_home':
        # Create a bar chart of Distance from Home by Job Role and Attrition
        fig = px.bar(df, x='JobRole', y='DistanceFromHome', color='Attrition', barmode='group',
                     title='Distance from Home by Job Role and Attrition')
        return dcc.Graph(figure=fig)
    
    elif selected_analysis == 'job_satisfaction':
        # Create a grouped bar chart of Job Satisfaction by Attrition
        fig = px.bar(df, x='JobSatisfaction', color='Attrition', barmode='group',
                     title='Job Satisfaction Overview')
        return dcc.Graph(figure=fig)
    
    elif selected_analysis == 'years_at_company':
        # Create a histogram of Years at Company
        fig = px.histogram(df, x='YearsAtCompany', title='Years at Company Distribution')
        return dcc.Graph(figure=fig)
    
    else:
        return "No analysis selected."

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
