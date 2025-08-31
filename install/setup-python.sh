#!/bin/bash
#
# This script sets up the Python virtual environment and installs necessary tools.
# It should be run by the Tester.

echo "Setting up Python virtual environment for tools..."

# Define the venv directory relative to the script's location
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_DIR=$(dirname "$SCRIPT_DIR")
VENV_DIR="$PROJECT_DIR/.venv"

# Create the virtual environment using uv
if command -v uv &> /dev/null; then
    echo "Creating virtual environment at $VENV_DIR..."
    uv venv "$VENV_DIR" --python python3
else
    echo "Error: 'uv' is not installed. Please install it first."
    exit 1
fi


# Install yq into the virtual environment
echo "Installing yq..."
source "$VENV_DIR/bin/activate"
uv pip install yq

echo "Python setup complete."
