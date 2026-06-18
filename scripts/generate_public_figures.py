from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    reports = root / "reports"
    out = reports / "figures"
    out.mkdir(parents=True, exist_ok=True)

    w = pd.read_csv(reports / "case_study_wfo_window_summary.csv")
    mon = pd.read_csv(reports / "case_study_monthly_summary.csv")
    comp = pd.read_csv(reports / "robustness_comparison.csv")
    metrics = pd.read_csv(reports / "case_study_metrics.csv").iloc[0]

    cum = w["cum_pnl_usd"].astype(float)
    peak = cum.cummax()
    dd = cum - peak

    plt.style.use("seaborn-v0_8-whitegrid")
    fig = plt.figure(figsize=(15, 10), dpi=160)
    gs = fig.add_gridspec(3, 2, height_ratios=[2.0, 1.15, 1.2], hspace=0.35, wspace=0.22)

    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(w["window_idx"], cum, marker="o", lw=2.5, color="#1f77b4")
    ax1.fill_between(w["window_idx"], cum, 0, alpha=0.08, color="#1f77b4")
    ax1.set_title(
        "Selected robust baseline — aggregated WFO/OOS replay (real private-system results, sanitized)",
        fontsize=14,
        weight="bold",
    )
    ax1.set_ylabel("Cumulative net PnL, USD")
    ax1.set_xlabel("Chronological WFO/OOS window")
    text = (
        f"Variant: {metrics['variant']}\n"
        f"Trades: {int(metrics['trades'])} | Net PnL: ${metrics['net_pnl_usd']:,.2f} | "
        f"Win rate: {metrics['win_rate_pct']:.2f}%\n"
        f"Max DD: ${metrics['max_drawdown_usd']:,.2f} | PnL/DD: {metrics['pnl_dd']:.2f} | "
        f"Negative traded windows: {int(metrics['negative_windows'])}"
    )
    ax1.text(
        0.012,
        0.96,
        text,
        transform=ax1.transAxes,
        va="top",
        ha="left",
        fontsize=9.5,
        bbox=dict(facecolor="white", edgecolor="#cccccc", boxstyle="round,pad=0.45", alpha=0.95),
    )

    ax2 = fig.add_subplot(gs[1, 0])
    ax2.bar(mon["month"], mon["net_pnl_usd"], color=["#2ca02c" if v >= 0 else "#d62728" for v in mon["net_pnl_usd"]])
    ax2.axhline(0, color="black", lw=0.8)
    ax2.set_title("Monthly aggregate PnL")
    ax2.set_ylabel("Net PnL, USD")
    ax2.tick_params(axis="x", rotation=45, labelsize=8)

    ax3 = fig.add_subplot(gs[1, 1])
    ax3.bar(w["window_idx"].astype(str), w["net_pnl_usd"], color=["#2ca02c" if v >= 0 else "#d62728" for v in w["net_pnl_usd"]])
    ax3.axhline(0, color="black", lw=0.8)
    ax3.set_title("WFO/OOS window PnL")
    ax3.set_ylabel("Net PnL, USD")

    ax4 = fig.add_subplot(gs[2, 0])
    ax4.fill_between(w["window_idx"], dd, 0, color="#d62728", alpha=0.25)
    ax4.plot(w["window_idx"], dd, color="#d62728", lw=2)
    ax4.set_title("Aggregated drawdown by WFO window")
    ax4.set_ylabel("Drawdown, USD")
    ax4.set_xlabel("Window")

    ax5 = fig.add_subplot(gs[2, 1])
    x = np.arange(len(comp))
    width = 0.35
    ax5.bar(x - width / 2, comp["net_pnl_usd"], width, label="Net PnL", color="#1f77b4")
    ax5.bar(x + width / 2, comp["max_drawdown_usd"], width, label="Max DD", color="#ff7f0e")
    for i, row in comp.iterrows():
        ax5.text(
            i,
            max(row["net_pnl_usd"], row["max_drawdown_usd"]) + 80,
            f"neg win: {int(row['negative_windows'])}\nPnL/DD: {row['pnl_dd']}",
            ha="center",
            fontsize=8,
        )
    ax5.set_xticks(x)
    ax5.set_xticklabels(["selected\nrobust", "max-PnL\nrejected"], fontsize=9)
    ax5.set_title("Why max-PnL was rejected")
    ax5.legend(fontsize=8)
    ax5.set_ylabel("USD")

    fig.text(
        0.5,
        0.01,
        "No raw trades, account identifiers, private model binaries, or production execution code are published.",
        ha="center",
        fontsize=9,
        color="#555555",
    )
    fig.savefig(out / "case_study_tearsheet.png", bbox_inches="tight")
    plt.close(fig)

    # Fund-style equity chart on a simple reference capital base.
    start_capital = 1000.0
    equity = start_capital + cum
    equity_peak = equity.cummax()
    equity_dd = equity - equity_peak

    fig2, (eq_ax, dd_ax) = plt.subplots(
        2,
        1,
        figsize=(14, 8),
        dpi=180,
        sharex=True,
        gridspec_kw={"height_ratios": [3.0, 1.0], "hspace": 0.08},
    )
    fig2.patch.set_facecolor("#0b0f17")
    for ax in (eq_ax, dd_ax):
        ax.set_facecolor("#0b0f17")
        ax.grid(True, color="#263241", alpha=0.65, linewidth=0.8)
        ax.tick_params(colors="#d7dde8")
        for spine in ax.spines.values():
            spine.set_color("#445064")

    eq_ax.plot(w["window_idx"], equity, color="#30d158", linewidth=3.0)
    eq_ax.fill_between(w["window_idx"], equity, start_capital, color="#30d158", alpha=0.12)
    eq_ax.axhline(start_capital, color="#8b949e", linewidth=1.0, linestyle="--", alpha=0.8)
    eq_ax.set_title("Equity Curve (2025–2026)", color="white", fontsize=18, weight="bold", pad=14)
    eq_ax.set_ylabel("Equity, USD", color="#d7dde8")

    stat_text = (
        "Start Capital: $1,000\n"
        f"Ending Equity: ${start_capital + float(metrics['net_pnl_usd']):,.0f}\n"
        f"Net PnL: ${float(metrics['net_pnl_usd']):,.0f}\n"
        f"Max Drawdown: ${float(metrics['max_drawdown_usd']):,.0f}\n"
        f"PnL/DD: {float(metrics['pnl_dd']):.2f}\n"
        f"Trades: {int(metrics['trades'])}"
    )
    eq_ax.text(
        0.025,
        0.94,
        stat_text,
        transform=eq_ax.transAxes,
        va="top",
        ha="left",
        color="#eef3fb",
        fontsize=11,
        bbox=dict(facecolor="#111827", edgecolor="#334155", boxstyle="round,pad=0.55", alpha=0.92),
    )
    eq_ax.text(
        0.99,
        0.04,
        "Selected robust baseline | aggregate WFO/OOS replay",
        transform=eq_ax.transAxes,
        va="bottom",
        ha="right",
        color="#9aa4b2",
        fontsize=10,
    )

    dd_ax.fill_between(w["window_idx"], equity_dd, 0, color="#ff453a", alpha=0.35)
    dd_ax.plot(w["window_idx"], equity_dd, color="#ff453a", linewidth=1.8)
    dd_ax.set_ylabel("Drawdown", color="#d7dde8")
    dd_ax.set_xlabel("Chronological WFO/OOS window", color="#d7dde8")
    fig2.savefig(out / "equity_curve_fund_style.png", bbox_inches="tight", facecolor=fig2.get_facecolor())
    plt.close(fig2)


if __name__ == "__main__":
    main()
