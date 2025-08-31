"""Command-line interface for the nmde application."""

import argparse

def main():
    """Main entry point for the nmde CLI."""
    parser = argparse.ArgumentParser(description="NMDE main application.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Composes command
    composes_parser = subparsers.add_parser("composes", help="Manage docker-compose stacks.")
    composes_parser.set_defaults(func=run_composes)

    # Generate logo command
    generate_logo_parser = subparsers.add_parser("generate-logo", help="Generate the NMDE logo.")
    generate_logo_parser.set_defaults(func=run_generate_logo)

    # Power Menu command
    power_menu_parser = subparsers.add_parser("menu-power", help="Show the power menu.")
    power_menu_parser.set_defaults(func=run_power_menu)

    # Restart Waybar command
    restart_waybar_parser = subparsers.add_parser("restart-waybar", help="Restart the Waybar service.")
    restart_waybar_parser.set_defaults(func=run_restart_waybar)

    # Refresh command
    refresh_parser = subparsers.add_parser("refresh", help="Refresh NMDE components.")
    refresh_subparsers = refresh_parser.add_subparsers(dest="component", help="Component to refresh")

    refresh_applications_parser = refresh_subparsers.add_parser("applications", help="Refresh application launchers and icons.")
    refresh_applications_parser.set_defaults(func=run_refresh_applications)

    refresh_config_parser = refresh_subparsers.add_parser("config", help="Refresh a config file.")
    refresh_config_parser.add_argument("config_file", help="Path to the config file to refresh.")
    refresh_config_parser.set_defaults(func=run_refresh_config)

    refresh_hypridle_parser = refresh_subparsers.add_parser("hypridle", help="Refresh hypridle configuration.")
    refresh_hypridle_parser.set_defaults(func=run_refresh_hypridle)

    refresh_hyprlock_parser = refresh_subparsers.add_parser("hyprlock", help="Refresh hyprlock configuration.")
    refresh_hyprlock_parser.set_defaults(func=run_refresh_hyprlock)

    refresh_plymouth_parser = refresh_subparsers.add_parser("plymouth", help="Refresh plymouth theme.")
    refresh_plymouth_parser.set_defaults(func=run_refresh_plymouth)

    refresh_swayosd_parser = refresh_subparsers.add_parser("swayosd", help="Refresh swayosd configuration.")
    refresh_swayosd_parser.set_defaults(func=run_refresh_swayosd)

    refresh_walker_parser = refresh_subparsers.add_parser("walker", help="Refresh walker configuration.")
    refresh_walker_parser.set_defaults(func=run_refresh_walker)

    refresh_waybar_parser = refresh_subparsers.add_parser("waybar", help="Refresh waybar configuration.")
    refresh_waybar_parser.set_defaults(func=run_refresh_waybar)

    # Spellbook command
    spellbook_parser = subparsers.add_parser("spellbook", help="A collection of utility scripts.")
    spellbook_subparsers = spellbook_parser.add_subparsers(dest="spell", help="Available spells")

    mkv_to_mp4_parser = spellbook_subparsers.add_parser("mkv-to-mp4", help="Convert an MKV file to MP4.")
    mkv_to_mp4_parser.add_argument("input_file", help="Path to the MKV file to convert.")
    mkv_to_mp4_parser.set_defaults(func=run_mkv_to_mp4)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

def run_composes(args):
    """Runs the nmde-composes TUI application."""
    from .composes import NmdeComposes
    app = NmdeComposes()
    app.run()

def run_generate_logo(args):
    """Runs the logo generation script."""
    from .logo import generate_logo
    generate_logo()

def run_power_menu(args):
    """Shows the power menu."""
    from .menu import show_power_menu
    show_power_menu()

def run_restart_waybar(args):
    """Restarts the Waybar service."""
    from .waybar import restart_waybar
    restart_waybar()

def run_refresh_applications(args):
    """Refreshes application launchers and icons."""
    from .refresh import refresh_applications
    refresh_applications()

def run_refresh_config(args):
    """Refreshes a config file."""
    from .refresh import refresh_config
    refresh_config(args.config_file)

def run_refresh_hypridle(args):
    """Refreshes hypridle configuration."""
    from .refresh import refresh_hypridle
    refresh_hypridle()

def run_refresh_hyprlock(args):
    """Refreshes hyprlock configuration."""
    from .refresh import refresh_hyprlock
    refresh_hyprlock()

def run_refresh_plymouth(args):
    """Refreshes plymouth theme."""
    from .refresh import refresh_plymouth
    refresh_plymouth()

def run_refresh_swayosd(args):
    """Refreshes swayosd configuration."""
    from .refresh import refresh_swayosd
    refresh_swayosd()

def run_refresh_walker(args):
    """Refreshes walker configuration."""
    from .refresh import refresh_walker
    refresh_walker()

def run_refresh_waybar(args):
    """Refreshes waybar configuration."""
    from .refresh import refresh_waybar
    refresh_waybar()

def run_mkv_to_mp4(args):
    """Converts an MKV file to MP4."""
    from .spellbook.video import mkv_to_mp4
    mkv_to_mp4(args.input_file)

if __name__ == "__main__":
    main()
