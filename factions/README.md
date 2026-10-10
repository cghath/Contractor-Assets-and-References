# Factions

Real-world-inspired factions for Contractor, as of October 2026: 77 ids (the player PMC plus 76 others). States and the real terrorist organisations use real names; cartels and rival PMCs are fictional. The Contractor design doc wins wherever it disagrees with this pack, and anything invented for gameplay is listed in each file's `proposed`.

- `factions/<id>.json`: one file per faction (schema below).
- [alliances.json](alliances.json): 47 alliances, treaties and blocs, proposed game rules (side-lock, war joining, reputation spill-over, selling) and the full 77 x 77 relations matrix.
- [ALLIANCES.md](ALLIANCES.md): the same in plain words, with the change log and open questions.
- Vehicles live in `../reference/vehicles/` and theatres in `../worldspaces/`. Validate with `python3 tools/validate_pack.py`.

## Faction file schema (short)

- Identity: `id`, `name`, `short`, `kind` (state, non_state, pmc, criminal), `inspired_by` (fictional factions), `flag_colors`.
- Politics: `blocs` (alliance ids from alliances.json), `traits` (descriptive tags), `campaign_tier`, `alignment_to_player`, `player_client`, `relations` (notable ones, -100..100; the full matrix is in alliances.json).
- World: `theatres`, `languages`, `callout_language`.
- Fighting: `doctrine` (summary, squad size, tactics, `ai_tuning` 0-1), `camo`, `small_arms` by role, `launchers`, `body_armor`, `vehicles` (catalogue ids with role and prevalence), `unit_templates`, `support_assets`.
- Economy: `player_trade` (sellable, rep tiers), `contract_types` (as_client, as_target).
- `notes`, `proposed`, `sources`; rival PMCs also have a `rivalry` object.

## Roster

| id | Name | Bloc | Tier | Alignment to player | Client | Theatres |
|---|---|---|---|---|---|---|
| player | Contractor Company (player PMC) | Player | early | friendly | no | all |
| usa | United States of America | US and Five Eyes | early | friendly | yes | levant_syria, mesopotamia, persian_gulf_coast, yemen_red_sea, horn_of_africa, baltic_coast, suwalki_gap, arctic_north, korean_dmz, taiwan_strait, south_china_sea, mexico_cartel_belt |
| gbr | United Kingdom | US and Five Eyes | early | friendly | yes | levant_syria, mesopotamia, persian_gulf_coast, yemen_red_sea, baltic_coast, arctic_north |
| can | Canada | US and Five Eyes | early | friendly | yes | baltic_coast, suwalki_gap, arctic_north, mesopotamia, levant_syria |
| aus | Australia | US and Five Eyes | mid | friendly | yes | south_china_sea, korean_dmz, persian_gulf_coast, mesopotamia |
| nzl | New Zealand | US and Five Eyes | mid | friendly | yes | south_china_sea, korean_dmz, mesopotamia, levant_syria |
| fra | France | Western Europe and Nordics | early | friendly | yes | sahel, horn_of_africa, lebanon_south, levant_syria, mesopotamia, persian_gulf_coast, yemen_red_sea, baltic_coast, black_sea_coast, alpine_europe |
| deu | Germany | Western Europe and Nordics | mid | friendly | yes | baltic_coast, suwalki_gap, mesopotamia, lebanon_south, yemen_red_sea, alpine_europe |
| ita | Italy | Western Europe and Nordics | early | friendly | yes | lebanon_south, mesopotamia, yemen_red_sea, horn_of_africa, black_sea_coast, baltic_coast, alpine_europe |
| esp | Spain | Western Europe and Nordics | early | friendly | yes | lebanon_south, mesopotamia, horn_of_africa, baltic_coast, sahel |
| nld | Netherlands | Western Europe and Nordics | mid | friendly | yes | baltic_coast, suwalki_gap, mesopotamia |
| bel | Belgium | Western Europe and Nordics | mid | friendly | yes | baltic_coast, black_sea_coast, mesopotamia, sahel |
| nor | Norway | Western Europe and Nordics | late | friendly | yes | arctic_north, baltic_coast, mesopotamia |
| dnk | Denmark | Western Europe and Nordics | mid | friendly | yes | arctic_north, baltic_coast, mesopotamia, yemen_red_sea |
| swe | Sweden | Western Europe and Nordics | late | friendly | yes | arctic_north, baltic_coast |
| fin | Finland | Western Europe and Nordics | late | friendly | yes | arctic_north, baltic_coast, lebanon_south |
| grc | Greece | Western Europe and Nordics | early | friendly | yes | yemen_red_sea, persian_gulf_coast, black_sea_coast |
| ukr | Ukraine | Ukraine and eastern flank | mid | friendly | yes | eastern_ukraine, black_sea_coast |
| pol | Poland | Ukraine and eastern flank | mid | friendly | yes | suwalki_gap, baltic_coast, lebanon_south, mesopotamia |
| est | Estonia | Ukraine and eastern flank | late | friendly | yes | baltic_coast, mesopotamia |
| lva | Latvia | Ukraine and eastern flank | late | friendly | yes | baltic_coast, mesopotamia |
| ltu | Lithuania | Ukraine and eastern flank | late | friendly | yes | suwalki_gap, baltic_coast, mesopotamia |
| rou | Romania | Ukraine and eastern flank | mid | friendly | yes | black_sea_coast |
| mda | Moldova | Ukraine and eastern flank | mid | friendly | yes | black_sea_coast |
| geo | Georgia | Ukraine and eastern flank | mid | neutral | yes | caucasus |
| rus | Russian Federation | Russia, CSTO, Caucasus | late | hostile | no | eastern_ukraine, black_sea_coast, baltic_coast, suwalki_gap, arctic_north, caucasus, levant_syria |
| blr | Republic of Belarus | Russia, CSTO, Caucasus | late | hostile | no | suwalki_gap, baltic_coast, eastern_ukraine |
| africa_corps | Africa Corps (Afrikansky Korpus) | Russia, CSTO, Caucasus | mid | hostile | no | sahel |
| kaz | Republic of Kazakhstan | Russia, CSTO, Caucasus | mid | neutral | yes | levant_syria, lebanon_south |
| srb | Republic of Serbia | Russia, CSTO, Caucasus | mid | neutral | yes | lebanon_south, alpine_europe |
| arm | Republic of Armenia | Russia, CSTO, Caucasus | mid | neutral | yes | caucasus |
| aze | Republic of Azerbaijan | Russia, CSTO, Caucasus | mid | neutral | yes | caucasus |
| chn | People's Republic of China | Asia-Pacific | late | hostile | no | taiwan_strait, south_china_sea, korean_dmz, kashmir_loc, afghan_highlands, horn_of_africa |
| prk | Democratic People's Republic of Korea | Asia-Pacific | late | hostile | no | korean_dmz, eastern_ukraine |
| jpn | Japan | Asia-Pacific | mid | friendly | yes | korean_dmz, taiwan_strait, south_china_sea, horn_of_africa, arctic_north |
| kor | Republic of Korea | Asia-Pacific | mid | friendly | yes | korean_dmz, persian_gulf_coast, horn_of_africa, lebanon_south |
| twn | Republic of China (Taiwan) | Asia-Pacific | late | friendly | yes | taiwan_strait, south_china_sea |
| ind | Republic of India | Asia-Pacific | mid | neutral | yes | kashmir_loc, afghan_highlands, persian_gulf_coast, yemen_red_sea |
| pak | Islamic Republic of Pakistan | Asia-Pacific | early | varies | yes | kashmir_loc, afghan_highlands, persian_gulf_coast |
| phl | Republic of the Philippines | Asia-Pacific | early | friendly | yes | south_china_sea |
| vnm | Socialist Republic of Vietnam | Asia-Pacific | mid | neutral | yes | south_china_sea |
| irn | Islamic Republic of Iran (Artesh and IRGC) | Middle East states | mid | hostile | no | iran_zagros, persian_gulf_coast, mesopotamia, lebanon_south, yemen_red_sea |
| isr | State of Israel (Israel Defense Forces) | Middle East states | mid | neutral | yes | israel, gaza_west_bank, lebanon_south, levant_syria, iran_zagros, yemen_red_sea |
| tur | Republic of Türkiye (Turkish Armed Forces) | Middle East states | mid | neutral | yes | levant_syria, mesopotamia, black_sea_coast, caucasus, horn_of_africa |
| sau | Kingdom of Saudi Arabia (Royal Saudi Land Forces and Saudi Arabian National Guard) | Middle East states | early | friendly | yes | yemen_red_sea, persian_gulf_coast |
| are | United Arab Emirates (UAE Armed Forces) | Middle East states | early | friendly | yes | persian_gulf_coast, yemen_red_sea, horn_of_africa |
| qat | State of Qatar (Qatar Armed Forces) | Middle East states | early | friendly | yes | persian_gulf_coast |
| egy | Arab Republic of Egypt (Egyptian Armed Forces) | Middle East states | mid | neutral | yes | gaza_west_bank, yemen_red_sea, horn_of_africa |
| jor | Hashemite Kingdom of Jordan (Jordanian Armed Forces - Arab Army) | Middle East states | early | friendly | yes | levant_syria, gaza_west_bank, mesopotamia |
| syr | Syrian Arab Republic (Transitional Government, Syrian Army / Ministry of Defence) | Middle East states | early | neutral | yes | levant_syria, mesopotamia, lebanon_south |
| irq | Republic of Iraq (Iraqi Security Forces) | Middle East states | early | neutral | yes | mesopotamia, levant_syria |
| pse_pa | Palestinian Authority Security Forces (State of Palestine) | Middle East states | early | neutral | yes | gaza_west_bank |
| hamas | Hamas (Izz ad-Din al-Qassam Brigades) | ME terrorist / armed groups | early | hostile | no | gaza_west_bank, israel |
| pij | Palestinian Islamic Jihad (al-Quds Brigades) | ME terrorist / armed groups | early | hostile | no | gaza_west_bank, israel |
| hezbollah | Hezbollah | ME terrorist / armed groups | mid | hostile | no | lebanon_south, israel, levant_syria |
| houthis | Houthis (Ansar Allah) | ME terrorist / armed groups | mid | hostile | no | yemen_red_sea |
| iraqi_militias | Iran-aligned Iraqi armed factions (Islamic Resistance in Iraq: Kata'ib Hezbollah, Harakat al-Nujaba and others) | ME terrorist / armed groups | early | hostile | no | mesopotamia, levant_syria |
| al_qaeda | al-Qaeda (core network) | ME terrorist / armed groups | early | hostile | no | afghan_highlands, levant_syria |
| aqap | al-Qaeda in the Arabian Peninsula | ME terrorist / armed groups | early | hostile | no | yemen_red_sea |
| isis | Islamic State (Iraq and Syria core, with Sahel and Somalia provinces) | ME terrorist / armed groups | early | hostile | no | mesopotamia, levant_syria, sahel, horn_of_africa |
| isis_k | Islamic State Khorasan Province | ME terrorist / armed groups | early | hostile | no | afghan_highlands |
| al_shabaab | al-Shabaab (Harakat al-Shabaab al-Mujahideen) | ME terrorist / armed groups | early | hostile | no | horn_of_africa |
| jnim | JNIM (Jama'at Nusrat al-Islam wal-Muslimin) | ME terrorist / armed groups | early | hostile | no | sahel |
| che | Swiss Armed Forces (Schweizer Armee) | Neutrals, Africa, cartels, PMCs | mid | neutral | yes | alpine_europe |
| aut | Austrian Armed Forces (Österreichisches Bundesheer) | Neutrals, Africa, cartels, PMCs | mid | neutral | yes | alpine_europe, lebanon_south |
| irl | Irish Defence Forces (Óglaigh na hÉireann) | Neutrals, Africa, cartels, PMCs | early | neutral | yes | lebanon_south |
| mex | Mexican Armed Forces and National Guard (SEDENA / SEMAR / Guardia Nacional) | Neutrals, Africa, cartels, PMCs | early | neutral | yes | mexico_cartel_belt |
| cartel_pacifico | Liga del Pacífico (fictional) | Neutrals, Africa, cartels, PMCs | early | hostile | no | mexico_cartel_belt |
| cartel_jalisco_nueva | Cártel Nueva Frontera (fictional) | Neutrals, Africa, cartels, PMCs | early | hostile | no | mexico_cartel_belt |
| afg_taliban | Islamic Emirate of Afghanistan armed forces (Taliban) | Neutrals, Africa, cartels, PMCs | early | neutral | yes | afghan_highlands |
| sdf | Syrian Democratic Forces (SDF) | Neutrals, Africa, cartels, PMCs | early | neutral | yes | levant_syria, mesopotamia |
| krg_peshmerga | Kurdistan Region Peshmerga (Ministry of Peshmerga Affairs) | Neutrals, Africa, cartels, PMCs | early | friendly | yes | mesopotamia, iran_zagros |
| sahel_aes | Alliance of Sahel States armed forces (Mali, Burkina Faso, Niger) | Neutrals, Africa, cartels, PMCs | early | neutral | yes | sahel |
| som | Somali National Army (SNA) | Neutrals, Africa, cartels, PMCs | early | neutral | yes | horn_of_africa |
| pmc_halcyon | Halcyon Global Risk (fictional) | Neutrals, Africa, cartels, PMCs | mid | hostile | no | mesopotamia, persian_gulf_coast, horn_of_africa, yemen_red_sea, levant_syria, mexico_cartel_belt |
| pmc_kestrel | Kestrel Security Group (fictional; 'Pustelga') | Neutrals, Africa, cartels, PMCs | mid | hostile | no | eastern_ukraine, sahel, levant_syria, caucasus, black_sea_coast |
| pmc_black_sable | Black Sable Services (fictional) | Neutrals, Africa, cartels, PMCs | mid | hostile | no | yemen_red_sea, horn_of_africa, persian_gulf_coast, sahel |

## Alliance matrix (major powers)

Symbols: `++` +50 or more, `+` +15 to +49, `0` -14 to +14, `-` -15 to -49, `--` -50 or less. Row is the row faction's view of the column; terror columns are the mean over each group. Full values are in `relations_matrix` in [alliances.json](alliances.json).

| row → col | usa | gbr | can | fra | deu | pol | ukr | rus | blr | chn | prk | irn | isr | tur | sau | player | Resistance axis | AQ network | IS network |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **usa** | · | ++ | ++ | ++ | ++ | ++ | + | -- | -- | -- | -- | -- | ++ | + | ++ | ++ | -- | -- | -- |
| **gbr** | ++ | · | ++ | ++ | ++ | ++ | ++ | -- | -- | - | -- | -- | + | + | + | ++ | -- | -- | -- |
| **can** | ++ | ++ | · | ++ | ++ | ++ | ++ | -- | -- | - | -- | -- | + | + | + | ++ | -- | -- | -- |
| **fra** | ++ | ++ | ++ | · | ++ | ++ | ++ | -- | -- | - | -- | -- | + | + | + | + | -- | -- | -- |
| **deu** | ++ | ++ | ++ | ++ | · | ++ | ++ | -- | -- | - | -- | -- | ++ | + | + | + | -- | -- | -- |
| **pol** | ++ | ++ | ++ | ++ | ++ | · | ++ | -- | -- | - | -- | -- | + | ++ | + | + | -- | -- | -- |
| **ukr** | ++ | ++ | ++ | ++ | ++ | ++ | · | -- | -- | - | -- | -- | + | + | + | + | - | -- | -- |
| **rus** | -- | -- | -- | -- | -- | -- | -- | · | ++ | ++ | ++ | ++ | 0 | + | + | -- | 0 | -- | -- |
| **blr** | - | -- | -- | -- | -- | -- | -- | ++ | · | ++ | + | + | 0 | 0 | 0 | -- | 0 | -- | -- |
| **chn** | -- | - | - | - | - | - | - | ++ | ++ | · | ++ | ++ | - | 0 | + | - | 0 | -- | -- |
| **prk** | -- | -- | -- | -- | -- | -- | -- | ++ | + | ++ | · | + | -- | - | - | -- | 0 | - | - |
| **irn** | -- | -- | -- | -- | -- | -- | -- | ++ | + | ++ | ++ | · | -- | - | -- | -- | ++ | -- | -- |
| **isr** | ++ | + | + | 0 | ++ | + | 0 | 0 | 0 | - | -- | -- | · | -- | 0 | 0 | -- | -- | -- |
| **tur** | + | + | + | 0 | + | + | + | + | 0 | 0 | - | - | -- | · | ++ | 0 | 0 | -- | -- |
| **sau** | ++ | ++ | + | + | + | + | + | + | 0 | + | - | -- | 0 | ++ | · | + | -- | -- | -- |

## Main alliances

| Alliance | Kind | Roster members |
|---|---|---|
| nato | military_alliance | usa, gbr, can, fra, deu, ita, esp, nld, bel, nor, dnk, swe, fin, grc, pol, est, lva, ltu, rou, tur |
| nato_partnership_for_peace | strategic_partnership | arm, aut, aze, che, geo, irl, kaz, mda, srb, ukr |
| eu | political_bloc | fra, deu, ita, esp, nld, bel, dnk, swe, fin, grc, pol, est, lva, ltu, rou, aut, irl, ukr (candidate), mda (candidate), geo (candidate), srb (candidate), tur (candidate) |
| eastern_partnership | political_bloc | arm, aze, geo, mda, ukr |
| five_eyes | intelligence_alliance | usa, gbr, can, aus, nzl |
| aukus | strategic_partnership | usa, gbr, aus |
| anzus | defence_treaty | usa, aus, nzl (suspended) |
| quad | strategic_partnership | usa, jpn, ind, aus |
| us_jpn_treaty | bilateral_treaty | usa, jpn |
| us_kor_treaty | bilateral_treaty | usa, kor |
| us_phl_treaty | bilateral_treaty | usa, phl |
| taiwan_relations_act | strategic_partnership | usa, twn |
| major_non_nato_ally_us | strategic_partnership | usa, aus (partner), egy (partner), isr (partner), jpn (partner), jor (partner), kor (partner), nzl (partner), pak (partner), phl (partner), qat (partner), sau (partner), twn (de_facto) |
| csto | military_alliance | rus, blr, kaz, arm (suspended) |
| union_state | defence_treaty | rus, blr |
| rus_prk_treaty | defence_treaty | rus, prk |
| chn_prk_treaty | defence_treaty | chn, prk |
| sco | political_bloc | chn, rus, ind, pak, kaz, irn, blr |
| brics | economic_bloc | rus, chn, ind, irn, egy, are, kaz (partner), blr (partner), vnm (partner) |
| cis | political_bloc | rus, blr, kaz, arm, aze |
| eaeu | economic_bloc | rus, blr, kaz, arm |
| guam | political_bloc | geo, ukr, aze, mda |
| organization_of_turkic_states | political_bloc | tur, aze, kaz |
| tur_aze | defence_treaty | tur, aze |
| mecca_joint_defence_agreement | defence_treaty | sau, tur, pak |
| gcc | political_bloc | sau, are, qat |
| arab_league | political_bloc | are, egy, irq, jor, pse_pa, qat, sau, som, syr |
| abraham_accords | political_bloc | isr, are, kaz |
| axis_of_resistance | axis | irn, hezbollah, houthis, iraqi_militias, hamas, pij |
| global_coalition_against_isis | political_bloc | usa, gbr, can, aus, nzl, fra, deu, ita, esp, nld, bel, nor, dnk, swe, fin, grc, pol, est, lva, ltu, rou, tur, jpn, kor, twn, aut, irl, ukr, geo, mda, sau, are, qat, egy, jor, irq, som, syr, sdf (partner), krg_peshmerga (partner) |
| islamic_military_counter_terrorism_coalition | political_bloc | sau, are, egy, jor, tur, pak, som, pse_pa |
| african_union | political_bloc | egy, som, sahel_aes (suspended) |
| aes | military_alliance | sahel_aes, africa_corps (partner) |
| asean | political_bloc | phl, vnm |
| jef | military_alliance | gbr, dnk, est, fin, lva, ltu, nld, nor, swe |
| nordefco | strategic_partnership | nor, dnk, swe, fin |
| nb8 | political_bloc | dnk, est, fin, lva, ltu, nor, swe |
| bucharest_nine | political_bloc | pol, rou, est, lva, ltu |
| weimar_triangle | political_bloc | fra, deu, pol |
| benelux | political_bloc | bel, nld |
| e3 | political_bloc | fra, deu, gbr |
| fpda | defence_treaty | gbr, aus, nzl |
| g7 | political_bloc | usa, gbr, can, fra, deu, ita, jpn |
| un_security_council_p5 | political_bloc | usa, gbr, fra, rus, chn |
| unifil | peacekeeping | aut, chn, deu, esp, fin, fra, ind, irl, ita, kaz, kor, pol, srb |
| al_qaeda_network | terror_network | al_qaeda, aqap, al_shabaab, jnim |
| islamic_state_network | terror_network | isis, isis_k |

## Proposals to settle

Each file's `proposed` list names its gameplay inventions. The most common, by number of files:

- `doctrine.ai_tuning`: 77 files
- `unit_templates`: 76 files
- `relations.player`: 74 files
- `campaign_tier`: 70 files
- `body_armor`: 63 files
- `vehicles[].prevalence`: 59 files
- `contract_types`: 40 files
- `alignment_to_player`: 32 files
- `player_trade.rep_tiers`: 30 files
- `player_trade`: 29 files
- `player_client`: 24 files
- `contract_types.as_target`: 21 files

Open questions for Captain are collected in [ALLIANCES.md](ALLIANCES.md) and in [docs/factions_handoff.md](../docs/factions_handoff.md).
