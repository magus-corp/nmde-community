#!/bin/bash

# This script prepares the environment for the nmde-env script.
# It should be run by the Tester.

# Install sqlite3
echo "Installing sqlite3..."
sudo apt-get update && sudo apt-get install -y sqlite3

# Create the database and table
echo "Creating the database and table..."
sqlite3 /home/cmgus/projects/magus/nmde/config/nmde.db "CREATE TABLE IF NOT EXISTS env_vars (app_name TEXT, key TEXT, value TEXT, PRIMARY KEY (app_name, key));"

echo "Environment setup complete."
