#!/bin/sh

set -e

for i in kirby2-anim000?.xcf; do
  xcf2png "$i" -o "${i%%.xcf}.png"
  convert -crop 107x107+10+0 -scale 50% "${i%%.xcf}.png" "${i%%.xcf}.png"
done

# EOF #
