# Worldspaces: handoff sheet

Snapshot as of 2026-10-10 09:25 UTC. Branch `factions-worldspaces` (draft PR #2). This sheet is for whoever builds `worldspaces/`, whether an agent or a person. The game rules and the faction pack it builds on are in [factions_handoff.md](factions_handoff.md).

## Status

- **Job 9 (2026-10-10, final validation):** Captain confirmed that the low-plausibility listings stay at low strength (blr in eastern_ukraine and baltic_coast; fra, bel and esp in sahel; jpn in arctic_north and korean_dmz; chn in korean_dmz and kashmir_loc; are in yemen_red_sea; usa in mexico_cartel_belt) and that rus stays on alpine_europe as a what-if. Each worldspace's `captain_confirmed` list records it. No worldspace question is open. The validator reports 0 errors and 0 warnings.
- **Job 7 (2026-10-10): 3 new theatres and Captain's decisions.** `mindanao_sulu` (southern Philippines: isis East Asia cells vs phl, usa advisers; coastal, LHD), `iraq_iran_border` (Diyala and Zagros-foothill borderlands: irq, krg_peshmerga, iraqi_militias, irn, isis remnants) and `eastern_congo` (North Kivu and Ituri: cod, m23, adf, with ind and chn as UN peacekeepers) are written; all three are early-game and 22-24 km per side. There are now 26 theatres; 11 are early-game and 14 have `lhd: true`. alpine_europe gained rus (Russian mountain troops) as a fictional what-if hostile force, alongside the generic arms-trafficker NPCs. Every worldspace file now has a `captain_confirmed` list holding the decisions moved out of `proposed` (map size, hot-zone area, the accepted materials, and per-file decisions: grey-zone escalation, LHD restrictions, qalat walls, Kashmir militants, UNIFIL chn/ind, the iran_zagros and south_china_sea gaps). `tools/validate_pack.py` now checks `factions_present` against each faction's `theatres` both ways; it reports 0 errors and 0 warnings.
- **Done (Job 5, 2026-10-10).** All 23 theatres are written in `worldspaces/<id>.json`, together with [worldspaces/README.md](../worldspaces/README.md), which has the theatre table, the zone fit, the generator approach and the material registry. The validator reports 0 errors and 0 warnings; the missing-worldspace warnings are gone.
  - Pass 1 covers Middle East and Africa (11). Pass 2 covers Europe, Asia and the Americas (12); it was built in the same job, which answers the pass-2 question below for now.
  - `early_game_suitable: true` is set on 8 theatres: levant_syria, gaza_west_bank, mesopotamia, yemen_red_sea, sahel, horn_of_africa, afghan_highlands and mexico_cartel_belt.
  - `lhd: true` is set on the 13 coastal maps.
  - The maps are 16-24 km per side. Each file has a `zone_plan` with 4 contract zones and 1-2 hot zones.
  - Town names are fictional. Names derived from real places were replaced in a cleanup pass.
  - afghan_highlands reflects the active Afghanistan-Pakistan border war (afg_taliban <-> pak at -90; the two clients lock each other out).
- **Faction coverage.** Every faction file's `theatres` entry is reflected in `factions_present`, and since Job 7 every faction present lists the theatre in its own file (chn.json and ind.json now list lebanon_south). The Job 5 questions below were answered by Captain on 2026-10-10 (see the end of this sheet):
  - Should iraqi_militias list iran_zagros?
  - Should isis list south_china_sea, for phl's counter-terror hook?
  - alpine_europe has no hostile faction.
  - kashmir_loc has no militant faction.
  - Several low-plausibility listings are flagged in the README: blr in eastern_ukraine and baltic_coast, fra, bel and esp in sahel, jpn in arctic_north, and chn in korean_dmz. Answered in Job 9: they stay at low strength (Captain, 2026-10-10; see the end of this sheet).
- Earlier note: Captain made the worldspaces the final job: they run after the 3 remaining faction blocs and the alliances job land.
- The job order is: middle_east_states, then me_terror, then others, then alliances, then worldspaces. Only one job runs at a time.
- Faction files already list their theatres (see the table below), so `factions_present` can be checked against them.

## Read first, in this order

1. This sheet.
2. `CONTEXT` and `WORLD_SPEC` in [tools/factions_workflow.js](../tools/factions_workflow.js). One correction applies: game world structures are 10 cm voxels (see "Engine facts" below), and the 5 cm figure there applies only to vehicle art.
3. [factions_handoff.md](factions_handoff.md), for the settled game rules (contract and hot zones, civilians, armor, LHD/FOB).
4. Every `factions/*.json` file, at least the `theatres`, `relations`, `doctrine.summary` and `vehicles` fields, so that `factions_present` and `frontline` match the factions.
5. `factions/alliances.json` and `factions/ALLIANCES.md` (written by the alliances job just before this one), so that frontlines follow who is allied with whom.
6. In the game repo: `B:\Contractor\README.md` (the "Design decisions" and "Known gaps" sections) and `B:\Contractor\scripts\world\voxel_world.gd`. Read only; never edit the game repo.

## What to build

- One file per theatre: `worldspaces/<theatre id>.json`. There are 23.
- `worldspaces/README.md`: a table of id, name, inspired_by, size, early_game_suitable and main factions, plus a note on how contract zones and hot zones fit each map.
- The exact JSON shape is `WORLD_SPEC` in [tools/factions_workflow.js](../tools/factions_workflow.js). Its game-wide rules are in `CONTEXT` in the same file.

These are modern-day-inspired **procedural** regions for Voxel Tools (5 cm voxels, terrain generated in code). Each file is a recipe, not a map:

- biomes with palettes
- noise layers and a generator approach
- settlement types and layout rules
- POIs, civilians, factions present, frontline behaviour, contract hooks, and insertion by LHD or FOB

## Engine facts the recipes must fit (from the game repo, `cghath/Contractor`)

These facts were read from Captain's local checkout (`B:\Contractor`, `README.md` and `scripts/world/voxel_world.gd`) on 2026-10-10. Read those two files yourself if you can.

### Scale and current limits

- **World structures are 10 cm voxels, not 5 cm.** The 5 cm figure applies only to vehicle art in this repo. Characters and gear are 1-2 cm voxel models.
- **The ground is not voxels today.** `VoxelWorld` uses a `VoxelTerrain` with a `VoxelGeneratorFlat` set to all air. The ground is a plain collider, and voxels are used only for destructible structures.
- **There is no voxel stream yet.** The editable area is limited to `VoxelWorld.BOUNDS`, about 44 x 44 m with 5.6 m of height. A km-scale map therefore can't be dense 10 cm voxels.

Write each recipe in two layers:

1. **Macro terrain** (km scale): a heightmap or noise recipe for a mesh or coarse ground. It could later become a `VoxelLodTerrain` with a `VoxelGeneratorGraph` or a heightmap generator. Give noise layers in metres, and keep the elevation range realistic.
2. **Micro structures** (the 10 cm destructible layer): buildings, walls, compounds and cover, placed only around the active contract zone or hot zone. Settlement `layout_rules` and POIs should describe these in plain building blocks: footprint in metres, storeys, wall thickness, courtyards, roof type, openings.

### Materials

The game's voxel materials today are `CONCRETE`, `PAINTED`, `WOOD` and `STEEL`, with the palette in `voxel_world.gd`.

- Map each settlement's `materials` to these where possible.
- Where a region needs more, list new materials as proposals in `proposed`. Examples: `MUD_BRICK`, `STONE`, `CINDER_BLOCK`, `SANDBAG`, `CORRUGATED_IRON`, `GLASS`, `DIRT_BERM`.
- Give each new material a hex colour.

### How the game uses a map

- **Missions** run on a persistent **zone-graph world map**. A worldspace is a region the game slices into zones, and each zone saves its own state (loot taken, dropped items, and the voxel edit log for bullet holes and breaches).
- So POIs and settlements should make sense as zone-sized chunks: one compound, one village quarter, one checkpoint and so on. They need clear entry routes and cover.
- **Destruction** is per voxel: walls chip and breach. State which building types are thin-walled (easily breached) and which are thick (cover). That is gameplay-relevant.
- **Vehicles** are drivable ground vehicles; aircraft are AI-flown only. Roads, bridges, wadis and chokepoints matter for convoy and ambush contracts.

## What makes each field useful (aim for this depth)

- **`biomes`:** 3-6 per region, each with shares summing to about 1. Use real vegetation species or types. `ground_palette` and `foliage_palette` should each have 4-6 hex colours sampled from real descriptions of the region: soil, rock, dry grass, crops and so on.
- **`terrain.generator`:** a recipe someone could implement directly.
  - Give 3-5 noise layers (type such as simplex, ridged or cellular, frequency in cycles per km, amplitude in metres, and purpose).
  - Add the erosion approach, the river and wadi rule, and how settlements flatten terrain.
- **`settlements`:** 3-6 types. Each needs:
  - real architectural traits of the region, such as flat roofs, courtyards, rooftop water tanks, rebar stubs, terraces or stone walls
  - footprint and storey ranges
  - a palette, layout rules (street grid or organic, a market square, a mosque or church landmark), and 4-8 fictional example names in the region's language style
- **`pois`:** 8-15 per region. Every POI is a playable chunk: what it looks like, why a contract would send you there, `loot_tier` (low or medium only), and `intel_chance`.
- **`factions_present`:** each entry needs `role`, `strength` and a concrete `where` (which biome, settlement type or terrain feature). It must match the faction files.
- **`frontline`:** how the persistent faction war moves on this map: who pushes where, what flips zones, and what posts contracts.
- **`contract_hooks`:** 6-10 mission types that use this map's specific terrain and factions.
- **`insertion`:** `lhd` is true only for coastal maps. The FOB entry says where a FOB sits and how players reach the zone.
- **`civilians`:** realistic density and behaviour, such as market hours, fleeing patterns, and civilian vehicles (minibuses, motorbikes, donkey carts and so on). Note where the casualty penalty makes a map harder.

## Rules

- **Towns are fictional.** Use fictional names inspired by the region. No real city is replicated.
- **Map size:** each map must hold several contract zones (2-4 km², 40-90 min) and at least one hot zone (8-16 km², 2-4 h). `map_size_km` is a proposal.
- **Loot** caps at the medium tier. Set `intel_chance` per POI.
- **Civilians:** density should be realistic. The penalties apply: a fine and reputation loss per casualty, and 8 casualties void the contract.
- **Sensitive regions:** israel, gaza_west_bank and iran_zagros were added at Captain's request. Keep them factual and neutral, with fictional towns and high civilian density where that is real.
- **Tactics** stay at game-design level only: IEDs as map hazards, tunnels, drones, ambush terrain.
- **Ids:** only canonical faction ids in `factions_present`, and only canonical theatre ids. Both lists are in the workflow script.
- **Early game:** mark terrorist-heavy theatres `early_game_suitable: true`.
- **Proposals:** anything invented for gameplay goes in `proposed`.
- **Research:** text only, for climate, terrain, vegetation, architecture and palettes. Image hosts are not used.

## Theatres, build order and current faction coverage

The **Faction files listing it** column is generated from each faction file's `theatres` field as of this snapshot. The Middle East states, terror and others blocs will add more, so re-read `factions/*.json` before writing.

### Pass 1: Middle East and Africa (early game, build first)

| Theatre | Inspired by | Faction files listing it | Expected once all blocs land |
|---|---|---|---|
| levant_syria | Syria (post-Assad transition) | can fra gbr kaz nzl rus usa | syr, tur, isr, sdf, isis, hezbollah, iraqi_militias |
| lebanon_south | South Lebanon / UNIFIL area | deu esp fin fra ita kaz kor pol srb (UNIFIL) | hezbollah, isr |
| israel | Israel (north, centre, Negev) | none yet | isr, hezbollah, hamas, pij |
| gaza_west_bank | Gaza Strip and West Bank | none yet | isr, hamas, pij, pse_pa |
| iran_zagros | Zagros mountains, western Iran | none yet | irn, iraqi_militias, krg_peshmerga |
| persian_gulf_coast | Gulf littoral, Strait of Hormuz | aus fra gbr grc ind kor pak usa | irn, sau, are, qat |
| mesopotamia | Iraq, Tigris and Euphrates | aus bel can deu dnk esp est fra gbr ita ltu lva nld nor nzl pol usa | irq, iraqi_militias, isis, krg_peshmerga, sdf |
| yemen_red_sea | Yemen and the Red Sea coast | deu dnk fra gbr grc ind ita usa | houthis, aqap, sau, are |
| sahel | Mali, Burkina Faso, Niger | africa_corps bel esp fra | sahel_aes, jnim, isis |
| horn_of_africa | Somalia, Djibouti | chn esp fra ita jpn kor usa | al_shabaab, som, are, tur |
| afghan_highlands | Afghanistan, Hindu Kush | chn ind pak | afg_taliban, isis_k, pak |

### Pass 2: Europe, Asia and Americas

| Theatre | Faction files listing it |
|---|---|
| baltic_coast | bel blr can deu dnk esp est fin fra gbr ita ltu lva nld nor pol rus swe usa |
| suwalki_gap | blr can deu ltu nld pol rus usa |
| eastern_ukraine | blr prk rus ukr |
| black_sea_coast | bel fra grc ita mda rou rus ukr |
| arctic_north | can dnk fin gbr jpn nor rus swe usa |
| caucasus | arm aze geo rus |
| alpine_europe | deu fra ita srb (plus che, aut once the others bloc lands) |
| taiwan_strait | chn jpn twn usa |
| korean_dmz | aus chn jpn kor nzl prk usa |
| south_china_sea | aus chn jpn nzl phl twn usa vnm |
| kashmir_loc | chn ind pak |
| mexico_cartel_belt | usa (plus mex, cartel_pacifico, cartel_jalisco_nueva once the others bloc lands) |

### Job 7 additions (2026-10-10)

| Theatre | Inspired by | Faction files listing it |
|---|---|---|
| mindanao_sulu | Southern Philippines (Mindanao and Sulu) | isis phl usa |
| iraq_iran_border | Iraq-Iran borderlands (Diyala, Zagros foothills) | iraqi_militias irn irq isis krg_peshmerga |
| eastern_congo | Eastern DR Congo (North Kivu, Ituri) | adf chn cod ind m23 |

alpine_europe also gained rus (Job 7), and lebanon_south is now listed by chn and ind.

`player` lists every theatre. The rival PMCs (pmc_halcyon, pmc_kestrel and pmc_black_sable) and africa_corps can appear as `rival_pmc` wherever their files place them.

## Checks before handing back

1. Every file parses, its `id` matches the filename, and all faction ids are canonical. Run the validator. CI uses `python3 tools/validate_pack.py`. On Captain's desktop, which has no Python, use the Perl port in the session scratchpad.
2. `factions_present` agrees with the faction files' `theatres`. Where a faction appears in a theatre its file doesn't list, add the theatre to the faction file, or record the mismatch as an open question.
3. Write `worldspaces/README.md` and update the Status section of `docs/factions_handoff.md`.
4. Don't run git from an agent. The session's auto-save loop commits and pushes to `factions-worldspaces` every 10 minutes when the validator passes. Never push to `main`, and never touch `local-completion-backup`.

## Open questions for Captain

Answered by Captain (2026-10-10), applied in Job 7:

- Hot zones are twice the AREA of a contract zone (8-16 km² vs 2-4 km²), not twice the width.
- Pass 2 (Europe, Asia and Americas) was built in Job 5 and stays.
- Map sizes of 16-24 km per side are confirmed.
- The 18 proposed materials and hex colours are accepted and were added to `voxel_world.gd` on the game's `dev` branch (commit 1ec1417; colours only so far).
- Grey-zone maps keep the late-game escalation what-if hot zone, clearly marked fictional.
- Qalat outer walls need breaching charges, grenade launchers or vehicles to breach; small arms cannot.
- The LHD restrictions on gaza_west_bank, taiwan_strait and mexico_cartel_belt stay.
- Kashmir keeps generic militant NPCs; no new faction.
- alpine_europe keeps the generic arms-trafficker NPCs and gains Russian mountain troops (rus) as the hostile force, as a fictional what-if.
- The theatre gaps are answered by the new maps: iraqi_militias is not added to iran_zagros (iraq_iran_border covers it), isis is not added to south_china_sea (mindanao_sulu covers it), and chn and ind keep their UNIFIL entry on lebanon_south and now list lebanon_south in their files.

Answered by Captain (2026-10-10), applied in a Job 7 follow-up:

- m23 stays a hostile non-client (relation -50 with the player, never hires or sells, like the cartels; not attacked by default during ceasefire phases). Recorded in eastern_congo's `captain_confirmed`.
- chn stays on eastern_congo as the what-if returning MONUSCO engineer and medical unit, clearly marked fictional. Recorded in eastern_congo's `captain_confirmed`.

Answered by Captain (2026-10-10), applied in Job 9 (final validation):

- The low-plausibility listings stay at low strength: blr in eastern_ukraine and baltic_coast; fra, bel and esp in sahel; jpn in arctic_north and korean_dmz; chn in korean_dmz and kashmir_loc; are in yemen_red_sea; usa in mexico_cartel_belt. rus stays on alpine_europe as a fictional what-if (its strength, medium, is unchanged and stays proposed). Each is recorded in that worldspace's `captain_confirmed` list and moved out of `proposed`, and in [worldspaces/README.md](../worldspaces/README.md).

No worldspace question is open.
