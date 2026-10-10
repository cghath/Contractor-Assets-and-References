# Middle East terrorist bloc (`me_terror`): handoff sheet

Snapshot as of 2026-10-10 09:30 UTC. Branch `factions-worldspaces` (draft PR #2). This is job 2 of 5, run one job at a time:

1. middle_east_states (running)
2. **me_terror**
3. others
4. alliances
5. worldspaces

Game rules and pack-wide decisions are in [factions_handoff.md](factions_handoff.md).

## Why this bloc matters

Captain asked for a Middle East terrorist bloc "like Hamas and al-Qaeda". The **early game sees a lot of fighting against these groups**, so they're the player's most common enemies in the first hours. In practice that means the following:

- **Unit templates come first.** They need to be rich and varied, because players will fight these units most.
- **Vehicles are early-game models.** Technicals, pickups, motorbikes and captured army kit are the first voxel models to build. Six `technical_*` models already exist.
- **Tuning should create a ramp.** Small-cell groups (Hamas, PIJ, AQAP and al-Shabaab cells) start easier, and the better-equipped groups (Hezbollah, the Houthis and Iraqi militias) come later.

## Read first, in this order

1. This sheet.
2. `CONTEXT` and `FACTION_SPEC` in [tools/factions_workflow.js](../tools/factions_workflow.js). Wherever they say `${REPO}`, use `B:\Contractor-Vehicle-Models`. Also read the `me_terror` entry in `BLOCS`.
3. [factions_handoff.md](factions_handoff.md): the settled rules on armor, launchers, civilians, contract zones and hot zones.
4. `factions/rus.json` and `factions/usa.json` as depth and style examples, and `reference/vehicles/technical_dshk.json` and `reference/vehicles/t72b3.json` as catalogue examples.
5. The Middle East states files once they land (`factions/irn.json`, `isr.json`, `syr.json`, `irq.json`, `sau.json`, `are.json` and so on). Their relations toward the terror groups must agree with yours.
6. [worldspaces_handoff.md](worldspaces_handoff.md), for which theatres exist and what the game engine can do.

## What to build

Eleven files, `factions/<id>.json`, one per faction, plus catalogue files for any new vehicles. The shapes are exactly as in `FACTION_SPEC`.

## Hard rules for this bloc (the validator enforces some of them)

- **Hostile only:**
  - `alignment_to_player`: `"hostile"`
  - `player_client`: `false`
  - `player_trade.sellable`: `false` with an empty `rep_tiers`
  - `relations.player` between -100 and -80
- **Content:**
  - Use the real organisation names. Be strictly factual, neutral and non-glorifying.
  - No slogans, no propaganda imagery, and no flags beyond neutral colour hexes.
  - **Tactics stay at game-design level only.** Write "IED as a map hazard", "tunnel network as level geometry", "drone-dropped munition as an AI ability", "ambush from a wadi". Never include real construction, sourcing or operational how-to.
- **Kind and tier:**
  - `kind`: `"non_state"`.
  - `campaign_tier`: `"early"` for most groups. Hezbollah, the Houthis and iraqi_militias may be `"mid"`.
- **Gear** is terrorist-style:
  - AK-pattern rifles (AKM, Type 56, AK-47), PKM, RPK, SVD and RPG-7 (PG-7V and OG-7V are in the game), and the DShK on technicals.
  - Some captured Western rifles (M16, M4) where that's real.
  - Body armor is mostly `none` or `light`, sometimes captured plates. Helmets are rare.
- **Launchers:** flag the ones in the game list (RPG-7 above all). Mention the ATGMs the better-equipped groups use, such as Kornet, Konkurs and Iranian copies like the Dehlavieh. These act as AI threats only; they aren't player launchers.
- **Relations:**
  - Factual 2026 alignments: affiliates of the same network are positive, and rival networks are strongly negative. For example, al-Qaeda and IS fight each other, and ISIS-K fights the Taliban.
  - Include `player` and the states that fight each group.
  - Link the affiliates as the spec asks: aqap, al_shabaab and jnim to al_qaeda; isis_k to isis.

## Roster: baseline facts to verify and expand

Verify each item on the web (2026 status). Everything here is a starting point, not a source.

| id | Name to use | Theatres | Known for (verify) | Suggested vehicles (catalogue ids) |
|---|---|---|---|---|
| hamas | Hamas (Izz ad-Din al-Qassam Brigades) | gaza_west_bank, israel | Urban and tunnel warfare in dense terrain, short-range rockets, locally made RPG-type launchers, small drones dropping munitions, motorbikes and pickups. Check its status after the October 2025 ceasefire. | toyota_hilux, toyota_land_cruiser, technical_dshk, motorcycle (new), fpv_drone |
| pij | Palestinian Islamic Jihad (al-Quds Brigades) | gaza_west_bank | Smaller than Hamas. Rocket units in Gaza; active in the northern West Bank (refugee-camp cells). | toyota_hilux, motorcycle |
| hezbollah | Hezbollah | lebanon_south, israel, levant_syria | ATGM teams, rockets and drones, and the Radwan force. Heavily degraded in 2024 and lost its Syrian supply route when Assad fell. It once paraded T-55s, M113s, BMP-1s and ZSU-57-2s. | toyota_hilux, technical_zu23, technical_rockets, t55, m113, bmp1, shahed136 (or a smaller Iranian-type drone) |
| houthis | Houthis (Ansar Allah) | yemen_red_sea | Hold north Yemen and Sanaa. Ex-Yemeni army armour (T-55, T-62, T-72, BMP), technicals, Iranian-designed drones and missiles, explosive boats and Red Sea shipping attacks. | technical_zu23, technical_dshk, toyota_land_cruiser, t55, bmp2, shahed136, fast_boat (new) |
| iraqi_militias | Iran-aligned Iraqi militias (Kata'ib Hezbollah, Harakat al-Nujaba and others). Note their partial integration into the state PMF. | mesopotamia, levant_syria | Drones and rocket attacks on US bases, PMF-issued Humvees and some captured US kit, Safir jeeps, pickups. | humvee, toyota_land_cruiser, safir_jeep, technical_dshk, technical_rockets, m113 |
| al_qaeda | al-Qaeda (core network) | afghan_highlands, levant_syria | A dispersed core leadership network. Hurras al-Din in Syria announced its dissolution in 2025, and HTS (formerly al-Qaeda-linked) is now the Syrian government, so don't put HTS here. Small cells and training camps. | toyota_hilux, toyota_land_cruiser, motorcycle |
| aqap | al-Qaeda in the Arabian Peninsula | yemen_red_sea | Southern and central Yemen (Shabwa, Abyan, al-Bayda, Marib). Desert raids, IEDs as a hazard, drones. | toyota_hilux, technical_dshk, motorcycle |
| isis | Islamic State (Iraq and Syria core) | mesopotamia, levant_syria, sahel | Desert insurgent cells and night raids. The detention camps in NE Syria are a flashpoint. Its Sahel Province overlaps the sahel theatre. In 2014-17 it fielded captured Humvees, M1117s, T-55s and SVBIEDs; SVBIEDs should appear only as a game hazard. | toyota_hilux, technical_dshk, technical_zpu, humvee, m1117, t55, motorcycle |
| isis_k | Islamic State Khorasan Province | afghan_highlands | Fights the Taliban. Mountain and urban cells; mass-casualty attacks belong only in briefing text. | toyota_hilux, toyota_land_cruiser, motorcycle, humvee (captured) |
| al_shabaab | al-Shabaab | horn_of_africa | Controls rural southern and central Somalia. Ambushes on AU and Somali forces, technicals, VBIED hazards. Affiliate of al-Qaeda. | technical_zu23, technical_dshk, technical_spg9, toyota_land_cruiser |
| jnim | JNIM (Jama'at Nusrat al-Islam wal-Muslimin) | sahel | The al-Qaeda Sahel affiliate. Motorbike swarms, pickups, captured Malian and Burkinabe army kit, and the 2025 fuel blockades around Bamako. | motorcycle, toyota_hilux, technical_dshk, technical_zpu |

### Catalogue gaps to fill in this job

Check `reference/vehicles/` first. As of this snapshot these are missing:

- `technical_m40`, `technical_rockets` and `technical_zpu`. These are **existing voxel models with no catalogue file**. Write them with `existing_model` set to their model id, `model_priority: "high"`, and the operators list.
- `motorcycle`: a generic 125-200 cc motorbike of the Honda CG / Chinese-copy type. Operators are most of this bloc, plus the Sahel and Afghan groups.
- `fast_boat`: a fibreglass skiff or explosive-boat hull for the Houthis. Its mention of explosive boats stays at game-hazard level.
- Reuse what exists rather than duplicating it: `toyota_hilux`, `toyota_land_cruiser`, `technical_dshk`, `technical_zu23`, `technical_spg9`, `t55`, `bmp1`, `bmp2`, `m113`, `humvee`, `m1117`, `safir_jeep`, `shahed136` and `fpv_drone` already have files.

## What makes each field useful (aim for this depth)

- **`unit_templates`** are the most important field in this bloc. Give 5-8 per group, each with a composition and a vehicle. Examples:
  - a 4-6 person cell
  - an ambush team (RPG, PKM and riflemen)
  - a technical crew (driver, gunner and 2 riflemen on the technical)
  - a motorbike raid pair
  - a drone team, where the drone is an AI hazard ability
  - an IED hazard team that appears as a map hazard, not as a how-to
  - an HVT guard detail (the leader plus a 4-6 person guard)
  - an urban defence squad for a held compound
- **`doctrine.ai_tuning`:**
  - Cells get lower discipline, medical care and night capability, and variable morale.
  - Hezbollah and the Houthis rate higher on discipline and suppression resistance.
  - All numbers go in `proposed`.
- **`doctrine.tactics`:** 5-8 game-level behaviours. Examples: shoot-and-scoot from technicals, fall back into civilian areas (this makes the casualty penalty a real constraint for the player), ambush at chokepoints, tunnel or rooftop movement, drone spotting.
- **`camo`:** usually civilian clothing plus mixed ex-army camo (woodland, desert DPM, Syrian and Iraqi patterns, Yemeni woodland). Give real palettes. Don't include insignia artwork.
- **`support_assets`:** what the group can bring as game events: mortars, rocket salvo, FPV or Shahed-type drone hazard, VBIED hazard, sniper overwatch.
- **`contract_types`:** `as_client` must be `[]`. `as_target` is where the content goes: HVT capture or kill, cache raid, hostage rescue, convoy ambush defence, cell clear-out, drone-team hunt, tunnel-entrance demolition, IED-route clearance.
- **`notes`:** a short factual background and its 2026 status. **`sources`:** Wikipedia and reputable references for each group.

## Checks before handing back

1. Run the validator. CI runs `python3 tools/validate_pack.py`. On Captain's desktop there's no Python, so run the Perl port in the session scratchpad. Fix every ERROR in your files. Warnings about missing others-bloc or worldspace files are expected.
2. Every vehicle referenced has a catalogue file, and your faction ids are in each file's `operators`.
3. Each terror faction has `player_client: false`, `sellable: false` and hostility to `player`.
4. Relations with the Middle East states agree in sign with the state files. Report any mismatch, and don't edit the state files. Reconciling relations is the alliances job.
5. Don't run git. The auto-save loop commits and pushes to `factions-worldspaces` every 10 minutes when the validator passes.
6. Update the Status section of `docs/factions_handoff.md`.

## Open questions for Captain

- Should `isis` cover IS's Sahel and West Africa provinces too, or should they stay inside `sahel` worldspace text only? The default is to cover them in `isis`.
- Hamas after the 2025 ceasefire: set it as a mid-strength early-game enemy in `gaza_west_bank`. The default is yes, with tunnels as level geometry.
- Should captured MRAPs and Humvees appear as enemy vehicles (an ISIS/Taliban look)? The default is yes, as rare.
