# mpl_drip

<div align="center">
<img src="https://raw.githubusercontent.com/TomHilder/mpl_drip/main/examples/histogram.png" alt="histogram" width="500"></img>
</div>

Installable matplotlib style sheet, a color cycle, and some nice colormaps.

I use these settings because I think they make plots that are "good", but also (as the kids would say) "dripped up".

## Installation

Currently clone and build. TODO: pypi

## Usage

```python
import mpl_drip
plt.style.use("mpl_drip.custom")
```

## Credit

The colour cycle is from [manim](https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html), and the `red_white_blue` colourmap is from [this repo](https://github.com/c-white/colormaps).
