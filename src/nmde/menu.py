"""Functions for handling NMDE menus."""

import subprocess

def show_power_menu():
    """Displays the power menu using walker and executes the selected command."""
    menu_options = " Lock\n󱄄 Save\n󰤄 Suspend\n Relaunch\n󰜉 Restart\n󰐥 Shutdown"
    try:
        selection_process = subprocess.run(
            ["walker", "--dmenu", "--theme", "dmenu_150"],
            input=menu_options,
            capture_output=True,
            text=True,
            check=True,
        )
        selection = selection_process.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error running walker: {e}")
        return

    if "Lock" in selection:
        subprocess.run(["hyprlock"])
    elif "Save" in selection:
        subprocess.run(["~/.local/share/nmde/bin/nmde-launch-screensaver"])
    elif "Suspend" in selection:
        subprocess.run(["systemctl", "suspend"])
    elif "Relaunch" in selection:
        subprocess.run(["uwsm", "stop"])
    elif "Restart" in selection:
        subprocess.run(["systemctl", "reboot"])
    elif "Shutdown" in selection:
        subprocess.run(["systemctl", "poweroff"])

if __name__ == "__main__":
    show_power_menu()
