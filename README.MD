
---

# Stonks

Stonks is a user-friendly and feature-rich web application built with Flask, Plotly, and yfinance. It empowers users to access comprehensive stock information, visualize real-time price trends, and make informed investment decisions.

Through late-night coding sessions in airport terminals, I transformed theoretical knowledge into practical implementation. The choice of technologies reflects both the class learnings from my Full Stack Web Development class and my personal interest in finance.

Disclaimer: While Stonks offers valuable insights, it is crucial to note that the information provided is not intended as real financial advice. Users are encouraged to conduct thorough research and consult with financial professionals before making investment decisions. The app serves as a tool for information and analysis, but individual financial situations vary, and caution is advised in financial decision-making.



## Features

- **Stock Information:** Enter a stock symbol to fetch and display information such as current price, P/E ratio, PEG ratio, P/S ratio, P/B ratio, and D/E ratio.

- **Real-time Stock Price Visualization:** View candlestick charts for real-time stock prices.

- **Interactive Stock Suggestions:** Choose from stock suggestions provided in a table with symbol, name, and sector details.

- **Dynamic Filtering:** Filter stock suggestions dynamically based on the entered stock symbol.



## Requirements

- [Flask](https://pypi.org/project/Flask/)
- [Plotly](https://plotly.com/python/getting-started/)
- [yfinance](https://pypi.org/project/yfinance/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/martinl5/Stonks.git
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   python app.py
   ```

4. **Access the app:**

   Open your web browser and go to [http://localhost:5000/](http://localhost:5000/).

## Usage

1. Enter a stock symbol in the form and click "Get Information" to fetch stock data.

2. Explore stock suggestions from the CSV file in the suggestions table. Click on a suggestion to autofill the form.

3. Visualize real-time stock prices in the candlestick chart.

4. Observe color-coded ratios indicating whether they meet specific conditions (e.g., P/E Ratio > 25 highlighted in red).

## Troubleshooting

- Check for required dependencies and review console output for errors.

## Contributing

Contributions are welcome! Open an issue or submit a pull request for suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).

---
