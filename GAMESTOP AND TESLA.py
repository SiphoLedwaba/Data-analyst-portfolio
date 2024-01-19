import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
from dash import Dash, dcc, html

# Function to extract revenue data from a given URL
def extract_revenue(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "historical_data_table"})

    if table:
        rows = table.find_all("tr")
        if len(rows) > 1:
            cells = rows[1].find_all("td")
            if len(cells) > 1:
                return cells[1].text
            else:
                print("Error: Could not find cells in the second row.")
        else:
            print("Error: Could not find rows in the table.")
    else:
        print("Error: Could not find the historical_data_table.")

# Function to create a graph
def make_graph(data, title):
    return {
        'data': [
            {'x': data.index, 'y': data['Close'], 'type': 'line', 'name': title},
        ],
        'layout': {
            'title': title
        }
    }

# Specify the ticker for Tesla
tesla_ticker = "TSLA"

# Extracting stock data using yfinance
tesla_stock_data = yf.download(tesla_ticker, start="2022-01-01", end="2023-01-01")

# Specify the URL for Tesla's revenue
tesla_revenue_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla-inc/revenue"
revenue_data = extract_revenue(tesla_revenue_url)

# Display the last few rows of the stock data
print(tesla_stock_data.tail())

# Display the revenue data
print("Tesla Revenue:", revenue_data)

# Create a Tesla graph using the make_graph function
tesla_graph = make_graph(tesla_stock_data, "Tesla Stock Price Over Time")

# Specify the ticker for GameStop
gamestop_ticker = "GME"

# Extracting stock data using yfinance
gamestop_stock_data = yf.download(gamestop_ticker, start="2022-01-01", end="2023-01-01")

# Specify the URL for GameStop's revenue
gamestop_revenue_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
revenue_data_gamestop = extract_revenue(gamestop_revenue_url)

# Display the last few rows of the stock data
print(gamestop_stock_data.tail())

# Display the revenue data
print("GameStop Revenue:", revenue_data_gamestop)

# Create a GameStop graph using the make_graph function
gamestop_graph = make_graph(gamestop_stock_data, "GameStop Stock Price Over Time")

# Create a Dash app for Tesla
app_tesla = Dash(__name__)

# Define the layout of the Tesla dashboard
app_tesla.layout = html.Div([
    html.H1("Tesla Stock and Revenue Dashboard"),
    dcc.Graph(
        id='tesla-stock-chart',
        figure=tesla_graph  # Use the Tesla graph dictionary here
    ),
])

# Create a Dash app for GameStop
app_gamestop = Dash(__name__)

# Define the layout of the GameStop dashboard
app_gamestop.layout = html.Div([
    html.H1("GameStop Stock and Revenue Dashboard"),
    dcc.Graph(
        id='gamestop-stock-chart',
        figure=gamestop_graph  # Use the GameStop graph dictionary here
    ),
])

# Run the Tesla app
if __name__ == '__main__':
    app_tesla.run_server(debug=True)

# Run the GameStop app
if __name__ == '__main__':
    app_gamestop.run_server(debug=True)
