# Data and Features

The private system uses historical and live crypto-perpetual market context. Raw datasets are not published because they are large, operationally sensitive, and tied to private research infrastructure.

## Publicly described feature families

Exact private formulas are not published, but the system uses families such as:

- open-interest expansion/compression regimes;
- funding dislocation and normalization;
- volatility clustering and shock context;
- liquidation/forced-flow proxies;
- trend/range/high-volatility regime filters;
- cross-sectional ranking and relative strength/weakness;
- short-term exhaustion vs continuation structure;
- execution-risk and fee/stop-distance filters.

## Leakage controls

The research process treats leakage as a first-class risk:

- chronological train/test splits;
- walk-forward validation;
- lagged features and point-in-time transforms;
- no future window statistics inside current-window decisions;
- replay checks before runtime activation;
- paper/live parity checks where applicable.

## Why raw trades are not included

Publishing raw timestamps, prices, and symbol-level trade paths can reveal strategy behavior. This repository therefore publishes aggregate statistics by window/month/side, while keeping raw logs private.
