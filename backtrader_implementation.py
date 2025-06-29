import backtrader as bt
import yfinance as yf

class MovingAverageStrategy(bt.Strategy):

    params = (('period_fast', 30), ('period_slow', 200),)

    def __init__(self):
        # get the data we have provided
        self.close_data = self.data.close
        self.fast_sma = bt.indicators.MovingAverageSimple(self.close_data, 
                                                           period= self.params.period_fast)
        self.slow_sma = bt.indicators.MovingAverageSimple(self.close_data, 
                                                           period= self.params.period_slow)

    
    # this function will be called automatically after a new data point (stock price) is available
    def next(self):

        # we have to check whether we have already opened a long position
        if not self.position:
            # we can open a long position if needed
            if self.fast_sma[0] > self.slow_sma[0] and self.fast_sma[-1] < self.slow_sma[-1]:
                self.buy()
            else:
                # check whether to close the long position 
                if self.fast_sma[0] < self.slow_sma[0] and self.fast_sma[-1] > self.slow_sma[-1]:
                    self.close()


if __name__ == '__main__':
    cerebro = bt.Cerebro()

    # Download data
    df = yf.download('MSFT', start='2010-01-01', end='2020-01-01')
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    # Pass dataname
    stock_data = bt.feeds.PandasData(dataname=df)

    # we have to add the data to Cerebro
    cerebro.adddata(stock_data)
    cerebro.addstrategy(MovingAverageStrategy)

    cerebro.addobserver(bt.observers.Value)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate= 0)
    cerebro.addanalyzer(bt.analyzers.Returns)
    cerebro.addanalyzer(bt.analyzers.DrawDown)

    cerebro.broker.set_cash(3000)
    print('initial capital: $%.2f' % cerebro.broker.getvalue())

    # commission fees - set 0.01%
    cerebro.broker.setcommission(0.01)

    # run the strategy
    results = cerebro.run()
    print('Sharpe ratio: %.2f' % results[0].analyzers.sharperatio.get_analysis()['sharperatio'])
    print('Return: %.2f%%' % results[0].analyzers.returns.get_analysis()['rnorm100'])
    print('Max Drawdown: %.2f%%' % results[0].analyzers.drawdown.get_analysis()['max']['drawdown'])
    print('Capital: $%.2f' % cerebro.broker.getvalue())