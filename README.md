# Contractor vehicle models

Voxel vehicle models for [Contractor](https://github.com/cghath/Contractor), built in code so they
stay in the game's voxel art style. This repo exists so the models can be refined on their own and
dropped into the game later.

Everything lives in one file, `scripts/vehicle_art.gd` (class `VehicleArt`). Shapes are drawn in
real metres on a 5 cm voxel canvas, then meshed once per model and paint scheme and cached.

## Models

| Model id | Vehicle | Paint schemes |
|---|---|---|
| `uh60` | UH-60 Black Hawk (door guns, canted tail rotor) | army, od |
| `ah1z` | AH-1Z Viper (rocket pods, Hellfires, Sidewinder rails, chin gun) | marine_gray |
| `aav7` | AAV-7A1 (Mk19/M2 weapon station) | od, desert |
| `bradley` | M2A3 Bradley (25 mm, TOW, side armour tiles) | desert, od |
| `abrams` | M1A2 SEP Abrams (120 mm, CROWS, bustle rack) | desert, od |
| `maxxpro` | MaxxPro MRAP with turret | desert, od |
| `matv` | M-ATV with turret | desert, od |
| `technical_dshk` | Hilux with DShK 12.7 mm | white, tan, red |
| `technical_zu23` | Land Cruiser 79 with ZU-23-2 | tan, white, red |
| `technical_spg9` | Hilux with SPG-9 73 mm recoilless rifle | white, tan, red |
| `technical_m40` | Hilux with M40 106 mm recoilless rifle | tan, white, red |
| `technical_rockets` | Land Cruiser 79 with a Type 63 107 mm rocket launcher | white, tan, red |
| `technical_zpu` | Land Cruiser 79 with ZPU-2 twin 14.5 mm | red, white, tan |

Helicopter rotors are separate nodes (`MainRotor`, `TailRotor`) so they can spin;
`VehicleArt.spin_rotors(node, delta)` turns them.

## Running the showcase

Open the project with the Voxel Tools build of Godot 4.7 (the same editor as Contractor; the mesher
is a Voxel Tools class) and press F5. Or render screenshots from the command line:

```
<voxel godot editor> --path . res://showcase/vehicle_showcase.tscn -- <output folder> [shot]
```

Shots: `helicopters`, `ah1z`, `armor`, `mraps`, `technicals`. Each saves `vehicles_<shot>.png`.

To check one model against reference photos, render it from six angles (left side, front, rear,
two three-quarter views and top) into one contact sheet, `<model>_views.png`:

```
<voxel godot editor> --path . res://showcase/model_views.tscn -- <output folder> <model> [scheme]
```

Both scenes need a window. On a headless Linux box, `xvfb-run` with `--rendering-driver opengl3`
works (the Voxel Tools release `godot.linuxbsd.editor.x86_64` from
https://github.com/Zylann/godot_voxel/releases/tag/v1.7 is the matching 4.7.2 editor).

## Adding a model

1. Add the id and its schemes to `MODELS`.
2. Write a `_name() -> Canvas` function. Create the canvas in voxels at 5 cm
   (`Canvas.new(Vector3i(w, h, l), 0.05)`), then draw in metres: x is centred (negative is left),
   y is up from the ground, z runs back from the nose.
   - `mhull(z0, z1, section, colour, shell)` for aircraft and vehicle bodies; `section(z)` returns
     a `Section`: flat bottom and top, a bottom and top half width (so sides can lean in), and
     rounded lower and upper corners. `Section.scaled()` rounds off noses and tails.
   - `mloft(z0, z1, profile, colour, squareness, shell)` for round bodies (pods, barrels, nacelles);
     `profile(z)` returns `Vector4(centre_x, centre_y, half_width, half_height)`. Use a `shell`
     for big hulls.
   - `mbox`, `mbar` (struts, barrels), `mdisc` (upright cylinders: masts, hatches, rings),
     `mwheel` (also carves wheel arches when drawn in `P.EMPTY`), and `mskin` (repaints only the
     outer skin: windows, seams, markings).
   - Shared parts: `_mtracks` (road wheels, sprocket teeth, return rollers, track shoes),
     `_mtire` (military tyre with tread and hub bolts), `_turret` (O-GPK gun shield with an M2),
     `_pickup` (Hilux or Land Cruiser 79 base for the technicals).
   - `c.rotor(name, position, radius, chord, blades, axis)` for rotors.
3. Add it to `_canvas_for()` and to the showcase line-up.

Colours come from the palette enum `P` and the scheme table `SCHEMES`.

## Integrating with Contractor

1. Copy `scripts/vehicle_art.gd` to `scripts/art/vehicle_art.gd` in the game.
2. For static vehicles, `VehicleArt.prop(model, scheme)` returns a `StaticBody3D` with the model and
   a box collider. The game's `vehicle-models` branch parks one of each outside the compound gate
   (`CompoundLevel.PARKED_VEHICLES` / `_park_vehicles()`).

## Next steps

- **Black Hawk:** rebuilt against Captain's reference images (UH-60M), which live locally in
  `C:\Users\noahg\Downloads\Reference folder for UH 60`; they aren't committed here because they're
  third-party photos. A local `references/` folder is ignored by git if you want copies next to the
  project.
- The other models had a detail pass from public dimensions and drawings. Reference photos for any
  of them (dropped in `references/`) would let the next pass match them as closely as the UH-60.
- Gameplay that will use these models (planned in the game, not built yet):
  - Vehicle armour: small calibre does nothing; 7.62x54R and up can penetrate or disable.
  - Anti-armour launchers: AT4, RPG-7 (PG-7V HEAT, OG-7V frag), Javelin, MAAWS, NLAW and SMAW,
    behaving like the real rounds.
  - Driveable and flyable vehicles.

## Factions, vehicles and worldspaces

Real-world faction data (`factions/`), a real-vehicle catalogue with modelling notes and photo links (`reference/vehicles/`), and proc-gen region specs (`worldspaces/`). Start with [docs/factions_handoff.md](docs/factions_handoff.md). For building and rendering models, see [docs/modelling_guide.md](docs/modelling_guide.md).
