#!/usr/bin/env python3
"""
Img-gen — Free Background Remover
CLI tool: drop images into the `input/` folder and run this script.
Outputs transparent PNG files into the `output/` folder.
"""

import argparse
import sys
from pathlib import Path

from PIL import Image
from rembg import remove


SUPPORTED = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def process_image(input_path: Path, output_dir: Path) -> Path:
    """Remove background from a single image and save as PNG."""
    with open(input_path, "rb") as f:
        input_data = f.read()

    output_data = remove(input_data)

    output_path = output_dir / (input_path.stem + "_nobg.png")
    output_path.write_bytes(output_data)
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Img-gen: Remove image backgrounds for free using rembg (AI-powered)."
    )
    parser.add_argument(
        "images",
        nargs="*",
        help="Image file(s) to process. If omitted, processes all images in the input/ folder.",
    )
    parser.add_argument(
        "-o", "--output",
        default="output",
        help="Output directory (default: output/)",
    )
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Collect input files
    if args.images:
        files = [Path(p) for p in args.images]
    else:
        input_dir = Path("input")
        if not input_dir.exists():
            print("❌  No images provided and input/ folder not found.")
            sys.exit(1)
        files = [p for p in input_dir.iterdir() if p.suffix.lower() in SUPPORTED]
        if not files:
            print(f"❌  No supported images found in input/. Supported: {', '.join(SUPPORTED)}")
            sys.exit(1)

    print(f"🔍  Found {len(files)} image(s) to process...\n")

    success, failed = 0, 0
    for img_path in files:
        if img_path.suffix.lower() not in SUPPORTED:
            print(f"⚠️   Skipping unsupported file: {img_path.name}")
            failed += 1
            continue
        try:
            out = process_image(img_path, output_dir)
            print(f"✅  {img_path.name}  →  {out}")
            success += 1
        except Exception as e:
            print(f"❌  Failed to process {img_path.name}: {e}")
            failed += 1

    print(f"\n🎉  Done! {success} succeeded, {failed} failed.")
    print(f"📁  Results saved to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
