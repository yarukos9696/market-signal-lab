# Results

This page summarizes the public aggregate results exported from the private system.

## Selected baseline

| Metric | Value |
|---|---:|
| Variant | strict_L3_S1_slots10_short_first |
| Period | 2025-04 to 2026-05 |
| Trades | 782 |
| Net PnL | $2,653.36 |
| Win rate | 40.15% |
| Max DD | $277.85 |
| PnL/DD | 9.55 |
| Windows with trades | 14 |
| Negative windows | 3 |
| Worst window | -$93.39 |
| Best window | $887.97 |

## Side contribution

| Side | Trades | Net PnL | Win rate |
|---|---:|---:|---:|
| LONG | 182 | $538.78 | 47.25% |
| SHORT | 600 | $2,114.58 | 38.00% |

## Post-WFO catch-up sanity check

A later aggregate replay/paper-style catch-up window from 2026-05-07 to 2026-06-18 produced:

- net PnL: $441.80;
- trades: 37;
- win rate: 48.65%;
- max drawdown: $54.61;
- SHORT-only in that exported summary; no trades after 2026-06-06.

This is reported as a sanity check, not as the main WFO result.

## Files

- `reports/case_study_metrics.csv`
- `reports/case_study_monthly_summary.csv`
- `reports/case_study_side_summary.csv`
- `reports/case_study_wfo_window_summary.csv`
- `reports/robustness_comparison.csv`
- `reports/post_wfo_catchup_metrics.csv`
- `reports/figures/case_study_tearsheet.png`
