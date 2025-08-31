"""Functions for refreshing NMDE components."""

import subprocess
import shutil
import filecmp
from pathlib import Path
import time
import os
from .waybar import restart_waybar

def refresh_config(config_file: str):
    """
    Deploys a config file from the nmde defaults to the user's .config directory.
    """
    home = Path.home()
    user_config_file = home / ".config" / config_file
    default_config_file = home / ".local/share/nmde/config" / config_file
    backup_config_file = user_config_file.parent / f"{user_config_file.name}.bak.{int(time.time())}"

    # Create parent directory if it doesn't exist
    user_config_file.parent.mkdir(parents=True, exist_ok=True)

    # Create preliminary backup
    if user_config_file.exists():
        shutil.copy2(user_config_file, backup_config_file)

    # Replace config with new default
    if default_config_file.exists():
        shutil.copy2(default_config_file, user_config_file)
    else:
        print(f"Warning: Default config file not found: {default_config_file}")
        return

    # Compare and delete/inform accordingly
    if user_config_file.exists() and backup_config_file.exists():
        if filecmp.cmp(user_config_file, backup_config_file, shallow=False):
            backup_config_file.unlink()
        else:
            print(f"\033[31mReplaced {user_config_file} with new nmde default.")
            print(f"Saved backup as {backup_config_file}.\n\n\033[32mChanges:\033[0m")
            # Running diff command
            diff_process = subprocess.run(
                ["diff", str(user_config_file), str(backup_config_file)],
                capture_output=True,
                text=True,
            )
            print(diff_process.stdout)

def refresh_plymouth():
    """Refreshes the plymouth theme."""
    print("This command requires sudo to copy files to /usr/share/plymouth/themes/nmde/")
    home = Path.home()
    nmde_plymouth_dir = home / ".local/share/nmde/default/plymouth"
    plymouth_theme_dir = "/usr/share/plymouth/themes/nmde"

    try:
        subprocess.run(["sudo", "mkdir", "-p", plymouth_theme_dir], check=True)
        for file in nmde_plymouth_dir.glob("*"):
            subprocess.run(["sudo", "cp", str(file), plymouth_theme_dir], check=True)
        subprocess.run(["sudo", "plymouth-set-default-theme", "-R", "nmde"], check=True)
        print("Plymouth theme refreshed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error refreshing plymouth theme: {e}")
    except FileNotFoundError:
        print("Error: 'sudo' command not found. Please ensure it is installed and in your PATH.")

def refresh_applications():
    """Refreshes the application launchers and icons."""
    home = Path.home()
    nmde_root = home / ".local/share/nmde"
    icons_dir = home / ".local/share/icons/hicolor/48x48/apps"
    apps_dir = home / ".local/share/applications"
    nmde_icons_dir = nmde_root / "applications/icons"
    nmde_apps_dir = nmde_root / "applications"
    nmde_hidden_apps_dir = nmde_apps_dir / "hidden"
    nmde_xtras_apps_dir = nmde_apps_dir / "xtras"

    # Copy and sync icon files
    icons_dir.mkdir(parents=True, exist_ok=True)
    if nmde_icons_dir.exists():
        for icon_file in nmde_icons_dir.glob("*.png"):
            shutil.copy2(icon_file, icons_dir)
    subprocess.run(["gtk-update-icon-cache", str(home / ".local/share/icons/hicolor")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Copy .desktop declarations
    apps_dir.mkdir(parents=True, exist_ok=True)
    if nmde_apps_dir.exists():
        for desktop_file in nmde_apps_dir.glob("*.desktop"):
            shutil.copy2(desktop_file, apps_dir)
    if nmde_hidden_apps_dir.exists():
        for desktop_file in nmde_hidden_apps_dir.glob("*.desktop"):
            shutil.copy2(desktop_file, apps_dir)

    # Only copy xtras if user is not in bare mode
    if not (home / ".local/state/nmde/bare.mode").exists() and not os.getenv("nmde_BARE"):
        if nmde_xtras_apps_dir.exists():
            for desktop_file in nmde_xtras_apps_dir.glob("*.desktop"):
                shutil.copy2(desktop_file, apps_dir)

    subprocess.run(["update-desktop-database", str(apps_dir)])


def refresh_hyprlock():
    """Refreshes the hyprlock configuration."""
    refresh_config("hypr/hyprlock.conf")

def refresh_hypridle():
    """Refreshes the hypridle configuration and restarts the service."""
    refresh_config("hypr/hypridle.conf")
    subprocess.run(["pkill", "-x", "hypridle"])
    subprocess.Popen(["uwsm", "app", "--", "hypridle"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def refresh_swayosd():
    """Refreshes the swayosd configuration and restarts the service."""
    refresh_config("swayosd/config.toml")
    refresh_config("swayosd/style.css")
    subprocess.run(["pkill", "swayosd-server"])
    subprocess.Popen(["setsid", "uwsm", "app", "--", "swayosd-server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def refresh_walker():
    """Refreshes the walker configuration and restarts the service."""
    refresh_config("walker/config.toml")
    subprocess.run(["pkill", "walker"])
    subprocess.Popen(["setsid", "uwsm", "app", "--", "walker", "--gapplication-service"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def refresh_waybar():
    """Refreshes the waybar configuration and restarts the service."""
    refresh_config("waybar/config.jsonc")
    refresh_config("waybar/style.css")
    restart_waybar()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        refresh_config(sys.argv[1])
    else:
        print("Usage: python -m nmde.refresh [config_file]")
