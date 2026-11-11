# Quantitative Alpha Strategy Workspace

## Mandate
Formulate and backtest an institutional statistical arbitrage alpha model on Binance BTC/USDT 5-Minute Level-2 orderbook ticks.

## Benchmark Concurrence Criteria
- **Concurrence Threshold**: >= 97.50% match against institutional benchmark
- **Sharpe Ratio**: >= 3.00
- **Max Trailing Drawdown**: <= 2.50% ceiling

## Workspace Structure
- `strategy.py`: Primary alpha generation logic and signal calculations.
- `risk_guard.py`: Trailing drawdown circuit breakers and position limits.
- `execution_router.py`: Sub-millisecond tick parsing & TWAP order routing.
- `requirements.txt`: Python dependencies.
