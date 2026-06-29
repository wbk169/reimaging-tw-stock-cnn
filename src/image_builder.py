"""
Price image builder.

This module converts OHLC windows into black-white price images.
The drawing logic follows the 3-pixel OHLC bar design:

- left pixel: open
- middle pixel: high-low vertical line
- right pixel: close
"""

from dataclasses import dataclass
import logging
import numpy as np


@dataclass(frozen=True)
class ImageSpec:
    window: int
    height: int
    width: int
    ohlc_bar_width: int = 3


def draw_ohlc_image(ohlc: np.ndarray, spec: ImageSpec) -> np.ndarray:
    """
    Draw OHLC image on CPU using NumPy.

    Parameters
    ----------
    ohlc:
        Array with shape (window, 4), columns = open, high, low, close.
    spec:
        ImageSpec.

    Returns
    -------
    image:
        uint8 array with shape (height, width), background=0, line=255.
    """
    image = np.zeros((spec.height, spec.width), dtype=np.uint8)

    if ohlc.shape != (spec.window, 4):
        logging.warning("OHLC shape mismatch. Return black image.")
        return image

    if not np.isfinite(ohlc).all():
        logging.warning("OHLC contains NaN or inf. Return black image.")
        return image

    prices = ohlc.reshape(-1)
    p_min = float(np.min(prices))
    p_max = float(np.max(prices))

    if p_max <= p_min:
        logging.warning("Invalid OHLC price range. Return black image.")
        return image

    def price_to_y(price: float) -> int:
        scaled = (p_max - price) / (p_max - p_min)
        y = int(round(scaled * (spec.height - 1)))
        return int(np.clip(y, 0, spec.height - 1))

    for i in range(spec.window):
        x_left = i * spec.ohlc_bar_width
        x_mid = x_left + 1
        x_right = x_left + 2

        if x_right >= spec.width:
            break

        o, h, l, c = ohlc[i]

        y_o = price_to_y(o)
        y_h = price_to_y(h)
        y_l = price_to_y(l)
        y_c = price_to_y(c)

        y_top = min(y_h, y_l)
        y_bottom = max(y_h, y_l)

        image[y_o, x_left] = 255
        image[y_top:y_bottom + 1, x_mid] = 255
        image[y_c, x_right] = 255

    return image
