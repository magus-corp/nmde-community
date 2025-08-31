# Utility Scripts

This directory contains general-purpose utility scripts that assist with various system tasks and workflows. These are typically single-execution scripts.

## Available Scripts

*   `backup_aider_data`: Backs up Aider-related data.
*   `create_shared_data_dirs`: Creates shared data directories.
*   `neo_note_dual`: Script for dual monitor setup (Neo Note).
*   `normal_dual_laptop`: Script for dual monitor setup (Normal Laptop).
*   `notebook_dual`: Script for dual monitor setup (Notebook).
*   `dev_server.py`: A simple Python-based web server to serve the repository files over the local network.

## Usage

To run any of these scripts, navigate to the `/home/magus/.config/mde/scripts/utility/` directory and execute them using `sh <script_name>` or `./<script_name>` if executable.

### Development Server for Local Installation

The `dev_server.py` script starts a local web server, allowing you to install the MDE environment on a new machine without exposing the repository to the public internet.

**To start the server:**

```bash
python3 /home/magus/.config/mde/scripts/utility/dev_server.py
```

The server will run on port 8000.

**To install on a new node:**

From the new machine, run the following command. Replace `<your-ip-address>` with the IP address of the machine running the server.

```bash
curl -sSL http://<your-ip-address>:8000/scripts/install/install_this_repo | bash
```
