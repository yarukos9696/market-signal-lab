# Failed Experiments and Research Rejections

This project was not built by picking a single good-looking backtest. A large part of the work was rejecting ideas that looked attractive in isolation but failed robustness, leakage, or runtime-readiness checks.

The examples below are intentionally described at the research-decision level. Exact private formulas, raw trades, symbols, and model artifacts are not published.

## 1. Max-PnL portfolio variant rejected

**Experiment**

Select the variant with the most attractive aggregate PnL.

**Observed result**

The higher-PnL comparison variant produced:

- variant: `pnl_L3_S3_slots10_short_first`;
- net PnL: `$3,606.41`;
- max drawdown: `$613.23`;
- negative windows: `8`;
- PnL/DD: `5.88`.

**Problem**

The headline PnL was better, but the equity path was less robust: larger drawdown, more negative windows, and weaker PnL/DD.

**Decision**

Rejected. The selected baseline was `strict_L3_S1_slots10_short_first`:

- net PnL: `$2,653.36`;
- max drawdown: `$277.85`;
- negative windows: `3`;
- PnL/DD: `9.55`.

This is the main research lesson of the public case study: robustness was preferred over maximum aggregate PnL.

## 2. Narrow holdout / single-window gate optimization rejected

**Experiment**

Use a narrow recent holdout fragment to select adaptive gates and side/regime filters.

**Observed result**

Some SHORT high-volatility configurations looked attractive on a recent fragment, especially when filtering aggressively by probability, expected-return rank, and fee-to-risk constraints.

**Problem**

When expanded to all available WFO/OOS windows, some attractive candidates traded in too few windows or showed unstable behavior. A configuration that looks good in one market regime can be a rare-regime candidate rather than a production baseline.

**Decision**

Rejected as primary production evidence. Such candidates can be monitored in shadow mode, but not presented as the robust baseline.

## 3. Broad relaxed SHORT filters constrained

**Experiment**

Relax SHORT filters to increase trade frequency and capture more opportunities.

**Observed result**

Broad SHORT configurations could produce positive aggregate PnL.

**Problem**

The additional trades increased the number of bad windows and made the path less clean. More trades did not automatically mean better portfolio quality.

**Decision**

Constrained. SHORT exposure remained useful, but it needed stricter ranking, fee, regime, and risk gates.

## 4. Regime-specific RR mapping kept research-only

**Experiment**

Map different reward/risk or exit policies to different market regimes to improve aggregate performance.

**Observed result**

Some regime-aware mappings looked attractive in full-OOS analysis.

**Problem**

A stricter prior-window / nested validation check did not confirm enough robustness. The apparent improvement was not strong enough to justify production rollout.

**Decision**

Kept research-only. The simpler locked baseline was preferred for paper/live evaluation.

## 5. Conservative exit assumptions did not automatically improve robustness

**Experiment**

Test more conservative exits and alternate RR overlays under the assumption that lower targets or smoother exits would reduce risk.

**Observed result**

Some conservative variants reduced certain tail outcomes, but they did not consistently improve the full robustness profile.

**Problem**

Lower nominal risk did not always translate into better PnL/DD, better worst-window behavior, or better side balance.

**Decision**

Rejected as an automatic upgrade. Exit policy changes must be validated across all windows, not assumed safer.

## 6. Funding as standalone signal rejected

**Experiment**

Use funding-rate dislocation as an independent signal family.

**Observed result**

Funding had useful context value but weak standalone predictive power.

**Problem**

Funding alone was too noisy and regime-dependent. It performed better as part of a broader market-state context alongside OI, volatility, trend/range state, and execution-risk filters.

**Decision**

Kept as contextual feature family, not as a standalone alpha.

## 7. Feature families constrained because of leakage risk

**Experiment**

Use rolling, cross-sectional, OI, and regime features aggressively.

**Observed result**

Some feature variants improved apparent backtest performance.

**Problem**

Crypto feature engineering is leakage-prone: rolling statistics, cross-sectional ranks, and regime labels can accidentally include information unavailable at decision time if built incorrectly.

**Decision**

Constrained to point-in-time construction and chronological validation. Candidate features that could not pass leakage/parity checks were removed or kept out of production.

## 8. Backtest/live mismatch treated as a blocker

**Experiment**

Move promising replay logic toward paper/live runtime.

**Observed result**

Research outputs can differ from runtime decisions if feature windows, data freshness, calibrators, model directories, or side-specific gates drift.

**Problem**

A good replay is not enough if the live bot cannot reproduce the same decision semantics.

**Decision**

Paper/live parity and runtime smoke checks became required before trusting a rollout.

## Summary

The system improved through rejection:

- do not choose max PnL blindly;
- do not trust one-window results;
- do not assume more trades are better;
- do not promote regime-specific mappings without strict validation;
- do not treat funding as standalone alpha;
- do not trust features that cannot be defended as point-in-time;
- do not trust replay results until runtime parity is checked.
