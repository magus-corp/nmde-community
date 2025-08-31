#!/bin/bash

# Ensure zsh is installed for Arch Linux
if ! command -v zsh &>/dev/null; then
  echo "Zsh is not installed. Installing it now using pacman..."
  sudo pacman -S --noconfirm zsh

  # Verify installation
  if ! command -v zsh &>/dev/null; then
    echo "Failed to install Zsh. Please install it manually and run this script again."
    exit 1
  fi
  echo "Zsh has been successfully installed."
fi

echo "Setting up Zsh and Powerlevel10k..."

# Install Oh My Zsh
echo "Installing Oh My Zsh..."
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
else
  echo "Oh My Zsh is already installed."
fi

# Install Powerlevel10k
echo "Installing Powerlevel10k..."
if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k" ]; then
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
else
  echo "Powerlevel10k is already installed."
fi

# Install zsh-autosuggestions
echo "Installing zsh-autosuggestions..."
if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions" ]; then
  git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
else
  echo "zsh-autosuggestions is already installed."
fi

# Install zsh-syntax-highlighting
echo "Installing zsh-syntax-highlighting..."
if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting" ]; then
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
else
  echo "zsh-syntax-highlighting is already installed."
fi

# Link .zshrc and .p10k.zsh
echo "Linking .zshrc and .p10k.zsh..."
ln -sf "$HOME/.local/share/nmde/default/zsh/zshrc" "$HOME/.zshrc"
ln -sf "$HOME/.local/share/nmde/default/zsh/p10k.zsh" "$HOME/.p10k.zsh"

# Set zsh as default shell in a non-interactive way
echo "Setting zsh as the default shell for user $USER..."
sudo usermod --shell "$(which zsh)" "$USER"
echo "Default shell has been set to Zsh. Please log out and log back in for the change to take effect."

echo "Zsh and Powerlevel10k setup complete. Remember to run 'p10k configure' after logging into zsh for the first time."
