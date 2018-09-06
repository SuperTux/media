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

for filename in os.listdir("glyphs"):
    idx = int(filename[0:4], 16)
    print("processing {} -> {}".format(filename, idx))
    glyph = font.createChar(idx)
    glyph.importOutlines(os.path.join("glyphs", filename))
    font.selection.select(idx)
    font.autoTrace()
    font.autoWidth(200)

font.generate("/tmp/SuperTux-Medium.otf")
font.save("/tmp/SuperTux-Medium.sfd")

# EOF #
