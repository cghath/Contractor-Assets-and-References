# Neutrals, Africa, Central Asia, cartels and rival PMCs (`others`): handoff sheet

Snapshot as of 2026-10-10 09:30 UTC. Branch `factions-worldspaces` (draft PR #2). This is job 3 of 5, run one job at a time:

1. middle_east_states
2. me_terror
3. **others**
4. alliances
5. worldspaces

Game rules and pack-wide decisions are in [factions_handoff.md](factions_handoff.md).

## Why this bloc matters

It's a mixed bag that fills the gaps the other blocs leave:

- **Neutral states** (che, aut, irl): arms markets, neutral contract sources, staging areas and UN peacekeepers.
- **Mexico and two fictional cartels:** the `mexico_cartel_belt` theatre.
- **De facto and local forces** (afg_taliban, sdf, krg_peshmerga, sahel_aes, som): these complicate early-game theatres. Each one is a client in one place and a target in another.
- **Three fictional rival PMCs:** the player's **recurring rivals**. They bid on the same contracts, show up as enemies, and act as bounty hunters.

## Read first, in this order

1. This sheet.
2. `CONTEXT` and `FACTION_SPEC` in [tools/factions_workflow.js](../tools/factions_workflow.js). Wherever they say `${REPO}`, use `B:\Contractor-Vehicle-Models`. Also read the `others` entry in `BLOCS`.
3. [factions_handoff.md](factions_handoff.md), for the settled rules.
4. `factions/player.json` (the PMC model your rival PMCs mirror), `factions/africa_corps.json` (the Russian state PMC, which is a rival contractor), and `factions/usa.json` and `factions/rus.json` for depth and style.
5. The Middle East states and terror files once they land. Relations with irn, tur, syr, irq, hamas, isis, isis_k, al_shabaab and jnim must agree.
6. [worldspaces_handoff.md](worldspaces_handoff.md), for theatres and engine facts.

## What to build

Fourteen files, `factions/<id>.json`, plus catalogue files for new vehicles. The shapes are exactly as in `FACTION_SPEC`.

## Rules for this bloc

- **Real versus fictional:**
  - che, aut, irl, mex, afg_taliban, sdf, krg_peshmerga, sahel_aes and som are real, and use real names.
  - `cartel_pacifico`, `cartel_jalisco_nueva`, `pmc_halcyon`, `pmc_kestrel` and `pmc_black_sable` are **fictional**. Give each an `inspired_by` description. Don't use real cartel names, leaders, or real company names or logos.
- **Kinds:**
  - `state` for che, aut, irl, mex and som.
  - `non_state` for afg_taliban (the de facto government, recognised by few states; say so neutrally), sdf, krg_peshmerga (the regional government's forces, so `state` is also defensible; pick one and note why) and sahel_aes (a confederation of juntas; `state` is acceptable).
  - `criminal` for the cartels and `pmc` for the PMCs.
- **Player client:**
  - The neutral states and Mexico can hire the player.
  - The SDF, Peshmerga, Somalia and sahel_aes can hire the player. sahel_aes works with africa_corps, so expect few contracts or harsh terms; record this as a proposal.
  - afg_taliban is a case for Captain. The default is `player_client: false` and neutral-to-hostile, as an open question.
  - The cartels are hostile and never hire the player.
  - Rival PMCs are hostile and never hire the player, but they appear as `rival_pmc` and bounty hunters.
- **Selling:** che and aut can sell to the player as arms markets, with rep tiers. Record this as a proposal and keep it neutral. The others don't sell, except possibly the Peshmerga for basic kit (a proposal).
- **Tone:** factual and neutral. Cartel violence and tactics stay at game level: roadblocks, armored "monster" trucks, drones, ambushes. No real operational detail.

## Roster: baseline facts to verify and expand

Verify each item on the web (2026 status).

| id | Kind | Theatres | Known for (verify) | Suggested vehicles (check the catalogue first) |
|---|---|---|---|---|
| che | state | alpine_europe | The Swiss Armed Forces: militia army and armed neutrality. Piranha (Radschützenpanzer), CV90 (Spz 2000), Leopard 2 (Pz 87), Eagle, M109, Duro trucks. | piranha, cv90, leopard2a6, eagle, m109 |
| aut | state | alpine_europe | Austrian Bundesheer. Pandur Evolution, Ulan (ASCOD), Leopard 2A4, Dingo, Black Hawk (UH-60M). Neutral and EU. | pandur_ii, ascod_ulan (new), leopard2a6, dingo, uh60 |
| irl | state | lebanon_south (UNIFIL) | Irish Defence Forces. Mowag Piranha III, RG-32M, Javelin. A long-serving UN peacekeeper. | piranha, rg32m (new) |
| mex | state | mexico_cartel_belt | SEDENA and Guardia Nacional. Humvee, Sandcat, Oshkosh SandCat-type armored trucks, DN-XI, Black Hawk, Mi-17. The cartel war. | humvee, sandcat, uh60, mi8, dnxi (new) |
| cartel_pacifico | criminal (fictional) | mexico_cartel_belt | Inspired by a Pacific-coast trafficking federation (no real name). Armored pickups and SUVs, .50-cal rifles, FPV drones, roadblocks. | toyota_hilux, narco_truck (new, a home-armored "monster" truck), fpv_drone, armored_suv (new) |
| cartel_jalisco_nueva | criminal (fictional) | mexico_cartel_belt | Inspired by a fast-expanding, paramilitary-style western Mexican cartel. Uniformed cells, armored trucks, drone bombs, mines as a map hazard. | narco_truck, toyota_hilux, armored_suv, fpv_drone |
| afg_taliban | non_state (de facto government) | afghan_highlands | The Islamic Emirate's forces, including former US-supplied Humvees, Ford Rangers, M1117s, MaxxPros and some Mi-17s. Fights ISIS-K. Border clashes with Pakistan in 2025. | humvee, ford_ranger (new, or a toyota_hilux variant), m1117, maxxpro, mi8, toyota_land_cruiser |
| sdf | non_state | levant_syria, mesopotamia | Syrian Democratic Forces (YPG-led). US-backed against IS, and guards the IS detention camps. Check the 2025 integration agreement with Damascus and its 2026 status. Humvees, up-armored local trucks, technicals. | humvee, technical_dshk, toyota_hilux, m1117 |
| krg_peshmerga | non_state or state | mesopotamia, iran_zagros (border) | Kurdistan Region Peshmerga, split between the KDP and PUK. Humvees, MRAPs (Cougar, MaxxPro), Dingo, MILAN; German- and US-supplied. | humvee, dingo, cougar, maxxpro, technical_dshk |
| sahel_aes | state (confederation) | sahel | The Alliance of Sahel States (Mali, Burkina Faso, Niger) military juntas. Works with africa_corps. Bayraktar TB2 and Akinci drones, BTR, technicals, pickups. | bayraktar_tb2, btr60, toyota_land_cruiser, technical_zpu, vbl, mi24 |
| som | state | horn_of_africa | Somali National Army, including the Turkish-trained Gorgor and the US-trained Danab. Technicals, Kirpi, Turkish TB2 support, alongside AU forces (AUSSOM). | technical_zu23, technical_dshk, kirpi, toyota_land_cruiser, bayraktar_tb2 |
| pmc_halcyon | pmc (fictional) | many: mesopotamia, persian_gulf_coast, horn_of_africa, yemen_red_sea | Proposal: a **Western** private military company, inspired by large US and UK security contractors. Well equipped: M4-pattern rifles, MRAPs, Land Cruisers, a contracted helicopter. | toyota_land_cruiser, maxxpro, matv, bell412, polaris_mrzr |
| pmc_kestrel | pmc (fictional) | eastern_ukraine, sahel, levant_syria, caucasus | Proposal: an **Eastern European, Russia-linked** contractor, distinct from the state-run africa_corps. AK-12/AK-74M rifles, Tigr, BTR, Mi-8. | gaz_tigr, btr82a, mi8, toyota_hilux |
| pmc_black_sable | pmc (fictional) | yemen_red_sea, horn_of_africa, persian_gulf_coast, sahel | Proposal: a **Gulf-funded** contractor recruiting internationally, inspired by Gulf-financed mercenary forces. Nimr, Land Cruisers, Wing Loong drones. | nimr, toyota_land_cruiser, wing_loong, technical_dshk |

### Catalogue notes

Existing ids to reuse include `piranha`, `cv90`, `leopard2a6`, `eagle`, `m109`, `pandur_ii`, `dingo`, `uh60`, `humvee`, `sandcat`, `mi8`, `m1117`, `maxxpro`, `cougar`, `bayraktar_tb2`, `btr60`, `vbl`, `mi24`, `kirpi`, `nimr`, `wing_loong`, `bell412`, `polaris_mrzr`, `gaz_tigr`, `btr82a` and `matv`.

New ids are likely to be: `ascod_ulan`, `rg32m`, `dnxi`, `narco_truck`, `armored_suv` and `ford_ranger`. Before creating any of them, check whether `motorcycle`, `fast_boat` or a technical variant from the terror job already covers it.

The fictional vehicles (`narco_truck`, `armored_suv`) are inspired-by types. Give them `origin: "improvised"` and describe the real-world type, not a specific photo.

## What makes each field useful (aim for this depth)

- **Neutral states:**
  - `contract_types.as_client`: escort UN or NGO convoys, protect peacekeepers, evacuate nationals, recover stolen arms.
  - `player_trade`: for che and aut as arms markets.
  - `relations`: mostly neutral, mildly positive toward the EU and UN contributors.
- **Cartels:**
  - `unit_templates`: a sicario cell, a roadblock (halcon lookouts plus an armored truck), a plaza defence, a drone team (as a hazard), a convoy escort.
  - `contract_types.as_target`: lab raid, HVT capture, hostage rescue, convoy interdiction.
  - The two cartels are hostile to each other (around -70 or below) and to `mex` and `usa`.
- **Rival PMCs:** these need the richest `doctrine` and `unit_templates` in the bloc.
  - Give them player-like 8-person squads, battle-buddy pairs and real kit, with medium-to-heavy armor.
  - Add a `rivalry` object: which contracts they bid on, when they show up as bounty hunters, and what beating them gives the player. Mark the whole object `proposed`.
- **Local forces** (sdf, krg_peshmerga, som, sahel_aes, afg_taliban):
  - Give realistic doctrine, kit and relations.
  - Show who they're fighting in 2026: the Taliban against ISIS-K, the SDF and Peshmerga against IS remnants, Somalia against al-Shabaab, the AES against JNIM and IS-Sahel.
- **All factions:** `notes` with a neutral 2026 status, and `sources`.

## Checks before handing back

1. Run the validator (CI uses Python; Captain's desktop uses the Perl port in the session scratchpad) and fix every ERROR in your files.
2. Every vehicle referenced has a catalogue file, and your faction ids are in each file's `operators`.
3. Every fictional faction has `inspired_by` and no real cartel or company names.
4. Relations agree in sign with the Middle East states and terror files already written. Report mismatches; reconciling them is the alliances job.
5. Don't run git. The auto-save loop pushes every 10 minutes when the validator passes.
6. Update the Status section of `docs/factions_handoff.md`.

## Open questions for Captain

- Can the Taliban ever hire the player? The default is no: it's neutral-to-hostile and an anti-ISIS-K target-of-opportunity faction.
- Should Switzerland and Austria act as arms markets for the player, and at what reputation?
- Which rival PMC is the main nemesis? The default proposal is `pmc_halcyon`, since it mirrors the player most closely.
- Should sahel_aes hire a Western PMC while partnered with africa_corps? The default is rarely, at harsh terms.
