# Reproducibility

This public repository can reproduce its charts from aggregate CSV files only.

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
make figures
```

The private research pipeline that produced the aggregate metrics is not included because it depends on private market data, feature code, models, and runtime infrastructure.

## What can be reproduced publicly

- the public tearsheet figure;
- aggregate tables;
- documentation and publication-boundary checks.

## What cannot be reproduced publicly

- raw historical data preparation;
- exact private feature calculation;
- model training artifacts;
- raw trade-by-trade replay;
- exchange/paper/live adapter behavior.
