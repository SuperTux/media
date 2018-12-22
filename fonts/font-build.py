#!/usr/bin/env python2

# SuperTux Font Build Script
# Copyright (C) 2018 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import fontforge
import psMat;

font = fontforge.font()

font.encoding = "unicode"

font.familyname = "SuperTux"
font.fullname = "SuperTux-Medium"
font.fontname = "SuperTux-Medium"

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
    # font.autoHint()

# for glyph in font.glyphs():
#     glyph.transform(psMat.translate(0, 30))

# font.ascent = 750
# font.descent = 150

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

# The next step requires the Google Noto fonts extracted into the noto/
# directory, they can be found at:
# https://noto-website-2.storage.googleapis.com/pkgs/Noto-hinted.zip

font.mergeFonts("noto/NotoSans-Regular.ttf")
font.mergeFonts("noto/NotoSansArabic-Regular.ttf")
font.mergeFonts("noto/NotoSansHebrew-Regular.ttf")

# These make fontforge crash
# font.mergeFonts("noto/NotoSansCJKjp-Regular.otf")
# font.mergeFonts("noto/NotoSansCJKkr-Regular.otf")

if not os.path.exists("build"):
    os.mkdir("build")
font.generate("build/SuperTux-Medium.otf")
font.generate("build/SuperTux-Medium.ttf")
font.save("build/SuperTux-Medium.sfd")

# EOF #
