#!/usr/bin/env python2

import os
import sys
import fontforge

font = fontforge.font()

font.encoding = "unicode"

font.familyname = "SuperTux"
font.fullname = "SuperTux Medium"
font.fontname = "SuperTux Medium"

glyph = font.createChar(ord(" "))
glyph.width = 500

# Import and OCR the SuperTux font
for filename in os.listdir("glyphs"):
    idx = int(filename[0:4], 16)
    print("processing {} -> {}".format(filename, idx))
    glyph = font.createChar(idx)
    glyph.importOutlines(os.path.join("glyphs", filename))
    font.selection.select(idx)
    font.autoTrace()
    font.autoWidth(200)

# Set digits to fixed width

# Calculate max digit_width
digit_width = 0
for c in "0123456789":
    glyph = font[ord(c)]
    digit_width = max(digit_width, glyph.width)

# Or better hardcode it
digit_width = 725

for c in "0123456789":
    glyph = font[ord(c)]
    old_width = glyph.width
    glyph.width = digit_width

    w = glyph.left_side_bearing + glyph.right_side_bearing
    glyph.left_side_bearing = w / 2
    glyph.right_side_bearing = w / 2

    # print(glyph.layers)
    # glyph.layers[1].nltransform("x - 400", "y")

    # Set glyph width twice, since left/right_side_bearing leads to
    # rounding issues and unequal width
    glyph.width = digit_width

# font.mergeFonts("")

font.generate("/tmp/SuperTux-Medium.otf")
font.generate("/tmp/SuperTux-Medium.ttf")
font.save("/tmp/SuperTux-Medium.sfd")

# EOF #
