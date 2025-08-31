#!/bin/bash

paru -S --noconfirm --needed \
  python-gobject \
  brightnessctl playerctl pamixer wiremix wireplumber \
  fcitx5 fcitx5-gtk fcitx5-qt wl-clip-persist \
  nautilus sushi ffmpegthumbnailer \
  slurp satty \
  mpv evince imv \
  qutebrowser

# Add screen recorder based on GPU
if lspci | grep -qi 'nvidia'; then
  paru -S --noconfirm --needed wf-recorder
else
  paru -S --noconfirm --needed wl-screenrec
fi
