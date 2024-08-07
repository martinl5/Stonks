import csv
from flask import Flask, render_template, request
import plotly.graph_objs as go
import plotly.offline as pyo
import yfinance as yf

app = Flask(__name__, static_url_path='/static')

def get_stock_data(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.info
        return data
    except ValueError as ve:
        print(f"ValueError fetching Stock data: {ve}")
        return None
    except KeyError as ke:
        print(f"KeyError fetching Stock data: {ke}")
        return None
    except Exception as e:
        print(f"Error fetching Stock data: {e}")
        return None
    
def get_calendar(symbol):
    try:
        ticker = yf.Ticker(symbol)
        calendar = ticker.calendar
        return calendar
    except Exception as e:
        print(f"Error fetching earnings for {symbol}: {e}")
        return None

def get_voo_data():
    voo_data = get_stock_data("VOO")
    return voo_data

def get_appl_data():
    appl_data = get_stock_data("AAPL")
    return appl_data

def read_stock_symbols_from_csv(file_path='stock_symbols.csv'):
    symbols = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            symbols.append({
                'symbol': row['Symbol'],
                'name': row['Name'],
                'sector': row['Sector']
            })
    return symbols



@app.route('/', methods=['GET', 'POST'])
def stock():
    symbol = None
    stock_data = None
    suggestions = read_stock_symbols_from_csv()
    graph_html = None
    voo_data= None
    appl_data= None
    earnings_data = None

    if request.method == 'POST':
        symbol = request.form['symbol'].upper()
        stock_data = get_stock_data(symbol)
        voo_data = get_voo_data()
        appl_data = get_appl_data()
        earnings_data = get_calendar(symbol)

    if symbol:
        try:
            df = yf.download(symbol, period='1mo', interval='5m') 
            df = df.dropna(subset=['Open', 'High', 'Low', 'Close'])

            if not df.empty:
                # Your existing code for plotting the stock data
                fig = go.Figure()

                fig.add_trace(go.Candlestick(x=df.index,
                                open=df['Open'],
                                high=df['High'],
                                low=df['Low'],
                                close=df['Close'], name='market data'))

                fig.update_xaxes(
                    rangeslider_visible=True,
                    rangeselector=dict(
                        buttons=list([
                            dict(count=15, label="15m", step="minute", stepmode="backward"),
                            dict(count=1, label="1h", step="hour", stepmode="backward"),
                            dict(count=1, label="1d", step="day", stepmode="backward"),
                            dict(count=7, label="1w", step="day", stepmode="backward"),
                            dict(count=1, label="1m", step="month", stepmode="backward"),
                            dict(step="all")
                        ])
                    ),
                    #excludes times that are outside of trading hours
                    rangebreaks=[
                        dict(bounds=["sat", "mon"]),
                        dict(bounds=[16, 9.5], pattern="hour"),
                        dict(values=["2023-12-25", "2024-01-01","2024-07-04"]) #need to add more
                    ]
                )

                graph_html = pyo.plot(fig, output_type='div')
        except ValueError as ve:
            print(f"ValueError fetching stock data: {ve}")
        except KeyError as ke:
            print(f"KeyError fetching stock data: {ke}")
        except Exception as e:
            print(f"Error fetching stock data: {e}")

    return render_template('stock.html', symbol=symbol, stock_data=stock_data, voo_data=voo_data,
                            appl_data=appl_data, suggestions=suggestions, graph_html=graph_html, 
                            earnings_data = earnings_data)

if __name__ == '__main__':
    app.run(debug=True)
