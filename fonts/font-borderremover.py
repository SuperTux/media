#!/usr/bin/env python3

# Take an font image file, split it appart and recombine it without
# the 1px border around each glyph

import os
import sys
import PIL
from PIL import Image

for filename in sys.argv[1:]:
    img = Image.open(filename)

    glyphs = []

    cols = img.size[0] // 22
    rows = img.size[1] // 24

    # 352x528
    for y in range(0, rows):
        for x in range(0, cols):
            glyph = img.crop((x*22 + 1,
                              y*24 + 1,
                              x*22 + 22 - 1,
                              y*24 + 24 - 1))
            glyphs.append(glyph)

    out = Image.new(img.mode, (cols * 20, rows * 22))

    for y in range(0, rows):
        for x in range(0, cols):
            glyph = glyphs[x + cols * y]
            out.paste(glyph, (x * 20, y * 22))

    out_filename = os.path.join("/tmp/", os.path.basename(filename))
    print("writing {}".format(out_filename))
    out.save(out_filename)

# EOF #
