# Contractor faction pack: handoff

Snapshot as of 2026-10-10 11:05 UTC. Captain paused all work at 09:34; the queue has since resumed, and Jobs 1 (middle_east_states), 2 (me_terror) and 3 (others) are done (2 and 3 ran in parallel). The pack lives on branch `factions-worldspaces` (draft PR #2 on the original repo; work now continues on the fork `cghath/Contractor-Assets-and-References`), and the folders on the branch are the live state.

The Contractor design doc (Claude Doc) is the source of truth for game design. Where it disagrees with this pack, the design doc wins. Anything this pack invents for gameplay is listed under `proposed` in each file, so it can be tuned.

## Handoffs (start here)

**Status (2026-10-10, after Job 4):** Jobs 1-4 are complete. All 77 factions exist and are reconciled to `factions/alliances.json` (47 alliances and the full 77 x 77 relations matrix), with 210 vehicles in the catalogue. The validator reports 0 errors. Job 6 (loadouts) is also complete: all 76 non-player factions have loadouts. Job 5 (worldspaces) is also complete: all 23 theatres are written. The validator reports 0 errors and 0 warnings. Remaining: merge duplicate vehicles and write `reference/vehicles/README.md`.

**Faction count:** the roster has 77 ids, not 76 as earlier versions of this file said (1 + 5 + 11 + 8 + 7 + 9 + 11 + 11 + 14).

Each job has a sheet in this repo and a matching Claude Doc:

| Job | Repo sheet | Claude Doc |
|---|---|---|
| Terrorist bloc (me_terror) | [me_terror_handoff.md](me_terror_handoff.md) | https://claude.ai/code/artifact/24090dda-b337-4f8b-bc34-6985e097e689 |
| Neutrals bloc (others) | [others_handoff.md](others_handoff.md) | https://claude.ai/code/artifact/37654e72-a033-4f2f-9417-008a5e36fed7 |
| Alliances | [alliances_handoff.md](alliances_handoff.md) | https://claude.ai/code/artifact/45389ec6-ee49-40e9-b15a-df9704aadb94 |
| Worldspaces | [worldspaces_handoff.md](worldspaces_handoff.md) | https://claude.ai/code/artifact/721887fe-5ac7-4eac-b048-0195fd684304 |
| Loadouts (Job 6, done on the fork) | [loadouts_handoff.md](loadouts_handoff.md) | n/a |

**Resume here.** Run one job at a time, in this order. Details are under "How to resume" at the end of this file.

1. ~~Finish syr, irq and pse_pa, and cross-check the 8 new Middle East files.~~ Done (10:45 UTC).
2. ~~me_terror.~~ Done (10:55 UTC).
3. ~~others.~~ Done (11:05 UTC).
4. ~~alliances.~~ Done (2026-10-10).
5. ~~worldspaces.~~ Done (2026-10-10).
6. ~~loadouts.~~ Done on the fork (2026-10-10).

The loadouts were owned by the "Faction loadout questions" thread, which never pushed any `loadouts/` files. On the fork, the job was taken over at the user's request and is now complete. The "don't touch `loadouts/`" rule is lifted; loadouts changes follow [loadouts_handoff.md](loadouts_handoff.md).

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

## Captain's decisions (2026-10-10)

Answers to the open questions of Jobs 1-3, applied during Job 4. Each one was moved out of the faction's `proposed` list and noted as Captain-confirmed in its `notes` (or `rivalry.role`).

- **Middle East states (Job 1):**
  - syr, irq and pse_pa all stay player clients; pse_pa is limited to escort, election security, VIP protection and training.
  - Syria and the SDF are neutral-to-friendly: syr -> sdf and sdf -> syr are +10 each (were -20 and -15), treating the integration as mostly done. The factual 2026 description of the integration process is unchanged.
- **Terrorist bloc (Job 2):**
  - isis keeps the Sahel and Somalia provinces (theatres include sahel and horn_of_africa).
  - Captured Humvees, M1117s and T-55s (isis, isis_k) and ex-Assad-era armour (hezbollah) appear as rare set pieces.
  - campaign_tier: only iraqi_militias moves from mid to early; hezbollah and houthis stay mid.
  - The single-source relations stay as they are: al_qaeda -> afg_taliban +40, houthis <-> aqap -60, houthis <-> al_shabaab +10.
  - The status notes based on the latest reporting found (Hamas roadmap to late July, Hezbollah/Lebanon to July, JNIM blockade to May) are acknowledged, with no change.
- **Others (Job 3):**
  - afg_taliban can hire the player as a limited client: player_client true, alignment neutral, relation -10 both ways with player, as_client counter-ISIS-K operations, convoy escort and infrastructure protection. It never sells gear. The factual recognition text is unchanged.
  - Arms markets are all on: che and aut sell at rep 20/40/60, and krg_peshmerga sells basic kit at rep 30/50.
  - The player's nemesis is **pmc_black_sable** (the Gulf-funded rival). pmc_halcyon is an ordinary rival. The rest of each rivalry object stays proposed.
  - The name "Halcyon" stays as is; any resemblance to a real security firm is coincidental. No trademark-check question remains in the repo files.
  - sahel_aes stays a rare client on harsh terms, relation -10 with the player.
  - The Ford Ranger has its own catalogue file, `ford_ranger` (medium priority, no model yet), with the Mexican Ford Lobo/F-series and Ram patrol pickups as its variants. afg_taliban (signature, plus Hilux as common) and mex point at it; the Ranger variants were removed from `toyota_hilux`.

- **Alliances (Job 4):**
  - Side-lock lasts 2-4 in-game weeks (14-28 days, scaled by contract severity).
  - NATO members outside the Five Eyes sell to the player at higher thresholds than usa/gbr/can (rep 20/40/60/80). tur does not sell (Captain-confirmed).
  - Reputation spill-over applies only between factions that share an alliance.
  - sau, are and qat sell at high reputation (rep 40/60/80; the unlock lists are proposed). isr hires the player but never sells.
  - Player relations with the rival PMCs (-20 to -45) and the cartels (-60 to -65) stay as written.
  - afg_taliban vs pak is -90 both ways (active border war since February 2026).

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

**Update, 2026-10-10: Job 5 (worldspaces) is complete.** All 23 theatres are written in `worldspaces/<id>.json`, plus `worldspaces/README.md` (theatre table, zone fit, generator approach, proposed materials with hex colours). `early_game_suitable` is true on 8 theatres: levant_syria, gaza_west_bank, mesopotamia, yemen_red_sea, sahel, horn_of_africa, afghan_highlands and mexico_cartel_belt. `lhd` is true on the 13 coastal maps. Maps are 16-24 km per side; each has a `zone_plan` with 4 contract zones and 1-2 hot zones. All towns are fictional. afghan_highlands models the active Afghanistan-Pakistan border war. `factions_present` matches every faction file's `theatres`, except that lebanon_south adds chn and ind as UNIFIL contributors (per alliances.json). Validator: 0 errors, 0 warnings. Remaining validation work: merge duplicate vehicles and write `reference/vehicles/README.md`.

**Update, 2026-10-10 (after Job 6): loadouts are complete on the fork.** The "Faction loadout questions" thread never pushed any files, so Job 6 was taken over on the fork at the user's request. New: `loadouts/<id>.json` for all 76 non-player factions (107 variants; 8 core roles each, plus crew/pilot where the faction fields the vehicles), `loadouts/weapons_index.json`, `loadouts/armor_index.json` and `loadouts/README.md` (roster and "what has to be built": 238 weapons, 33 magazines, 13 calibres, the 6 launcher items, 22 underbarrel launchers, 13 optics, 9 medical items, 1 new plate `plate_steel_light`). Real-world designations throughout; the 8 unanswered loadout defaults are applied and marked proposed. Every `game_kit` id exists in the game repo's `data/items.json`. `tools/validate_pack.py` now checks loadouts: 0 errors. [loadouts_handoff.md](loadouts_handoff.md) has the schema and 10 new open questions for Captain.

**Update, 2026-10-10: Job 4 (alliances) is complete.** New files: `factions/alliances.json` (47 alliances with member status, obligations and proposed game effects; proposed `game_rules` for side-lock, war joining, reputation spill-over and selling; the full 77 x 77 `relations_matrix`), `factions/ALLIANCES.md` (plain-words version, major-power matrix, change log, open questions), `factions/README.md` (schema, roster table, alliance matrix) and `reference/vehicles/ford_ranger.json`. All 77 faction files were reconciled:
  - `relations`: 694 missing reverse entries added, so every pair a file lists is now listed by both sides (same sign, within 30 points). This closed the known gaps (European, Baltic and Asian states vs the terror groups; Nordic, Benelux and Southern European states vs afg_taliban, sdf, krg_peshmerga and sahel_aes; usa vs the PMCs; the terror files vs the PMCs and neutral states; player vs che, aut, irl, mex and prk). One mismatch fixed: aze <-> geo (40 vs 75) set to 58 both ways. The 1,450 pairs that no file lists are filled only in the matrix (judged pairs, group rules and a formula, all proposed).
  - `blocs`: each file now lists exactly the alliances it belongs to (any member status). csto_suspended, eu_candidate, eu_partnership and nato_partner became alliance ids with a member_status; descriptive tags (neutral, schengen, g20, rival_pmc, cartel and others) moved to a new `traits` list.
  - Captain's decisions (section above) were applied in the same pass. Validator: 0 errors.
  - Next job: worldspaces; loadouts are job 6 (after alliances, can run alongside worldspaces).

**Update, 2026-10-10 11:05 UTC: Job 3 (others) is complete.** All 14 files are written: che, aut, irl, mex, cartel_pacifico, cartel_jalisco_nueva, afg_taliban, sdf, krg_peshmerga, sahel_aes, som, pmc_halcyon, pmc_kestrel and pmc_black_sable. All 77 factions now exist. Next job: alliances.

**Update, 2026-10-10 10:55 UTC: Job 2 (me_terror) is complete.** The next job is others, which is already running in a separate agent in the same checkout.

**Update, 2026-10-10 10:45 UTC: Job 1 (middle_east_states) is complete.** The queue resumed one job at a time; the next job is me_terror.

**Update, 2026-10-10 09:40 UTC: ALL WORK PAUSED by Captain at 09:34.** Every agent is stopped and the auto-save loop is off. Don't resume anything until Captain says so.

The queue, run one job at a time on Captain's desktop, is:

1. middle_east_states (**done**, 10:45 UTC)
2. me_terror (**done**, 10:55 UTC)
3. others (**done**, 11:05 UTC)
4. alliances (**done**, 2026-10-10)
5. worldspaces (**done**)
6. loadouts (**done** on the fork)

**Loadouts moved (Captain, 09:38 UTC):** the faction loadouts are now built by the separate "Faction loadout questions" project thread, which writes only into `loadouts/`. The bloc and worldspace jobs must never edit `loadouts/`, `tools/loadouts_catalog_wip.pl` or `docs/loadouts_handoff.md`. Because another session pushes to this branch too, always pull (rebase) before pushing.

Each job has its own handoff sheet:

- [me_terror_handoff.md](me_terror_handoff.md)
- [others_handoff.md](others_handoff.md)
- [alliances_handoff.md](alliances_handoff.md)
- [worldspaces_handoff.md](worldspaces_handoff.md)
- [loadouts_handoff.md](loadouts_handoff.md)

Current state:

- **Factions done (77 of 77):** every bloc is written, plus `player`.
- **Neutrals/others bloc (14 of 14 written):** che, aut, irl, mex, cartel_pacifico, cartel_jalisco_nueva, afg_taliban, sdf, krg_peshmerga, sahel_aes, som, pmc_halcyon, pmc_kestrel and pmc_black_sable.
  - che, aut and irl are neutral states that can hire the player; che and aut sell to the player at rep 20/40/60 (Captain-confirmed 2026-10-10). irl lists only 3 vehicles because its armoured fleet is that small.
  - The cartels ("Liga del Pacifico", "Cartel Nueva Frontera") and the rival PMCs (Halcyon, Western; Kestrel, Russia-linked and separate from africa_corps; Black Sable, Gulf-funded) are fictional, each with `inspired_by`. The PMCs carry a proposed `rivalry` object; pmc_black_sable is the nemesis (Captain-confirmed 2026-10-10), pmc_halcyon an ordinary rival.
  - afg_taliban was hostile and never a client; by Captain's decision (2026-10-10) it is now a limited client (neutral, relation -10 with player). sdf -> syr was -15 (syr -> sdf -20); both are now +10 (Captain's decision). krg_peshmerga and sahel_aes are kind non_state (proposed).
  - Cross-check: no sign mismatches or gaps over 30 points with any existing file. Missing reverse entries for the alliances job: usa has none for the three PMCs, the me_terror files mostly omit the PMCs and neutral states, and player.json has no che, aut, irl or mex entries.
- **Middle East terrorist bloc (11 of 11 written):** hamas, pij, hezbollah, houthis, iraqi_militias, al_qaeda, aqap, isis, isis_k, al_shabaab and jnim are done.
  - All 11 are hostile-only: `kind` non_state, `player_client` false, `sellable` false with empty `rep_tiers`, `relations.player` -100 (iraqi_militias -85), `as_client` empty. Each has 4-11 vehicles and 6-9 unit templates (cells, ambush teams, technical crews, motorbike pairs, drone teams and IED teams as hazards, HVT guard details).
  - `campaign_tier`: hezbollah and houthis are `mid`; the other 9 are `early` (iraqi_militias moved from mid to early by Captain's decision, 2026-10-10). Tuning ramps from pij (lowest) up through hamas and the al-Qaeda/IS cells to hezbollah and the houthis (highest discipline and suppression resistance).
  - Affiliate links: aqap 90, al_shabaab 85 and jnim 85 with al_qaeda (all three in bloc `al_qaeda_network`); isis_k 90 with isis (`islamic_state_network`). The two networks are -85 to -95 toward each other. hamas, pij, hezbollah, houthis and iraqi_militias form `axis_of_resistance` with irn.
  - `iraqi_militias` follows the irq.json boundary: the PMF is not this faction, units appear without PMF markings, and iraqi_militias -> irq is -15 (irq -> iraqi_militias is -20).
  - `isis` covers the Iraq/Syria core plus the Sahel and Somalia provinces (theatres mesopotamia, levant_syria, sahel, horn_of_africa); isis_k is separate.
  - Cross-check: every relation these 11 files write to an existing faction agrees in sign with that file and is within 30 points. Many European, Baltic and Asian states list the terror groups one way only; the alliances job should add the reverse entries.
- **Middle East states (11 of 11 written):** irn, isr, tur, sau, are, qat, egy, jor, syr, irq and pse_pa are done.
  - `syr` is the post-Assad transitional government (al-Sharaa; Turkish-supplied vehicles, captured Assad-era armour, technicals).
  - `irq` is the Iraqi Security Forces (Army, Federal Police, CTS). Its notes define the game boundary: the PMF is part of the Iraqi state and is not a faction; `iraqi_militias` covers the Iran-aligned factions acting outside state command (irq -> iraqi_militias = -20).
  - `pse_pa` is the PA Security Forces. It lists only 3 vehicles (the spec asks for 4-12) because PA forces are limited to light weapons and light vehicles.
  - Cross-check of the 8 earlier files: relation signs agree across all 11, every vehicle id exists, and israel, gaza_west_bank, iran_zagros and persian_gulf_coast are all covered. One fix: `sau` added to the operators of `toyota_land_cruiser`.
- **Vehicle catalogue:** 210 vehicles. Job 4 added `ford_ranger` (medium; Captain's decision) and moved the Ranger and Mexican patrol-pickup variants out of `toyota_hilux`. Before that: 209 vehicles (38 high, 62 medium, 109 low priority). Job 3 added `rg32m`, `narco_truck` and `armored_suv`, put DN-XI (sandcat), Pandur Evolution (pandur_ii), Ford Ranger and Mexican patrol pickups (toyota_hilux) and Super Puma (sa330) in as variants, and updated operators on 35 files. Job 2 added `technical_m40`, `technical_rockets` and `technical_zpu` (catalogue files for existing voxel models, all high), `motorcycle` (high, no model yet) and `fast_boat` (Houthi skiff, explosive variant as a game hazard only; medium). It also added the bloc's ids to the operators of `toyota_hilux`, `toyota_land_cruiser`, `technical_dshk`, `technical_zu23`, `technical_spg9`, `fpv_drone`, `shahed136`, `humvee`, `m1117`, `m113`, `t55`, `t72b3`, `bmp1` and `bmp2`. Job 1 added `al_jawad` (Jordanian-built PA armoured vehicle, with the Al-Maha as a variant). `ejder_yalcin` got `syr` and the Ejder 6x6 variant, `mi8` got `irq`, and `toyota_land_cruiser` got `sau`. Earlier: `aras` and `wolf_av` were added at 200, and `ah1z`, `dingo` and `t55` got operator updates.
- **Worldspaces (23 of 23 written):** see `worldspaces/README.md`. 8 theatres are early-game (levant_syria, gaza_west_bank, mesopotamia, yemen_red_sea, sahel, horn_of_africa, afghan_highlands, mexico_cartel_belt); `lhd` is true on the 13 coastal maps. Faction-coverage gaps are listed in the README and in the worldspaces handoff's open questions.
- **Validation:** partly done in Job 4: relation ids and symmetry are fixed and `factions/README.md` (roster and alliance matrix) is written. Still to do: merge duplicate vehicles and write `reference/vehicles/README.md` and `worldspaces/README.md`.

## Next voxel models to build

These are the high-priority vehicles in the catalogue that have no model yet, as of this snapshot:

ah64, bmp1, bmp2, bmp3, boxer, btr82a, ch47, cv90, fpv_drone, gaz_tigr, griffon, jltv, leclerc, leopard2a6, m113, merkava4, mi8, motorcycle, stryker, t64bv, t72b3, t90m, toyota_hilux, type99a, vbci, zbd04a.

For the early game the most useful of these are `motorcycle` (9 of the 11 terror groups use it), `toyota_hilux` (all 11) and `fpv_drone` (8 groups).

Early-game (terrorist) theatres lean on the existing technicals, Hiluxes, BMP/BTR/T-72-family vehicles and captured army kit. Those are the best candidates to model first.

## Open questions for Captain

- Who fields the AH-1Z, MRAPs, Bradley and Abrams in the game (real-world operators are recorded).
- Whether hot zones are twice the area (current) or twice the width.
- Reputation thresholds and prices for buying from the USA, GB and Canada; the values in the files are proposals.

## How to resume (current plan, 2026-10-10 09:50 UTC)

Captain paused everything at 09:34 UTC. Resume only when Captain says so. Run **one job at a time**, in this order, with one subagent per job. Every job has its own handoff sheet. Give the agent that sheet as its brief, and tell it to read the sheet first.

| # | Job | Handoff sheet | State |
|---|---|---|---|
| 1 | middle_east_states: finish **syr, irq, pse_pa** | This file, plus `middle_east_states` in `BLOCS` in `tools/factions_workflow.js` | **Done** (11 of 11, 10:45 UTC) |
| 2 | me_terror (11 groups) | [me_terror_handoff.md](me_terror_handoff.md) | **Done** (11 of 11, 10:55 UTC) |
| 3 | others: neutrals, cartels, PMCs (14 factions) | [others_handoff.md](others_handoff.md) | **Done** (14 of 14, 11:05 UTC) |
| 4 | alliances: `factions/alliances.json`, `ALLIANCES.md`, the relations matrix, and reconciling all 77 files | [alliances_handoff.md](alliances_handoff.md) | **Done** (2026-10-10) |
| 5 | worldspaces: 23 theatres, Middle East and Africa first | [worldspaces_handoff.md](worldspaces_handoff.md) | **Done** (23 of 23, 2026-10-10) |
| n/a | loadouts | [loadouts_handoff.md](loadouts_handoff.md) | **Done** (Job 6, on the fork; 76 of 76). |

### Job 1 details: finishing the Middle East states

- **Write `factions/syr.json`, `factions/irq.json` and `factions/pse_pa.json`.**
  - Use CONTEXT and FACTION_SPEC from `tools/factions_workflow.js`, with `${REPO}` = `B:\Contractor-Vehicle-Models`.
  - Follow the `middle_east_states` notes in `BLOCS`:
    - **syr:** the post-Assad transitional government (since December 2024), described accurately for 2026.
    - **irq:** the Iraqi Security Forces. Keep the PMF relationship clear against the `iraqi_militias` faction.
    - **pse_pa:** the Palestinian Authority Security Forces.
- **Vehicles:** list `reference/vehicles/` first and reuse existing ids, adding operators.
- **Cross-check the 8 files already written:** irn, isr, tur, sau, are, qat, egy and jor. The agent stopped before it could check them. Look at relations sign agreement within the bloc, at vehicles, and at `theatres`. israel, gaza_west_bank, iran_zagros and persian_gulf_coast should be covered.
- **Finish up:** update the Status section above.

### Rules for every job

- **Agents never run git.** A 10-minute auto-save loop does it. It runs from the session scratchpad on Captain's desktop; if it's gone, recreate it. The loop:
  - stages only `factions/`, `reference/`, `worldspaces/`, these docs and `tools/validate_pack.py`, and never `loadouts/`
  - runs the validator
  - pulls with `git pull --rebase --autostash` (another session pushes `loadouts/` to the same branch)
  - pushes to `factions-worldspaces` only, never to `main`
- **Validator:** CI runs `python3 tools/validate_pack.py`. Captain's desktop has no Python, so a Perl port with the same checks lives in the session scratchpad. Keep it at 0 errors.
- **Don't touch** the local-only branch `local-completion-backup` (e7782a7). It is a thin template backup.
- **Agents write files as they finish them**, so a usage-limit cutoff loses little. Job 1 was cut off by one at 09:34.
- **Report** each landed job to the cloud thread: what landed, the commit hash and the counts.

### Alternative: the workflow script

`tools/factions_workflow.js` can still run the whole pipeline. It runs 8 bloc agents in parallel, then 2 worldspace agents, then a validator. Captain asked for one job at a time, so prefer the queue above. If you use the script anyway, drop the finished entries from `ROSTER`/`BLOCS`, and change `REPO` to the local path.
