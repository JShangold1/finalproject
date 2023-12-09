from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_stock_data(stock_symbol):
    url = f"https://finance.yahoo.com/quote/{stock_symbol}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract relevant information from the Yahoo Finance page
        company_name = soup.find('h1', {'data-reactid': '7'}).text
        latest_price = soup.find('span', {'data-reactid': '50'}).text

        stock_data = {
            'company_name': company_name,
            'latest_price': latest_price,
        }

        return stock_data

    return None

def scrape_stock_projections(stock_symbol, interval):
    url = f"https://finance.yahoo.com/quote/{stock_symbol}/analysis?p={stock_symbol}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        projections = []

        # Example: Extract projections from elements with a specific class
        projection_elements = soup.find_all('td', class_='data-col2')
        for element in projection_elements:
            projection = element.get_text(strip=True)
            projections.append(projection)

        return projections

    return None

# ... (existing code)

# Update the get_stock_info route
@app.route('/get_stock_info', methods=['POST'])
def get_stock_info():
    stock_symbol = request.form.get('stock_symbol')
    initial_investment = float(request.form.get('initial_investment'))

    # Use web scraping to get stock information and projections
    stock_data = scrape_stock_data(stock_symbol)
    stock_projections = scrape_stock_projections(stock_symbol, interval=1)  # Change the interval as needed

    if stock_data and stock_projections:
        stock_data['symbol'] = stock_symbol
        stock_data['projections'] = stock_projections

        return render_template('index.html', stock_info=stock_data, initial_investment=initial_investment)
    else:
        return render_template('index.html', stock_info=None)

# ... (existing code)
