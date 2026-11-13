"""news-image-01 entry: copy the bundled image to the output directory.

The image is a fixed, original collage summarising the world news of
Friday 13 November 2026 (see NOTES.md). The program does no network
access and no drawing: it only copies the bytes, so every run writes
identical output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = OUT_DIR / "entry.png"
    shutil.copyfile(src, dst)
    # Guard against a truncated copy: the gate rejects a partial image.
    if dst.stat().st_size != src.stat().st_size:
        raise RuntimeError("copied entry.png has an unexpected size")


if __name__ == "__main__":
    main()
