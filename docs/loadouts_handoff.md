# AI default loadouts: handoff sheet

Snapshot as of 2026-10-10 (updated after Captain's answers). **Job 6 is complete on the fork** (`cghath/Contractor-Assets-and-References`, branch `factions-worldspaces`).

## Status

- **Ownership:** this job was owned by the separate "Faction loadout questions" thread, which never pushed any `loadouts/` files. On 2026-10-10 the user asked for the job to be taken over and completed on the fork, after the alliances job (Job 4). Captain's 09:34 pause had been lifted for the queue by then (see [factions_handoff.md](factions_handoff.md)).
- **Done (2026-10-10):**
  - `loadouts/<faction id>.json` for all **79 non-player factions**: 120 variants in total (76 factions and 112 variants after Job 6; Job 7 added adf, m23 and cod and the rus `mountain` variant). Every variant has the 8 core roles, plus `crew` where the faction fields armoured vehicles (MBT, IFV, APC, MRAP) and `pilot` where it fields helicopters.
  - `loadouts/weapons_index.json`, `loadouts/armor_index.json` and `loadouts/rounds_index.json` with users and in-game flags.
  - `loadouts/README.md` with the roster and the "what has to be built" summary.
  - Loadouts checks in `tools/validate_pack.py`. The validator reports 0 errors and 0 warnings.
  - **Update (2026-10-10, Job 7):** new loadouts for adf (`regular`, `elite`; s_me_terror.py), m23 (`regular`, `assault`) and cod (`regular`, `republican_guard`, `wazalendo`; both in s_others.py), and a rus `mountain` variant (34th Separate Guards Mountain Motor Rifle Brigade type: Ratnik 6B45/6B47 over Gorka-type mountain suits, AK-74M/AK-12, PKP, SVDM, SV-98, RPG-7V2 and RPG-26, all 8 core roles) for the alpine_europe what-if. The weapon, magazine, optic and launcher counts of the "what has to be built" summary are unchanged (no new catalogue items); `plate_steel_light` is now used by 22 factions (cod and m23 added). The generator reproduces the committed files exactly.
  - **Update (2026-10-10, Central Africa bloc):** by Captain's decision adf, m23 and cod form a new `central_africa` bloc; their specs moved from s_me_terror.py and s_others.py into `tools/loadouts_gen/s_central_africa.py` (adf still uses the `T` and `elite` helpers from s_me_terror.py). The regenerated `loadouts/` is unchanged except the bloc label of the three rows in `loadouts/README.md` (now "Central Africa") and one m23 note (hostile non-client, now Captain-confirmed instead of proposed).
  - **Update (2026-10-10):** Captain answered all 10 open questions (see "Captain's decisions (2026-10-10)" below). The answers are applied, and the generator is committed at `tools/loadouts_gen/`.
- The WIP Perl catalogue, [tools/loadouts_catalog_wip.pl](../tools/loadouts_catalog_wip.pl), is superseded by `tools/loadouts_gen/catalog.py` and the index files. Its ids were kept, except `m110_sniper`, which duplicated `m110`. One correction: the INSAS rifle now uses `mag_556_20`, because 20 rounds in `mag_556` broke the one-id-per-calibre-and-type rule. Its `%GAME_IDS` list is out of date; use the live `data/items.json`.
- The files are made by the generator in [tools/loadouts_gen/](../tools/loadouts_gen/). Change the specs there and re-run it; don't hand-edit `loadouts/`.

## What Captain asked for

- AI default loadouts for **every non-player faction**: one file per faction at `loadouts/<faction id>.json`, plus `loadouts/README.md`.
- These loadouts are the **baseline for every weapon and armor piece the game needs** across the factions. So also write:
  - `loadouts/weapons_index.json`: every weapon, calibre and ammo type, optic, launcher and grenade, with its users, and whether it already exists in the game repo.
  - `loadouts/armor_index.json`: every helmet, vest, plate carrier and plate, with its tier and users.
  - A "what has to be built" summary in the README.
  - Keep ids stable.
- The agent must **ask questions** rather than guess. Questions go to Captain through the project assistant. Open questions don't block the work: their defaults are applied and marked `proposed`.

## Captain's decisions (2026-10-10)

Captain's answers to the 10 questions raised by Job 6 are all applied.

1. **Light steel plates: both.** `plate_steel_light` (steel, III, fits light) is a new item to build, and the loadouts and `armor_index.json` list it. Until it exists, each role's `game_kit` uses `plate_pe_l3` in its place. It is used by 22 factions (20 before Job 7 added cod and m23; the list is in loadouts/README.md).
2. **Launcher items:** `at4`, `rpg7`, `javelin`, `maaws`, `nlaw` and `smaw`.
   - The reloadable launchers' rounds are `pg7v`, `og7v`, `ffv551`, `ffv441d`, `mk6_heaa` and `mk3_hedp`, plus `javelin_missile`. AT4 and NLAW are single-shot, so the launcher item is the round.
   - These ids appear as `proposed_game_item_id` on each launcher and round.
3. **Hezbollah Radwan is light,** like other terror elites: a light vest with an improvised or captured steel plate, and helmets on squad leaders. The hezbollah notes say this differs from the faction file's medium by Captain's decision.
4. **Crew helmets:** the TSh tanker helmet and the aircrew flight helmet are cosmetic, non-ballistic items to build (`helmet_tanker`, `helmet_flight`; tier `none`, `cosmetic: true`).
5. **Heavy (III++) helmets** go to elite, SOF and PMC assault variants only, never regulars. They are worn on the assault roles (rifleman, autorifleman, grenadier, at, medic, squad_leader); marksman and sniper keep the standard helmet.
   - K6-3 / Altyn-type with visor: rus `spetsnaz`, pmc_kestrel `assault`.
   - Visored assault helmet (Caiman / FAST class): ukr `assault`, are `presidential_guard`, egy `saaka`, irq `cts`, pmc_halcyon `regular` (its assault team), pmc_black_sable `regular` (its contractor assault team).
   - No Western SOF variant exists, and chn, isr, tur, kor, jpn, ind, pol, sau and qat have no elite variant, so none was created for this.
6. **No collapsing of weapon families:** every designation stays its own model to build (238 weapons).
7. **Rounds** are specced in the pack only, in `loadouts/rounds_index.json`: 21 round specs covering the 13 calibres with no round and the 6 designations that used a generic round. Each spec has calibre, designation, projectile, approximate muzzle velocity and mass, level on the game's armor ladder (with what stops it and what it defeats), users, and `in_game: false`.
   - Each `ammo` entry keeps `game_round_id` (exact or generic) and adds `proposed_round_id`.
   - The game repo is not edited.
8. **Variants:** the 16 extra variants stay. New: rus `storm` and `mobilised`, ukr `assault`, irn `basij` and sau `sang`, each with all 8 core roles and real-world kit. That made 112 variants (120 after Job 7).
9. **pse_pa has a light grenadier:** an AKM with 4 hand grenades and no launcher. No PA combat 40 mm launcher is documented: the faction file lists only a 37/40 mm tear-gas launcher, and PA forces are limited to light weapons. The at and sniper roles stay `not_fielded`.
10. **The generator is committed** at `tools/loadouts_gen/`. It runs from the repo root with `python3 -I tools/loadouts_gen/gen.py --game <game repo>` and reproduces the committed files exactly.

## Captain's answer (09:32 UTC, loadout questions thread)

> "faction loadouts should be based on real life, armor and helmet and weapon names, ammunition types etc."

So use **real-world designations** for every faction:

- **Weapons:** the actual service rifles, MGs, sidearms and launchers. Examples: AK-74M, AK-12, HK416, C8A3, L85A3, M4A1, Type 95, PKM.
- **Ammo types:** real designations. Examples: 5.45x39 7N6/7N10, 5.56x45 M855A1/SS109, 7.62x54R 7N13, 7.62x39 57-N-231.
- **Armor:** real vest, plate and helmet models, mapped to the game's light/medium/heavy tiers and NIJ ratings. Examples: 6B45 and 6B47 (Ratnik), IOTV/SPCS with ESAPI, Mk7 helmet, Virtus, ECH.
- **Fictional cartels and PMCs still use real gear.**
- **Terror groups use their real-world kit:** AK-pattern rifles, PKM, RPG-7, mostly no armor.

Where no specific model name could be confirmed (often the vest or helmet of a smaller army), the index entry has `designation: "class"` and a descriptive name, for example "Modular plate carrier, national issue". These entries are listed in `armor_index.json` so they can be replaced with real model names later.

## The 9 questions: defaults applied

Only the "real-life names" answer came back. The other 8 defaults were applied as written and are marked `proposed` in every loadout file.

1. **Variants (applied):** 1-3 per faction, and every faction has `regular`.
   - Real splits from the default: usa `usmc`; rus `spetsnaz` and `vdv`; irn `irgc` (regular = Artesh); ukr `territorial`; every terror group `elite` (regular = fighters).
   - Added where the faction file itself describes a separately equipped force: are `presidential_guard`, egy `saaka`, syr `elite`, irq `cts`, afg_taliban `elite`, sdf `yat`, krg_peshmerga `zeravani`, sahel_aes `vdp`, som `danab` and `gorgor`, both cartels `street`, pmc_halcyon `protective_detail`, pmc_kestrel `assault`, pmc_black_sable `auxiliary`.
2. **Crew and pilot roles (applied):** derived from the faction's vehicles in `reference/vehicles/` (`type` mbt/ifv/apc/mrap gives `crew`; attack_heli/transport_heli gives `pilot`).
3. **Counts (applied):** real integer counts, all proposed. `count` is the total carried, including the magazine in the weapon.
4. **Launchers outside the game's 6 (applied):** the real launcher is recorded with `in_game: false` and a `game_substitute` from the 6. RPG-26 maps to AT4, PF-98 or Panzerfaust 3 to MAAWS, and Spike or HJ-12 to Javelin. MANPADS have `game_substitute: null`.
5. **Plates (applied):** polyethylene (`polyethylene`) is the third material alongside steel and ceramic. Light PE plates map to `plate_pe_l3`.
6. **Medical (applied):** the game now already has `pressure_bandage`, `chest_seal`, `splint` and `morphine`. The still-missing ids are `iv_18g`, `io_fast1`, `saline_500`, `decompression_needle`, `epinephrine`, `adenosine`, `atropine`, `surgical_kit` and `defibrillator`. `ifak` and `trauma_kit` stay as containers.
7. **Optics and smoke (applied):** optics are proposed class ids (`red_dot`, `prism4`, `lpvo`, `pso1` and so on). Smoke is white for screening (`smoke_grenade`), and green, red or violet for signalling (proposed `smoke_green`, `smoke_red`, `smoke_violet`).
8. **Magazines (applied):** one id per calibre and type, for example `mag_545x39_30` and `belt_762x54r_100`. Pistol magazines share `mag_9mm` per calibre, as in the WIP catalogue.
9. **Terror armor (applied):** regular fighters get none. Elites get a light vest with an improvised or captured steel plate, and only their squad leaders get a helmet; NVGs follow the faction's night capability. Hezbollah and iraqi_militias regulars wear light soft vests, as their faction files say. Hezbollah's Radwan elite is light by Captain's decision (above).

## Rules

- **Stay consistent** with `factions/<id>.json`: small_arms, launchers, body_armor, camo and doctrine. Where a faction file disagrees with reality or with itself, the loadout's `notes` say so. Faction files are not edited by this job.
- **Roles:** rifleman, autorifleman, marksman, grenadier, at, medic, squad_leader and sniper, plus crew and pilot where relevant. Other roles used by `unit_templates` (team_leader, driver, gunner, drone_operator, leader_hvt and so on) are mapped to one of these in `role_map`.
- **Armor tiers** (from the design doc):
  - LIGHT is an aramid vest with frontal fragment protection plus some ballistic; it takes one light plate (front only), and a light plate stops .223 at most.
  - MEDIUM has front and back plates.
  - HEAVY has front, back and side plates.
  - Helmets: light IIA, medium IIIA, heavy NIJ III++.
- **Medical** follows ACE3: the drugs are only epinephrine, morphine, adenosine and atropine. Surgery kits and defibrillators are for the player and medics only. The medical level of each variant comes from `doctrine.ai_tuning.medical_care` (0.8 and up `full`, 0.6 `standard`, 0.4 `basic`, below that `minimal`); elite variants get one level more.
- **In-game launchers:** AT4, RPG-7 (PG-7V and OG-7V), Javelin, MAAWS, NLAW and SMAW.
- **Game repo is read only.** The items are in the game repo's `data/items.json` (`B:\Contractor\data\items.json` on Captain's desktop), with rounds in `data/rounds.json` and squad kits in `data/roles.json`. As of 2026-10-10, items.json has 35 items. It has grown since the WIP `%GAME_IDS` list was written. The newer ids are `pressure_bandage`, `hemostatic_gauze`, `chest_seal`, `splint`, `morphine` and `npa`, plus three non-loadout items: `electronics_salvage`, `hvt_case` and `supply_crate`. Always check the live file.
- **Faction count:** all 80 faction ids exist (77 before Job 7); 79 are non-player (everything except `player`). Each one has a loadout.

## Captain's decisions reflected (2026-10-10)

- **iraqi_militias is early tier.** Its armor is kept at light: a soft vest for regulars, and a light vest with a steel plate for elites. The faction file notes some medium (PMF-issued plate carriers); that is left out for the early game.
- **afg_taliban is a limited client but never sells gear.** Its loadout notes say its gear reaches the player only as loot.
- **pmc_black_sable is the nemesis** and pmc_halcyon an ordinary rival; this is noted in the files and does not change kit.
- **hezbollah and houthis stay mid tier.** hezbollah regulars wear light soft vests; its Radwan elite wears the light terror-elite kit (Captain's decision, item 3 above).

## File schema

All files are UTF-8 JSON. Ids are stable snake_case. Item references share these fields:

- `id`: pack id, the key into `weapons_index.json` or `armor_index.json`.
- `name`: the real-world designation (weapons, launchers, grenades, armor).
- `game_item_id`: the `data/items.json` id that represents the item in the game today, or `null` if none does. For weapons, magazines and launchers the match is exact. For grenades, armor and medical items it is the generic game item of that kind (for example `frag_grenade` for an M67 or an RGD-5, `plate_ceramic_l4` for ESAPI).
- `game_substitute`: present when `game_item_id` is `null` and an existing item can stand in, for example `m4a1` for an HK416.

### `loadouts/<faction id>.json`

```
{
  "id": "<faction id>",                 // canonical, not "player"; matches the filename
  "faction": "<faction name>",          // copied from factions/<id>.json
  "schema_version": 1,
  "kind": "state|non_state|pmc|criminal",
  "campaign_tier": "early|mid|late",    // copied from the faction file
  "default_variant": "regular",
  "variants": [ <variant>, ... ],       // first is always "regular"
  "role_map": { "<unit_templates role>": "<loadout role>" },
  "notes": [ "..." ],                   // includes faction-file disagreements
  "proposed": [ "..." ],
  "sources": [ "factions/<id>.json", "<url>", ... ]
}

<variant> = {
  "id": "regular|usmc|spetsnaz|elite|...",
  "name": "...",
  "camo": "<name of an entry in the faction file's camo list>",
  "armor_tier": "none|light|medium|heavy",     // the regular infantry vest tier
  "medical_level": "minimal|basic|standard|full",
  "roles": { "<role>": <role>, ... },          // all 8 core roles, plus crew / pilot where relevant
  "team_weapons": [ <launcher>, ... ],          // ATGMs, MANPADS and other crew-served launchers
  "notes": [ "..." ]                            // optional
}

<role> = {
  "primary": {
    "id", "name", "calibre", "game_item_id", "game_substitute"?,
    "optic": { "id", "name" },                  // optic class id (Q7)
    "ammo": { "id": "<mag id>", "round": "<real round designation>", "game_round_id": "<rounds.json id>|null",
              "proposed_round_id"?: "<rounds_index.json id>",   // when game_round_id is null or only a generic match
              "rounds_per_mag", "count", "game_item_id" },
    "underbarrel"?: { "id", "name", "calibre", "game_item_id": null,
                      "ammo": [ { "id", "name", "count", "game_item_id": null } ] },
    "alternates"?: [ "<weapon id>", ... ]       // other weapons the faction file lists for this role
  },
  "secondary": <weapon as primary, without optic> | null,
  "launcher": <launcher> | null,
  "grenades": [ { "id", "name", "kind": "frag|smoke_white|smoke_green|smoke_red|smoke_violet|flash",
                  "count", "game_item_id", "game_substitute"? } ],
  "armor": {
    "vest":   { "id", "name", "tier": "light|medium|heavy", "game_item_id" } | null,
    "plates": { "id", "name", "material": "ceramic|steel|polyethylene", "real_rating", "front", "back",
                "game_rating", "game_item_id", "game_substitute"?, "proposed_game_id"? } | null,
    "side_plates": { "id", "name", "material", "count", "game_item_id": "plate_side" } | null,   // heavy only
    "helmet": { "id", "name", "tier": "none|light|medium|heavy", "game_rating", "game_item_id",
                "cosmetic"?: true, "proposed_game_id"? } | null      // cosmetic: non-ballistic crew helmets
  },
  "medical": { "container": "ifak|trauma_kit|null", "items": [ { "id", "count", "game_item_id" } ] },
  "other": [ { "id", "count", "game_item_id" } ],          // backpack, radio, binoculars, NVG
  "game_kit": [ [ "<items.json id>", <count> ], ... ],     // data/roles.json format; existing items only
  "notes"?: "..."
}
// A role the faction does not field: { "not_fielded": true, "note": "...", "stand_in_role": "rifleman" }

<launcher> = {
  "id", "name", "kind": "disposable|recoilless|rocket|atgm|thermobaric|manpads",
  "in_game": true|false,                 // true = one of the 6 design-doc launchers
  "game_launcher": "AT4|RPG-7|Javelin|MAAWS|NLAW|SMAW" | null,
  "game_substitute": "<one of the 6>" | null,   // when in_game is false; null for MANPADS
  "game_item_id": null,                  // items.json has no launchers yet
  "proposed_game_item_id"?: "at4|rpg7|javelin|maaws|nlaw|smaw",   // in_game launchers only
  "rounds": [ { "name": "PG-7V", "type": "HEAT|tandem HEAT|HE|HEDP|frag|thermobaric|SAM|top attack", "count",
                "proposed_game_item_id"?: "pg7v|og7v|ffv551|ffv441d|mk6_heaa|mk3_hedp|javelin_missile" } ],
  "alternates"?: [ "<launcher id>", ... ]
}
```

`game_kit` is a stand-in kit the game can load today. It uses exact or generic items and `game_substitute` items: weapons, and `plate_pe_l3` in place of the not-yet-built `plate_steel_light`. Ammunition is converted to the substitute's magazine by round count, capped at 12. It leaves out launchers, underbarrel ammo, optics, NVGs, cosmetic helmets and medical items that do not exist yet.

### `loadouts/weapons_index.json`

```
{
  "schema_version": 1, "_note": "...",
  "weapons":   [ { "id", "name", "calibre", "class", "mag", "rounds_per_mag", "in_game", "game_item_id", "game_substitute"?, "users": [faction ids] } ],
  "calibres":  [ { "calibre", "in_game", "rounds": [ { "round", "game_round_id", "game_match": "exact|generic|null", "users" } ] } ],
  "magazines": [ { "id", "name", "calibre", "kind": "mag|belt|drum", "rounds", "in_game", "game_item_id", "users" } ],
  "optics":    [ { "id", "name", "in_game", "game_item_id", "users" } ],
  "underbarrel_launchers": [ { "id", "name", "calibre", "ammo", "in_game", "game_item_id", "users" } ],
  "underbarrel_ammo":      [ { "id", "name", "calibre", "in_game", "game_item_id", "users" } ],
  "launchers": [ { "id", "name", "kind", "in_game", "game_launcher", "game_substitute", "game_item_id", "proposed_game_item_id", "rounds", "users" } ],
  "launcher_rounds": [ { "launcher", "round", "type", "in_game_launcher", "users" } ],
  "grenades":  [ { "id", "name", "kind", "in_game", "game_item_id", "game_match", "proposed_game_id"?, "game_substitute"?, "users" } ],
  "medical":   [ { "id", "name", "in_game", "game_item_id", "users" } ],
  "other":     [ { "id", "name", "in_game", "game_item_id", "users" } ]
}
```

`users` lists faction ids that use the item in any variant or role, including as an alternate.

### `loadouts/rounds_index.json`

```
{
  "schema_version": 1, "_note": "...",
  "ladder": [ "IIA", "II", "IIIA", "III", "III+", "III++", "IV", "ABOVE_IV" ],
  "game_armor_ratings": [ { "armor", "rating" } ],
  "rounds": [ { "id", "calibre", "designations": [...], "projectile", "muzzle_velocity_mps", "mass_g", "class",
                "game_level", "stopped_by": [game armor], "defeats": [game armor],
                "current_game_round_id": "<generic rounds.json id>|null", "in_game": false, "users" } ]
}
```

### `loadouts/armor_index.json`

```
{
  "schema_version": 1, "_note": "...",
  "tiers": { "vest": {...}, "helmet": {...}, "plate": {...} },   // tier -> generic game item
  "helmets": [ { "id", "name", "tier", "designation": "specific|class", "real_rating", "game_rating", "game_item_id", "game_match", "cosmetic"?, "proposed_game_id"?, "users" } ],
  "vests":   [ { "id", "name", "designation", "tiers": [worn at], "game_item_ids": { tier: item }, "game_match", "users" } ],
  "plates":  [ { "id", "name", "material", "designation", "real_rating", "side_plate", "vest_tiers", "game_item_ids": { tier: item or "NEW ..." }, "users" } ]
}
```

## How the files were made

- The generator is [tools/loadouts_gen/](../tools/loadouts_gen/) (its README explains the files and spec keys). It holds the catalogue (started as a port of the WIP Perl file), one spec per bloc and the rules above.
- It reads `factions/<id>.json` (names, camo, tier, vehicles, unit_templates, `ai_tuning`), `reference/vehicles/` (vehicle types) and the game's `data/items.json`. It writes the 79 faction files, the three indexes and the README in one run.
- Run it from the repo root: `python3 -I tools/loadouts_gen/gen.py --game <path to the Contractor game repo>` (on Captain's desktop, `--game B:\Contractor`). Then run `python3 -I tools/validate_pack.py`. The output is deterministic, and an unchanged checkout regenerates byte for byte.

## Validator

`tools/validate_pack.py` checks every `loadouts/<id>.json` except the three index files:

- The id is a canonical faction id, not `player`, and matches the filename.
- A `regular` variant exists, variant ids are unique, and every variant has all 8 core roles (a role may be `not_fielded`).
- `in_game` launchers name one of the 6 in-game launchers; other launchers name one of the 6 or `null` as `game_substitute`.
- Vest tiers are light, medium or heavy; helmet tiers are none, light, medium or heavy; side plates appear only on heavy vests.
- It warns on a `role_map` target that is not a role, and on a missing loadout file.

On Captain's desktop, which has no Python, mirror these checks in the session's Perl port.

## Open questions for Captain

None open for this job. The 10 questions raised by Job 6 were answered on 2026-10-10 (see "Captain's decisions (2026-10-10)").
