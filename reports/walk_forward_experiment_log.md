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
| Chen 雙通道 | 2008–2025 | 0.5485 | 0.5312 | 29.45% | 1.7181 | 37.92% | 3.7692 |
| Jiang 單通道 | 2000–2025 | 0.5487 | 0.5298 | 32.25% | 1.9493 | 42.70% | 5.9075 |
| Chen 雙通道 | 2000–2025 | 0.5513 | 0.5327 | 31.81% | 1.8255 | 43.54% | 4.1688 |
| retbar 雙通道 | 2000–2025 | 0.5508 | 0.5305 | 34.10% | 1.8685 | 46.63% | 4.1467 |

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

## 3. Chen 雙通道：2008–2025 walk-forward time split

### 設定

```text
模型：Chen 雙通道
資料起始：2008-01-01
測試期間：2018-01-01 至 2025-12-31
image_variant：chen_2ch
wf_train_val_split_mode：time
輸出資料夾：outputs_wf_2008_chen_2ch_W20_H5_time
```

### 分類結果

| 指標 | 結果 |
|---|---:|
| 平均 AUC | 0.5485 |
| 加權平均 AUC | 0.5484 |
| 平均 ACC | 0.5312 |
| 加權平均 ACC | 0.5311 |
| 測試樣本數合計 | 2,943,596 |

### Non-overlap portfolio

| 組合 | 年化報酬 | 年化波動 | Sharpe |
|---|---:|---:|---:|
| D1 | -8.47% | 18.77% | -0.4511 |
| D10 | 29.45% | 17.14% | 1.7181 |
| D10-D1 | 37.92% | 10.06% | 3.7692 |

---

## 4. Jiang 單通道：2000–2025 walk-forward time split

### 設定

```text
模型：Jiang 單通道
資料起始：2000-01-01
測試期間：2018-01-01 至 2025-12-31
image_variant：jiang_ma
wf_train_val_split_mode：time
輸出資料夾：outputs_wf_2000_*/wf_2000_jiang_W20_H5
```

### 分類結果

| 指標 | 結果 |
|---|---:|
| 平均 AUC | 0.5487 |
| 加權平均 AUC | 0.5486 |
| 平均 ACC | 0.5298 |
| 加權平均 ACC | 0.5297 |
| 測試樣本數合計 | 3,357,679 |

### Non-overlap portfolio

| 組合 | 年化報酬 | Sharpe |
|---|---:|---:|
| D1 | -10.45% | -0.7221 |
| D10 | 32.25% | 1.9493 |
| D10-D1 | 42.70% | 5.9075 |

---

## 5. Chen 雙通道：2000–2025 walk-forward time split

### 設定

```text
模型：Chen 雙通道
資料起始：2000-01-01
測試期間：2018-01-01 至 2025-12-31
image_variant：chen_2ch
wf_train_val_split_mode：time
輸出資料夾：outputs_wf_2000_*/wf_2000_chen_2ch_W20_H5
```

### 分類結果

| 指標 | 結果 |
|---|---:|
| 平均 AUC | 0.5513 |
| 加權平均 AUC | 0.5513 |
| 平均 ACC | 0.5327 |
| 加權平均 ACC | 0.5325 |
| 測試樣本數合計 | 2,943,596 |

### Non-overlap portfolio

| 組合 | 年化報酬 | Sharpe |
|---|---:|---:|
| D1 | -11.73% | -0.6189 |
| D10 | 31.81% | 1.8255 |
| D10-D1 | 43.54% | 4.1688 |

---

## 6. retbar 雙通道：2000–2025 walk-forward time split

### 設定

```text
模型：retbar 雙通道
第一通道：Jiang 價格圖
第二通道：報酬率 retbar
資料起始：2000-01-01
測試期間：2018-01-01 至 2025-12-31
image_variant：ret_bar_2ch
wf_train_val_split_mode：time
輸出資料夾：outputs_wf_2000_*/wf_2000_retbar_2ch_W20_H5
```

### 分類結果

| 指標 | 結果 |
|---|---:|
| 平均 AUC | 0.5508 |
| 加權平均 AUC | 0.5507 |
| 平均 ACC | 0.5305 |
| 加權平均 ACC | 0.5304 |
| 測試樣本數合計 | 2,947,230 |

### Non-overlap portfolio

| 組合 | 年化報酬 | Sharpe |
|---|---:|---:|
| D1 | -12.53% | -0.6533 |
| D10 | 34.10% | 1.8685 |
| D10-D1 | 46.63% | 4.1467 |

---

## 初步比較

2008 起算結果中，retbar 雙通道的 D10 年化報酬與 D10-D1 年化報酬最高；Jiang 單通道的 D10-D1 Sharpe 最高；Chen 雙通道在 2008 起算下沒有超過 Jiang 或 retbar。

2000 起算結果中，Chen 雙通道的 AUC 與 ACC 最高；retbar 雙通道的 D10 年化報酬與 D10-D1 年化報酬最高；Jiang 單通道的 D10-D1 Sharpe 最高。

---

## 後續待跑

1. 2008 price + chip total 2ch clip12 walk-forward time split。
2. 2008 custom 3ch：Jiang + retbar + chip signed bar clip12 walk-forward time split。
3. 2000 / 2008 系列的 random70 對照結果。
