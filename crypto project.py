import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import glob
import ipywidgets as widgets
from ipywidgets import interact
import warnings

def load_data(csv_files_path):
    """
    Load data from CSV files into a dictionary of DataFrames.

    Parameters:
    - csv_files_path (str): Path to the directory containing CSV files.

    Returns:
    - dict: Dictionary of DataFrames.
    """
    dataframes = {}
    csv_files = glob.glob(csv_files_path)

    for csv_file in csv_files:
        file_name = csv_file.split('\\')[-1].split('.')[0]
        dataframes[file_name] = pd.read_csv(csv_file)

    return dataframes

def combine_dataframes(dataframes):
    """
    Combine individual DataFrames into a single DataFrame.

    Parameters:
    - dataframes (dict): Dictionary of DataFrames.

    Returns:
    - pd.DataFrame: Combined DataFrame.
    """
    combined_df = pd.concat(dataframes.values(), ignore_index=True)
    return combined_df

def clean_and_process_data(combined_df):
    """
    Clean and process the combined DataFrame.

    Parameters:
    - combined_df (pd.DataFrame): Combined DataFrame.

    Returns:
    - pd.DataFrame: Cleaned and processed DataFrame.
    """
    #Handling missing values
    combined_df = combined_df.dropna()

    #Converting 'date' column to DateTime format
    combined_df['date'] = pd.to_datetime(combined_df['date'])

    return combined_df

def generate_compliance_metrics(combined_df):
    """
    Generate compliance metrics and add them to the DataFrame.

    Parameters:
    - combined_df (pd.DataFrame): Combined DataFrame.

    Returns:
    - pd.DataFrame: DataFrame with added compliance metrics.
    """
    combined_df['Daily Trading Volume'] = combined_df.groupby(['date', 'ticker'])['close'].transform('sum')
    combined_df['Volatility'] = combined_df['high'] - combined_df['low']
    combined_df['Number of Trades'] = combined_df.groupby(['date', 'ticker']).cumcount() + 1
    combined_df['Average Daily Close Price'] = combined_df.groupby(['date'])['close'].transform('mean')
    combined_df['Number of Unique Tickers Traded'] = combined_df.groupby(['date'])['ticker'].transform('nunique')

    return combined_df

def create_ticker_category_column(combined_df, unique_tickers_list):
    """
    Create a new column 'Ticker_Category' based on the unique tickers list.

    Parameters:
    - combined_df (pd.DataFrame): DataFrame to add the column to.
    - unique_tickers_list (list): List of unique tickers.

    Returns:
    - pd.DataFrame: DataFrame with added 'Ticker_Category' column.
    """
    combined_df['Ticker_Category'] = combined_df['ticker'].isin(unique_tickers_list)
    return combined_df

def generate_reports(combined_df):
    """
    Generate and save compliance reports.

    Parameters:
    - combined_df (pd.DataFrame): Combined DataFrame.

    Returns:
    - None
    """
    #Daily Trading Volume Report
    daily_volume_report = combined_df.groupby('date')['Daily Trading Volume'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=daily_volume_report, x='date', y='Daily Trading Volume', marker='o')
    plt.title('Daily Trading Volume Report')
    plt.xlabel('Date')
    plt.ylabel('Daily Trading Volume')
    plt.show()

    #Volatility Report
    volatility_report = combined_df.groupby('date')['Volatility'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=volatility_report, x='date', y='Volatility', marker='o')
    plt.title('Volatility Report')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.show()

    #Saving the generated reports to files
    daily_volume_report.to_csv('daily_trading_volume_report.csv', index=False)
    volatility_report.to_csv('volatility_report.csv', index=False)

def interactive_daily_volume_report(ticker):
    """
    Function to generate an interactive report for a specific ticker.

    Parameters:
    - ticker (str): Ticker symbol.

    Returns:
    - None
    """
    selected_ticker_report = combined_df[combined_df['ticker'] == ticker].groupby('date')['Daily Trading Volume'].sum().reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=selected_ticker_report, x='date', y='Daily Trading Volume', marker='o')
    plt.title(f'Daily Trading Volume Report for Ticker: {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Daily Trading Volume')
    plt.show()

#path to the directory containing CSV files
csv_files_path = r'C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Crypto\*.csv'

#Loading data
dataframes = load_data(csv_files_path)

#Combining DataFrames
combined_df = combine_dataframes(dataframes)

#Defining the list of unique tickers
unique_tickers_list = ['1INCH', 'AAVE', 'ADA', 'ALGO', 'ANKR', 'APE', 'AR', 'ASTR', 'ATOM', 'AUDIO',
 'AVAX', 'AXS', 'BAT', 'BCH', 'BICO', 'BNB', 'BSV', 'BTC', 'BTG', 'BTT', 'BUSD',
 'CAKE', 'CELO', 'CFX', 'CHZ', 'COMP', 'CRO', 'CRV', 'CSPR', 'CVX', 'DAI', 'DASH',
 'DCR', 'DESO', 'DOGE', 'DOT', 'EGLD', 'ELF', 'ENJ', 'ENS', 'EOS', 'ETC', 'ETH',
 'ETHW', 'FET', 'FIL', 'FLOW', 'FLUX', 'FTM', 'FTT', 'FXS', 'GALA', 'GLM', 'GLMR',
 'GMT', 'GNO', 'GRT', 'GT', 'HBAR', 'HNT', 'HOT', 'HT', 'ICP', 'ICX', 'ILV', 'IMX',
 'INJ', 'IOTA', 'IOTX', 'JST', 'KAVA', 'KCS', 'KDA', 'KLAY', 'KSM', 'LDO', 'LEO',
 'LINK', 'LPT', 'LRC', 'LTC', 'MANA', 'MATIC', 'METIS', 'MINA', 'MKR', 'MOBILE',
 'MOVR', 'MX', 'NEAR', 'NEO', 'NEXO', 'NFT', 'OCEAN', 'OKB', 'ONE', 'ONT', 'OSMO',
 'PAXG', 'QNT', 'QTUM', 'RAY', 'RNDR', 'ROSE', 'RPL', 'RUNE', 'RVN', 'SAND', 'SC',
 'SHIB', 'SKL', 'SNX', 'SOL', 'SSV', 'STORJ', 'STX', 'SUPER', 'SUSHI', 'SXP', 'T',
 'TFUEL', 'THETA', 'TRAC', 'TRX', 'TUSD', 'TWT', 'UNI', 'USDC', 'USDD', 'USDT',
 'VET', 'WAVES', 'WAXP', 'WEMIX', 'WOO', 'XAUt', 'XCH', 'XDC', 'XEC', 'XEM', 'XLM',
 'XMR', 'XRP', 'XTZ', 'YFI', 'ZEC', 'ZIL', 'ZRX']

#Creating 'Ticker_Category' column
combined_df = create_ticker_category_column(combined_df, unique_tickers_list)

#Cleaning and processing data
combined_df = clean_and_process_data(combined_df)

#Generating compliance metrics
combined_df = generate_compliance_metrics(combined_df)

#Saving the cleaned and processed DataFrame to a CSV file
cleaned_data_path = r'C:\Users\Snipes\OneDrive\Documents\DA Portfolio-20230122T081035Z-001\DA Portfolio\Crypto\cleaned_data.csv'
combined_df.to_csv(cleaned_data_path, index=False)
print(f"Cleaned data saved to: {cleaned_data_path}")

#Generating reports
generate_reports(combined_df)

#Creating a dropdown widget with unique tickers
ticker_dropdown = widgets.Dropdown(options=combined_df['ticker'].unique(), description='Select Ticker:')

#Using the interact function to update the report based on selected ticker
interact(interactive_daily_volume_report, ticker=ticker_dropdown)

# Example: Test the report generator for multiple tickers
tickers_to_test = ['BTC', 'ETH', 'XRP']

for ticker in tickers_to_test:
    interactive_daily_volume_report(ticker)

#Creating interactive daily trading volume report using Plotly
fig = px.line(combined_df, x='date', y='Daily Trading Volume', color='ticker', title='Interactive Daily Trading Volume Report')
fig.update_layout(xaxis_title='Date', yaxis_title='Daily Trading Volume')
fig.show()

#Suppressing specific warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="_plotly_utils.basevalidators")
