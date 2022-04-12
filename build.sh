#!/bin/bash

echo "Packing for Kodi <=18 (Python 2)"
zip -r -0 plugin.video.2x2.zip plugin.video.2x2

echo "Packing for Kodi >=19 (Python 3)"
cp plugin.video.2x2/addon.xml addon.xml.bak
sed -i "s/2.1.0/3.0.0/gi" plugin.video.2x2/addon.xml
zip -r -0 plugin.video.2x2-matrix.zip plugin.video.2x2
mv addon.xml.bak plugin.video.2x2/addon.xml

echo "Done."
