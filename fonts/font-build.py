#!/usr/bin/env python2

import os
import sys
import fontforge

font = fontforge.font()
font.encoding = "unicode"
for filename in os.listdir("glyphs"):
    idx = int(filename[0:4], 16)
    print("processing {} -> {}".format(filename, idx))
    glyph = font.createChar(idx)
    glyph.importOutlines(os.path.join("glyphs", filename))
    font.selection.select(idx)
    font.autoTrace()

font.generate("/tmp/out.otf")
font.save("/tmp/out.sfd")

# EOF #
