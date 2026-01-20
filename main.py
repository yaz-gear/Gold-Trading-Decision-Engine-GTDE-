from utils.loader import load_price_data
from indicators.moving_average import sma
from indicators.rsi import rsi
from indicators.macd import macd
from indicators.volatility import volatility
from engine.signal_engine import generate_signal
from engine.strategy import apply_strategy
from engine.backtest import backtest

df = load_price_data("data/gold_prices.csv")

df['sma_fast'] = sma(df['close'], 20)
df['sma_slow'] = sma(df['close'], 50)
df['rsi'] = rsi(df['close'])
df['macd'], df['macd_signal'], df['macd_hist'] = macd(df['close'])
df['volatility'] = volatility(df['close'])

df['signal'] = df.apply(generate_signal, axis=1)

df = apply_strategy(df)

results = backtest(df)

print("Backtest Results:")
for k, v in results.items():
    print(f"{k}: {v}")
