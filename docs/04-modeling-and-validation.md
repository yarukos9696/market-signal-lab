# Modeling and Validation

The private system separates model selection from portfolio/risk selection.

## Validation style

- Chronological walk-forward / out-of-sample windows.
- Side-specific evaluation for LONG and SHORT candidates.
- Net-of-cost replay assumptions.
- Portfolio slot limits.
- Metrics beyond total PnL: drawdown, PnL/DD, negative windows, worst window, trade count, side concentration.

## Selected baseline

The selected public baseline is:

`strict_L3_S1_slots10_short_first`

It was chosen because it had stronger robustness characteristics than a higher aggregate-PnL alternative.

## Rejected max-PnL comparison

| Variant | Net PnL | Max DD | Negative windows | PnL/DD | Decision |
|---|---:|---:|---:|---:|---|
| strict_L3_S1_slots10_short_first | $2,653.36 | $277.85 | 3 | 9.55 | selected |
| pnl_L3_S3_slots10_short_first | $3,606.41 | $613.23 | 8 | 5.88 | rejected |

The rejected variant looked better on headline PnL but was less stable across windows.
