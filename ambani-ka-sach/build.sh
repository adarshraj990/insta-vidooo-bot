#!/bin/sh
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
LIB=${LIB:-/c/Users/Adarsh/lemo-opuscar}
export LIB
[ -f "$LIB/core/render/video.mjs" ] || { echo "set LIB to the Lemo-Opuscar library folder"; exit 1; }
cd "$LIB"

"$LIB/.venv/bin/python" -X utf8 core/tts/tts_zh.py "$HERE/voice/lines.json" "$HERE/voice/out"
node core/render/events.mjs "$HERE"
node core/render/readcheck.mjs "$HERE"
"$LIB/.venv/bin/python" -X utf8 "$HERE/make_cues.py"
"$LIB/.venv/bin/python" -X utf8 core/render/srt.py "$HERE/out/cues.json" "$HERE/ambani-ka-sach.srt"
"$LIB/.venv/bin/python" -X utf8 "$HERE/mix.py"
node core/render/video.mjs "$HERE" --fps 30 --workers 3 --out "$HERE/out/video.mp4"
sh core/render/mux.sh "$HERE/out/video.mp4" "$HERE/out/mix.wav" "$HERE/ambani-ka-sach.mp4" 30 2
node core/render/still.mjs "$HERE" 48.5 --out "$HERE/out"
cp "$HERE/out/t_48.5.jpg" "$HERE/poster.jpg"

