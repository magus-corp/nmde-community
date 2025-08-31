"""Video utility functions."""

import subprocess
from pathlib import Path
import shutil

def mkv_to_mp4(input_file: str):
    """
    Converts a Matroska video file (MKV) to an MP4 container without re-encoding video.
    """
    input_path = Path(input_file)
    output_path = input_path.with_suffix(".mp4")

    if not input_path.is_file():
        print(f"Error: Input file not found at '{input_path}'")
        return

    if not shutil.which("ffmpeg"):
        print("Error: ffmpeg is not installed. Please install it to use this script.")
        return

    print(f"Converting '{input_path}' to '{output_path}'...")
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-i", str(input_path),
                "-map", "0",
                "-c", "copy",
                "-c:a", "aac",
                str(output_path),
            ],
            check=True,
        )
        print("Conversion complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        # This should be caught by shutil.which, but as a fallback
        print("Error: ffmpeg is not installed. Please install it to use this script.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        mkv_to_mp4(sys.argv[1])
    else:
        print("Usage: python -m nmde.spellbook.video <input_file.mkv>")
