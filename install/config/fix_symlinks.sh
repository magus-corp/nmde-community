#!/bin/bash
# This script replaces copied configuration files with symlinks to the nmde repository.

for config_path in $HOME/.local/share/nmde/config/*; do
  config_name=$(basename "$config_path")
  target_path="$HOME/.config/$config_name"
  echo "Replacing $target_path with a symlink."
  rm -rf "$target_path"
  ln -s "$config_path" "$target_path"
done

echo "Replacing ~/.bashrc with a symlink."
rm -f $HOME/.bashrc
ln -s $HOME/.local/share/nmde/default/bashrc $HOME/.bashrc

echo "Done. Please restart Hyprland for the changes to take effect."
