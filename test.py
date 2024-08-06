import yfinance as yf

ticker = yf.Ticker('AAPL')
data = ticker.calendar
earnings = data['Earnings Date']

print("Earnings Dates:")
for i in earnings:
    print(i)

for item in data.items():
    print(item)
