import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stocks = ['SBIN.BO', 'ICICIBANK.BO', 'HDFCBANK.BO']  
start_date = '2021-01-01'
end_date = '2023-08-31'

data = yf.download(stocks, start=start_date, end=end_date)

adj_close_data = data['Adj Close']

daily_returns = adj_close_data.pct_change()

shares_sbi = 1500
shares_icici = 1200
shares_hdfc = 900

portfolio_value = (shares_sbi * adj_close_data['SBIN.BO'] +
                   shares_icici * adj_close_data['ICICIBANK.BO'] +
                   shares_hdfc * adj_close_data['HDFCBANK.BO'])

portfolio_returns = portfolio_value.pct_change()

plt.figure(figsize=(12, 6))
plt.plot(portfolio_returns.index, portfolio_returns, label='Portfolio Daily Return', color='black')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.title('Daily Returns of Portfolio')
plt.legend()
plt.grid(True)
plt.show()

avg_daily_return_sbi = daily_returns['SBIN.BO'].mean()
avg_daily_return_icici = daily_returns['ICICIBANK.BO'].mean()
avg_daily_return_hdfc = daily_returns['HDFCBANK.BO'].mean()
avg_daily_return_portfolio = portfolio_returns.mean()

volatility_sbi = daily_returns['SBIN.BO'].std()
volatility_icici = daily_returns['ICICIBANK.BO'].std()
volatility_hdfc = daily_returns['HDFCBANK.BO'].std()
volatility_portfolio = portfolio_returns.std()

annual_return_sbi = avg_daily_return_sbi * 252
annual_return_icici = avg_daily_return_icici * 252
annual_return_hdfc = avg_daily_return_hdfc * 252
annual_return_portfolio = avg_daily_return_portfolio * 252

annual_volatility_sbi = volatility_sbi * np.sqrt(252)
annual_volatility_icici = volatility_icici * np.sqrt(252)
annual_volatility_hdfc = volatility_hdfc * np.sqrt(252)
annual_volatility_portfolio = volatility_portfolio * np.sqrt(252)

moving_avg_return = portfolio_returns.rolling(window=30).mean()
moving_avg_volatility = portfolio_returns.rolling(window=30).std()

plt.figure(figsize=(12, 6))
plt.plot(portfolio_returns.index, moving_avg_return, label='30-Day MA Return')
plt.plot(portfolio_returns.index, moving_avg_volatility, label='30-Day MA Volatility')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('30-Day Moving Average Return and Volatility of Portfolio')
plt.legend()
plt.grid(True)
plt.show()

print("SBI - Annualized Return:", annual_return_sbi)
print("ICICI Bank - Annualized Return:", annual_return_icici)
print("HDFC Bank - Annualized Return:", annual_return_hdfc)
print("Portfolio - Annualized Return:", annual_return_portfolio)
print("\nSBI - Annualized Volatility:", annual_volatility_sbi)
print("ICICI Bank - Annualized Volatility:", annual_volatility_icici)
print("HDFC Bank - Annualized Volatility:", annual_volatility_hdfc)
print("Portfolio - Annualized Volatility:", annual_volatility_portfolio)

