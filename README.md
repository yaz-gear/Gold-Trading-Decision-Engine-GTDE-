# Gold Trading Decision Engine (GTDE)

## Overview

GTDE is a Python-based algorithmic decision engine designed to generate Buy, Sell, or Hold signals for gold trading using multiple technical indicators.

It mirrors real-world trading analytics pipelines used by dealers, trading desks, and financial analytics teams.

---

## Problem Statement

Gold trading decisions are often:

* Emotion-driven
* Indicator-fragmented
* Hard to backtest consistently

GTDE solves this by aggregating signals into a single scoring-based decision engine.

---

## Use Cases

* Gold dealers hedging inventory exposure
* Trading desks evaluating technical signals
* Quant research and strategy prototyping
* Financial data engineering portfolios

---

## Features

* Technical indicators (SMA, EMA, RSI, MACD, Volatility)
* Weighted signal aggregation
* Buy/Sell/Hold classification
* Backtesting engine
* Risk-aware strategy logic

---

## Architecture

* Modular indicator system
* Decoupled strategy and signal logic
* Extendable for API or live feeds

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

