#!/bin/bash

ansi_art='                                                                   
▗▖  ▗▖▗▖  ▗▖▗▄▄▄ ▗▄▄▄▖
▐▛▚▖▐▌▐▛▚▞▜▌▐▌  █▐▌   
▐▌ ▝▜▌▐▌  ▐▌▐▌  █▐▛▀▀▘
▐▌  ▐▌▐▌  ▐▌▐▙▄▄▀▐▙▄▄▖'
clear
echo -e "
$ansi_art
"

sudo pacman -Sy --noconfirm --needed git

echo -e "
Cloning nmde..."
rm -rf ~/.local/share/nmde/
git clone https://github.com/magus-corp/nmde.git ~/.local/share/nmde >/dev/null

# Use custom branch if instructed
if [[ -n "$nmde_REF" ]]; then
  echo -e "\eUsing branch: $nmde_REF"
  cd ~/.local/share/nmde
  git fetch origin "${nmde_REF}" && git checkout "${nmde_REF}"
  cd -
fi

echo -e "
Installation starting..."
bash ~/.local/share/nmde/install.sh
