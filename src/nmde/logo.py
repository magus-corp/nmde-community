"""Functions for handling the NMDE logo."""

import subprocess
from pathlib import Path

def generate_logo():
    """Generates the NMDE logo from a text file using ImageMagick."""
    nmde_root = Path.home() / ".local/share/nmde"
    logo_txt = nmde_root / "logo.txt"
    output_dir = nmde_root / "default/plymouth"
    output_file = output_dir / "logo.png"

    if not logo_txt.is_file():
        print(f"Error: logo.txt not found at {logo_txt}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating logo.png from logo.txt...")
    
    with open(logo_txt, "r") as f:
        logo_content = f.read()

    try:
        subprocess.run(
            [
                "magick",
                "-background", "none",
                "-fill", "white",
                "-font", "CaskaydiaMono-NF-Regular",
                "-pointsize", "14",
                f"label:{logo_content}",
                str(output_file),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        print(f"Successfully created logo.png at {output_file}")
    except subprocess.CalledProcessError as e:
        print("Error: Failed to generate logo.")
        print("Please ensure ImageMagick and the CaskaydiaMono Nerd Font are installed.")
        print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print("Error: Failed to generate logo.")
        print("Please ensure ImageMagick is installed and in your PATH.")

if __name__ == "__main__":
    generate_logo()
