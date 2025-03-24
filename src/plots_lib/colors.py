from pathlib import Path

import matplotlib.pyplot as plt

# Load the style sheet (so it applies to the rcParams)
style_file = Path(__file__).parent / "custom.mplstyle"
plt.style.use(style_file)

# Extract the color cycle from the style
_prop_cycle = plt.rcParams["axes.prop_cycle"]
COLORS = _prop_cycle.by_key().get("color", [])


# Make colors accessible by name
def get_color(index: int):
    """Returns a color from the style's color cycle by index."""
    return COLORS[index % len(COLORS)]  # Wrap around if index is too large
