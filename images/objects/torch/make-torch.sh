#!/bin/sh

set -e

for i in flame[1-4].xcf; do
  xcf2png "$i" -o "${i%%.xcf}.png"
  convert -scale 50% "${i%%.xcf}.png" "${i%%.xcf}.png"
done

# EOF #
