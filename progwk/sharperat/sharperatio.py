
import yfinance as yf
import numpy as np

ticker_symbol = "EQUITAS.NS"
start_date = "2022-01-01"
end_date = "2023-01-01"

equitas_data = yf.download(ticker_symbol, start=start_date, end=end_date)

returns = equitas_data['Adj Close'].pct_change().dropna()

risk_free_rate = 0.0

mean_return = np.mean(returns)
std_deviation = np.std(returns)
excess_return = mean_return - risk_free_rate

annual_excess_return = excess_return * np.sqrt(252)
annual_std_deviation = std_deviation * np.sqrt(252)
sharpe_ratio = annual_excess_return / annual_std_deviation

print("Sharpe Ratio:", sharpe_ratio)
