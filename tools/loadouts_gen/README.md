# Loadouts generator

Writes everything in `loadouts/`: the 79 `loadouts/<faction id>.json` files (one per non-player faction), `weapons_index.json`, `armor_index.json`, `rounds_index.json` and `README.md`. The schema and rules are in [docs/loadouts_handoff.md](../../docs/loadouts_handoff.md).

## Run

From the repo root (Python 3, standard library only; nothing is written outside `loadouts/`, and no `__pycache__` is created):

```
python3 -I tools/loadouts_gen/gen.py --game <path to the Contractor game repo>
```

`--game` is only read: the generator takes the item ids from `<game>/data/items.json`. Without `--game` it tries the `CONTRACTOR_GAME` environment variable, then `../Contractor` next to this repo, then `B:/Contractor`. Run `python3 -I tools/validate_pack.py` afterwards.

The output is deterministic. Running it on an unchanged checkout reproduces the committed files byte for byte.

## Files

| File | Holds |
|---|---|
| `gen.py` | Rules (families, optic styles, kit profiles, medical levels, counts), the role builder, `game_kit`, and the JSON writer. Also reads `factions/<id>.json` and `reference/vehicles/`. |
| `catalog.py` | Catalogue of weapons, magazines, round designations and specs, underbarrel launchers, optics, launchers, grenades, helmets, vests and plates. Ids are stable; it started as a port of `tools/loadouts_catalog_wip.pl`. |
| `sutil.py` | Spec helpers: `W(...)` weapons per role, `A(...)` armor (helmet, vest, tier, plate, side plate). |
| `s_<bloc>.py` | One spec per bloc (the ROSTER keys in `tools/factions_workflow.js`, e.g. `s_central_africa.py` for adf, m23 and cod): each faction's regular variant, extra variants (as overrides of regular), notes and sources. A new bloc file is listed in `BLOCS` in `gen.py` and named in `BLOC_NAMES` in `readme.py`. |
| `index.py` | Writes the three index files. |
| `readme.py` | Writes `loadouts/README.md` (roster and the "what has to be built" summary). |

## Changing a loadout

Edit the faction's entry in its `s_<bloc>.py`, or the catalogue for a new item, then re-run the generator. Don't hand-edit files in `loadouts/`: the next run overwrites them.

The variant keys used in the specs:

- `w` / `w_over`: weapons per role (`gr` is `(rifle, underbarrel or None)`, `at` is `(rifle, launcher)`).
- `alt`: alternate weapons per role.
- `at_alt`: alternate AT launchers.
- `team`: crew-served ATGMs and MANPADS.
- `rif_launcher`: a disposable launcher carried by riflemen.
- `armor`.
- `helmet_roles`: only these roles get the helmet.
- `heavy_helmet`: the heavy helmet for assault roles.
- `role_grenades`: a fixed grenade list per role.
- `elite`: one medical level and one night-capability step up.
- `camo`: an index into the faction file's camo list.
- `profile`, `optics`, `grenades`, `ammo`: the families defined in `gen.py`.
- `not_fielded`: a note for each role the faction does not field.
- `vnotes`: variant notes.
