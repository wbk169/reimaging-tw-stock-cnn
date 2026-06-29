#!/usr/bin/env bash
set -euo pipefail

python src/train.py \
  --config configs/chen_dual_channel.yaml
