"""Functions for handling Waybar."""

import subprocess

def restart_waybar():
    """Restarts the Waybar service."""
    # Kill existing waybar processes, ignoring errors if none are running
    subprocess.run(["killall", "waybar"], check=False)

    # Start a new waybar process in the background
    subprocess.Popen(
        ["setsid", "uwsm", "app", "--", "waybar"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

if __name__ == "__main__":
    restart_waybar()
