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

def get_stock_projection(stock_symbol, months):
    # Placeholder logic: Assume a constant growth rate for demonstration purposes
    # In a real-world scenario, you might use financial libraries or APIs for accurate projections
    growth_rate = 0.02  # 2% growth per month (adjust as needed)
    latest_price = float(scrape_stock_data(stock_symbol)['latest_price'])
    projected_price = latest_price * (1 + growth_rate) ** months
    return f"${projected_price:.2f}"

def simulate_investment_logic(stock_symbol, initial_investment):
    # Placeholder logic: Assume a simple investment strategy for demonstration purposes
    # In a real-world scenario, you might use more sophisticated investment strategies
    stock_info = scrape_stock_data(stock_symbol)
    latest_price = float(stock_info['latest_price'])
    
    # Buy the stock with the initial investment
    shares_bought = initial_investment / latest_price
    
    # Placeholder: Assume selling after a fixed period with 5% profit
    sell_price = latest_price * 1.05  # 5% profit
    simulated_portfolio_value = shares_bought * sell_price
    
    return simulated_portfolio_value

@app.route('/')
def index():
    return render_template('index.html', stock_info=None)

@app.route('/get_stock_info', methods=['POST'])
def get_stock_info():
    stock_symbol = request.form.get('stock_symbol')
    initial_investment = float(request.form.get('initial_investment'))

    # Use web scraping to get stock information and projections
    stock_data = scrape_stock_data(stock_symbol)

    if stock_data:
        stock_data['symbol'] = stock_symbol
        stock_data['projection_1_month'] = get_stock_projection(stock_symbol, 1)
        stock_data['projection_6_months'] = get_stock_projection(stock_symbol, 6)
        stock_data['projection_1_year'] = get_stock_projection(stock_symbol, 12)
        stock_data['projection_5_years'] = get_stock_projection(stock_symbol, 60)

        return render_template('index.html', stock_info=stock_data, initial_investment=initial_investment)
    else:
        return render_template('index.html', stock_info=None)

@app.route('/simulate_investment', methods=['POST'])
def simulate_investment():
    stock_symbol = request.form.get('stock_symbol')
    initial_investment = float(request.form.get('initial_investment'))

    # Simulate investment logic, e.g., calculate new portfolio value
    simulated_portfolio_value = simulate_investment_logic(stock_symbol, initial_investment)

    return f"Simulated Portfolio Value: ${simulated_portfolio_value:.2f}"

if __name__ == '__main__':
    app.run(debug=True)
