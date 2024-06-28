import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
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
            {'label': 'Age wise Attrition Analysis', 'value': 'Age-wise Attrition Analysis'},
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
    
    elif selected_analysis == 'Age-wise Attrition Analysis':
        # Create a grouped bar chart of Job Satisfaction by Attrition
        # Prepare the data
        age_att = df.groupby(['Age', 'Attrition']).size().reset_index(name='Counts')

        # Separate data for 'Yes' and 'No' attrition
        age_yes = age_att[age_att['Attrition'] == 'Yes']
        age_no = age_att[age_att['Attrition'] == 'No']

        # Create a bar chart
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=age_yes['Age'],
            y=age_yes['Counts'],
            name='Attrition: Yes',
            marker_color='indianred'
        ))

        fig.add_trace(go.Bar(
            x=age_no['Age'],
            y=age_no['Counts'],
            name='Attrition: No',
            marker_color='lightsalmon'
        ))

        # Add title and labels
        fig.update_layout(
            title='Age Distribution by Attrition Status',
            xaxis_title='Age',
            yaxis_title='Counts',
            barmode='group'
        )

        # Add annotations for highest and lowest attrition counts
        highest_attrition = age_yes.loc[age_yes['Counts'].idxmax()]
        # lowest_attrition = age_yes.loc[age_yes['Counts'].idxmin()]

        fig.add_annotation(
            x=highest_attrition['Age'],
            y=highest_attrition['Counts'],
            text='Highest Attrition',
            showarrow=True,
            arrowhead=1
        )

        # fig.add_annotation(
        #     x=lowest_attrition['Age'],
        #     y=lowest_attrition['Counts'],
        #     text='Lowest Attrition',
        #     showarrow=True,
        #     arrowhead=1
        # )
        # fig = px.histogram(df, x='JobSatisfaction', color='Attrition', barmode='group', 
        #            title='Attrition by Job Satisfaction', 
        #            category_orders={'JobSatisfaction': ['1', '2', '3', '4']})
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
