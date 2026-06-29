import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from image_builder import ImageSpec, draw_ohlc_image


def make_demo_ohlc(window: int = 20) -> np.ndarray:
    rng = np.random.default_rng(42)

    close = 100 + np.cumsum(rng.normal(0, 1.2, size=window))
    open_ = close + rng.normal(0, 0.6, size=window)

    high = np.maximum(open_, close) + rng.uniform(0.3, 1.5, size=window)
    low = np.minimum(open_, close) - rng.uniform(0.3, 1.5, size=window)

    return np.column_stack([open_, high, low, close]).astype(float)


def main() -> None:
    spec = ImageSpec(
        window=20,
        height=64,
        width=20 * 3,
        ohlc_bar_width=3,
    )

    ohlc = make_demo_ohlc(spec.window)
    image = draw_ohlc_image(ohlc, spec)

    out_dir = ROOT / "outputs_sample" / "sample_images"
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "sample_001.png"

    plt.figure(figsize=(6, 4))
    plt.imshow(image, cmap="gray", vmin=0, vmax=255)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(out_path, dpi=200, bbox_inches="tight", pad_inches=0)
    plt.close()

    print(f"saved: {out_path}")


if __name__ == "__main__":
    main()
