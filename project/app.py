import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import requests
from bs4 import BeautifulSoup

def get_sp500_symbols():
    # Fetching the list of S&P 500 stocks from Wikipedia
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    symbols = [row.find_all('td')[0].text.strip() for row in table.find_all('tr')[1:]]
    return symbols

def get_recommendation(investment_amount, risk_score, timeline_days):
    # Fetching S&P 500 stock symbols
    stock_symbols = get_sp500_symbols()

    # Fetching historical stock data and training models for each stock
    valid_stock_data = {}
    for symbol in stock_symbols:
        stock_data = yf.download(symbol, period=f"{timeline_days}d")

        # Check if the stock_data is not empty
        if not stock_data.empty:
            stock_data['Date'] = stock_data.index
            stock_data['Date'] = pd.to_datetime(stock_data['Date']).astype('int64') / 10**9
            X = stock_data[['Date']].values
            y = stock_data['Close'].values

            # Training a linear regression model for each stock
            model = LinearRegression()
            model.fit(X, y)
            stock_data['Predicted'] = model.predict(X)

            valid_stock_data[symbol] = stock_data

    if not valid_stock_data:
        # No valid stock data found
        raise ValueError("No valid stock data found. Please check your stock symbols or try again later.")

    # Selecting the stock with the highest predicted growth rate
    selected_stock = max(valid_stock_data.keys(), key=lambda symbol: (valid_stock_data[symbol]['Predicted'].iloc[-1] - valid_stock_data[symbol]['Close'].iloc[-1]) / valid_stock_data[symbol]['Close'].iloc[-1])

    # Calculating the expected total amount including the initial investment
    final_date = valid_stock_data[selected_stock]['Date'].max() + (timeline_days * 24 * 60 * 60)
    expected_final_price = model.predict(np.array([[final_date]]))[0]
    expected_total_amount = investment_amount + (investment_amount * (expected_final_price - valid_stock_data[selected_stock]['Close'].iloc[-1]) / valid_stock_data[selected_stock]['Close'].iloc[-1])

    return selected_stock, expected_total_amount

# Taking user inputs
investment_amount = float(input("Enter your investment amount: "))
risk_score = int(input("Enter your risk score (1-10): "))
timeline_days = int(input("Enter your investment timeline in days: "))

# Getting recommendation
recommended_stock, expected_total_amount = get_recommendation(investment_amount, risk_score, timeline_days)

# Displaying recommendation
print(f"\nRecommended Stock: {recommended_stock}")
print(f"Expected Total Amount: ${expected_total_amount:.2f}")
