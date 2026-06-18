# Research Log

This file records examples of decisions that were rejected or constrained during research.

## Max-PnL variant rejected

A higher aggregate-PnL candidate existed:

- `pnl_L3_S3_slots10_short_first`;
- net PnL: $3,606.41;
- max drawdown: $613.23;
- negative windows: 8;
- PnL/DD: 5.88.

It was rejected in favor of `strict_L3_S1_slots10_short_first`:

- net PnL: $2,653.36;
- max drawdown: $277.85;
- negative windows: 3;
- PnL/DD: 9.55.

Reason: robustness and drawdown quality mattered more than aggregate PnL.

## Single-window cherry-picking avoided

Variants that looked attractive on a narrow holdout fragment were not treated as production-ready unless they survived broader WFO/OOS checks.

## Feature leakage risk treated seriously

Rolling, cross-sectional, funding, and OI-derived features can accidentally leak future context if not built point-in-time. The research process therefore uses chronological splits and replay/parity checks.

## Runtime parity matters

Backtest results are not trusted unless the live/paper runtime can reproduce the same feature and decision semantics closely enough for the intended rollout.
