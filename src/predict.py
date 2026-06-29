"""
Prediction entry point.

This module documents the expected output format for out-of-sample predictions.
Prediction CSV should contain:

- date
- stock_id
- score
- future_return

score = model estimated probability of positive future return.
"""

import argparse
from pathlib import Path

import pandas as pd


def validate_prediction_file(path: str) -> pd.DataFrame:
    pred_path = Path(path)

    if not pred_path.exists():
        raise FileNotFoundError(f"找不到預測檔：{pred_path}")

    pred = pd.read_csv(pred_path)

    required = {"date", "stock_id", "score", "future_return"}
    missing = required - set(pred.columns)

    if missing:
        raise ValueError(f"預測檔缺少必要欄位：{missing}")

    return pred


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", type=str, required=True)
    args = parser.parse_args()

    pred = validate_prediction_file(args.pred)

    print("預測檔格式檢查通過")
    print(f"rows: {len(pred):,}")
    print(pred[["date", "stock_id", "score", "future_return"]].head())


if __name__ == "__main__":
    main()
