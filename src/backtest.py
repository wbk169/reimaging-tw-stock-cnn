"""
Backtest module.

This script converts model predictions into decile returns and D10-D1 returns.
Expected input columns:
- date
- stock_id
- score
- future_return
"""

import argparse
from pathlib import Path

import pandas as pd

from portfolio import assign_deciles


def compute_decile_returns(pred: pd.DataFrame) -> pd.DataFrame:
    pred = assign_deciles(pred)

    decile_ret = (
        pred.groupby(["date", "decile"])["future_return"]
        .mean()
        .reset_index()
    )

    pivot = decile_ret.pivot(index="date", columns="decile", values="future_return")
    pivot["D10_D1"] = pivot[10] - pivot[1]
    pivot = pivot.reset_index()

    return pivot


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", type=str, required=True)
    parser.add_argument("--out", type=str, default="reports/backtest_returns.csv")
    args = parser.parse_args()

    pred_path = Path(args.pred)
    if not pred_path.exists():
        raise FileNotFoundError(f"找不到預測檔：{pred_path}")

    pred = pd.read_csv(pred_path)

    required = {"date", "stock_id", "score", "future_return"}
    missing = required - set(pred.columns)

    if missing:
        raise ValueError(f"預測檔缺少必要欄位：{missing}")

    result = compute_decile_returns(pred)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(out_path, index=False)

    print(f"已輸出回測結果：{out_path}")
    print(result["D10_D1"].describe())


if __name__ == "__main__":
    main()
