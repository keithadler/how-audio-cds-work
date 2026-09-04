# How Audio CDs Work

An interactive explainer that teaches the compact disc by writing one real song onto
one at true Red Book scale, then letting you fly the read head along it.

Drop in any WAV or MP3 and it becomes the subject.

## What it does

**Draws the disc honestly.** A CD is a single spiral cut hub-outward at a track pitch of
1.6 µm across a program area from 25 mm to 57.8 mm radius, scanned at a constant
1.2 m/s. Radius here follows the real area rule — radius grows with the square root of
elapsed pit-track length — so a 4:46 song occupies its true share of the platter and
everything past the dashed line is bare polycarbonate. The drawing compresses 20,500
revolutions into 28 visible turns; the radii are not compressed.

**Teaches while it plays.** Fifteen illustrated liner notes advance with the read head,
five of them interactive:

| Figure | What you can do |
| --- | --- |
| Pit depth | Drag the depth and watch the reflection cancel at a quarter wavelength |
| Beam focus | Drag a surface scratch and see how little of an out-of-focus beam it costs |
| Constant linear velocity | Drag the head and watch rpm fall from 458 to 198 while pit speed never moves |
| Sampling | Push a tone past 22.05 kHz and watch it fold back to a lower frequency |
| CIRC | Drag damage along the track and find the correct / conceal / audible edges |

Eight retrieval questions at the bottom, answers hidden until you commit to one.

**Shows the loudness war as a physical object.** Toggle between the delivered master, a
simulated 1990 master (transient restoration against a 200 ms average, gentle shelf
cuts, peak-normalized) and a simulated 2026 loud master (0.5 ms brickwall at −0.3 dBFS
chasing a −9 dBFS average). Ribbon thickness is absolute level against one shared
reference, so a louder master genuinely is a fatter groove. Neither alternate is
archival — limiting cannot be perfectly undone, and the page says so.

## Running it

No build step, no dependencies, no network calls.

```
python3 -m http.server 8931
```

Then open <http://localhost:8931>. The page falls back to fetching `audio/` from
alongside itself.

To produce a single portable file with the audio inlined:

```
python3 build.py
```

## How it works

Everything runs in the browser. `AudioContext.decodeAudioData()` handles MP3, WAV,
FLAC, AAC and Ogg natively — no WASM decoder needed. Analysis is an 18,000-bucket
peak/RMS envelope plus a 4,200-frame spectrogram from a hand-rolled radix-2 FFT, used
for the spectral-centroid coloring. Decoding is pinned to an `OfflineAudioContext` at
**44,100 Hz** rather than the system output rate, because a CD is 44.1 kHz by
definition — which also happens to be the resampling a 48 kHz master gets on its way
to a disc.

Rendering is 2D canvas: a static disc layer with a two-tap bloom pass, redrawn as live
vectors when zoomed past 1× so magnification stays sharp.

## Credits and licensing

**The software** is MIT licensed. See `LICENSE`.

**The music is not.** "The One Who Let You Go", written by Keith Adler
(BMI, IPI 551038589), performed as Marty Gregg, from *The Aura Principle Soundtrack*.
© 2026 Keith Adler. **All rights reserved.** The recording in `audio/` is included so
the explainer has something real to draw, and is not licensed for reuse,
redistribution, sampling or any other purpose.
