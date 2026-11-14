"""news-image-01 entry: copy the bundled image to the output directory.

Round 2 image (replaces round 1): a front page with one dominant lead photo
— the Ukraine peace talks, Europe getting a seat — above three mid stories
(Microsoft 365 outage, Nvidia CEO resigns, Hormuz tanker claim) and two
bottom stories (Indonesia's vice-presidential vote, the Nasser hospital
strike in Gaza). All six stories are from the verified 13 November 2026
digest (see NOTES.md); the Hormuz panel is labelled as Iran's claim, not
as fact. The program does no network access and no drawing: it only copies
the bytes, so every run writes identical output.
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
    # The file holds JPEG bytes (recognised by its first bytes): refuse to
    # hand the gate a copy whose header is not a JPEG start marker.
    with open(dst, "rb") as fh:
        if fh.read(3) != b"\xff\xd8\xff":
            raise RuntimeError("copied entry.png does not start with a JPEG marker")


if __name__ == "__main__":
    main()
