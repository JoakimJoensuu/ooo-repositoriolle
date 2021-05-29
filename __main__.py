from PIL import Image
import numpy as np

SHADES_PER_COLOR = 2
HEIGHT = 2160
WIDTH = 3840

COLOR_SHADES = 255
NUMBER_OF_COLORS = 3

shade_spacing = COLOR_SHADES / (SHADES_PER_COLOR - 1) if SHADES_PER_COLOR > 1 else 255
shades = np.array(
    np.arange(0, COLOR_SHADES + shade_spacing, shade_spacing), dtype=np.uint8
)
shades_mirrored = np.concatenate((shades, np.flip(shades)))

red = np.tile(shades_mirrored, int(SHADES_PER_COLOR ** 2 / 2))
green = np.tile(np.repeat(shades_mirrored, SHADES_PER_COLOR), int(SHADES_PER_COLOR / 2))

if SHADES_PER_COLOR % 2:
    red = np.concatenate((red, shades))
    green = np.concatenate((green, np.repeat(shades, SHADES_PER_COLOR)))


blue = np.repeat(shades, SHADES_PER_COLOR ** 2)

red = red[..., None]
green = green[..., None]
blue = blue[..., None]

rgb = np.dstack((red, green, blue))
rgb = np.repeat(rgb, HEIGHT/SHADES_PER_COLOR**3, 0)
rgb = np.repeat(rgb, WIDTH, 1)

img = Image.fromarray(rgb, "RGB")
img.save("color_bands.png")
