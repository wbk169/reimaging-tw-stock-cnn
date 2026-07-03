# Walk-forward 實驗紀錄

本文件紀錄目前已完成的 walk-forward rolling backtest 結果。主結果採用 `time split`，原因是股票樣本具有時間相依性，且 W20 / H5 會造成相鄰樣本高度重疊；因此 train / validation 以時間前後切分，避免同一段行情同時出現在 train 與 validation。

---

## 固定設定

| 項目 | 設定 |
|---|---|
| 評估方式 | expanding walk-forward |
| Train/Validation 切分 | time split |
| 測試期間 | 2018–2025 |
| Window | 20 |
| Horizon | 5 |
| Image height | 64 |
| Epochs | 20 |
| Learning rate | 1e-5 |
| Batch size | 128 |
| Patience | 2 |
| Device | CUDA GPU |
| AMP | enabled |
| 投資組合統計 | non-overlap decile portfolio |

---

## 已完成結果摘要

| 模型 | 資料期間 | AUC | ACC | D10 年化報酬 | D10 夏普 | D10-D1 年化報酬 | D10-D1 夏普 |
|---|---|---:|---:|---:|---:|---:|---:|
| Jiang 單通道 | 2008–2025 | 0.5489 | 0.5317 | 29.99% | 1.7894 | 40.19% | 5.2249 |
| retbar 雙通道 | 2008–2025 | 0.5489 | 0.5317 | 33.12% | 1.8191 | 42.68% | 3.9880 |

---

## 1. Jiang 單通道：2008–2025 walk-forward time split

### 設定

```text
模型：Jiang 單通道
資料起始：2008-01-01
測試期間：2018-01-01 至 2025-12-31
image_variant：jiang_ma
wf_train_val_split_mode：time
輸出資料夾：outputs_wf_2008_jiang_W20_H5_time
```

### 分類結果

| 指標 | 結果 |
|---|---:|
| 平均 AUC | 0.5489 |
| 加權平均 AUC | 0.5488 |
| 平均 ACC | 0.5317 |
| 加權平均 ACC | 0.5317 |
| 測試樣本數合計 | 3,357,679 |

### Non-overlap portfolio

| 組合 | 年化報酬 | 年化波動 | Sharpe |
|---|---:|---:|---:|
| D1 | -10.20% | 14.62% | -0.6977 |
| D10 | 29.99% | 16.76% | 1.7894 |
| D10-D1 | 40.19% | 7.69% | 5.2249 |

---

## 2. retbar 雙通道：2008–2025 walk-forward time split

### 設定

```text
模型：retbar 雙通道
第一通道：Jiang 價格圖
第二通道：報酬率 retbar
資料起始：2008-01-01
測試期間：2018-01-01 至 2025-12-31
image_variant：ret_bar_2ch
wf_train_val_split_mode：time
輸出資料夾：outputs_wf_2008_retbar_2ch_W20_H5_time
```

### 分類結果

| 指標 | 結果 |
|---|---:|
| 平均 AUC | 0.5489 |
| 加權平均 AUC | 0.5483 |
| 平均 ACC | 0.5317 |
| 加權平均 ACC | 0.5319 |
| 測試樣本數合計 | 2,947,230 |

### Non-overlap portfolio

| 組合 | 年化報酬 | 年化波動 | Sharpe |
|---|---:|---:|---:|
| D1 | -9.57% | 19.12% | -0.5004 |
| D10 | 33.12% | 18.20% | 1.8191 |
| D10-D1 | 42.68% | 10.70% | 3.9880 |

---

## 初步比較

retbar 雙通道相較 Jiang 單通道，在 walk-forward time split 下提高了 D10 年化報酬與 D10-D1 年化報酬，但 D10-D1 Sharpe 較低，代表額外報酬伴隨更高波動。分類 AUC 與 ACC 幾乎持平。

---

## 後續待跑

1. 2008 Chen 雙通道 walk-forward time split。
2. 2008 price + chip total 2ch clip12 walk-forward time split。
3. 2008 custom 3ch：Jiang + retbar + chip signed bar clip12 walk-forward time split。
4. 2000 Jiang / Chen / retbar 系列 walk-forward time split。
