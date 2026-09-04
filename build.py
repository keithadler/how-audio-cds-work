#!/usr/bin/env python3
"""Inline the audio as a data payload so the page is a single portable file.

index.html carries a __TRACK_B64__ placeholder. In development the page falls
back to fetching audio/ from alongside itself; the built file needs no server.
"""
import base64, pathlib, sys

root = pathlib.Path(__file__).parent
shell = (root / "index.html").read_text()
mp3 = root / "audio" / "the-one-who-let-you-go.mp3"

if "__TRACK_B64__" not in shell:
    sys.exit("index.html has no __TRACK_B64__ placeholder")

b64 = base64.b64encode(mp3.read_bytes()).decode("ascii")
out = root / "dist" / "how-audio-cds-work.html"
out.parent.mkdir(exist_ok=True)
out.write_text(shell.replace("__TRACK_B64__", b64))
print(f"{out}  {out.stat().st_size / 1048576:.2f} MB")
