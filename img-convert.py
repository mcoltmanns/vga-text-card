import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".him"
    
    im = Image.open(f + ".png")
    out = open(outfile, "wb")
    
    width, height = im.size

    for x in range(width):
        for y in range(height):
            px = im.getpixel((y,x)) # not sure why these have to be backwards
            # 3 bits for r, 3 for g, 2 for b
            r = (px[0] >> 5) << 5
            g = (px[1] >> 5) << 2
            b = (px[2] >> 6)
            out.write((r+g+b).to_bytes(1, 'little'))

    out.close()