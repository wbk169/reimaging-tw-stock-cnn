"""
Dataset index construction.

This module documents the rules used to build valid samples before training.
The key idea is pre-filtering:
- Skip windows with insufficient history.
- Skip windows containing NaN or inf.
- Skip samples without valid future-return labels.
"""

from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class SampleIndexConfig:
    window: int
    horizon: int
    date_col: str = "date"
    stock_col: str = "stock_id"


def is_valid_window(values: np.ndarray, expected_rows: int) -> bool:
    """
    Return True if the feature window is usable.
    """
    if values.shape[0] != expected_rows:
        return False

    if not np.isfinite(values).all():
        return False

    return True


def build_sample_index(
    df: pd.DataFrame,
    config: SampleIndexConfig,
    feature_cols: list[str],
    label_col: str,
) -> pd.DataFrame:
    """
    Build a valid sample index.

    Returned columns:
    - stock_id
    - date
    - row_start
    - row_end
    - label
    """
    required = {config.date_col, config.stock_col, label_col, *feature_cols}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"缺少必要欄位：{missing}")

    out_rows = []

    df = df.sort_values([config.stock_col, config.date_col]).reset_index(drop=True)

    for stock_id, g in df.groupby(config.stock_col, sort=False):
        g = g.reset_index(drop=True)

        if len(g) < config.window + config.horizon:
            continue

        feature_values = g[feature_cols].to_numpy(dtype=float)
        labels = g[label_col].to_numpy()

        for end_idx in range(config.window - 1, len(g) - config.horizon):
            start_idx = end_idx - config.window + 1
            window_values = feature_values[start_idx:end_idx + 1]
            label = labels[end_idx]

            if not is_valid_window(window_values, config.window):
                continue

            if pd.isna(label):
                continue

            out_rows.append(
                {
                    "stock_id": stock_id,
                    "date": g.loc[end_idx, config.date_col],
                    "row_start": start_idx,
                    "row_end": end_idx,
                    "label": int(label),
                }
            )

    return pd.DataFrame(out_rows)
