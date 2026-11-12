"""Copy and verify the Dandelion Planet artwork at the harness output path.

Local run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

source = Path(__file__).resolve().with_name("entry.png")
if not source.is_file():
    raise FileNotFoundError(f"Required artwork is missing: {source}")
if source.stat().st_size > 1_048_576:
    raise ValueError(f"Artwork exceeds the 1,048,576-byte limit: {source}")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
destination = output_dir / "entry.png"
shutil.copyfile(source, destination)
if source.read_bytes() != destination.read_bytes():
    raise OSError(f"Copied artwork verification failed: {destination}")
print(f"Copied and verified {destination.stat().st_size} bytes at {destination}")
