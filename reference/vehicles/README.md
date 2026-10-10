# Vehicle catalogue

The shared real-vehicle catalogue of the Contractor faction pack: 211 vehicles, one `reference/vehicles/<id>.json` per vehicle or vehicle family, as of October 2026. Faction files (`factions/<id>.json`, `vehicles[].vehicle_id` and `unit_templates[].vehicle_id`) point at these ids, and the loadouts generator reads each vehicle's `type` to decide which factions get `crew` and `pilot` roles.

- **Real-world facts, game notes marked.** Operators, armament, dimensions and service status are real-world (October 2026). `protection` adds how the vehicle sits under the game's armor rule (small calibre cannot hurt vehicles; 7.62x54R and up can disable or penetrate light ones; launchers penetrate).
- **Photos are linked, not stored.** The cloud build container can read web text but cannot download images (image hosts are blocked), so each file links its photo pages in `reference_pages` (Wikipedia articles and Wikimedia Commons categories). For exact matching Captain can drop photos into a local folder, as was done for the UH-60.
- **Operators are the game assignment.** `operators` lists the roster factions that really field the vehicle. For the existing voxel models (AH-1Z, MaxxPro, M-ATV, Bradley, Abrams) Captain confirmed on 2026-10-10 that their real operators field them in game, so their `operators` lists are the game assignment; captured vehicles appear only as rare set pieces where a faction file says so. Fictional factions (the rival PMCs, the cartels) are listed where their files field the type.
- Validate with `python3 -I tools/validate_pack.py` from the repo root: every `vehicle_id` a faction uses must have a file here, each file's `id` must match its filename, and every operator must be a canonical faction id.

## Schema

The shape is the catalogue part of `FACTION_SPEC` in [../../tools/factions_workflow.js](../../tools/factions_workflow.js):

| Field | Holds |
|---|---|
| `id` | lowercase family designation, same as the filename (`t72b3`, `bmp2`, `leopard2a6`); existing voxel models use the model id (`abrams`, `bradley`, `uh60`, `ah1z`, `aav7`, `maxxpro`, `matv`, `technical_*`) |
| `name`, `aliases` | display name and other designations, export names and nicknames |
| `origin` | country (or countries) of origin; `improvised` for inspired-by types such as `narco_truck` |
| `type` | one of `mbt`, `ifv`, `apc`, `mrap`, `light`, `technical`, `truck`, `artillery`, `mlrs`, `air_defense`, `attack_heli`, `transport_heli`, `uav`, `boat`, `other` (the faction `vehicles[].role` values) |
| `operators` | canonical faction ids that field it (see above) |
| `crew`, `passengers`, `dimensions_m`, `weight_t` | size and capacity |
| `armament`, `protection` | weapons, real-world protection and the game armor-rule note |
| `visual_notes`, `colour_schemes` | what a voxel modeller needs: hull and turret shape, wheels or road wheels, ERA, slat and cope cages, hatches, optics, stowage; palettes as hex colours |
| `variants` | variants and national versions of the same family (variants go here, not in new files) |
| `existing_model` | the voxel model id if one exists in the game, else `null` |
| `model_priority` | `high` (signature vehicle of an early-game or major faction), `medium` or `low` |
| `reference_pages`, `sources` | photo pages and cited sources |

## Counts

211 vehicles: 38 high, 63 medium and 110 low priority. 13 have an existing voxel model.

| Type | Vehicles | High | Medium | Low |
|---|---|---|---|---|
| mbt | 32 | 8 | 9 | 15 |
| ifv | 27 | 7 | 9 | 11 |
| apc | 35 | 6 | 9 | 20 |
| mrap | 14 | 2 | 5 | 7 |
| light | 33 | 4 | 13 | 16 |
| technical | 6 | 5 | 1 | 0 |
| artillery | 16 | 0 | 2 | 14 |
| mlrs | 11 | 1 | 1 | 9 |
| air_defense | 2 | 0 | 0 | 2 |
| attack_heli | 11 | 1 | 5 | 5 |
| transport_heli | 10 | 3 | 3 | 4 |
| uav | 9 | 1 | 2 | 6 |
| boat | 2 | 0 | 2 | 0 |
| other | 3 | 0 | 2 | 1 |
| **total** | **211** | **38** | **63** | **110** |

## Existing voxel models

These vehicles already have a voxel model in the game:

| id | Name | Type | Operators |
|---|---|---|---|
| `uh60` | Sikorsky UH-60 Black Hawk | transport_heli | swe, grc, nor, usa, aus, lva, ltu, jpn, kor, twn, phl, isr, tur, sau, are, jor, aut, mex, afg_taliban |
| `ah1z` | AH-1Z Viper | attack_heli | usa, twn, jpn, pak, irn |
| `aav7` | AAV-7A1 | apc | ita, esp, usa, jpn, kor, phl |
| `maxxpro` | International MaxxPro | mrap | usa, ukr, irq, pak, are, afg_taliban, krg_peshmerga, jor, sdf, pmc_halcyon |
| `matv` | Oshkosh M-ATV | mrap | usa, are, ukr, afg_taliban, sau, pol, pmc_halcyon, pmc_black_sable |
| `bradley` | M2 Bradley | ifv | usa, ukr, sau |
| `abrams` | M1 Abrams | mbt | usa, aus, pol, ukr, egy, sau, irq, twn, rou |
| `technical_dshk` | Toyota Hilux technical with DShK | technical | isis, al_shabaab, houthis, afg_taliban, jnim, aqap, al_qaeda, iraqi_militias, sdf, krg_peshmerga, som, syr, africa_corps, irn, hamas, isis_k, sahel_aes, pmc_kestrel, pmc_black_sable, cod |
| `technical_m40` | Pickup technical with M40 106 mm recoilless rifle | technical | al_shabaab, som |
| `technical_rockets` | Pickup technical with Type 63 107 mm rocket launcher | mlrs | hezbollah, iraqi_militias |
| `technical_spg9` | Toyota technical with SPG-9 | technical | syr, houthis, aqap, al_shabaab |
| `technical_zpu` | Pickup technical with ZPU 14.5 mm anti-aircraft gun | technical | isis, jnim, al_shabaab |
| `technical_zu23` | Toyota technical with ZU-23-2 | technical | syr, hezbollah, houthis, isis, al_shabaab, sdf, sahel_aes, som, m23 |

The technical models are the Toyota Hilux and Land Cruiser 79 gun trucks; `toyota_hilux` itself (unarmed) has no model yet.

## Next models to build

High priority and no model yet (26), early game first: sorted by how many early-tier factions field them, then by operator count.

| # | id | Name | Type | Early-tier operators | Operators |
|---|---|---|---|---|---|
| 1 | `toyota_hilux` | Toyota Hilux pickup (unarmed) | light | 18 | 23 |
| 2 | `motorcycle` | Light motorcycle (125-200 cc Honda CG type) | light | 13 | 15 |
| 3 | `fpv_drone` | FPV strike drone (family) | uav | 10 | 16 |
| 4 | `m113` | M113 | apc | 9 | 17 |
| 5 | `mi8` | Mil Mi-8 / Mi-17 family | transport_heli | 6 | 18 |
| 6 | `ah64` | AH-64 Apache | attack_heli | 6 | 14 |
| 7 | `ch47` | Boeing CH-47 Chinook | transport_heli | 6 | 10 |
| 8 | `leopard2a6` | Leopard 2A6 | mbt | 4 | 16 |
| 9 | `bmp1` | BMP-1 | ifv | 4 | 12 |
| 10 | `leclerc` | Leclerc | mbt | 3 | 3 |
| 11 | `t72b3` | T-72B3 / T-72 family | mbt | 2 | 14 |
| 12 | `jltv` | Joint Light Tactical Vehicle | light | 2 | 8 |
| 13 | `boxer` | Boxer | apc | 2 | 6 |
| 14 | `vbci` | VBCI | ifv | 2 | 2 |
| 15 | `t90m` | T-90M Proryv | mbt | 1 | 5 |
| 16 | `bmp3` | BMP-3 | ifv | 1 | 4 |
| 17 | `t64bv` | T-64BV | mbt | 1 | 3 |
| 18 | `griffon` | VBMR Griffon | apc | 1 | 2 |
| 19 | `stryker` | Stryker | apc | 1 | 2 |
| 20 | `bmp2` | BMP-2 | ifv | 0 | 11 |
| 21 | `cv90` | CV90 | ifv | 0 | 9 |
| 22 | `btr82a` | BTR-82A / BTR-80 family | apc | 0 | 8 |
| 23 | `gaz_tigr` | GAZ Tigr | light | 0 | 5 |
| 24 | `merkava4` | Merkava Mk 4 / 4M / Barak | mbt | 0 | 1 |
| 25 | `type99a` | ZTZ-99A (Type 99A) | mbt | 0 | 1 |
| 26 | `zbd04a` | ZBD-04A | ifv | 0 | 1 |

`toyota_hilux`, `motorcycle` and `fpv_drone` matter most for the early game: the terror groups and the other early-tier factions drive Hiluxes and motorbikes and fly FPV drones in almost every early theatre. The M113 and the Mi-8/Mi-17 family come next, followed by the BMP and T-72 families, whose ex-army and captured examples turn up with many early enemies.

## Duplicate review (Job 9, 2026-10-10)

All 211 files were compared by id, name, aliases and variants for the same vehicle or family filed under two ids. No true duplicate was found, so no file was merged and no reference changed: the catalogue already keeps each family in one file, and earlier jobs put later finds in as variants (Ulan into `pizarro`, DN-XI into `sandcat`, Pandur Evolution into `pandur_ii`, Super Puma into `sa330`, the older Cobras into `ah1z`, BMD-2 into `bmd1`, BTR-80 into `btr82a`, Mi-17 into `mi8`), and `ford_ranger` is separate from `toyota_hilux` by Captain's decision. Separate models in service that share a chassis or family stay separate (for example `bmp1`/`bmp2`/`bmp3`, `t72b3`/`t90m`/`pt91`/`m84`, `lav6`/`stryker`/`piranha`, `aw129`/`t129`, `sisu_pasi`/`patria_6x6`, `btr60`/`tab71`, `pizarro`/`ajax`).

Possible duplicates, kept separate by Captain's decision (2026-10-10):

- `type59` and `t55`: the Type 59 is the Chinese licence-built T-54A, so an unmodified Type 59 looks like a T-54; but it is a separate production model in service (pak, vnm, prk, cod), and the Al-Zarrar rebuild looks different. Merging would make `type59` a variant of `t55`.
- `armored_suv` and `toyota_land_cruiser`: both cover commercially armoured SUVs (the Land Cruiser file has the alias "armoured SUV"); `armored_suv` is the full-size Suburban-type cartel SUV, so they are different base vehicles.

Alias or name overlaps only (different vehicles): `bell412` (alias CH-146 Griffon) and `griffon` (VBMR Griffon); `stryker` (alias "LAV III family") and `lav6` (alias LAV III); `csk131` (alias Warrior) and `warrior`; `g_wagen` (alias Wolf) and `wolf_av`; `sa330` (Puma) and `puma_ifv`; `tapv` (Commando Elite) and `v150` (Commando); `ah1z` (Cobra) and `cobra` (Otokar Cobra).

## All vehicles

Sorted by priority, then id. "Ops" is the number of roster factions in `operators`.

| id | Name | Type | Origin | Priority | Existing model | Ops |
|---|---|---|---|---|---|---|
| `aav7` | AAV-7A1 | apc | United States | high | `aav7` | 6 |
| `abrams` | M1 Abrams | mbt | United States | high | `abrams` | 9 |
| `ah64` | AH-64 Apache | attack_heli | United States | high | - | 14 |
| `bmp1` | BMP-1 | ifv | Soviet Union | high | - | 12 |
| `bmp2` | BMP-2 | ifv | Soviet Union | high | - | 11 |
| `bmp3` | BMP-3 | ifv | Soviet Union / Russia | high | - | 4 |
| `boxer` | Boxer | apc | Germany/Netherlands | high | - | 6 |
| `bradley` | M2 Bradley | ifv | United States | high | `bradley` | 3 |
| `btr82a` | BTR-82A / BTR-80 family | apc | Russia | high | - | 8 |
| `ch47` | Boeing CH-47 Chinook | transport_heli | United States | high | - | 10 |
| `cv90` | CV90 | ifv | Sweden | high | - | 9 |
| `fpv_drone` | FPV strike drone (family) | uav | Ukraine and Russia (mass-produced by both sides from commercial components) | high | - | 16 |
| `gaz_tigr` | GAZ Tigr | light | Russia | high | - | 5 |
| `griffon` | VBMR Griffon | apc | France | high | - | 2 |
| `jltv` | Joint Light Tactical Vehicle | light | United States | high | - | 8 |
| `leclerc` | Leclerc | mbt | France | high | - | 3 |
| `leopard2a6` | Leopard 2A6 | mbt | Germany | high | - | 16 |
| `m113` | M113 | apc | United States | high | - | 17 |
| `matv` | Oshkosh M-ATV | mrap | United States | high | `matv` | 8 |
| `maxxpro` | International MaxxPro | mrap | United States | high | `maxxpro` | 10 |
| `merkava4` | Merkava Mk 4 / 4M / Barak | mbt | Israel | high | - | 1 |
| `mi8` | Mil Mi-8 / Mi-17 family | transport_heli | Soviet Union / Russia | high | - | 18 |
| `motorcycle` | Light motorcycle (125-200 cc Honda CG type) | light | Japan (design) / China, India and others (copies) | high | - | 15 |
| `stryker` | Stryker | apc | United States / Canada | high | - | 2 |
| `t64bv` | T-64BV | mbt | Soviet Union (modernised in Ukraine by the Kharkiv Armoured Plant) | high | - | 3 |
| `t72b3` | T-72B3 / T-72 family | mbt | Soviet Union / Russia | high | - | 14 |
| `t90m` | T-90M Proryv | mbt | Russia | high | - | 5 |
| `technical_dshk` | Toyota Hilux technical with DShK | technical | Japan (vehicle) / USSR (gun) | high | `technical_dshk` | 20 |
| `technical_m40` | Pickup technical with M40 106 mm recoilless rifle | technical | Japan (vehicle) / USA (gun) | high | `technical_m40` | 2 |
| `technical_rockets` | Pickup technical with Type 63 107 mm rocket launcher | mlrs | Japan (vehicle) / China (launcher) | high | `technical_rockets` | 2 |
| `technical_spg9` | Toyota technical with SPG-9 | technical | Japan / Soviet Union (weapon) | high | `technical_spg9` | 4 |
| `technical_zpu` | Pickup technical with ZPU 14.5 mm anti-aircraft gun | technical | Japan (vehicle) / USSR (gun) | high | `technical_zpu` | 3 |
| `technical_zu23` | Toyota technical with ZU-23-2 | technical | Japan / Soviet Union (weapon) | high | `technical_zu23` | 9 |
| `toyota_hilux` | Toyota Hilux pickup (unarmed) | light | Japan | high | - | 23 |
| `type99a` | ZTZ-99A (Type 99A) | mbt | China (Norinco) | high | - | 1 |
| `uh60` | Sikorsky UH-60 Black Hawk | transport_heli | United States | high | `uh60` | 19 |
| `vbci` | VBCI | ifv | France | high | - | 2 |
| `zbd04a` | ZBD-04A | ifv | China (Norinco) | high | - | 1 |
| `acv` | Amphibious Combat Vehicle | apc | United States / Italy | medium | - | 1 |
| `acv15` | FNSS ACV-15 (AIFV/AAPC) | ifv | Turkey (from US AIFV) | medium | - | 3 |
| `ah1z` | AH-1Z Viper | attack_heli | United States | medium | `ah1z` | 5 |
| `armored_suv` | Commercially armoured full-size SUV | light | improvised | medium | - | 3 |
| `bayraktar_tb2` | Bayraktar TB2 | uav | Turkey | medium | - | 4 |
| `bohdana` | 2S22 Bohdana | artillery | Ukraine (Kramatorsk Heavy Duty Machine Tool Plant) | medium | - | 2 |
| `boragh` | Boragh tracked APC | apc | Iran | medium | - | 1 |
| `bv206` | Bandvagn 206 | other | Sweden | medium | - | 7 |
| `caesar` | CAESAR | artillery | France | medium | - | 8 |
| `caterpillar_d9` | Caterpillar D9 armoured bulldozer (IDF) | other | United States (IDF armour kit, Israel) | medium | - | 1 |
| `centauro` | B1 Centauro | light | Italy | medium | - | 3 |
| `challenger2` | Challenger 2 | mbt | United Kingdom | medium | - | 3 |
| `chonma` | Chonma series (Chonma-ho / Pokpung-ho / Chonma-20) | mbt | North Korea | medium | - | 1 |
| `cm32` | CM-32 Clouded Leopard (Yunpao) | ifv | Taiwan (Ordnance Readiness Development Center) | medium | - | 1 |
| `cobra` | Otokar Cobra / Cobra II | light | Turkey | medium | - | 7 |
| `csk131` | Dongfeng Mengshi (CSK-131 / CSK-181) | light | China (Dongfeng) | medium | - | 1 |
| `eitan` | Eitan 8x8 APC | apc | Israel | medium | - | 1 |
| `ejder_yalcin` | Nurol Ejder Yalçın 4x4 | mrap | Turkey | medium | - | 3 |
| `fahd` | Fahd APC | apc | Egypt | medium | - | 1 |
| `fast_boat` | Fibreglass skiff / fast boat | boat | Various (local and Gulf builders) | medium | - | 2 |
| `ford_ranger` | Ford Ranger pickup (unarmed) | light | United States (T6 generation engineered by Ford Australia) | medium | - | 2 |
| `foxhound` | Foxhound (Ocelot) | mrap | United Kingdom | medium | - | 1 |
| `freccia` | VBM Freccia | ifv | Italy | medium | - | 1 |
| `himars` | M142 HIMARS | mlrs | United States | medium | - | 15 |
| `humvee` | HMMWV (Humvee) | light | United States (AM General) | medium | - | 20 |
| `iveco_lmv` | Iveco LMV | light | Italy | medium | - | 5 |
| `jackal` | Jackal (MWMIK) | light | United Kingdom | medium | - | 2 |
| `jaguar_ebrc` | EBRC Jaguar | light | France | medium | - | 2 |
| `k21` | K21 IFV | ifv | South Korea (Hanwha Aerospace) | medium | - | 1 |
| `k2_black_panther` | K2 Black Panther | mbt | South Korea (Hyundai Rotem) | medium | - | 2 |
| `ka52` | Kamov Ka-52 Alligator | attack_heli | Russia | medium | - | 2 |
| `karrar` | Karrar main battle tank | mbt | Iran | medium | - | 1 |
| `kirpi` | BMC Kirpi MRAP | mrap | Turkey | medium | - | 4 |
| `kozak2` | Kozak-2 | mrap | Ukraine (Praktika) | medium | - | 1 |
| `lav6` | LAV 6.0 | ifv | Canada | medium | - | 4 |
| `leopard1` | Leopard 1 | mbt | West Germany | medium | - | 3 |
| `m1117` | M1117 Guardian | apc | United States | medium | - | 5 |
| `marauder` | Paramount Marauder / Arlan | mrap | South Africa (licence production in Kazakhstan and Azerbaijan) | medium | - | 2 |
| `mi24` | Mil Mi-24 / Mi-35M Hind | attack_heli | Soviet Union / Russia | medium | - | 13 |
| `mtlb` | MT-LB | apc | Soviet Union | medium | - | 8 |
| `namer` | Namer heavy APC / IFV | apc | Israel | medium | - | 1 |
| `narco_truck` | Improvised armoured cartel truck ('monstruo') | technical | improvised | medium | - | 2 |
| `nh90` | NHIndustries NH90 | transport_heli | France/Germany/Italy/Netherlands | medium | - | 10 |
| `nimr` | NIMR Ajban / Hafeet / Jais | light | United Arab Emirates | medium | - | 5 |
| `piranha` | Mowag Piranha | apc | Switzerland | medium | - | 7 |
| `puma_ifv` | Puma (IFV) | ifv | Germany | medium | - | 1 |
| `safir_jeep` | Safir light jeep | light | Iran | medium | - | 3 |
| `shahed136` | Shahed-136 loitering munition | uav | Iran | medium | - | 5 |
| `t55` | T-54 / T-55 family | mbt | Soviet Union | medium | - | 10 |
| `t80bvm` | T-80BVM | mbt | Russia | medium | - | 2 |
| `tiger` | Eurocopter Tiger | attack_heli | France/Germany | medium | - | 4 |
| `toyota_land_cruiser` | Toyota Land Cruiser (70/200/300 series, unarmed or armoured SUV) | light | Japan | medium | - | 26 |
| `type10` | Type 10 (TK-X) | mbt | Japan (Mitsubishi Heavy Industries) | medium | - | 1 |
| `type16` | Type 16 Maneuver Combat Vehicle | ifv | Japan (Mitsubishi Heavy Industries) | medium | - | 1 |
| `v22` | Bell Boeing V-22 Osprey | transport_heli | United States | medium | - | 2 |
| `vbl` | Panhard VBL | light | France | medium | - | 3 |
| `wolf_av` | Wolf (Ze'ev) Armoured Vehicle | apc | Israel | medium | - | 3 |
| `z10` | CAIC Z-10 | attack_heli | China (CAIC) | medium | - | 2 |
| `z20` | Harbin Z-20 | transport_heli | China (Harbin) | medium | - | 1 |
| `zbd05` | ZBD-05 amphibious IFV | ifv | China (Norinco) | medium | - | 1 |
| `zbl08` | ZBL-08 (Type 08 family) | ifv | China (Norinco) | medium | - | 1 |
| `zolfaghar_fac` | IRGC Navy fast attack craft (Zolfaghar / Seraj / Tareq family) | boat | Iran | medium | - | 1 |
| `ztq15` | ZTQ-15 (Type 15) light tank | mbt | China (Norinco) | medium | - | 1 |
| `2s19` | 2S19 Msta-S | artillery | Russia | low | - | 2 |
| `ajax` | General Dynamics Ajax | ifv | United Kingdom / Spain-Austria (ASCOD) | low | - | 1 |
| `al_jawad` | JLVM Al-Jawad armoured security vehicle | light | Jordan | low | - | 1 |
| `al_khalid` | Al-Khalid (MBT-2000) | mbt | Pakistan / China (HIT, Norinco) | low | - | 1 |
| `altay` | Altay main battle tank | mbt | Turkey | low | - | 2 |
| `aras` | Aras / Aras-2 tactical vehicle | light | Iran | low | - | 1 |
| `archer` | Archer | artillery | Sweden | low | - | 3 |
| `ariete` | C1 Ariete | mbt | Italy | low | - | 1 |
| `arjun` | Arjun Mk1 / Mk1A | mbt | India (DRDO / HVF) | low | - | 1 |
| `arma` | Otokar Arma | apc | Turkey (Otokar) | low | - | 3 |
| `atags` | ATAGS 155 mm towed gun | artillery | India | low | - | 2 |
| `atmos` | ATMOS 2000 | artillery | Israel | low | - | 4 |
| `aw129` | Agusta A129 Mangusta | attack_heli | Italy | low | - | 1 |
| `bastion` | ACMAT Bastion | apc | France | low | - | 2 |
| `bell412` | Bell 412 / CH-146 Griffon | transport_heli | United States / Canada | low | - | 7 |
| `bmd1` | BMD-1 / BMD-2 | ifv | Soviet Union | low | - | 3 |
| `bmr` | Pegaso BMR-600 | apc | Spain | low | - | 1 |
| `borsuk` | Borsuk | ifv | Poland (Huta Stalowa Wola) | low | - | 1 |
| `btr60` | BTR-60 | apc | Soviet Union | low | - | 4 |
| `bushmaster` | Bushmaster PMV | mrap | Australia | low | - | 5 |
| `bvp_m80` | BVP M-80 | ifv | Yugoslavia / Serbia | low | - | 1 |
| `bvs10` | BvS10 Viking | apc | Sweden | low | - | 4 |
| `ch4` | CASC CH-4 Rainbow | uav | China | low | - | 1 |
| `cm11` | CM-11 Brave Tiger | mbt | Taiwan / United States | low | - | 1 |
| `cougar` | Cougar (Mastiff / Ridgback) | mrap | United States | low | - | 14 |
| `cvrt` | CVR(T) Scimitar / Spartan family | light | United Kingdom (Alvis) | low | - | 2 |
| `dana` | ShKH vz. 77 DANA | artillery | Czechoslovakia | low | - | 3 |
| `dardo` | VCC-80 Dardo | ifv | Italy | low | - | 1 |
| `dhruv` | HAL Dhruv / Rudra | transport_heli | India (HAL) | low | - | 1 |
| `didgori` | Didgori | mrap | Georgia (STC Delta) | low | - | 1 |
| `dingo` | ATF Dingo | mrap | Germany | low | - | 5 |
| `eagle` | Mowag Eagle | light | Switzerland | low | - | 3 |
| `fajr5` | Fajr-5 333 mm MLRS | mlrs | Iran | low | - | 1 |
| `fennek` | Fennek | light | Germany/Netherlands | low | - | 3 |
| `fuchs` | TPz Fuchs | apc | West Germany | low | - | 2 |
| `g6` | Denel G6 Rhino | artillery | South Africa | low | - | 1 |
| `g_wagen` | Mercedes-Benz G-Class (military) | light | Germany / Austria | low | - | 7 |
| `guarani` | VBTP-MR Guarani | apc | Brazil (IVECO) | low | - | 1 |
| `harop` | IAI Harop | uav | Israel | low | - | 1 |
| `hawkei` | Thales Hawkei | light | Australia | low | - | 1 |
| `hermes450` | Elbit Hermes 450 | uav | Israel | low | - | 3 |
| `iron_dome` | Iron Dome battery | air_defense | Israel | low | - | 2 |
| `k1` | K1 / K1A2 | mbt | South Korea (Hyundai Rotem) | low | - | 1 |
| `k200` | K200 KIFV | apc | South Korea (Hanwha/Doosan) | low | - | 1 |
| `k239` | K239 Chunmoo | mlrs | South Korea (Hanwha Aerospace) | low | - | 5 |
| `k808` | K806 / K808 White Tiger | apc | South Korea (Hyundai Rotem) | low | - | 1 |
| `k9` | K9 Thunder | artillery | South Korea | low | - | 10 |
| `kltv` | Kia Light Tactical Vehicle | light | South Korea (Kia) | low | - | 1 |
| `kn25` | KN-25 600 mm super-large MLRS | mlrs | North Korea | low | - | 1 |
| `koksan` | M1978 / M1989 Koksan 170 mm SPG | artillery | North Korea | low | - | 2 |
| `komatsu_lav` | Komatsu Light Armored Vehicle | light | Japan (Komatsu) | low | - | 1 |
| `krab` | AHS Krab | artillery | Poland (Huta Stalowa Wola; K9 chassis, AS-90-derived turret) | low | - | 2 |
| `lazar3` | Lazar 3 | apc | Serbia | low | - | 1 |
| `m109` | M109 | artillery | United States | low | - | 10 |
| `m2010` | M-2010 wheeled APC | apc | North Korea | low | - | 1 |
| `m270` | M270 MLRS | mlrs | United States | low | - | 5 |
| `m60` | M60 Patton | mbt | United States | low | - | 6 |
| `m777` | M777 howitzer | artillery | United Kingdom / United States | low | - | 6 |
| `m84` | M-84 | mbt | Yugoslavia / Serbia | low | - | 1 |
| `marder` | Marder 1 | ifv | West Germany | low | - | 4 |
| `md500` | MD 500 / Hughes 500 Defender | attack_heli | United States | low | - | 2 |
| `mi28` | Mil Mi-28 Havoc | attack_heli | Russia | low | - | 3 |
| `milos` | BOV M16 Milos | mrap | Serbia | low | - | 1 |
| `mli84` | MLI-84M Jderul | ifv | Romania (BMP-1 derivative) | low | - | 1 |
| `mohajer6` | Qods Mohajer-6 UAV | uav | Iran | low | - | 2 |
| `nora_b52` | Nora B-52 | artillery | Serbia | low | - | 2 |
| `orlan10` | Orlan-10 | uav | Russia | low | - | 4 |
| `pandur_ii` | Pandur II | ifv | Austria / Czech Republic (GDELS, Excalibur Army) | low | - | 2 |
| `pantsir` | Pantsir-S1 | air_defense | Russia | low | - | 4 |
| `patria_6x6` | Patria 6x6 | apc | Finland | low | - | 8 |
| `patria_amv` | Patria AMV | apc | Finland | low | - | 4 |
| `pcl181` | PCL-181 155 mm wheeled SPH | artillery | China (Norinco) | low | - | 2 |
| `phl16` | PHL-16 (PCH-191) modular MLRS | mlrs | China (Norinco) | low | - | 1 |
| `pinaka` | Pinaka MBRL | mlrs | India | low | - | 2 |
| `pinzgauer` | Pinzgauer | light | Austria | low | - | 4 |
| `pizarro` | ASCOD Pizarro | ifv | Spain/Austria | low | - | 4 |
| `polaris_mrzr` | Polaris MRZR | light | United States | low | - | 6 |
| `polonez` | Polonez | mlrs | Belarus | low | - | 2 |
| `prachand` | HAL Prachand (LCH) | attack_heli | India (HAL) | low | - | 1 |
| `pt76` | PT-76 | light | Soviet Union | low | - | 2 |
| `pt91` | PT-91 Twardy | mbt | Poland (Bumar-Łabędy, T-72M1 derivative) | low | - | 2 |
| `puls` | PULS | mlrs | Israel | low | - | 5 |
| `pzh2000` | Panzerhaubitze 2000 | artillery | Germany | low | - | 7 |
| `redback` | Hanwha AS21 Redback | ifv | South Korea / Australia | low | - | 1 |
| `rg32m` | BAE Systems RG-32M | light | South Africa | low | - | 1 |
| `rm70` | RM-70 | mlrs | Czechoslovakia | low | - | 3 |
| `sa330` | SA 330 Puma / IAR 330 | transport_heli | France (licence-built in Romania by IAR) | low | - | 3 |
| `sandcat` | Plasan SandCat | light | Israel | low | - | 3 |
| `serval` | VBMR-L Serval | apc | France | low | - | 2 |
| `simba` | GKN Simba | apc | United Kingdom (GKN), assembled in the Philippines | low | - | 1 |
| `sisu_pasi` | Sisu Pasi | apc | Finland | low | - | 4 |
| `surion` | KAI KUH-1 Surion | transport_heli | South Korea (KAI) | low | - | 1 |
| `t129` | TAI T129 ATAK | attack_heli | Turkey (AW129-derived) | low | - | 1 |
| `tab71` | TAB-71 / Romanian TAB family | apc | Romania (licence BTR-60PB/BTR-70/BTR-80 derivatives) | low | - | 3 |
| `tapv` | Textron TAPV | mrap | United States (for Canada) | low | - | 1 |
| `themis` | Milrem THeMIS | other | Estonia (Milrem Robotics) | low | - | 3 |
| `tr85` | TR-85M1 Bizonul | mbt | Romania | low | - | 1 |
| `type59` | Type 59 / Al-Zarrar | mbt | China (Norinco), Al-Zarrar upgrade by HIT Pakistan | low | - | 4 |
| `type90` | Type 90 | mbt | Japan (Mitsubishi Heavy Industries) | low | - | 1 |
| `type96` | ZTZ-96 (Type 96) | mbt | China (Norinco) | low | - | 1 |
| `type96_wapc` | Type 96 Wheeled Armored Personnel Carrier | apc | Japan (Komatsu) | low | - | 1 |
| `v150` | Cadillac Gage V-150 Commando | apc | United States | low | - | 4 |
| `vamtac` | URO VAMTAC | light | Spain | low | - | 1 |
| `volat_v1` | MZKT Volat V1 | light | Belarus | low | - | 1 |
| `vt4` | VT-4 / Haider | mbt | China (Norinco), local assembly HIT Pakistan | low | - | 1 |
| `vtt323` | VTT-323 (M1973) | apc | North Korea (based on Chinese Type 63) | low | - | 1 |
| `vuran` | BMC Vuran | mrap | Turkey (BMC) | low | - | 2 |
| `warrior` | FV510 Warrior | ifv | United Kingdom | low | - | 1 |
| `wing_loong` | CAIG Wing Loong I / II | uav | China | low | - | 6 |
| `zorawar` | Zorawar light tank | mbt | India (DRDO / Larsen & Toubro) | low | - | 1 |

## Adding a vehicle

1. List this folder first. If the vehicle or its family already has a file, reuse that id: add your faction id to its `operators` and any new version to `variants` (and `aliases`), keeping the edit small. Variants never get their own file.
2. Otherwise write `reference/vehicles/<id>.json` with every field in the schema above. Use the lowercase family designation as the id (`t72b3`, `bmp2`, `k2_black_panther`), or the voxel model id if a model already exists. Fictional or improvised types (`narco_truck`, `armored_suv`) get `origin: "improvised"` and describe the real-world type.
3. Fill `operators` with the canonical faction ids that really field it, `reference_pages` with photo pages (the en.wikipedia article and, when known, `https://commons.wikimedia.org/wiki/Category:<Name>`) and `sources`. Set `model_priority` by how much the game needs it, and `existing_model` to `null` unless a model exists.
4. Add `{"vehicle_id": "<id>", "role": "<type>", "prevalence": "...", "notes": "..."}` to each operator's `factions/<id>.json` `vehicles` list.
5. If the vehicle's `type` is mbt, ifv, apc or mrap (crew) or attack_heli or transport_heli (pilot) and the faction had no such vehicle before, re-run the loadouts generator (`python3 -I tools/loadouts_gen/gen.py --game <game repo>`; see [../../tools/loadouts_gen/README.md](../../tools/loadouts_gen/README.md)).
6. Run `python3 -I tools/validate_pack.py --strict` (0 errors, 0 warnings) and update this README's tables.

To retire a duplicate file: keep the canonical id (an existing voxel model id first, then the family designation), move the other file's operators, variants, aliases, visual notes, colour schemes, reference pages and sources into it, delete the duplicate, and rewrite every `vehicle_id` that pointed at it in `factions/*.json`, `worldspaces/*.json` and the loadouts generator specs before regenerating `loadouts/`.
