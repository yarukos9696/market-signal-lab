# Backtesting and Risk

The goal of replay/backtesting is not to maximize a single aggregate number. The goal is to find candidates that survive regime changes and operational constraints.

## Risk controls considered

- side-specific LONG/SHORT gates;
- signal thresholds;
- expected-return/rank filters;
- fee and stop-distance filters;
- max concurrent positions / portfolio slots;
- regime filters;
- stop/target/timeout behavior;
- drawdown and worst-window analysis.

## Metrics used

- net PnL;
- trades;
- win rate;
- max drawdown;
- PnL/DD;
- windows with trades;
- negative traded windows;
- worst and best window PnL;
- side contribution.

## Public aggregate result

See `reports/case_study_metrics.csv`, `reports/case_study_wfo_window_summary.csv`, and `reports/robustness_comparison.csv`.
