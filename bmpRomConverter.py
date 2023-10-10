import os, sys, math
from PIL import Image

# expects a 128x128 bitmap png of an 8x8 font
# dwarf fortress tilesets are a great place to find these!

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".rom"

    bmp = Image.open(f + ".png").convert("RGB")
    rom = open(outfile, "wb")

    width, height = bmp.size

    for y in range(16):
        for x in range(16):
            for charY in range(8):
                for charX in range(8):
                    r, g, b = bmp.getpixel((x * 8 + charX, y * 8 + charY))
                    pxval = 0
                    if r == g == b:
                        pxval = ((r >> 5) << 5) + ((g >> 5) << 2) + (b >> 6)
                    rom.write(pxval.to_bytes(1, 'little'))
                # padding bytes
                p = 0
                rom.write(p.to_bytes(8))
