#!/usr/bin/env bash
set -euo pipefail

python src/stats_test.py \
  --backtest reports/backtest_returns.csv
