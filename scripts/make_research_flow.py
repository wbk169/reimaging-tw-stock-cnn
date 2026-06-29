import matplotlib.pyplot as plt

steps = [
    "TEJ OHLCV / Chip Data",
    "Data Cleaning",
    "Price Image Generation",
    "CNN Training",
    "Out-of-Sample Prediction",
    "Stock Ranking",
    "Portfolio Backtest",
    "Statistical Tests",
]

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis("off")

y_positions = list(range(len(steps), 0, -1))

for y, step in zip(y_positions, steps):
    ax.text(
        0.5,
        y,
        step,
        ha="center",
        va="center",
        fontsize=14,
        bbox=dict(boxstyle="round,pad=0.4", edgecolor="black", facecolor="white"),
    )

    if y > 1:
        ax.annotate(
            "",
            xy=(0.5, y - 0.35),
            xytext=(0.5, y - 0.75),
            arrowprops=dict(arrowstyle="->", lw=1.5),
        )

ax.set_xlim(0, 1)
ax.set_ylim(0.5, len(steps) + 0.5)

plt.tight_layout()
plt.savefig("outputs_sample/research_flow.png", dpi=200)
print("saved: outputs_sample/research_flow.png")
