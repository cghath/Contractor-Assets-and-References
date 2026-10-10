# AI default loadouts: handoff sheet

Snapshot as of 2026-10-10 11:45 UTC. **Job 6 is complete on the fork** (`cghath/Contractor-Assets-and-References`, branch `factions-worldspaces`).

## Status

- **Ownership:** this job was owned by the separate "Faction loadout questions" thread, which never pushed any `loadouts/` files. On 2026-10-10 the user asked for the job to be taken over and completed on the fork, after the alliances job (Job 4). Captain's 09:34 pause had been lifted for the queue by then (see [factions_handoff.md](factions_handoff.md)).
- **Done (2026-10-10):**
  - `loadouts/<faction id>.json` for all **76 non-player factions**: 107 variants in total. Every variant has the 8 core roles, plus `crew` where the faction fields armoured vehicles (MBT, IFV, APC, MRAP) and `pilot` where it fields helicopters.
  - `loadouts/weapons_index.json` and `loadouts/armor_index.json` with users and in-game flags.
  - `loadouts/README.md` with the roster and the "what has to be built" summary.
  - Loadouts checks in `tools/validate_pack.py`. The validator reports 0 errors (warnings are only the worldspaces still being written).
- The WIP Perl catalogue, [tools/loadouts_catalog_wip.pl](../tools/loadouts_catalog_wip.pl), is superseded by the two index files. Its ids were kept, except `m110_sniper`, which duplicated `m110`. One correction: the INSAS rifle now uses `mag_556_20`, because 20 rounds in `mag_556` broke the one-id-per-calibre-and-type rule. Its `%GAME_IDS` list is out of date; use the live `data/items.json`.
- The files were made by a generator script kept in the session scratchpad, not in the repo (see "How the files were made"). Edit the JSON directly, or regenerate with a new script.

## What Captain asked for

- AI default loadouts for **every non-player faction**: one file per faction at `loadouts/<faction id>.json`, plus `loadouts/README.md`.
- These loadouts are the **baseline for every weapon and armor piece the game needs** across the factions. So also write:
  - `loadouts/weapons_index.json`: every weapon, calibre and ammo type, optic, launcher and grenade, with its users, and whether it already exists in the game repo.
  - `loadouts/armor_index.json`: every helmet, vest, plate carrier and plate, with its tier and users.
  - A "what has to be built" summary in the README.
  - Keep ids stable.
- The agent must **ask questions** rather than guess. Questions go to Captain through the project assistant. Open questions don't block the work: their defaults are applied and marked `proposed`.

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
9. **Terror armor (applied):** regular fighters get none. Elites get a light vest with an improvised or captured steel plate, and only their squad leaders get a helmet; NVGs follow the faction's night capability. Exceptions that follow the faction files are listed under "Captain's decisions reflected" and in the open questions.

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
- **Faction count:** all 77 faction ids exist; 76 are non-player (everything except `player`). Each one has a loadout.

## Captain's decisions reflected (2026-10-10)

- **iraqi_militias is early tier.** Its armor is kept at light: a soft vest for regulars, and a light vest with a steel plate for elites. The faction file notes some medium (PMF-issued plate carriers); that is left out for the early game.
- **afg_taliban is a limited client but never sells gear.** Its loadout notes say its gear reaches the player only as loot.
- **pmc_black_sable is the nemesis** and pmc_halcyon an ordinary rival; this is noted in the files and does not change kit.
- **hezbollah and houthis stay mid tier.** hezbollah regulars wear light soft vests, and its Radwan elite wears medium armor, as the faction file says (see open questions).

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
    "helmet": { "id", "name", "tier": "none|light|medium|heavy", "game_rating", "game_item_id" } | null
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
  "rounds": [ { "name": "PG-7V", "type": "HEAT|tandem HEAT|HE|HEDP|frag|thermobaric|SAM|top attack", "count" } ],
  "alternates"?: [ "<launcher id>", ... ]
}
```

`game_kit` is a stand-in kit the game can load today. It uses exact or generic items and `game_substitute` weapons. Ammunition is converted to the substitute's magazine by round count, capped at 12. It leaves out launchers, underbarrel ammo, optics, NVGs and medical items that do not exist yet.

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

### `loadouts/armor_index.json`

```
{
  "schema_version": 1, "_note": "...",
  "tiers": { "vest": {...}, "helmet": {...}, "plate": {...} },   // tier -> generic game item
  "helmets": [ { "id", "name", "tier", "designation": "specific|class", "real_rating", "game_rating", "game_item_id", "game_match", "users" } ],
  "vests":   [ { "id", "name", "designation", "tiers": [worn at], "game_item_ids": { tier: item }, "game_match", "users" } ],
  "plates":  [ { "id", "name", "material", "designation", "real_rating", "side_plate", "vest_tiers", "game_item_ids": { tier: item or "NEW ..." }, "users" } ]
}
```

## How the files were made

- A Python generator held the catalogue (ported from the WIP Perl file, with additions), one spec per bloc (weapons per role, armor, variants and notes per faction) and the rules above. It read `factions/<id>.json` for names, camo, tier, vehicles, unit_templates and `ai_tuning`, and `data/items.json` for the game ids. It wrote the 76 files, the two indexes and the README in one run.
- The script was kept in the session scratchpad, as this job's brief asked, so it is not in the repo. To change a loadout, edit the JSON and keep the indexes in step, or ask for the generator to be committed (open question below).

## Validator

`tools/validate_pack.py` checks every `loadouts/<id>.json` except the two index files:

- The id is a canonical faction id, not `player`, and matches the filename.
- A `regular` variant exists, variant ids are unique, and every variant has all 8 core roles (a role may be `not_fielded`).
- `in_game` launchers name one of the 6 in-game launchers; other launchers name one of the 6 or `null` as `game_substitute`.
- Vest tiers are light, medium or heavy; helmet tiers are none, light, medium or heavy; side plates appear only on heavy vests.
- It warns on a `role_map` target that is not a role, and on a missing loadout file.

On Captain's desktop, which has no Python, mirror these checks in the session's Perl port.

## Open questions for Captain

These are new questions raised while doing the job. Their defaults are applied and marked `proposed`.

1. **Light steel plates.** Several faction files give light vests with steel plates: grc, mda, pak, phl, vnm, Artesh conscripts (irn), egy conscripts, sahel_aes and the terror elites except Hezbollah's Radwan (18 factions in all). The game has only a PE light plate. Default: a new `plate_steel_light` (steel, III, fits light), with `plate_pe_l3` standing in. Alternatives: use PE, or move these factions to medium.
2. **Launcher items.** `data/items.json` has none of the 6 design-doc launchers yet. Proposed ids are `at4`, `rpg7`, `javelin`, `maaws`, `nlaw` and `smaw`, with their rounds (PG-7V, OG-7V, FFV551, FFV441D, Mk 6, Mk 3).
3. **Hezbollah Radwan armor.** The faction file says medium, while the terror-elite default (Q9) is a light vest with a steel plate. Medium was kept. Confirm.
4. **Non-ballistic crew helmets.** Tank crews (TSh tanker helmet) and aircrew (flight helmet) wear helmets with no ballistic rating. Default: helmet tier `none`, which needs a cosmetic helmet item. Alternatively, crews could wear the tier helmets.
5. **Heavy helmets.** No AI default uses a heavy (III++) helmet, because no faction file gives one. Should Spetsnaz, PMC assault teams or other SOF variants get one for gameplay?
6. **Build scope for weapons.** 238 weapons would have to be built, many used by 1-3 factions. Should close relatives share one model with skins (for example AK-74/AK-74M, the Minimi family, the G36 family, Carl Gustaf M2/M3/M4)?
7. **Rounds.** 13 calibres have no round in `data/rounds.json`, and 6 designations (M855A1, SS109, M80A1, 7N13, and Chinese 7.62x51 and 9x19) use a generic round of the same calibre. Should they get their own rounds?
8. **Extra variants.** Confirm the variants added beyond the Q1 list. Should Russian mobilised and Storm units, Ukrainian assault units, Basij, SANG and the other forces that faction files mention get variants too?
9. **pse_pa.** The faction file lists no AT weapons, no sniper rifles and only a riot-control launcher, so grenadier, at and sniper are `not_fielded` (stand-in: rifleman). Confirm.
10. **Generator.** Should the generator script be committed under `tools/` so the files can be regenerated, rather than edited by hand?
