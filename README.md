# HR Analytics

## Overview

This project is an interactive dashboard developed using Dash Plotly to visualize and analyze the IBM HR Analytics Employee Attrition & Performance dataset. The primary goal is to uncover the factors that lead to employee attrition and explore various aspects of employee performance, satisfaction, and other HR-related metrics.

## Dataset

- **Dataset Name**: IBM HR Analytics Employee Attrition & Performance
- **Source**: [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/data)
- **Description**: This dataset is a fictional set created by IBM data scientists to understand the factors contributing to employee attrition and performance. It includes various attributes related to employees' personal and professional aspects.

## Features

| Hierarchy_Level                  | Education Levels | Environment Satisfaction | Job Involvement | Job Satisfaction | Performance Rating | Relationship Satisfaction | Work-Life Balance |
|--------------------------|------------------|---------------------------|-----------------|------------------|--------------------|----------------------------|-------------------|
| 1                  | Below College    | Low                       | Low             | Low              | Low                | Low                        | Bad               |
| 2                  | College          | Medium                    | Medium          | Medium           | Good               | Medium                     | Good              |
| 3                  | Bachelor         | High                      | High            | High             | Excellent          | High                       | Better            |
| 4                  | Master           | Very High                 | Very High       | Very High        | Outstanding        | Very High                  | Best              |
| 5                  | Doctor           | -                         | -               | -                | -                  | -                          | -                 |

## Project Objectives

1. **Analyze Employee Attrition**: Uncover key factors that lead to employee attrition.
2. **Explore Job Roles and Distance from Home**: Break down the distance from home by job role and attrition status.
3. **Compare Income by Education and Attrition**: Compare the average monthly income based on education level and attrition status.
4. **Visualize Satisfaction and Performance Metrics**: Visualize different satisfaction metrics and performance ratings across various employee demographics.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hr-analytics-dashboard.git
   cd hr-analytics-dashboard


2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to `http://127.0.0.1:8050/` to view the dashboard.

## Project Structure

```
hr-analytics-dashboard/
│
├── src/                     # Source folder
│   ├── app.py               # Main application file
│   ├── assets/              # Folder for CSS and JS files
│   └── data/                # Folder for dataset files
│       └── HR_Analytics.csv # Dataset file
├── requirements.txt         # Required packages
├── README.md                # Project README
└── screenshots/             # Folder for screenshots of the dashboard
```

This structure reflects the inclusion of the "src" folder, where the application files are located.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- IBM for creating the fictional HR dataset.
- Dash Plotly for providing the tools to build interactive web applications.
- Kaggle for hosting the dataset.

```
df1.drop(columns=['Over18','EmployeeNumber'])
```
