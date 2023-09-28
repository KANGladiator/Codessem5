import yfinance as yf
from statsmodels import api as sm
import pandas as pd

stocks = ['SBIN.BO', 'ICICIBANK.BO', 'HDFCBANK.BO']
start_date = '2021-01-01'
end_date = '2023-08-31'

data = yf.download(stocks, start=start_date, end=end_date)
adj_close_data = data['Adj Close']
daily_returns = adj_close_data.pct_change()

market_data = yf.download('^BSESN', start=start_date, end=end_date)
market_returns = market_data['Adj Close'].pct_change()

risk_free_rate = 0.05

merged_data = pd.merge(daily_returns, market_returns, left_index=True, right_index=True, how='inner').dropna()

def calculate_alpha_beta(excess_return_stock, excess_return_market):
    excess_return_market = sm.add_constant(excess_return_market)
    model = sm.OLS(excess_return_stock, excess_return_market).fit()
    alpha = model.params[0]
    beta = model.params[1]
    return alpha, beta

alpha_sbi, beta_sbi = calculate_alpha_beta(merged_data['SBIN.BO'] - risk_free_rate, merged_data['Adj Close'] - risk_free_rate)
alpha_icici, beta_icici = calculate_alpha_beta(merged_data['ICICIBANK.BO'] - risk_free_rate, merged_data['Adj Close'] - risk_free_rate)
alpha_hdfc, beta_hdfc = calculate_alpha_beta(merged_data['HDFCBANK.BO'] - risk_free_rate, merged_data['Adj Close'] - risk_free_rate)

portfolio_returns = (1500 * merged_data['SBIN.BO'] + 1200 * merged_data['ICICIBANK.BO'] + 900 * merged_data['HDFCBANK.BO'])
alpha_portfolio, beta_portfolio = calculate_alpha_beta(portfolio_returns - risk_free_rate, merged_data['Adj Close'] - risk_free_rate)

print("Alpha and Beta for SBI:")
print("Alpha :", alpha_sbi)
print("Beta :", beta_sbi)
print("\nAlpha and Beta for ICICI Bank:")
print("Alpha:", alpha_icici)
print("Beta :", beta_icici)
print("\nAlpha and Beta for HDFC Bank:")
print("Alpha :", alpha_hdfc)
print("Beta :", beta_hdfc)
print("\nAlpha and Beta for the Portfolio:")
print("Alpha :", alpha_portfolio)
print("Beta :", beta_portfolio)

