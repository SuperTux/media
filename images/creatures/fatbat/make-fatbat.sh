#!/bin/sh

set -e

for i in fatbat-anim000?.xcf; do
  xcf2png "$i" -o "${i%%.xcf}.png"
  convert -crop 128x84+0+20 -scale 50% "${i%%.xcf}.png" "${i%%.xcf}.png"
done

# EOF #
