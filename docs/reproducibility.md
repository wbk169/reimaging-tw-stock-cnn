# 公開版本使用方式與可重現性

本儲存庫**不能單獨重現最終碩士論文的完整實驗**。本頁明確區分「目前可操作的程式」及「論文所記錄但尚未完整公開的研究流程」。

## 已有的公開內容

| 檔案 | 實際功能 | 是否足以重現正式論文 |
|---|---|---|
| `scripts/make_sample_image.py` | 以合成 OHLC 資料產生簡化黑白示例圖 | 否；缺少均線、成交量、日報酬第二通道 |
| `src/image_builder.py` | 基本 OHLC 圖像繪製 | 否 |
| `src/model.py` | 簡化 CNN 模型定義 | 否；與表 3-3 正式架構不同 |
| `src/train.py` | 讀取 YAML、檢查 CUDA、列出參數 | **否；不執行模型訓練** |
| `src/backtest.py` | 依預測 CSV 計算基礎十分位結果 | 否；未包含論文完整投資組合程序 |
| `src/stats_test.py` | 計算平均報酬的 t 統計量 | 否；不提供正式完整統計推論 |

## 可執行的獨立示例

需要 Python 及 `numpy`、`matplotlib`：

```bash
git clone https://github.com/wbk169/reimaging-tw-stock-cnn.git
cd reimaging-tw-stock-cnn
python -m pip install numpy matplotlib
python scripts/make_sample_image.py
```

輸出 `outputs_sample/sample_images/sample_001.png`。此為**隨機合成資料**，不是 TEJ 原始行情或最終論文雙通道輸入。

完整套件清單見 [requirements.txt](../requirements.txt)。若嘗試執行 `python src/train.py --config configs/baseline_ohlc.yaml`，只會列出舊版設定和 CUDA 資訊；**不會完成正式論文模型訓練**。

## 尚未公開或尚未核對的重現條件

- 完整的授權 TEJ 資料，以及與正式論文相符的清理與樣本索引。
- 正式論文的單／雙通道圖像建構、CNN、RankNet 完整訓練程式。
- 與正式論文每批次一一對應的設定檔、模型權重、預測輸出與投資組合結果。
- 環境版本鎖定及端對端測試；目前 `requirements.txt` **沒有釘選套件版本**。

## 舊實驗與正式論文差異

`configs/` 和 `reports/` 中包含其他資料切分、通道配置及歷史擴張視窗記錄；它們**不得用來宣稱已重現正式論文表 4-1 至表 4-4**。請見 [研究版本對照](thesis_alignment.md)。

## 授權與結果解讀

TEJ 授權資料不在公開儲存庫。論文報酬數據為歷史樣本外實驗，主要回測沒有完整納入交易摩擦；正式統計顯著性與多重假設檢定亦未完整執行。

請勿把歷史 `reports/statistical_tests.csv` 中空白的檢定欄位視為已有檢定結果。