# Alpha Thesis

The hypothesis is not that a generic machine-learning model can predict crypto direction in isolation.

The thesis is that short-horizon crypto perpetual markets periodically exhibit forced-flow imbalances:

- rapid open-interest expansion or compression;
- funding dislocation;
- volatility clustering;
- liquidation-like moves;
- regime-dependent trend continuation or exhaustion;
- cross-sectional crowding and unwind behavior.

These conditions can create temporary market inefficiencies. The model/ranking layer is used to prioritize candidates, while the risk/execution layer decides whether the trade is admissible.

## Why risk layer matters

A high model score alone is not enough. A candidate can be rejected because:

- expected reward is too low relative to stop distance;
- fees consume too much of the expected move;
- regime context is unfavorable;
- portfolio slots are full;
- data is stale or incomplete;
- live/paper parity checks are not satisfied.

The system is therefore better understood as a research + risk-control pipeline, not just a classifier.
