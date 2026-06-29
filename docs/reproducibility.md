# 可重現性說明

## 1. 環境需求

本專案主要使用 Python 與 PyTorch。

必要套件列於 requirements.txt。

---

## 2. 安裝套件

執行：

pip install -r requirements.txt

---

## 3. 資料準備

由於 TEJ 為授權資料，本 repo 不提供原始資料。

若要完整重現，需要在本機準備相同欄位格式的台股 OHLCV 資料。

---

## 4. 訓練流程

範例流程：

python src/train.py --config configs/baseline_ohlc.yaml

---

## 5. 回測流程

範例流程：

python src/backtest.py --pred reports/predictions.csv

---

## 6. 統計檢定

範例流程：

python src/stats_test.py --backtest reports/backtest_returns.csv

---

## 7. 隨機種子

所有主要實驗需記錄 seed。

目前主要 seed：

| seed | 用途 |
|---|---|
| 42 | baseline |
| 43-46 | robustness check |

---

## 8. 不公開內容

本 repo 不公開：

1. TEJ 原始資料。
2. 完整 parquet 資料。
3. 大型模型權重。
4. 大型訓練輸出。
5. nohup log。
