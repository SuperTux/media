#!/usr/bin/env python3

import os
import sys
import PIL
from PIL import Image


def glyphsplit(filename, chars):
    print("processing {}".format(filename))
    img = Image.open(filename)

    glyphs = []

    cw = 80
    ch = 88

    cols = img.size[0] // cw
    rows = img.size[1] // ch

    print(len(chars), cols * rows)
    assert len(chars) == cols * rows

    for y in range(0, rows):
        for x in range(0, cols):
            glyph_idx = x + cols * y
            if chars[glyph_idx] == " ":
                continue
            glyph = img.crop((x * cw,
                              y * ch,
                              x * cw + cw,
                              y * ch + ch))
            out_filename = "{:04x}.png".format(ord(chars[glyph_idx]))
            out_filename = os.path.join("glyphs", out_filename)
            print("saving {}".format(out_filename))
            assert not os.path.exists(out_filename)
            glyph.save(out_filename)


glyphsplit("font-game.png",
           "\0!\"#$%&'()*+,-./"
           "0123456789:;<=>?"
           "@ABCDEFGHIJKLMNO"
           "PQRSTUVWXYZ[\\]^_"
           "`abcdefghijklmno"
           "pqrstuvwxyz{|}~ "
           " ¡¢£¤¥¦§¨©ª«¬ ®¯"
           "°±²³´µ¶·¸¹º»¼½¾¿"
           "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏ"
           "ÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"
           "àáâãäåæçèéêëìíîï"
           "ðñòóôõö÷øùúûüýþÿ"
           "ĀāĂăĄąĆćĈĉĊċČčĎď"
           "ĐđĒēĔĕĖėĘęĚěĜĝĞğ"
           "ĠġĢģĤĥĦħĨĩĪīĬĭĮį"
           "İıĲĳĴĵĶķĸĹĺĻļĽľĿ"
           "ŀŁłŃńŅņŇňŉŊŋŌōŎŏ"
           "ŐőŒœŔŕŖŗŘřŚśŜŝŞş"
           "ŠšŢţŤťŦŧŨũŪūŬŭŮů"
           "ŰűŲųŴŵŶŷŸŹźŻżŽžſ"
           "…ắầặảạếệẻịỉốộồơớ"
           "ởợụủưựửứừữọấểềỏậ")

glyphsplit("font-cyr.png",
           "ӘЁӨҢЄ ІЇ ЎҺҖҮ   "
           "АБВГДЕЖЗИЙКЛМНОП"
           "РСТУФХЦЧШЩЪЫЬЭЮЯ"
           "абвгдежзийклмноп"
           "рстуфхцчшщъыьэюя"
           " ё  є ії ўһүәҗөң")

glyphsplit("font-greek.png",
           "ΑΒΓΔΕΖΗΙΚΛΜΝΞΟΠΡ"
           "ΣΤΥΦΧΨΩΉΈΆ      "
           "αβγδεζηικλμνξοπρ"
           "ςστυφχψω        "
           "Θθ              "
           "άέίύώήό         ")

# EOF #
