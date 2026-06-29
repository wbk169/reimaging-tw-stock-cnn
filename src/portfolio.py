"""
Portfolio construction utilities.

Convert model prediction scores into decile portfolios.
"""

import pandas as pd


def assign_deciles(
    df: pd.DataFrame,
    date_col: str = "date",
    score_col: str = "score",
    decile_col: str = "decile",
) -> pd.DataFrame:
    """
    Assign stocks into deciles by prediction score on each date.

    D1 = lowest score group.
    D10 = highest score group.
    """
    required = {date_col, score_col}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"缺少必要欄位：{missing}")

    out = df.copy()

    def _qcut(x: pd.Series) -> pd.Series:
        return pd.qcut(x, 10, labels=False, duplicates="drop") + 1

    out[decile_col] = out.groupby(date_col)[score_col].transform(_qcut)
    return out
