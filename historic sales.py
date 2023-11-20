import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Excel file
file_path = r"C:\Users\Snipes\Downloads\Historic automotive sales\historical_automobile_sales.xlsx"
df = pd.read_excel(file_path)

# Convert 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Print a message
print('Data downloaded and read into a dataframe!')

# Task 1.1: Line chart for automobile sales fluctuation from year to year
df['Year'] = df['Date'].dt.year
average_sales_per_year = df.groupby('Year')['Automobile_Sales'].mean()

plt.figure(figsize=(10, 6))
average_sales_per_year.plot(kind='line', marker='o')
plt.title('Automobile Sales during Recession')
plt.xlabel('Year')
plt.ylabel('Average Automobile Sales')
plt.xticks(ticks=average_sales_per_year.index, labels=average_sales_per_year.index, rotation=45)
plt.annotate('Recession 1', xy=(1980, average_sales_per_year.loc[1980]), xytext=(1980, average_sales_per_year.loc[1980] + 500),
             arrowprops=dict(facecolor='red', arrowstyle='->'))
plt.annotate('Recession 5', xy=(2008, average_sales_per_year.loc[2008]), xytext=(2008, average_sales_per_year.loc[2008] + 500),
             arrowprops=dict(facecolor='red', arrowstyle='->'))
plt.show()

# Task 1.2: Line chart for different vehicle types
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Automobile_Sales', hue='Vehicle_Type', data=df)
plt.title('Automobile Sales Trends by Vehicle Type during Recession')
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.show()

# Task 1.3: Bar chart for sales trend per vehicle type for recession and non-recession periods
plt.figure(figsize=(12, 8))
sns.barplot(x='Year', y='Automobile_Sales', hue='Vehicle_Type', data=df)
plt.title('Sales Trend per Vehicle Type - Recession vs Non-Recession')
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.show()

# Task 1.4: Subplot for variations in GDP during recession and non-recession
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
sns.lineplot(x='Year', y='GDP', data=df[df['Recession'] == 1])
plt.title('GDP during Recession')
plt.xlabel('Year')
plt.ylabel('GDP')

plt.subplot(2, 1, 2)
sns.lineplot(x='Year', y='GDP', data=df[df['Recession'] == 0])
plt.title('GDP during Non-Recession')
plt.xlabel('Year')
plt.ylabel('GDP')

plt.tight_layout()
plt.show()

# Task 1.5: Bubble plot for the impact of seasonality on Automobile Sales
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Month', y='Automobile_Sales', size='Seasonality_Weight', data=df[df['Recession'] == 0])
plt.title('Seasonality Impact on Automobile Sales')
plt.xlabel('Month')
plt.ylabel('Automobile Sales')
plt.show()

# Task 1.6: Scatter plot for correlation between average vehicle price and sales volume during recessions
plt.figure(figsize=(10, 6))
plt.scatter(df['Price'], df['Automobile_Sales'])
plt.title('Correlation between Average Vehicle Price and Sales Volume during Recessions')
plt.xlabel('Average Vehicle Price')
plt.ylabel('Automobile Sales')
plt.show()

# Task 1.7: Pie chart for advertising expenditure during recession and non-recession periods
expenditure_by_recession = df.groupby('Recession')['Advertising_Expenditure'].sum()
plt.figure(figsize=(8, 8))
plt.pie(expenditure_by_recession, labels=['Non-Recession', 'Recession'], autopct='%1.1f%%', startangle=90)
plt.title('Advertising Expenditure during Recession and Non-Recession Periods')
plt.show()

# Task 1.8: Pie chart for total Advertisement expenditure for each vehicle type during recession period
expenditure_by_type = df[df['Recession'] == 1].groupby('Vehicle_Type')['Advertising_Expenditure'].sum()
plt.figure(figsize=(8, 8))
plt.pie(expenditure_by_type, labels=expenditure_by_type.index, autopct='%1.1f%%', startangle=90)
plt.title('Total Advertisement Expenditure for Each Vehicle Type during Recession Period')
plt.show()

# Task 1.9: Count plot for the effect of the unemployment rate on vehicle type and sales during the Recession Period
plt.figure(figsize=(12, 8))
sns.countplot(x='Vehicle_Type', hue='unemployment_rate', data=df[df['Recession'] == 1])
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales during Recession')
plt.xlabel('Vehicle Type')
plt.ylabel('Count')
plt.show()

# loading packages
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_excel(r"C:\Users\Snipes\Downloads\Historic automotive sales\historical_automobile_sales.xlsx")

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the layout of the app
app.layout = html.Div([
    html.H1("Automobile Statistics Dashboard"),
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='select-statistics',
            options=[
                {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
            ],
            value='Yearly Statistics',
            placeholder='Select Statistics'
        )
    ]),
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': year, 'value': year} for year in data['Year'].unique()],
            value=data['Year'].min(),
            placeholder='Select Year'
        )
    ]),
    html.Div(id='output-figures', className='output-container')
])

# Callback for output container
@app.callback(
    Output(component_id='output-figures', component_property='children'),
    [Input(component_id='select-statistics', component_property='value'),
     Input(component_id='select-year', component_property='value')]
)
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        # Charts based on recession data
        fig_line = px.line(data[data['Year'] == input_year], x='Date', y='Recession')
        fig_bar = px.bar(data[data['Year'] == input_year], x='Month', y='Recession')
        fig_pie = px.pie(data[data['Year'] == input_year], values='Recession', names='Month')
        fig_scatter = px.scatter(data[data['Year'] == input_year], x='Date', y='Recession')

        return [
            dcc.Graph(figure=fig_line),
            dcc.Graph(figure=fig_bar),
            dcc.Graph(figure=fig_pie),
            dcc.Graph(figure=fig_scatter)
        ]

    elif selected_statistics == 'Yearly Statistics' and input_year:
        # Charts based on yearly data
        fig_line = px.line(data[data['Year'] == input_year], x='Month', y='Automobile_Sales')
        fig_bar = px.bar(data[data['Year'] == input_year], x='Month', y='Automobile_Sales')
        fig_pie = px.pie(data[data['Year'] == input_year], values='Automobile_Sales', names='Month')
        fig_scatter = px.scatter(data[data['Year'] == input_year], x='Month', y='Automobile_Sales')

        return [
            dcc.Graph(figure=fig_line),
            dcc.Graph(figure=fig_bar),
            dcc.Graph(figure=fig_pie),
            dcc.Graph(figure=fig_scatter)
        ]

    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

