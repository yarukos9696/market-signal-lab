# Lessons Learned

- Robustness beats maximizing aggregate backtest PnL.
- A lower-PnL candidate can be better if drawdown and negative-window behavior are materially stronger.
- Crypto feature engineering is leakage-prone; point-in-time discipline is mandatory.
- Funding alone is weak; it is more useful as part of regime/context.
- Open-interest and forced-flow context are useful but must be gated by execution risk.
- The risk layer matters as much as the signal layer.
- Paper/live parity checks are required before trusting replay results operationally.
- Low trade frequency after filtering can be acceptable if robustness improves.
- Monitoring needs precise alert patterns; overly broad watch strings create noise.
