# 實驗報告索引｜請先確認實驗版本

此資料夾包含**歷史探索性實驗資料**與研究說明文件，**並非最終碩士論文所有正式表格的原始輸出集合**。正式論文的主結果以根目錄 [README](../README.md)、[版本對照](../docs/thesis_alignment.md) 及最終提交的論文表 4-1～4-4 為準。

## 檔案分類

| 檔案 | 性質 | 應如何解讀 |
|---|---|---|
| [research_summary.md](research_summary.md) | **依正式論文校正的摘要** | 附有研究方法、主結果與限制 |
| [strategy_rules.md](strategy_rules.md) | **依正式論文校正的方法說明** | 不等於公開回測程式完整實現 |
| [limitations.md](limitations.md) | **依正式論文校正的限制說明** | 不主張已有統計顯著性結論 |
| [main_results.csv](main_results.csv) | **歷史探索實驗** | 包含 Chen 與籌碼配置，非正式論文表 4-3 的數值來源 |
| [all_experiments_summary.csv](all_experiments_summary.csv) | **歷史進度清單** | `pending`／`running` 為建立清單時狀態，不能視為最新完成情況 |
| [walk_forward_experiment_log.md](walk_forward_experiment_log.md) | **歷史擴張視窗實驗記錄** | 主要 OOS 折次為 2018–2025，不等於最終論文固定切分主結果 |
| [walk_forward_results_2000_time.csv](walk_forward_results_2000_time.csv) | **歷史探索 CSV** | 與正式論文主表採不同期間／程序 |
| [walk_forward_results_2008_time.csv](walk_forward_results_2008_time.csv) | **歷史探索 CSV** | 與正式論文主表採不同期間／程序 |
| [statistical_tests.csv](statistical_tests.csv) | **未填值的檢定規劃表** | `statistic`、`p_value` 欄位為空，**沒有可引用的檢定結果** |

## 不可混用的主結果

- 論文表 4-1：W20H5 單批次分類基準 D10−D1 年化報酬差 **49.39%**。
- 論文表 4-2：W20H5 RankNet 三次訓練平均 **59.77%**。
- 論文表 4-3：W20H5 核心受控比較基準 **57.90%**、獨立日報酬雙通道 **74.08%**。

49.39% 和 57.90% 為不同實驗彙整口徑，不能互換；**舊 CSV 的 36.39%、43.72%、44.34% 等數值也不是上述正式論文受控比較結果**。

保留歷史資料是為了追蹤研究過程，並不代表全部探索數據均通過與最終論文相同的驗證程序。