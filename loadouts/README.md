# AI default loadouts

Default AI loadouts for the 79 non-player factions in `factions/` (every faction id except `player`), as of 2026-10-10. Weapons, ammunition, armor and helmets use real-world designations (Captain, 2026-10-10); fictional cartels and PMCs use real gear. The schema is in [docs/loadouts_handoff.md](../docs/loadouts_handoff.md). Counts, optics, medical levels and the game kits are proposals (`proposed` in each file).

- `loadouts/<faction id>.json`: one file per faction: variants, each with every role's weapons, ammunition, launcher, grenades, armor, medical kit, other kit and a `game_kit` built only from items that exist in the game today.
- [weapons_index.json](weapons_index.json): every weapon, calibre and round, magazine, optic, underbarrel launcher, launcher, launcher round and grenade (plus medical and other kit), with users and in-game flags.
- [armor_index.json](armor_index.json): every helmet, vest / plate carrier and plate, with tier, game mapping and users.
- [rounds_index.json](rounds_index.json): proposed specs for every round with no exact match in the game's `data/rounds.json` (Captain, 2026-10-10): calibre, designation, projectile, approximate muzzle velocity and mass, level on the game's armor ladder, which game armor stops it, users. Spec only; the loadouts point at these through `proposed_round_id`.
- [../tools/loadouts_gen/](../tools/loadouts_gen/): the generator that writes everything in this folder (see its README).
- Validate with `python3 tools/validate_pack.py` (loadouts checks included).

## Roster

Armor is the regular variant's vest tier (helmet tier); AT is the at role's launcher, with the in-game launcher or its substitute in brackets.

| id | Bloc | Tier | Variants | Rifleman | Armor | AT | Crew / pilot |
|---|---|---|---|---|---|---|---|
| usa | US and Five Eyes | early | regular, usmc | M4A1 carbine | heavy (medium) | M3E1 MAAWS (84mm) [MAAWS] | crew/pilot |
| gbr | US and Five Eyes | early | regular | L85A3 (SA80) | heavy (medium) | NLAW [NLAW] | crew/pilot |
| can | US and Five Eyes | early | regular | C7A2 rifle | medium (medium) | Carl Gustaf M3 (84mm) [MAAWS] | crew/pilot |
| aus | US and Five Eyes | mid | regular | EF88 Austeyr | medium (medium) | Carl Gustaf M3 (84mm) [MAAWS] | crew/pilot |
| nzl | US and Five Eyes | mid | regular | MARS-L (LMT CQB16) | medium (medium) | Carl Gustaf M3 (84mm) [MAAWS] | crew/pilot |
| fra | Western Europe and Nordics | early | regular | HK416 F | heavy (medium) | AT4 CS (84mm) [AT4] | crew/pilot |
| deu | Western Europe and Nordics | mid | regular | HK G36 | medium (medium) | Panzerfaust 3 (110mm) [sub MAAWS] | crew/pilot |
| ita | Western Europe and Nordics | early | regular | Beretta ARX160 | medium (medium) | Panzerfaust 3 (110mm) [sub MAAWS] | crew/pilot |
| esp | Western Europe and Nordics | early | regular | HK G36E | medium (medium) | Instalaza C90 (90mm) [sub AT4] | crew/pilot |
| nld | Western Europe and Nordics | mid | regular | C7NLD rifle | medium (medium) | Panzerfaust 3 (110mm) [sub MAAWS] | crew/pilot |
| bel | Western Europe and Nordics | mid | regular | FN SCAR-L | medium (medium) | RGW 90 (90mm) [sub AT4] | crew/pilot |
| nor | Western Europe and Nordics | late | regular | HK416 | medium (medium) | Carl Gustaf M4 (84mm) [MAAWS] | crew/pilot |
| dnk | Western Europe and Nordics | mid | regular | Gevaer M/25 (C8 MRR) | medium (medium) | Carl Gustaf M4 (84mm) [MAAWS] | crew |
| swe | Western Europe and Nordics | late | regular | Ak 5C | medium (medium) | Grg m/86 (Carl Gustaf M3) [MAAWS] | crew/pilot |
| fin | Western Europe and Nordics | late | regular | RK 62 | medium (medium) | NLAW [NLAW] | crew/pilot |
| grc | Western Europe and Nordics | early | regular | HK G3A3 | light (medium) | Carl Gustaf M2 (84mm) [MAAWS] | crew/pilot |
| ukr | Ukraine and eastern flank | mid | regular, territorial, assault | AK-74 / AKS-74 | medium (medium) | RPG-7 [RPG-7] | crew |
| pol | Ukraine and eastern flank | mid | regular | MSBS Grot C16 FB-A2 | medium (medium) | Carl Gustaf M4 (84mm) [MAAWS] | crew/pilot |
| est | Ukraine and eastern flank | late | regular | LMT R-20 Rahe | medium (medium) | Carl Gustaf M4 (84mm) [MAAWS] | crew |
| lva | Ukraine and eastern flank | late | regular | HK G36 | medium (medium) | M136 AT4 (84mm) [AT4] | crew/pilot |
| ltu | Ukraine and eastern flank | late | regular | HK G36 | medium (medium) | Carl Gustaf M4 (84mm) [MAAWS] | crew/pilot |
| rou | Ukraine and eastern flank | mid | regular | PA md. 86 | medium (medium) | AG-7 (Romanian RPG-7) [RPG-7] | crew/pilot |
| mda | Ukraine and eastern flank | mid | regular | AKM | light (light) | RPG-7 [RPG-7] | crew |
| geo | Ukraine and eastern flank | mid | regular | M4A1 carbine | medium (medium) | RPG-7 [RPG-7] | crew/pilot |
| rus | Russia, CSTO, Caucasus | late | regular, spetsnaz, vdv, storm, mobilised, mountain | AK-74M | medium (medium) | RPG-7V2 [RPG-7] | crew/pilot |
| blr | Russia, CSTO, Caucasus | late | regular | AK-74 / AKS-74 | medium (light) | RPG-7 [RPG-7] | crew/pilot |
| africa_corps | Russia, CSTO, Caucasus | mid | regular | AK-74M | medium (medium) | RPG-7 [RPG-7] | crew/pilot |
| kaz | Russia, CSTO, Caucasus | mid | regular | AK-74 / AKS-74 | medium (light) | RPG-7 [RPG-7] | crew/pilot |
| srb | Russia, CSTO, Caucasus | mid | regular | Zastava M19 | medium (medium) | M80 Zolja (64mm) [sub AT4] | crew/pilot |
| arm | Russia, CSTO, Caucasus | mid | regular | AK-74 / AKS-74 | medium (light) | RPG-7 [RPG-7] | crew/pilot |
| aze | Russia, CSTO, Caucasus | mid | regular | AK-74M | medium (medium) | RPG-7 [RPG-7] | crew/pilot |
| chn | Asia-Pacific | late | regular | QBZ-191 | medium (medium) | PF-98 (120mm) [sub MAAWS] | crew/pilot |
| prk | Asia-Pacific | late | regular | Type 88 (AK-74 pattern) | none (light) | RPG-7 copy (DPRK) [RPG-7] | crew/pilot |
| jpn | Asia-Pacific | mid | regular | Howa Type 20 | medium (medium) | Carl Gustaf M4 (84mm) [MAAWS] | crew/pilot |
| kor | Asia-Pacific | mid | regular | Daewoo K2C1 | medium (medium) | Panzerfaust 3 (110mm) [sub MAAWS] | crew/pilot |
| twn | Asia-Pacific | late | regular | T91 | medium (medium) | Kestrel (66mm) [sub AT4] | crew/pilot |
| ind | Asia-Pacific | mid | regular | AK-203 | medium (medium) | Carl Gustaf M4 (84mm) [MAAWS] | crew/pilot |
| pak | Asia-Pacific | early | regular | G3P4 (POF licence G3) | light (medium) | RPG-7 [RPG-7] | crew/pilot |
| phl | Asia-Pacific | early | regular | Remington R4A3 | light (light) | RPG-7 [RPG-7] | crew/pilot |
| vnm | Asia-Pacific | mid | regular | STV-380 | light (light) | B41 (Vietnamese RPG-7) [RPG-7] | crew/pilot |
| irn | Middle East states | mid | regular, irgc, basij | KL-7.62 (Iranian AKM) | light (light) | RPG-7 (Iranian copy) [RPG-7] | crew/pilot |
| isr | Middle East states | mid | regular | IWI Tavor X95 | medium (medium) | MATADOR (RGW 90 family, 90mm) [sub AT4] | crew/pilot |
| tur | Middle East states | mid | regular | MKE MPT-76 | medium (medium) | HAR-66 (66mm, M72 type) [sub AT4] | crew/pilot |
| sau | Middle East states | early | regular, sang | HK G36 | medium (medium) | M136 AT4 (84mm) [AT4] | crew/pilot |
| are | Middle East states | early | regular, presidential_guard | Caracal CAR 816 | medium (medium) | M136 AT4 (84mm) [AT4] | crew/pilot |
| qat | Middle East states | early | regular | FN SCAR-L | medium (medium) | AT4 CS (84mm) [AT4] | crew/pilot |
| egy | Middle East states | mid | regular, saaka | Misr (Egyptian AKM) | light (light) | RPG-7 [RPG-7] | crew/pilot |
| jor | Middle East states | early | regular | M16A4 | medium (medium) | RPG-32 Hashim (105mm) [sub RPG-7] | crew/pilot |
| syr | Middle East states | early | regular, elite | AKM | light (light) | RPG-7 [RPG-7] | crew |
| irq | Middle East states | early | regular, cts | M16A4 | medium (medium) | RPG-7 [RPG-7] | crew/pilot |
| pse_pa | Middle East states | early | regular | AKM | light (light) | none | - |
| hamas | ME terrorist / armed groups | early | regular, elite | AKM | none (none) | RPG-7 [RPG-7] | - |
| pij | ME terrorist / armed groups | early | regular, elite | AR-15 / M4-pattern rifle (commercial or captured) | none (none) | RPG-7 [RPG-7] | - |
| hezbollah | ME terrorist / armed groups | mid | regular, elite | AKM | light (none) | RPG-7 [RPG-7] | crew |
| houthis | ME terrorist / armed groups | mid | regular, elite | AKM | none (none) | RPG-7 [RPG-7] | crew |
| iraqi_militias | ME terrorist / armed groups | early | regular, elite | AKM | light (none) | RPG-7 [RPG-7] | - |
| al_qaeda | ME terrorist / armed groups | early | regular, elite | AKM | none (none) | RPG-7 [RPG-7] | - |
| aqap | ME terrorist / armed groups | early | regular, elite | AKM | none (none) | RPG-7 [RPG-7] | - |
| isis | ME terrorist / armed groups | early | regular, elite | AKM | none (none) | RPG-7 [RPG-7] | crew |
| isis_k | ME terrorist / armed groups | early | regular, elite | AKM | none (none) | RPG-7 [RPG-7] | - |
| al_shabaab | ME terrorist / armed groups | early | regular, elite | AKM | none (none) | RPG-7 [RPG-7] | - |
| jnim | ME terrorist / armed groups | early | regular, elite | AKM | none (none) | RPG-7 [RPG-7] | - |
| che | Neutrals, Africa, cartels, PMCs | mid | regular | Stgw 90 (SIG SG 550) | medium (medium) | NLAW [NLAW] | crew/pilot |
| aut | Neutrals, Africa, cartels, PMCs | mid | regular | StG 77 A1 (Steyr AUG) | medium (medium) | PAR 66/79 (Carl Gustaf family, 84mm) [MAAWS] | crew/pilot |
| irl | Neutrals, Africa, cartels, PMCs | early | regular | Steyr AUG A3 | medium (medium) | Carl Gustaf M3 (84mm) [MAAWS] | crew |
| mex | Neutrals, Africa, cartels, PMCs | early | regular | FX-05 Xiuhcoatl | medium (medium) | M136 AT4 (84mm) [AT4] | pilot |
| cartel_pacifico | Neutrals, Africa, cartels, PMCs | early | regular, street | AK-47 / Type 56 pattern | medium (light) | RPG-7 [RPG-7] | - |
| cartel_jalisco_nueva | Neutrals, Africa, cartels, PMCs | early | regular, street | AR-15 / M4-pattern rifle (commercial or captured) | medium (medium) | RPG-7 [RPG-7] | - |
| afg_taliban | Neutrals, Africa, cartels, PMCs | early | regular, elite | AKM | none (none) | RPG-7 [RPG-7] | crew/pilot |
| sdf | Neutrals, Africa, cartels, PMCs | early | regular, yat | AKM | light (none) | RPG-7 [RPG-7] | crew |
| krg_peshmerga | Neutrals, Africa, cartels, PMCs | early | regular, zeravani | AKM | light (medium) | RPG-7 [RPG-7] | crew |
| sahel_aes | Neutrals, Africa, cartels, PMCs | early | regular, vdp | AK-47 / Type 56 pattern | light (light) | RPG-7 [RPG-7] | crew/pilot |
| som | Neutrals, Africa, cartels, PMCs | early | regular, danab, gorgor | AKM | light (none) | RPG-7 [RPG-7] | crew |
| pmc_halcyon | Neutrals, Africa, cartels, PMCs | mid | regular, protective_detail | M4A1 carbine | heavy (heavy) | M136 AT4 (84mm) [AT4] | crew/pilot |
| pmc_kestrel | Neutrals, Africa, cartels, PMCs | mid | regular, assault | AK-12 | medium (medium) | RPG-7 [RPG-7] | crew/pilot |
| pmc_black_sable | Neutrals, Africa, cartels, PMCs | mid | regular, auxiliary | Caracal CAR 816 | medium (heavy) | RPG-7 [RPG-7] | crew |
| adf | Central Africa | early | regular, elite | AK-47 / Type 56 pattern | none (none) | RPG-7 [RPG-7] | - |
| m23 | Central Africa | mid | regular, assault | AK-47 / Type 56 pattern | light (none) | RPG-7 [RPG-7] | crew |
| cod | Central Africa | early | regular, republican_guard, wazalendo | AKM | none (none) | RPG-7 [RPG-7] | crew/pilot |

## What has to be built

Counted from the 79 loadout files against the game's `data/items.json` (35 items) and `data/rounds.json`. Full lists with users are in the two index files.

| Category | Used | Already in game | To build |
|---|---|---|---|
| Weapons (primary, sidearm, alternates) | 242 | 4 (m110, m17, m4a1, mk18) | 238 |
| Magazines and belts | 36 | 3 (mag_556, mag_762, mag_9mm) | 33 |
| Rounds (rounds.json) | 20 calibres | 7 calibres have a round | 21 round specs in rounds_index.json: 13 calibres with no round, plus 6 designations that use a generic round today |
| Launchers | 79 | 20 map to the 6 design-doc launchers, which have no items.json entry yet | 6 launcher items (at4, javelin, maaws, nlaw, rpg7, smaw) and 7 round items (ffv441d, ffv551, javelin_missile, mk3_hedp, mk6_heaa, og7v, pg7v); AT4 and NLAW are single-shot; 59 other launchers use a game_substitute |
| Underbarrel launchers / their ammo | 22 / 5 | 0 | 22 / 5 |
| Optics (class ids) | 13 | 0 | 13 |
| Hand grenades | 24 models | frag, white smoke and stun covered by frag_grenade, smoke_grenade, flashbang | 3 signal smokes (smoke_green, smoke_red, smoke_violet) |
| Helmets | 29 models | 27 map to helmet_bump / helmet / helmet_heavy by tier | 2 cosmetic non-ballistic helmets (helmet_flight, helmet_tanker); models are skins of the tier items |
| Vests / plate carriers | 24 models | all map to the 3 carrier tiers | visual variants only |
| Plates | 14 models | ceramic, steel, PE and side plates map to existing plates | 1 new item: plate_steel_light (light-tier steel plate; used by 22 factions: al_qaeda, al_shabaab, aqap, cod, egy, grc, hamas, hezbollah, houthis, iraqi_militias, irn, isis, isis_k, jnim, m23, mda, pak, phl, pij, rus, sahel_aes, vnm). Until it is built, `game_kit` uses plate_pe_l3 in its place |
| Medical | 18 | 9 | 9 (adenosine, atropine, decompression_needle, defibrillator, epinephrine, io_fast1, iv_18g, saline_500, surgical_kit) |
| Other kit | 7 | 2 (backpacks) | 5 (binoculars, nvg_bino, nvg_envgb, nvg_mono, radio) |

Heavy (III++) helmets go only to elite, SOF and PMC assault variants (Captain, 2026-10-10), on the assault roles (marksman and sniper keep the standard helmet): ukr assault, rus spetsnaz, are presidential_guard, egy saaka, irq cts, pmc_halcyon regular, pmc_kestrel assault, pmc_black_sable regular.

### Early game first

The early game is mostly fighting terrorist groups (Captain). These are the items to build first, ranked by how many of the 36 early-tier factions use them.

| Item | Kind | Early-tier users | All users |
|---|---|---|---|
| PKM (`pkm`) | weapon, 7.62x54R | 21 | 39 |
| AKM (`akm`) | weapon, 7.62x39mm | 19 | 33 |
| SVD Dragunov (`svd`) | weapon, 7.62x54R | 17 | 34 |
| M4 carbine (`m4`) | weapon, 5.56x45mm | 16 | 20 |
| Glock 17 (`glock17`) | weapon, 9x19mm | 15 | 28 |
| AKMS (folding stock) (`akms`) | weapon, 7.62x39mm | 15 | 18 |
| Type 56 (`type56`) | weapon, 7.62x39mm | 14 | 16 |
| PM Makarov (`pm_makarov`) | weapon, 9x18mm | 12 | 22 |
| Barrett M82A1 (`m82a1`) | weapon, 12.7x99mm (.50 BMG) | 11 | 17 |
| AK-47 / Type 56 pattern (`ak47`) | weapon, 7.62x39mm | 11 | 12 |
| FN Minimi (`minimi`) | weapon, 5.56x45mm | 9 | 18 |
| RPK (`rpk`) | weapon, 7.62x39mm | 8 | 13 |
| FN MAG 58 (`mag58`) | weapon, 7.62x51mm | 7 | 15 |
| M249 SAW (`m249`) | weapon, 5.56x45mm | 7 | 9 |
| M16A4 (`m16a4`) | weapon, 5.56x45mm | 6 | 7 |
| 7.62x39mm 30-round magazine (`mag_762x39_30`) | magazine | 22 | 41 |
| 7.62x54R 100-round belt (box) (`belt_762x54r_100`) | magazine | 21 | 43 |
| 7.62x51mm 100-round belt (`belt_762x51_100`) | magazine | 18 | 46 |
| 5.56x45mm 200-round belt (box or soft pouch) (`belt_556_200`) | magazine | 18 | 38 |
| 7.62x54R 10-round magazine (`mag_762x54r_10`) | magazine | 17 | 38 |
| 12.7x99mm 10-round magazine (`mag_50bmg_10`) | magazine | 13 | 26 |
| RPG-7 (`rpg7`) | launcher, game RPG-7 | 23 | 40 |
| M136 AT4 (84mm) (`at4`) | launcher, game AT4 | 8 | 17 |
| FGM-148 Javelin (`javelin`) | launcher, game Javelin | 6 | 17 |
| Carl Gustaf M2 (84mm) (`cg_m2`) | launcher, game MAAWS | 3 | 5 |
| M203 (`m203`) | underbarrel launcher | 13 | 16 |
| GP-25 / GP-30 (`gp25`) | underbarrel launcher | 9 | 23 |
| 40 mm underbarrel launcher (`ugl40`) | underbarrel launcher | 4 | 13 |

Calibres with no round in `data/rounds.json`: .300 Norma Magnum, .300 Winchester Magnum, .338 Lapua Magnum, 12.7x108mm, 14.5x114mm, 5.45x39mm, 5.7x28mm, 5.8x42mm, 6.8x51mm, 7.62x25mm, 7.92x57mm, 9x18mm, 9x39mm.

Designations that currently use a generic round (same calibre, different load): 5.56x45mm M855A1 EPR; 5.56x45mm SS109 / M855 (NATO ball); 7.62x51mm (Chinese DVC12-class ball); 7.62x51mm M80A1 EPR; 7.62x54R 7N13 (steel core), 7N1 for the SVD; 9x19mm DAP92-9 (Chinese).

### Weapons to build, by number of users

| Weapon | Class | Calibre | Users | Game substitute |
|---|---|---|---|---|
| PKM (`pkm`) | gpmg | 7.62x54R | 39 | m4a1 |
| SVD Dragunov (`svd`) | dmr | 7.62x54R | 34 | m110 |
| AKM (`akm`) | rifle | 7.62x39mm | 33 | m4a1 |
| Glock 17 (`glock17`) | pistol | 9x19mm | 28 | m17 |
| PM Makarov (`pm_makarov`) | pistol | 9x18mm | 22 | m17 |
| M4 carbine (`m4`) | carbine | 5.56x45mm | 20 | mk18 |
| AKMS (folding stock) (`akms`) | carbine | 7.62x39mm | 18 | mk18 |
| FN Minimi (`minimi`) | lmg | 5.56x45mm | 18 | m4a1 |
| Barrett M82A1 (`m82a1`) | amr | 12.7x99mm (.50 BMG) | 17 | m110 |
| Type 56 (`type56`) | rifle | 7.62x39mm | 16 | m4a1 |
| FN MAG 58 (`mag58`) | gpmg | 7.62x51mm | 15 | m4a1 |
| RPK (`rpk`) | lmg | 7.62x39mm | 13 | m4a1 |
| AK-47 / Type 56 pattern (`ak47`) | rifle | 7.62x39mm | 12 | m4a1 |
| M107A1 (`m107a1`) | amr | 12.7x99mm (.50 BMG) | 11 | m110 |
| MG3 (`mg3`) | gpmg | 7.62x51mm | 10 | m4a1 |
| AKS-74U (`aks74u`) | carbine | 5.45x39mm | 9 | mk18 |
| M249 SAW (`m249`) | lmg | 5.56x45mm | 9 | m4a1 |
| AK-74 / AKS-74 (`ak74`) | rifle | 5.45x39mm | 7 | m4a1 |
| HK417 (`hk417`) | dmr | 7.62x51mm | 7 | m110 |
| M16A4 (`m16a4`) | rifle | 5.56x45mm | 7 | m4a1 |
| M24 SWS (`m24`) | sniper | 7.62x51mm | 7 | m110 |
| M240B/L (`m240b`) | gpmg | 7.62x51mm | 7 | m4a1 |
| HK G3A3 (`g3a3`) | br | 7.62x51mm | 6 | m4a1 |
| M16A2 (`m16a2`) | rifle | 5.56x45mm | 6 | m4a1 |
| RPK-74 (`rpk74`) | lmg | 5.45x39mm | 6 | m4a1 |
| HK G36 (`g36`) | rifle | 5.56x45mm | 5 | m4a1 |
| SR-25 / KAC DMR (`sr25`) | dmr | 7.62x51mm | 5 | m110 |
| Sako TRG-42 (`trg42`) | sniper | .338 Lapua Magnum | 5 | m110 |
| AK-12 (`ak12`) | rifle | 5.45x39mm | 4 | m4a1 |
| AK-74M (`ak74m`) | rifle | 5.45x39mm | 4 | m4a1 |
| AM-50 Sayyad (`am50`) | amr | 12.7x99mm (.50 BMG) | 4 | m110 |
| AR-15 / M4-pattern rifle (commercial or captured) (`ar15_pattern`) | carbine | 5.56x45mm | 4 | mk18 |
| M60 (`m60`) | gpmg | 7.62x51mm | 4 | m4a1 |
| FN Minimi 7.62 Mk3 (`minimi_762`) | gpmg | 7.62x51mm | 4 | m4a1 |
| Steyr HS .50 (`steyr_hs50`) | amr | 12.7x99mm (.50 BMG) | 4 | m110 |
| Orsis T-5000 (`t5000`) | sniper | .338 Lapua Magnum | 4 | m110 |
| Accuracy International AW (`ai_aw`) | sniper | 7.62x51mm | 3 | m110 |
| Accuracy International AXMC (`axmc`) | sniper | .338 Lapua Magnum | 3 | m110 |
| HK G28 (`g28`) | dmr | 7.62x51mm | 3 | m110 |
| HK G36K (`g36k`) | carbine | 5.56x45mm | 3 | mk18 |

The other 198 weapons to build are used by 3 factions or fewer each; see weapons_index.json.

## Conventions

- Ids are stable snake_case and reuse `tools/loadouts_catalog_wip.pl` (one WIP id was dropped: `m110_sniper`, a duplicate of `m110`).
- `game_item_id` is set only where the item exists in the game repo; armor, grenades and medical items map to the generic game item of their kind. `game_substitute` names the existing item that stands in until the real one is built.
- Launchers: `in_game` is true when the launcher is one of the 6 design-doc launchers (AT4, RPG-7, Javelin, MAAWS, NLAW, SMAW); otherwise `game_substitute` names one of the 6 (MANPADS have none).
- `count` is the total carried, including the magazine in the weapon.
- `role_map` maps every role used by the faction's unit_templates that has no loadout of its own to the role whose loadout it uses.
- Roles a faction does not field are marked `not_fielded` with a `stand_in_role` (only pse_pa: at and sniper).
- `proposed_round_id` (in `ammo`) points at a rounds_index.json spec wherever `game_round_id` is missing or only a generic match; `proposed_game_item_id` gives the proposed items.json id for the 6 in-game launchers and their rounds; `proposed_game_id` marks other new items (plate_steel_light, signal smokes, cosmetic helmets).

