#!/bin/bash

# TODO: Add a modern Plymouth theme
# paru -S --noconfirm --needed plymouth-theme-adi-arch

# Use dark mode for QT apps too (like kdenlive)
if ! paru -Q kvantum-qt5 &>/dev/null; then
  paru -S --noconfirm kvantum-qt5
fi

# Prefer dark mode everything
if ! paru -Q gnome-themes-extra &>/dev/null; then
  paru -S --noconfirm gnome-themes-extra # Adds Adwaita-dark theme
fi

# Allow icons to match the theme
if ! paru -! yaru-icon-theme &>/dev/null; then
  paru -S --noconfirm yaru-icon-theme
fi

gsettings set org.gnome.desktop.interface gtk-theme "Adwaita-dark"
gsettings set org.gnome.desktop.interface color-scheme "prefer-dark"
gsettings set org.gnome.desktop.interface icon-theme "Yaru-blue"

# Setup theme links
mkdir -p ~/.config/nmde/themes
for f in ~/.local/share/nmde/themes/*; do ln -nfs "$f" ~/.config/nmde/themes/; done

# Set initial theme
mkdir -p ~/.config/nmde/current
ln -snf ~/.config/nmde/themes/tokyo-night ~/.config/nmde/current/theme
ln -snf ~/.config/nmde/current/theme/backgrounds/1-scenery-pink-lakeside-sunset-lake-landscape-scenic-panorama-7680x3215-144.png ~/.config/nmde/current/background

# Set specific app links for current theme
ln -snf ~/.config/nmde/current/theme/neovim.lua ~/.config/nvim/lua/plugins/theme.lua

mkdir -p ~/.config/btop/themes
ln -snf ~/.config/nmde/current/theme/btop.theme ~/.config/btop/themes/current.theme

mkdir -p ~/.config/mako
ln -snf ~/.config/nmde/current/theme/mako.ini ~/.config/mako/config
