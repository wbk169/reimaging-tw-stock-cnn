#!/usr/bin/env bash
set -euo pipefail

python src/backtest.py \
  --pred reports/predictions.csv \
  --out reports/backtest_returns.csv
