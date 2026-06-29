"""
Statistical tests for strategy returns.

Includes:
- t-stat for mean D10-D1 return
- bootstrap helper structure
"""

import argparse
import numpy as np
import pandas as pd


def t_stat_mean(x: np.ndarray) -> float:
    x = x[np.isfinite(x)]
    if len(x) < 2:
        return float("nan")

    mean = np.mean(x)
    std = np.std(x, ddof=1)

    if std == 0:
        return float("nan")

    return float(mean / (std / np.sqrt(len(x))))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--backtest", type=str, required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.backtest)

    if "D10_D1" not in df.columns:
        raise ValueError("backtest file must contain D10_D1 column")

    returns = df["D10_D1"].to_numpy(dtype=float)
    stat = t_stat_mean(returns)

    print(f"D10-D1 t-stat: {stat:.4f}")


if __name__ == "__main__":
    main()
