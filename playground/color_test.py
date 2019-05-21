from terminal_palette import Palette

palette = Palette()

print(palette.rgb(10, 147, 256)("Hello, World!")) # foreground
print(palette.bg_rgb(255, 100, 147)("Hello, World!")) # background

print(palette.bg_rgb(255, 120, 33)(chr(49)))

