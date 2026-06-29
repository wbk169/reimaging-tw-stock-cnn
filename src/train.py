"""
Training entry point.

This public version documents the training workflow:
1. Load experiment config.
2. Check CUDA GPU.
3. Build dataset index.
4. Generate price images on CPU.
5. Train CNN on GPU.
6. Export out-of-sample predictions.
"""

import argparse
from pathlib import Path

import torch
import yaml


def load_config(path: str) -> dict:
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"找不到設定檔：{config_path}")

    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def print_runtime_info(seed: int) -> None:
    if not torch.cuda.is_available():
        raise RuntimeError("找不到 CUDA GPU，請確認 NVIDIA driver 與 PyTorch CUDA 版本。")

    print(f"PyTorch Version: {torch.__version__}")
    print(f"CUDA Device Name: {torch.cuda.get_device_name(0)}")
    print(f"Global Seed: {seed}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True)
    args = parser.parse_args()

    config = load_config(args.config)
    seed = int(config["model"]["seed"])

    print_runtime_info(seed)

    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = True

    print("訓練流程摘要：")
    print(f"- experiment: {config['experiment_name']}")
    print(f"- image variant: {config['image']['variant']}")
    print(f"- window: {config['image']['window']}")
    print(f"- horizon: {config['image']['horizon']}")
    print(f"- channels: {config['model']['channels']}")
    print(f"- batch size: {config['model']['batch_size']}")
    print(f"- learning rate: {config['model']['learning_rate']}")

    print("公開版 train.py 僅保留流程入口；完整訓練程式於本機研究環境執行。")


if __name__ == "__main__":
    main()
