📈 Moving Average Crossover Strategy with Backtrader

This project demonstrates how to implement and backtest a simple Moving Average Crossover Strategy using the powerful Python library Backtrader. The strategy is applied to historical stock data from Yahoo Finance, simulating realistic trading behavior and analyzing performance metrics like Sharpe Ratio, Return, and Drawdown.

🧠 Strategy Logic

The strategy buys when the fast Simple Moving Average (SMA) crosses above the slow SMA, and exits the position when the fast SMA crosses below the slow SMA.
Entry Condition:

    Fast SMA > Slow SMA and

    Fast SMA was ≤ Slow SMA on the previous day

Exit Condition:

    Fast SMA < Slow SMA and

    Fast SMA was ≥ Slow SMA on the previous day

🛠 Features

    📊 SMA crossover logic with bt.indicators.MovingAverageSimple

    🔁 Backtest using Backtrader engine

    📥 Historical stock data via yfinance

    📈 Performance metrics:

        Sharpe Ratio

        Normalized Return (%)

        Maximum Drawdown

    💰 Initial capital and commission settings

📂 File Structure

backtrader_implementation.py

▶️ How to Run
1. Install Dependencies

pip install yfinance backtrader

2. Run the Script

python backtrader_implementation.py

📉 Output

Upon execution, you will see:

    Initial and final capital

    Strategy return (%)

    Sharpe ratio

    Maximum drawdown (%)

📋 Example Output

initial capital: $3000.00
Sharpe ratio: 0.72
Return: 114.50%
Max Drawdown: 23.78%
Capital: $6423.20

📌 Notes

    Stock: MSFT

    Time period: 2010-01-01 to 2020-01-01

    Fast SMA: 30 days

    Slow SMA: 200 days

    Commission: 0.01%

You can tweak the parameters directly in the script to test different stocks or strategy variations.
📜 License

This project is licensed under the MIT License.
🙏 Acknowledgements

    Backtrader

    Yahoo Finance via yfinance
