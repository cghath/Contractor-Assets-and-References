# Worldspaces

Procedural region recipes for Contractor: 26 theatres inspired by modern-day regions as of October 2026 (23 from Job 5, plus mindanao_sulu, iraq_iran_border and eastern_congo from Job 7). Each `worldspaces/<theatre id>.json` is a recipe, not a map. It gives the biomes and palettes, a terrain generator, settlement and building rules, points of interest, civilians, factions present, how the persistent faction war moves, contract hooks, a zone plan, and insertion by LHD or FOB.

- Every town, village, camp and base name is **fictional**, in the style of the region's languages. No real city is replicated. Real-place-derived names were removed in a cleanup pass.
- Tone is factual and neutral. IEDs, mines, tunnels, drones and chemical labs appear only as map hazards and level geometry (game-level), never as how-to.
- Anything invented for gameplay is listed in each file's `proposed`. Decisions Captain has confirmed (2026-10-10) are listed in each file's `captain_confirmed` instead. The Contractor design doc wins where it disagrees.
- The shape follows `WORLD_SPEC` in [../tools/factions_workflow.js](../tools/factions_workflow.js). A few fields were added: `zone_plan`, `early_game_notes`, settlement `footprint_m`, `storeys` and `wall_class`, POI `contract_use`, civilian `casualty_risk_notes`, terrain `generator.settlement_flattening`, `map_layout_note` (gaza_west_bank only) and `captain_confirmed` (Job 7: Captain's confirmed decisions, moved out of `proposed`).
- Validate with `python3 -I tools/validate_pack.py` from the repo root.

## Theatres

Main factions are those present at medium or high strength. Every file also lists low-strength presences (advisers, naval patrols, peacekeepers, rival PMCs); see its `factions_present`. The `player` faction lists every theatre and is not repeated in the files.

| id | Name | Inspired by | Size (km) | Early game | LHD | Main factions |
|---|---|---|---|---|---|---|
| levant_syria | Wadi Furat Marches | Central and north-east Syria in the post-Assad transition: Euphrates valley, Badia steppe, Jazira plain, a basalt plateau | 24 x 20 | yes | no | syr, sdf, isis, tur, isr |
| lebanon_south | Jabal Amil Frontier | South Lebanon between the Litani and the Blue Line; UNIFIL drawdown | 16 x 14 | no | yes | hezbollah, isr, UNIFIL contributors (fra, ita, esp) |
| israel | Coastline to Negev Corridor | Israel compressed north to south: Galilee, coastal plain, northern Negev | 18 x 26 | no | yes | isr (hezbollah, hamas, pij only at the edges, low) |
| gaza_west_bank | Coastal Strip and Highlands | Gaza Strip after the October 2025 ceasefire, and the northern West Bank, as two sectors | 20 x 16 | yes | yes (restricted) | hamas, isr, pij, pse_pa |
| iran_zagros | Hawraz Border Ranges | Kurdish central Zagros straddling the Iran-Iraq border | 20 x 20 | no | no | irn, krg_peshmerga |
| persian_gulf_coast | Strait of Khawr Sabah | Strait of Hormuz: Iranian coast, Musandam-type peninsula, Gulf terminals | 24 x 22 | no | yes | irn, are, usa, pmc_black_sable |
| mesopotamia | Land Between the Rivers | Central and northern Iraq: Tigris plain, Jazira desert, Hamrin hills, Kurdistan front ranges | 24 x 24 | yes | no | irq, iraqi_militias, isis, krg_peshmerga |
| yemen_red_sea | Tihama and the Southern Gate | Tihama coast, terraced highlands and interior wadis of Yemen; Bab al-Mandab | 24 x 24 | yes | yes | houthis, aqap, sau, usa, pmc_black_sable |
| sahel | Boucle du Fleuve | Central Sahel of Mali, Burkina Faso and western Niger | 24 x 24 | yes | no | jnim, sahel_aes, isis, africa_corps |
| horn_of_africa | Shabelle Coast | Southern and central Somalia, a Puntland-type range and a Djibouti-type port enclave | 24 x 24 | yes | yes | al_shabaab, som, tur, egy, pmc_black_sable |
| afghan_highlands | Koh-e Safed Valleys | Eastern Afghanistan (Nangarhar and Kunar types) on the Pakistan border, during the 2026 border war | 20 x 20 | yes | no | afg_taliban, pak, isis_k |
| baltic_coast | Amber Coast Frontier | Estonian, Latvian and Lithuanian coast with a river border to Russia | 20 x 20 | no | yes | est, lva, ltu, pol, fin, swe, deu, gbr, can, rus |
| suwalki_gap | Lakeland Corridor | The Polish-Lithuanian corridor between Kaliningrad and Belarus | 16 x 20 | no | no | pol, ltu, deu, usa, rus, blr |
| eastern_ukraine | Donets Steppe Front | Donbas front: steppe, tree lines, mining towns | 20 x 20 | no | no | ukr, rus, pmc_kestrel |
| black_sea_coast | Delta and Liman Coast | Danube delta, Budjak steppe and limans, with Romanian and Moldovan edges | 22 x 20 | no | yes | ukr, rou, rus |
| arctic_north | High Fjell Border | Finnmark fjords and fells, a Lapland border valley, the Kola border | 22 x 20 | no | yes | nor, fin, usa, rus |
| caucasus | Three Borders Highlands | Georgia-Armenia-Azerbaijan meeting area: volcanic plateau, gorges, Kura valley | 20 x 20 | no | no | arm, aze, geo, rus |
| alpine_europe | High Passes Cantons | Central Alps where Switzerland, Austria, Italy, Germany and France meet | 18 x 18 | no | no | che, aut, rus (what-if covert mountain troops; generic arms traffickers stay) |
| taiwan_strait | Strait Coast and Outer Isles | Taiwan's west coast and a Kinmen-type outer island group | 22 x 22 | no | yes | twn, chn |
| korean_dmz | Imjin Border Hills | Western sector of the Korean DMZ and the Han-type estuary | 20 x 18 | no | yes | kor, prk, usa |
| south_china_sea | Reef Line and Karst Isles | A Palawan-type island and a Spratly-type reef group | 24 x 22 | no | yes | phl, chn |
| kashmir_loc | Line of Control Valleys | A river gorge crossing the Kashmir LoC, with a valley corner and a high plateau corner | 20 x 20 | no | no | ind, pak |
| mexico_cartel_belt | Sierra y Costa del Pacifico | Sinaloa, Jalisco and Michoacan types: Pacific plain, Sierra Madre, avocado highland | 24 x 22 | yes | yes | cartel_pacifico, cartel_jalisco_nueva, mex |
| mindanao_sulu | Lake Plateau and Sulu Arc | Southern Philippines: Lanao-type lake plateau, Liguasan-type marsh and jungle cordillera, Sulu-type island chain (Job 7) | 24 x 22 | yes | yes | phl, isis (East Asia cells); usa advisers low |
| iraq_iran_border | Hamrin and the Eastern Gate | Iraq-Iran borderlands: Diyala-type palm plain, Hamrin-type ridge and reservoir, disputed foothills, Iranian Zagros foothills (Job 7) | 22 x 20 | yes | no | irq, iraqi_militias, krg_peshmerga, irn; isis remnants low |
| eastern_congo | Kivu Highlands and Forest Edge | Eastern DR Congo (North Kivu and Ituri): lake and lava shore, highlands, rift savanna, northern rainforest; UN peacekeeping map (Job 7) | 24 x 24 | yes | no | cod, m23, adf, ind (UN); chn (UN, what-if) low |

**Early game (`early_game_suitable: true`, 11 theatres):** the theatres where the early-tier hostile factions (isis, isis_k, al_qaeda, aqap, al_shabaab, jnim, adf, hamas, pij, iraqi_militias, and the two early-tier cartels) carry most of the fighting: levant_syria, gaza_west_bank, mesopotamia, yemen_red_sea, sahel, horn_of_africa, afghan_highlands, mexico_cartel_belt and, since Job 7, mindanao_sulu (isis East Asia cells), iraq_iran_border (isis remnants and iraqi_militias) and eastern_congo (adf; m23 is mid tier and fights only in fighting phases). In yemen_red_sea the early zones are the AQAP wadis in the east; the Houthi zones (mid tier) open later. gaza_west_bank is flagged early because hamas and pij are early-tier, but its extreme civilian density means early contracts there should be escort, election-security and UXO work. Each file's `early_game_notes` explains the flag.

## Contract zones and hot zones on each map

- **Sizes.** Contract zones are about 2-4 km² (40-90 min) and hot zones about 8-16 km² (2-4 h). The maps are 16-24 km per side (224-576 km²; Captain-confirmed 2026-10-10), so each holds 4 or more contract zones and 1-2 hot zones with buffer between them. Hot zones are twice the area of a contract zone (8-16 km² vs 2-4 km²; Captain-confirmed 2026-10-10).
- **`zone_plan`.** Each file names 4 contract zones, each anchored on a POI with an area and a note on terrain and civilians, plus 1-2 hot zones laid out the design doc's way: an enemy HQ, 3-6 outposts, road checkpoints, roaming patrols and 1-2 QRF bases. Contract zones and hot zones share the same map regions (design doc), so a hot zone usually contains or touches two contract-zone anchors.
- **Zone graph.** POIs and settlement quarters are sized as zone chunks (one compound, one village quarter, one checkpoint) with clear entry routes. Each zone saves its own state: loot taken, dropped items and the voxel edit log.
- **Loot.** POI `loot_tier` is low or medium only. Every POI has an `intel_chance`.
- **Insertion.** `lhd: true` only on coastal maps (14 of 26; mindanao_sulu is the Job 7 addition). Inland maps name a FOB site. Some coastal maps restrict the LHD, and the restrictions stay (Captain-confirmed 2026-10-10): gaza_west_bank (evacuations only), taiwan_strait (withdrawn in escalation) and mexico_cartel_belt (with Mexican approval). Mountain maps (iran_zagros, afghan_highlands, kashmir_loc, caucasus, alpine_europe) rule out AAVs, following Captain's rule that AAVs are no use in the mountains.
- **Late-game escalation.** The grey-zone theatres (baltic_coast, suwalki_gap, arctic_north, black_sea_coast, taiwan_strait, korean_dmz, south_china_sea) describe the real 2026 situation as their default state and a late-game escalation hot zone. That escalation is a game what-if, labelled "fictional what-if" in each hot zone's name; keeping it is Captain-confirmed (2026-10-10).

## Generator approach (all files)

Each recipe has two layers, to fit the engine as it is today:

1. **Macro terrain (km scale).** A heightmap at 5-20 m resolution, built in code from 3-5 noise layers. Each layer gives a type (simplex fbm, ridged multifractal, cellular/Worley, ramps, stamps), a frequency in cycles per km, an amplitude in metres and a purpose. The recipe then applies an erosion pass, places rivers and wadis as splines or by flow accumulation, and flattens terrain under settlements (rules in `generator.settlement_flattening`). Coastal maps carry bathymetry as negative heights. Today the ground is a plain collider and `VoxelWorld.BOUNDS` is about 44 x 44 m with no stream, so the macro layer is meant for a mesh or coarse ground now, and a `VoxelLodTerrain` with a `VoxelGeneratorGraph` or heightmap generator later. Elevation ranges are realistic for each region.
2. **Micro structures (10 cm destructible voxels).** These are built only around the active contract or hot zone. Settlements give `footprint_m`, `storeys`, `wall_class` (thin and breachable or thick cover), `materials` and `layout_rules`. Qalat outer walls (afghan_highlands) are the thickest case: small arms cannot breach them; only breaching charges, grenade launchers or vehicles can (Captain-confirmed 2026-10-10). POIs describe their building blocks in plain terms. The 5 cm figure in `CONTEXT` applies to vehicle art only.

Biome shares and settlement shares each sum to 1.0. Every biome has 4-6 ground and 4-6 foliage hex colours.

### Materials

The game's `voxel_world.gd` started with four voxel materials: `CONCRETE` #8a8577, `PAINTED` #5f6b58, `WOOD` #8c6a46 and `STEEL` #4a4d50. The files also use these 18 materials, with the same hex everywhere. Captain accepted them (2026-10-10), and they were added to `VoxelWorld.Mat` and `PALETTE` on the game's `dev` branch (commit 1ec1417), appended after `STEEL`. In the game they are colours only so far; the wall classes below are not yet modelled:

| Material | Hex | Used for | Wall class |
|---|---|---|---|
| MUD_BRICK | #a47e57 | mud brick, adobe, banco, rammed earth | thick (40-100 cm), chips slowly |
| STONE | #8f8676 | field stone, rubble stone, dry-stone walls | thick |
| LIMESTONE | #d6caa8 | dressed pale stone and cladding (Levant) | thick |
| BASALT | #4b4845 | basalt blocks (Hauran, Caucasus) | thick |
| TUFF | #c48a6a | Armenian volcanic tuff blocks | thick |
| CORAL_STONE | #cbbf9f | Gulf, Red Sea and Somali coral-stone houses | thick |
| BRICK | #9c5a3c | fired brick | medium |
| CINDER_BLOCK | #9a978f | hollow concrete block infill | thin (breachable) |
| PLASTER | #e3dccb | lime or cement render, whitewash | finish only |
| ROOF_TILE | #a4553b | clay roof tiles | thin |
| FIBRE_CEMENT | #a5a49c | asbestos-cement slate roofs (former USSR) | thin |
| CORRUGATED_IRON | #8b8e8c | tin roofs, sheds, shacks | thin, no cover |
| THATCH | #b49a5e | thatch, reed, mat huts | no cover |
| TARP | #3f6d8c | tents, plastic sheeting | no cover |
| GLASS | #9fbcc4 | windows, curtain walls | no cover |
| SANDBAG | #b8a378 | sandbag positions | thick |
| HESCO | #a99a6c | HESCO and blast barriers | thick |
| DIRT_BERM | #8a6f4e | earth berms, earth roofs, dugouts | thick |

## Faction coverage

`factions_present` was checked against every faction file's `theatres`, and since Job 7 `tools/validate_pack.py` checks it both ways (a warning for any mismatch). Every listing now agrees: chn and ind, the UNIFIL contributors on lebanon_south, list lebanon_south in their own files since Job 7 (Captain, 2026-10-10). Some listings are thin or need care, and the files mark them as low-strength or edge presences. Captain confirmed on 2026-10-10 that these low-plausibility listings stay at low strength (blr in eastern_ukraine and baltic_coast; fra, bel and esp in sahel; jpn in arctic_north and korean_dmz; chn in korean_dmz and kashmir_loc; are in yemen_red_sea; usa in mexico_cartel_belt), and that rus stays on alpine_europe as a fictional what-if; each file records this in its `captain_confirmed` list:

- **sahel:** fra, bel and esp appear only at the south edge, from a neighbouring partner state, because their forces left the AES states.
- **baltic_coast:** blr appears only as covert sabotage teams.
- **eastern_ukraine:** blr and prk appear only as Russian-attached rear elements.
- **arctic_north:** jpn appears only as researchers and observers.
- **korean_dmz:** jpn and chn appear only as liaison or off-map factors.
- **kashmir_loc:** chn appears only as engineers on a road project. Militants stay generic NPCs with no roster faction (Captain-confirmed 2026-10-10).
- **mexico_cartel_belt:** usa appears only offshore and as liaison (a game what-if, per usa.json).
- **yemen_red_sea:** are appears only offshore and in contracts (UAE forces withdrew from Yemen in December 2025).
- **alpine_europe:** srb is the Balkan stand-in transit. rus (Russian mountain troops) is the hostile force as a fictional what-if (added by Captain's decision, 2026-10-10; the presence itself is proposed); generic arms-trafficker NPCs stay.
- **mindanao_sulu:** usa appears only as a small non-combat adviser team.
- **eastern_congo:** chn appears as a UN engineer and medical company, a fictional game what-if: China's MONUSCO contingent left in April 2024 (alliance `monusco`, member_status what_if). Captain confirmed on 2026-10-10 that it stays, clearly marked fictional. m23 is a hostile non-client whose units are not attacked by default in ceasefire phases (Captain-confirmed 2026-10-10).
- **iran_zagros and south_china_sea:** iraqi_militias is not added to iran_zagros and isis is not added to south_china_sea; those gaps are answered by iraq_iran_border and mindanao_sulu (Captain-confirmed 2026-10-10).

No worldspace question is open any more; the answered ones are listed in [docs/worldspaces_handoff.md](../docs/worldspaces_handoff.md).

## Sources

Each file cites text sources for terrain, climate, vegetation and architecture (Wikipedia articles), plus the faction files' October 2026 situation notes. Image hosts were not used.
