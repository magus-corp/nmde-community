#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# --- START: Make the script position-independent ---

# Define the destination directory for nmde
NMDE_DEST_DIR="$HOME/.local/share/nmde"
# Get the directory of the currently running script (assumes it's in the project root)
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

# Check if we are already running from the final destination directory
if [ "$SCRIPT_DIR" != "$NMDE_DEST_DIR" ]; then
  echo "Preparing nmde for installation..."
  # Ensure the parent directory exists
  mkdir -p "$HOME/.local/share"
  # Remove any previous installation to ensure a clean state
  rm -rf "$NMDE_DEST_DIR"
  # Copy the entire project directory to the destination
  cp -r "$SCRIPT_DIR" "$NMDE_DEST_DIR"
  echo "Installation files are now located in $NMDE_DEST_DIR."
  echo "Re-launching the installer from the new location..."
  echo ""
  # Execute the script from its new, standardized location and exit the current script
  bash "$NMDE_DEST_DIR/install.sh"
  exit 0
fi

# --- END: Make the script position-independent ---

# From this point on, the script is running from ~/.local/share/nmde
# All hardcoded paths will now resolve correctly.
nmde_INSTALL=$NMDE_DEST_DIR/install

# Check for --full flag to determine installation type
if [[ " $@ " =~ " --full " ]]; then
  nmde_BARE=""
else
  nmde_BARE="true"
fi

# Give people a chance to retry running the installation
catch_errors() {
  echo -e "
\e[31mnmde installation failed!\e[0m"
  echo "You can retry by running: bash ~/.local/share/nmde/install.sh"
  echo "Get help from the community: https://discord.gg/tXFUdasqhY"
}

trap catch_errors ERR

export nmde_text=$(gum input --placeholder "Enter the branding of your system" --prompt "Branding> ")
echo nmde_text >$NMDE_DEST_DIR/logo.txt

show_logo() {
  clear
  # All paths are now relative to the new script location
  tte -i "$NMDE_DEST_DIR/logo.txt" --frame-rate ${2:-120} ${1:-expand}
  echo
}

show_subtext() {
  echo "$1" | tte --frame-rate ${3:-640} ${2:-wipe}
  echo
}

# Install prerequisites
source $nmde_INSTALL/preflight/aur.sh
source $nmde_INSTALL/preflight/presentation.sh

# Configuration
show_logo beams 240
show_subtext "Let's install nmde! [1/5]"
source $nmde_INSTALL/config/identification.sh
source $nmde_INSTALL/config/config.sh
source $nmde_INSTALL/config/detect-keyboard-layout.sh
source $nmde_INSTALL/config/fix-fkeys.sh
source $nmde_INSTALL/config/network.sh
source $nmde_INSTALL/config/power.sh
source $nmde_INSTALL/config/timezones.sh
source $nmde_INSTALL/config/login.sh
source $nmde_INSTALL/config/nvidia.sh
source $nmde_INSTALL/config/fix_symlinks.sh

# Development
show_logo decrypt 920
show_subtext "Installing terminal tools [2/5]"
source $nmde_INSTALL/development/terminal.sh
source $nmde_INSTALL/development/development.sh
source $nmde_INSTALL/development/nvim.sh
source $nmde_INSTALL/development/ruby.sh
source $nmde_INSTALL/development/docker.sh
source $nmde_INSTALL/development/firewall.sh
source $nmde_INSTALL/development/zsh.sh

# Generate Plymouth Logo
show_logo slice 240
show_subtext "Generating custom boot logo"
$NMDE_DEST_DIR/bin/nmde-generate-logo

# Desktop
show_logo slice 60
show_subtext "Installing desktop tools [3/5]"
source $nmde_INSTALL/desktop/desktop.sh
source $nmde_INSTALL/desktop/hyprlandia.sh
source $nmde_INSTALL/desktop/theme.sh

source $nmde_INSTALL/desktop/bluetooth.sh
source $nmde_INSTALL/desktop/asdcontrol.sh
source $nmde_INSTALL/desktop/fonts.sh
source $nmde_INSTALL/desktop/printer.sh

# Apps
show_logo expand
show_subtext "Installing default applications [4/5]"
source $nmde_INSTALL/apps/webapps.sh
source $nmde_INSTALL/apps/xtras.sh
source $nmde_INSTALL/apps/mimetypes.sh

# Updates
show_logo highlight
show_subtext "Updating system packages [5/5]"
sudo updatedb
sudo pacman -Syu --noconfirm

# Reboot
show_logo laseretch 920
show_subtext "You're done! So we'll be rebooting now..."
sleep 2
reboot
