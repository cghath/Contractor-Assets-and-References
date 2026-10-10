# AI default loadouts: handoff sheet

Snapshot as of 2026-10-10 09:40 UTC. **PAUSED by Captain at 09:34 UTC.** Don't resume until Captain says so.

## Status

- No `loadouts/` files have been written yet. The agent was stopped while it was building its generator.
- Its partial weapon and gear catalogue, written as a Perl data file, is saved at [tools/loadouts_catalog_wip.pl](../tools/loadouts_catalog_wip.pl). It has stable snake_case ids and records which ids already exist in the game's `B:\Contractor\data\items.json`. Reuse it or replace it; it's work in progress and not run by CI.
- The validator has **no** loadouts checks yet.

## What Captain asked for

- AI default loadouts for **every non-player faction**: one file per faction at `loadouts/<faction id>.json`, plus `loadouts/README.md`.
- These loadouts are the **baseline for every weapon and armor piece the game needs** across the factions. So also write:
  - `loadouts/weapons_index.json`: every weapon, calibre and ammo type, optic, launcher and grenade, with its users, and whether it already exists in the game repo.
  - `loadouts/armor_index.json`: every helmet, vest, plate carrier and plate, with its tier and users.
  - A "what has to be built" summary in the README.
  - Keep ids stable.
- The agent must **ask questions** rather than guess. Questions go to Captain in a separate thread, through the project assistant.

## Captain's answer (09:32 UTC, loadout questions thread)

> "faction loadouts should be based on real life, armor and helmet and weapon names, ammunition types etc."

So use **real-world designations** for every faction:

- **Weapons:** the actual service rifles, MGs, sidearms and launchers. Examples: AK-74M, AK-12, HK416, C8A3, L85A3, M4A1, Type 95, PKM.
- **Ammo types:** real designations. Examples: 5.45x39 7N6/7N10, 5.56x45 M855A1/SS109, 7.62x54R 7N13, 7.62x39 57-N-231.
- **Armor:** real vest, plate and helmet models, mapped to the game's light/medium/heavy tiers and NIJ ratings. Examples: 6B45 and 6B47 (Ratnik), IOTV/SPCS with ESAPI, Mk7 helmet, Virtus, ECH.
- **Fictional cartels and PMCs still use real gear.**
- **Terror groups use their real-world kit:** AK-pattern rifles, PKM, RPG-7, mostly no armor.

## The agent's 9 questions and their defaults

Only the "real-life names" answer has come back so far. The other defaults stand until Captain answers.

1. **Variants:** 1-3 per faction. Every faction gets `regular`, plus real splits: usa army and usmc; rus line, spetsnaz and vdv; irn artesh and irgc; ukr regular and territorial; terror groups fighter and elite.
2. **Crew and pilot roles:** optional, only where the faction fields vehicles or aircraft.
3. **Counts:** real integer counts for magazines and medical items, marked as `proposed`.
4. **Launchers outside the game's 6:** record the real launcher with `in_game: false`, plus a `game_substitute` from the 6. RPG-26 maps to AT4, PF-98 or Panzerfaust 3 to MAAWS, and Spike or HJ-12 to Javelin.
5. **Plates:** add polyethylene (`pe`) as a third plate material alongside steel and ceramic. Light plates map to the game's `plate_pe_l3`.
6. **Medical:** new ids for bandage, IV/saline, chest seal, splint, epinephrine, morphine, adenosine, atropine, surgical kit and defibrillator. `ifak` and `trauma_kit` stay as containers.
7. **Optics and smoke:** optic names become proposed ids. Smoke is white for screening, and green, red or violet for signalling.
8. **Magazines:** one id per calibre and type, for example `mag_545x39_30` and `belt_762x54r_100`.
9. **Terror armor:** none for regular fighters. Elites get a light vest with improvised or captured steel plates, and a few get helmets or NVGs.

## Rules to keep when resuming

- **Stay consistent** with `factions/<id>.json`: small_arms, launchers, body_armor, camo and doctrine. Where a faction file disagrees with reality, note it.
- **Roles:** rifleman, autorifleman, marksman, grenadier, at, medic, squad_leader and sniper, plus crew and pilot where relevant.
- **Armor tiers** (from the design doc):
  - LIGHT is an aramid vest with frontal fragment protection plus some ballistic; a light plate stops .223 at most.
  - MEDIUM has front and back plates.
  - HEAVY has front, back and side plates.
  - A heavy helmet is NIJ III++.
- **Medical** follows ACE3: the drugs are only epinephrine, morphine, adenosine and atropine. Surgery kits and defibrillators are for the player and medics only.
- **In-game launchers:** AT4, RPG-7 (PG-7V and OG-7V), Javelin, MAAWS, NLAW and SMAW.
- **Game repo is read only:** reuse ids from `B:\Contractor\data\items.json`.
- **Validator:** add loadouts checks to `tools/validate_pack.py`. The checks are: faction id is canonical and not `player`, all core roles are present, `in_game` launchers are among the 6, and armor tiers are valid. Skip the two index files. On Captain's desktop, which has no Python, mirror the checks in the session's Perl port.
- **Order:** do the 40 finished non-player factions first, then each new bloc as it lands.
