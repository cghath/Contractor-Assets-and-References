# How the vehicle models were built and rendered

This guide is for the next agent who picks up the voxel vehicles. It is written from the cloud detail pass that took place on 2026-10-10 (PR #1). That pass rebuilt all 13 models and checked each one against renders. `README.md` has the API summary. This file covers the setup, the working loop, the techniques used, and the mistakes to avoid.

## 1. Setup

The models are GDScript only. There are no mesh files: `scripts/vehicle_art.gd` draws every vehicle into a Voxel Tools `VoxelBuffer` at 5 cm voxels. A `VoxelMesherCubes` turns that buffer into a mesh when the game runs, and the mesh is cached per model and paint scheme. Nothing is exported to `.glb`, `.vox` or `.res` yet.

You need the **Voxel Tools build** of Godot 4.7.2, because stock Godot lacks the voxel classes:

- **Windows desktop** (Captain's machine): this is the same editor Contractor uses. Open the project and press F5 for the showcase.
- **Linux or cloud container:**
  ```
  mkdir -p ~/godot && cd ~/godot
  curl -sSLO https://github.com/Zylann/godot_voxel/releases/download/v1.7/godot.linuxbsd.editor.x86_64.zip
  unzip godot.linuxbsd.editor.x86_64.zip && chmod +x godot.linuxbsd.editor.x86_64
  ```
  The GitHub API and the releases page may return 403 through the cloud proxy. The direct asset URL above worked.
  - The cloud has no Vulkan. Always run with `--rendering-driver opengl3` under `xvfb-run`; plain `--headless` renders nothing.
  - Colours come out slightly washed out in that renderer compared with the desktop.

## 2. Render loop (do this after every change)

```
tools/render_views.sh <model> [scheme] [out_dir]
```

This loads `showcase/model_views.tscn` and writes one contact sheet, `<model>_views.png`, with six views: left side, front, rear, front three-quarter, rear three-quarter, and top. A parse error in `vehicle_art.gd` appears as `SCRIPT ERROR` / `Parse` lines, and then no PNG is written. Always check for `saved ...` in the output.

Group shots (several models side by side) need a window:
```
xvfb-run -a -s "-screen 0 1600x900x24" $GODOT --rendering-driver opengl3 --path . res://showcase/vehicle_showcase.tscn -- <out> <shot>
```
The shots are `helicopters`, `ah1z`, `armor`, `mraps` and `technicals`.

The working loop is:
1. Edit one part.
2. Render the sheet.
3. Open the PNG with an image viewer or the Read tool and compare it against the reference: the side view for proportions, the three-quarter views for shape, the top view for plan-form.
4. Repeat.

Small steps work better: one render per change catches mistakes while they are still easy to find.

## 3. How a model was built

1. **Gather numbers first.** Use the real vehicle's length, width, height, wheelbase or track length, road-wheel count, wheel diameter, and turret ring position.
   - `reference/vehicles/<id>.json` already has `dimensions_m`, `visual_notes` and `reference_pages` for about 200 real vehicles.
   - Wikipedia text pages fetch fine; image hosts are blocked in the cloud.
   - For an exact match, ask Captain for photos in a local folder. The UH-60 was matched this way from `C:\Users\noahg\Downloads\Reference folder for UH 60`, read through the device folder tools. Never commit third-party photos.
2. **Size the canvas** in voxels: `Canvas.new(Vector3i(w, h, l), 0.05)`, which is metres / 0.05 plus a little margin. Then draw only in metres:
   - x is centred, and negative x is the vehicle's left.
   - y runs up from the ground.
   - z runs back from the nose, which sits at 0.
3. **Draw big to small:**
   - **Body:** use `mhull(z0, z1, section_fn, colour, shell)`. `section_fn(z)` returns `Section(bottom, top, half_bottom, half_top, r_bottom, r_top, cx)`. Lean the sides by giving different bottom and top half widths. Round the corners with the radii. Taper noses and tails with `Section.scaled(k, centre_y)`, lerping k over the first or last metre. Use `shell` (about 0.1-0.15 m) for big hulls so they stay hollow and fast.
   - **Round bodies** (pods, barrels, booms, nacelles): use `mloft(z0, z1, profile_fn, colour, squareness, shell)`, where the profile returns `Vector4(cx, cy, half_w, half_h)`.
   - **Flat-sided armour:** use `mbox`, or the `_hull` helper for boat-like bows (AAV).
   - **Cut-outs:** draw in `P.EMPTY`. For example, `mwheel(..., P.EMPTY, P.EMPTY)` carves wheel arches before the wheels go in.
   - **Running gear:** for tracks use `_mtracks(c, inner, outer, z0, z1, wheels, r, sprocket_front, rollers)`. For military tyres use `_mtire`. For pickups use `_pickup(c, "hilux"|"lc79")`, which returns the bed height.
   - **Weapons and fittings:** use `mbar` for barrels, struts, rails and antennas, and `mdisc` for hatches, rings, masts and drums. `_turret` adds the O-GPK shield and M2.
   - **Surface detail last:** `mskin(x0, y0, z0, x1, y1, z1, colour, only_over)` repaints only the outer skin. Use it for windows, door seams, handles, markings, rust and mismatched panels. Detail painted this way doesn't change the silhouette, so it's cheap to iterate.
   - **Rotors:** `c.rotor(name, pos, radius, chord, blades, axis)` creates separate `MainRotor`/`TailRotor` nodes that `spin_rotors()` turns.
4. **Register the model:**
   1. Add `MODELS[id] = [schemes...]`.
   2. Add a case to `_canvas_for()`.
   3. Add it to the showcase line-up.
   4. Render every scheme once.
5. **Colours:** use the palette enum `P` (PAINT, PAINT_DARK, PAINT_LIGHT, METAL, GLASS, TIRE, BLACK, RUST, ...). `SCHEMES` maps paint and marking hex per camo, and `PAINT` follows the scheme. Add new camo colours as schemes rather than hard-coding hex.

## 4. Mistakes that cost time (avoid them)

- **Sawtooth edges:** leaning sides on narrow parts make stair-step artefacts at 5 cm. Set the lean to 0 for small parts, as with the Abrams turret cheeks.
- **Invisible detail:** a gap or tile smaller than about 2 voxels vanishes. Make gaps at least 0.1 m and put a darker backing plate behind them, as with the Bradley armour tiles.
- **Parts hiding parts:** check the draw order. Later draws overwrite earlier ones, which hid the AAV bow behind side panels until the panels were started at z 1.8.
- **Spikes:** a loft or section that goes to zero width abruptly leaves one-voxel spikes. Clamp the taper, as on the AAV bow.
- **Top view clipped or camera too close:** fixed in `model_views.gd` by fitting the length to the frame and using a `Vector3.LEFT` up vector for the top view. Keep that if you edit the camera.
- **Washed-out renders:** the lights in `model_views.gd` were lowered on purpose. Judge colour on the desktop build.
- **Rotor shadows** stripe the hull and hide detail, so they are turned off in the views scene only.
- **Big edits:** to replace one model function wholesale, swap the whole `## doc comment + static func` block. A small Python splice by function name was used for this; it is safer than many tiny string edits.

## 5. What to build next

`reference/vehicles/README.md` (written by the faction pack validator) and `docs/factions_handoff.md` list the high-priority vehicles with no model yet. Early-game (terrorist-theatre) vehicles come first: the Toyota Hilux base (already in `_pickup`), BMP-1/2, BTR-82A, T-72B3, M113, Mi-8, and captured army kit.

To reuse shared parts:
- Tracked vehicles reuse `_mtracks`.
- Wheeled APCs reuse `_mtire`.
- Pickup variants reuse `_pickup`.

Vehicle armour and launchers are gameplay code. They belong in the game repo (`cghath/Contractor`), not here.
