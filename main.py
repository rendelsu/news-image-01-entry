"""news-image-01 ronde 3: peta dunia + 30 berita.

Program ini hanya menyalin entry.png (JPEG final 1024x1024, dibuat offline
dengan PIL dari peta dunia hasil generate image + teks DejaVu) ke direktori
output. Deterministik: byte keluar sama persis dengan byte masuk.

Konsep mengikuti pola pemenang papan peringkat: satu peta dunia sebagai
jangkar visual dengan 30 pin bernomor, plus indeks 30 berita singkat yang
nomornya cocok dengan pin. Semua berita dari digest terverifikasi 13 Nov
2026; klaim yang belum terkonfirmasi independen diberi label CLAIM.

Verifikasi: jalankan dua kali dengan MAKEFUN_OUTPUT_DIR berbeda, sha256
ketiga file (entry.png + dua salinan) harus identik; PIL verify OK.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
JPEG_MAGIC = b"\xff\xd8\xff"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        head = f.read(3)
    if head != JPEG_MAGIC:
        raise SystemExit("entry.png bukan JPEG (magic byte salah)")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, dst)
    if os.path.getsize(dst) != os.path.getsize(SRC):
        raise SystemExit("ukuran salinan tidak cocok dengan entry.png")


if __name__ == "__main__":
    main()
