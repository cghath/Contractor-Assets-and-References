#!/bin/bash
# Render a 6-angle contact sheet of one model, headless (Linux cloud container or WSL).
# usage: tools/render_views.sh <model> [scheme] [out_dir]
# Needs: the Voxel Tools Godot 4.7.2 editor at $GODOT (default ~/godot/godot.linuxbsd.editor.x86_64)
# and xvfb-run. Writes <out_dir>/<model>_views.png (default out_dir: ./renders, git-ignored).
set -e
GODOT=${GODOT:-$HOME/godot/godot.linuxbsd.editor.x86_64}
MODEL=${1:?model id}; SCHEME=${2:-}; OUT=${3:-$(pwd)/renders}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."
timeout 300 xvfb-run -a -s "-screen 0 1600x900x24" "$GODOT" --rendering-driver opengl3 --path . \
  res://showcase/model_views.tscn -- "$OUT" "$MODEL" $SCHEME 2>&1 \
  | grep -E "SCRIPT ERROR|ERROR|Parse|saved" | grep -v -E "ALSA|audio|init_output_device" || true
