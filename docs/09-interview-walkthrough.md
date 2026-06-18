# Interview Walkthrough

A suggested way to present this project:

1. **Alpha thesis**: forced-flow imbalances in crypto perpetuals can create short-lived continuation/exhaustion opportunities.
2. **Research discipline**: point-in-time features, chronological WFO/OOS validation, net-of-cost replay.
3. **Robustness decision**: selected baseline had lower PnL than max-PnL variant but much better drawdown and fewer negative windows.
4. **Runtime thinking**: explain poller, feature store, inference, risk engine, ledger, monitoring, and parity checks.
5. **Publication boundary**: aggregate numbers are real; raw trades and private edge are withheld.

Key phrase:

> I did not optimize for the prettiest backtest. I selected a lower-PnL baseline because it had better PnL/DD, lower drawdown, and fewer negative windows across chronological OOS windows.
