# Contractor faction pack: handoff

Snapshot as of 2026-10-10 04:35 UTC. The pack is still being generated on branch `factions-worldspaces` (draft PR #2). Finished files push automatically every 10 minutes, so the folders on the branch are the live state. Check them against the "Status" section below.

The Contractor design doc (Claude Doc) is the source of truth for game design. Where it disagrees with this pack, the design doc wins. Anything this pack invents for gameplay is listed under `proposed` in each file, so it can be tuned.

## What Captain asked for (2026-10-10)

- Factions for every major global political player "from the US to Russia" (Ukraine, Russia, Poland, Switzerland, etc.), with their modern-day alliances.
- Modern-day-inspired proc-gen worldspaces. These are the final stage and are built on the finished factions.
- Real-world vehicles that each faction is known for using, with reference photos scraped from the web.
- Regional procs for Israel and for Palestine/Iran.
- A Middle East terrorist bloc, "like Hamas and al-Qaeda". The early game sees a lot of fighting against terrorists.
- Push factions to the repo as they finish, and save progress before any usage-limit cutoff.

## Settled game decisions the pack follows

- The player faction is a PMC company (`player`). The USA, GB and Canada are friendly, and reputation unlocks buying their gear and vehicles.
- Enemy factions use Chinese, Russian, Iranian or terrorist-style gear depending on region.
- Contracts come from a regional board and from faction fixers, negotiated MW5-style. Working for one side locks you out of its enemies' contracts for a while.
- The world is persistent. Factions fight simulated operations between missions, and the war posts matching contracts.
- Contract zone: about 2-4 km², 40-90 min.
- Hot zone: about 8-16 km², 2-4 h; the players choose when to extract.
- Supports deploy from an LHD (coastal) or a FOB (inland).
- Civilians are present on maps. Casualties caused by players or their AI cost a fine and reputation; 8 casualties void the contract.
- Vehicle armor ignores small-calibre fire; 7.62x54R and up can penetrate.
- In-game launchers: AT4, RPG-7 (PG-7V, OG-7V), Javelin, MAAWS, NLAW, SMAW.
- Armor tiers follow Captain's light/medium/heavy rules (see the design doc).
- Existing voxel models: `uh60`, `ah1z`, `aav7`, `maxxpro`, `matv`, `bradley`, `abrams`, `technical_*`. Their real-world operators are recorded as fact. **Which game faction fields the AH-1Z, MRAPs, Bradley and Abrams is still OPEN**; any assignment in the pack is a proposal.

## Defaults this thread picked (Captain can override)

- **Names:** states and the terrorist groups Captain named use real names. Cartels, rival PMCs and all worldspace towns are fictional and inspired by real regions; no real city is replicated.
- **Terrorist groups:** hostile-only. They never hire the player and never sell to the player.
- **Tone:** factual and neutral. Tactics are described at game-design level only (ambushes, tunnels, IEDs as map hazards, drones).
- **"Palestine/Iran":** built as separate regions, `gaza_west_bank` and `iran_zagros`, plus `persian_gulf_coast`, because one map can't hold both. `israel` is its own region.
- **Photos:** the cloud build container can read web text (Wikipedia) but cannot download images; curl, upload.wikimedia.org and Commons are blocked. Each vehicle file therefore links its photo pages in `reference_pages` rather than storing photos. For exact matching, Captain can drop photos in a local folder, as was done for the UH-60.

## Roster (canonical ids)

| Bloc | Factions |
|---|---|
| Player | player |
| US and Five Eyes | usa (Army and USMC), gbr, can, aus, nzl |
| Western Europe and Nordics | fra, deu, ita, esp, nld, bel, nor, dnk, swe, fin, grc |
| Ukraine and NATO eastern flank | ukr, pol, est, lva, ltu, rou, mda, geo |
| Russia, CSTO, Caucasus | rus, blr, africa_corps (Russian state PMC, rival), kaz, srb, arm, aze |
| Asia-Pacific | chn, prk, jpn, kor, twn, ind, pak, phl, vnm |
| Middle East states | irn (Artesh and IRGC), isr, tur, sau, are, qat, egy, jor, syr, irq, pse_pa |
| Middle East terrorist and armed non-state groups (early game) | hamas, pij, hezbollah, houthis, iraqi_militias, al_qaeda, aqap, isis, isis_k, al_shabaab, jnim |
| Neutrals, Africa, Central Asia, cartels, rival PMCs | che, aut, irl, mex, cartel_pacifico, cartel_jalisco_nueva (fictional), afg_taliban, sdf, krg_peshmerga, sahel_aes, som, pmc_halcyon, pmc_kestrel, pmc_black_sable (fictional) |

## Theatres (worldspace ids)

- Europe, Asia and Americas: baltic_coast, suwalki_gap, eastern_ukraine, black_sea_coast, arctic_north, caucasus, alpine_europe, taiwan_strait, korean_dmz, south_china_sea, kashmir_loc, mexico_cartel_belt.
- Middle East and Africa: levant_syria, lebanon_south, israel, gaza_west_bank, iran_zagros, persian_gulf_coast, mesopotamia, yemen_red_sea, sahel, horn_of_africa, afghan_highlands.

## Layout and schemas

- `factions/<id>.json` holds:
  - identity: kind, blocs, campaign tier, alignment to the player, player_client
  - relations (-100..100, keyed by faction id), theatres and languages
  - doctrine, plus `ai_tuning` values from 0 to 1
  - camo palettes, small arms by role, launchers and body-armor tier
  - vehicles (catalogue ids with role and prevalence) and unit templates
  - support assets, player_trade reputation tiers, contract types
  - `proposed`, and sources
- `reference/vehicles/<id>.json` is the shared real-vehicle catalogue. Each file has:
  - operators, crew, dimensions and weight, armament
  - protection, with notes on how it fits the game's armor rule
  - `visual_notes` for voxel modelling, colour schemes, variants
  - `existing_model`, `model_priority` (high/medium/low), and `reference_pages` (photo pages)
- `worldspaces/<theatre>.json` holds:
  - map size, climate, biomes with palettes
  - terrain, with a Voxel Tools generator recipe
  - settlements and architecture, infrastructure, POIs (loot capped at medium), weather and civilians
  - factions present, how the frontline moves, contract hooks, insertion (LHD/FOB), and whether it suits the early game

## Status at this snapshot

- **Factions done (42 of 76):** every faction in the Five Eyes, Western Europe, eastern flank, Russia/CSTO and Asia-Pacific blocs, plus `player`.
- **Factions still generating:** the Middle East states, the terrorist bloc, and the neutrals/others bloc.
- **Vehicle catalogue:** 198 vehicles (34 high, 58 medium, 106 low priority).
- **Worldspaces:** not started. They run after all the factions are done.
- **Validation:** not started. It will fix ids and relation symmetry, merge duplicate vehicles, and write `factions/README.md` (roster and alliance matrix), `reference/vehicles/README.md` and `worldspaces/README.md`.

## Next voxel models to build

These are the high-priority vehicles in the catalogue that have no model yet, as of this snapshot:

ah64, bmp1, bmp2, bmp3, boxer, btr82a, ch47, cv90, fpv_drone, gaz_tigr, griffon, jltv, leclerc, leopard2a6, m113, merkava4, mi8, stryker, t64bv, t72b3, t90m, toyota_hilux, type99a, vbci, zbd04a.

Early-game (terrorist) theatres lean on the existing technicals, Hiluxes, BMP/BTR/T-72-family vehicles and captured army kit. Those are the best candidates to model first.

## Open questions for Captain

- Who fields the AH-1Z, MRAPs, Bradley and Abrams in the game (real-world operators are recorded).
- Whether hot zones are twice the area (current) or twice the width.
- Reputation thresholds and prices for buying from the USA, GB and Canada; the values in the files are proposals.
- Whether any non-Five-Eyes friendly (for example Poland or France) should also sell to the player.

## How to resume if the run is interrupted

The generator is in `tools/factions_workflow.js`. It is a Claude Code Workflow script with 8 bloc agents, then 2 worldspace agents, then 1 validator.

1. Re-run only the blocs whose faction files are missing. Edit the `BLOCS` list to keep those blocs, or drop the finished entries from `ROSTER`.
2. Then run the Worldspaces and Validate phases.

Agents write straight into `factions/`, `reference/vehicles/` and `worldspaces/`. Before creating a vehicle file, they list the vehicle folder first so they don't make duplicates.
