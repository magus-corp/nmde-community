#!/bin/bash

if [ -z "$nmde_BARE" ]; then
  paru -S --noconfirm --needed \
    gnome-calculator gnome-keyring signal-desktop \
    obsidian-bin libreoffice obs-studio kdenlive \
    xournalpp localsend-bin

  # Packages known to be flaky or having key signing issues are run one-by-one
  for pkg in pinta typora spotify zoom; do
    paru -S --noconfirm --needed "$pkg" ||
      echo -e "\e[31mFailed to install $pkg. Continuing without!\e[0m"
  done

  paru -S --noconfirm --needed 1password-beta 1password-cli ||
    echo -e "\e[31mFailed to install 1password. Continuing without!\e[0m"
fi

# Copy over nmde applications
source ~/.local/share/nmde/bin/nmde-refresh-applications || true
