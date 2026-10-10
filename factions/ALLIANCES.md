# Alliances and relations

As of October 2026. Machine-readable source: [alliances.json](alliances.json) (alliances, proposed game rules and the full 77 x 77 relations matrix). Faction files keep their notable `relations`; the matrix is the single source of truth. Each faction's `blocs` lists exactly the alliances it belongs to (any member status); descriptive tags moved to a `traits` list.

## Alliances

Member status is full unless marked. Game effect: war_join / side_lock / rep_spill (all proposals).

### Military alliance

- **North Atlantic Treaty Organization** (`nato`): usa, gbr, can, fra, deu, ita, esp, nld, bel, nor, dnk, swe, fin, grc, pol, est, lva, ltu, rou, tur.
  - Obligation: Article 5 collective defence: an armed attack on one member in Europe or North America is an attack on all.
  - Game: war_join auto, side_lock yes, rep_spill 0.5.
  - Notes: 32 members in 2026; 20 are in the roster. Finland joined in April 2023 and Sweden in March 2024. Non-roster members include Albania, Bulgaria, Croatia, Czechia, Hungary, Iceland, Luxembourg, Montenegro, North Macedonia, Portugal, Slovakia and Slovenia. tur is a full member but its relations with several allies (grc, the sdf issue) are strained; war_join for tur is still auto by treaty. Partner states are modelled in nato_partnership_for_peace, not here. Ukraine and Georgia are aspirants (2008 Bucharest declaration) with no accession timetable.
- **Collective Security Treaty Organization** (`csto`): rus, blr, kaz, arm (suspended).
  - Obligation: Article 4 collective defence: aggression against one member is aggression against all.
  - Game: war_join likely, side_lock yes, rep_spill 0.5.
  - Notes: Non-roster members: Kyrgyzstan and Tajikistan. Armenia froze its participation in February 2024, has paid no contributions for two years and its prime minister said in August 2026 that Armenia will not return within five years; it has not formally withdrawn (member_status suspended, war_join never applies to it). The CSTO intervened in Kazakhstan in January 2022 but did not act for Armenia in 2021-2022. Replaces the csto_suspended tag.
- **Alliance of Sahel States (Confederation of Sahel States)** (`aes`): sahel_aes, africa_corps (partner).
  - Obligation: Liptako-Gourma Charter (2023): an attack on one is an attack on all; confederation since July 2024 with a unified force.
  - Game: war_join auto, side_lock yes, rep_spill 0.5.
  - Notes: Mali, Burkina Faso and Niger are modelled together as sahel_aes. africa_corps is a partner (Russian state contractor working for the juntas), not a member. The three left ECOWAS in January 2025.
- **Joint Expeditionary Force** (`jef`): gbr, dnk, est, fin, lva, ltu, nld, nor, swe.
  - Obligation: UK-led high-readiness force framework; no treaty defence commitment beyond NATO.
  - Game: war_join possible, side_lock yes, rep_spill 0.3.
  - Notes: Non-roster member: Iceland.

### Strategic partnership

- **NATO Partnership for Peace** (`nato_partnership_for_peace`): arm, aut, aze, che, geo, irl, kaz, mda, srb, ukr.
  - Obligation: Bilateral cooperation programmes with NATO; no defence commitment either way.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Roster participants only. Russia and Belarus are formal participants whose cooperation with NATO is suspended or dormant; they are left out for game purposes. Ukraine also has the NATO-Ukraine Council, and Georgia and Ukraine are NATO aspirants. Replaces the free-form tags nato_partner and nato_partnership_for_peace.
- **AUKUS** (`aukus`): usa, gbr, aus.
  - Obligation: Trilateral security and technology partnership: Pillar I nuclear-powered submarines for Australia, Pillar II advanced capabilities. It has no mutual-defence clause.
  - Game: war_join possible, side_lock yes, rep_spill 0.3.
  - Notes: The handoff sheet suggested kind defence_treaty; AUKUS contains no mutual-defence obligation, so it is modelled as a strategic partnership. Defence ties among the three come from anzus and nato.
- **Quadrilateral Security Dialogue** (`quad`): usa, jpn, ind, aus.
  - Obligation: Diplomatic and security dialogue; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
- **Taiwan Relations Act (US law, 1979)** (`taiwan_relations_act`): usa, twn.
  - Obligation: US law, not a treaty: the US provides defensive arms and maintains the capacity to resist force against Taiwan. No defence commitment (strategic ambiguity).
  - Game: war_join possible, side_lock yes, rep_spill 0.3.
  - Notes: Modelled at partnership level because there is no treaty; the US has no diplomatic relations with Taiwan.
- **US Major Non-NATO Ally designation** (`major_non_nato_ally_us`): usa, aus (partner), egy (partner), isr (partner), jpn (partner), jor (partner), kor (partner), nzl (partner), pak (partner), phl (partner), qat (partner), sau (partner), twn (de_facto).
  - Obligation: US designation easing arms sales, defence-research cooperation and war-reserve stockpiles; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: usa is the designating state; others are partners. Saudi Arabia was designated in November 2025. Taiwan is treated as a major non-NATO ally under US law without formal designation (member_status de_facto). Non-roster designees include Argentina, Bahrain, Brazil, Colombia, Kenya, Kuwait, Morocco, Thailand and Tunisia.
- **Nordic Defence Cooperation** (`nordefco`): nor, dnk, swe, fin.
  - Obligation: Defence cooperation; no separate defence commitment (all four are NATO members).
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Non-roster member: Iceland.

### Political bloc

- **European Union** (`eu`): fra, deu, ita, esp, nld, bel, dnk, swe, fin, grc, pol, est, lva, ltu, rou, aut, irl, ukr (candidate), mda (candidate), geo (candidate), srb (candidate), tur (candidate).
  - Obligation: Article 42.7 TEU mutual assistance ('obligation of aid and assistance by all the means in their power'), without prejudice to the neutrality of some members.
  - Game: war_join likely, side_lock yes, rep_spill 0.3.
  - Notes: 17 roster members are full members. Candidates (member_status candidate): ukr and mda (accession talks opened June 2024), geo (candidate since December 2023, process de facto halted by the EU in 2024), srb (talks open, slow) and tur (talks frozen since 2018). war_join applies to full members only; aut and irl are militarily neutral and contribute non-military aid. Replaces the eu_candidate tag.
- **EU Eastern Partnership** (`eastern_partnership`): arm, aze, geo, mda, ukr.
  - Obligation: EU association and partnership agreements; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Belarus suspended its participation in 2021 and is not listed. Armenia, the only member without candidate status, signed a Comprehensive and Enhanced Partnership Agreement and passed a law in 2025 to begin an EU accession process. Replaces the eu_partnership tag.
- **Shanghai Cooperation Organisation** (`sco`): chn, rus, ind, pak, kaz, irn, blr.
  - Obligation: Security and political cooperation; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Iran joined in 2023 and Belarus in 2024. Non-roster members: Kyrgyzstan, Tajikistan, Uzbekistan.
- **Commonwealth of Independent States** (`cis`): rus, blr, kaz, arm, aze.
  - Obligation: Post-Soviet political forum; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Ukraine stopped participating in 2014-2018 and Georgia left in 2009. Moldova has been leaving CIS agreements and is not listed.
- **GUAM Organization for Democracy and Economic Development** (`guam`): geo, ukr, aze, mda.
  - Obligation: Political and economic cooperation; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Largely dormant at summit level.
- **Organization of Turkic States** (`organization_of_turkic_states`): tur, aze, kaz.
  - Obligation: Political and cultural cooperation; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Non-roster members: Kyrgyzstan, Uzbekistan. Observers include Hungary and Turkmenistan.
- **Gulf Cooperation Council** (`gcc`): sau, are, qat.
  - Obligation: Joint Defence Agreement (2000) and the Peninsula Shield Force; political and economic union.
  - Game: war_join possible, side_lock yes, rep_spill 0.3.
  - Notes: Non-roster members: Bahrain, Kuwait, Oman. The 2017-2021 Qatar blockade shows the limits of cohesion.
- **Arab League** (`arab_league`): are, egy, irq, jor, pse_pa, qat, sau, som, syr.
  - Obligation: Joint Defence and Economic Cooperation Treaty (1950), rarely invoked.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Syria was readmitted in May 2023. Palestine is represented by the PLO/State of Palestine (pse_pa).
- **Abraham Accords** (`abraham_accords`): isr, are, kaz.
  - Obligation: Normalisation of relations with Israel; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Non-roster members: Bahrain, Morocco (Sudan signed the declaration). Kazakhstan joined in November 2025, a largely symbolic step since it already had full relations with Israel. Egypt (1979) and Jordan (1994) have separate peace treaties with Israel, modelled as relations only.
- **Global Coalition to Defeat ISIS** (`global_coalition_against_isis`): usa, gbr, can, aus, nzl, fra, deu, ita, esp, nld, bel, nor, dnk, swe, fin, grc, pol, est, lva, ltu, rou, tur, jpn, kor, twn, aut, irl, ukr, geo, mda, sau, are, qat, egy, jor, irq, som, syr, sdf (partner), krg_peshmerga (partner).
  - Obligation: Political coalition of 90 members (Syria became the 90th in November 2025); military operations are run by members, not the coalition.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Roster members listed as far as verified; the full partner list was not re-checked line by line (phl and srb membership not verified, left out). sdf and krg_peshmerga are not members: they are partner forces on the ground (member_status partner). Syria's accession is a political declaration without military provisions.
- **Islamic Military Counter Terrorism Coalition** (`islamic_military_counter_terrorism_coalition`): sau, are, egy, jor, tur, pak, som, pse_pa.
  - Obligation: Saudi-led counter-terrorism coordination centre in Riyadh; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Roster members from the original 2015 founding list. Qatar's status since the 2017 Gulf crisis is unclear and it is left out; Mali, Burkina Faso and Niger are members as states, but the sahel_aes faction is not listed.
- **African Union** (`african_union`): egy, som, sahel_aes (suspended).
  - Obligation: Political union; the Peace and Security Council mandates missions such as AUSSOM in Somalia.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Mali, Burkina Faso and Niger (sahel_aes) are suspended after their coups (member_status suspended).
- **Association of Southeast Asian Nations** (`asean`): phl, vnm.
  - Obligation: Political and economic association; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Both claim parts of the South China Sea against China.
- **Nordic-Baltic Eight** (`nb8`): dnk, est, fin, lva, ltu, nor, swe.
  - Obligation: Regional cooperation format; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Non-roster member: Iceland.
- **Bucharest Nine** (`bucharest_nine`): pol, rou, est, lva, ltu.
  - Obligation: NATO eastern-flank coordination format; no separate commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Non-roster members: Bulgaria, Czechia, Hungary, Slovakia.
- **Weimar Triangle** (`weimar_triangle`): fra, deu, pol.
  - Obligation: Consultation format; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
- **Benelux Union** (`benelux`): bel, nld.
  - Obligation: Economic and political union; no separate defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Non-roster member: Luxembourg.
- **E3 (France, Germany, United Kingdom)** (`e3`): fra, deu, gbr.
  - Obligation: Diplomatic format, chiefly on Iran's nuclear programme (snapback of UN sanctions in 2025).
  - Game: war_join none, side_lock no, rep_spill 0.15.
- **Group of Seven** (`g7`): usa, gbr, can, fra, deu, ita, jpn.
  - Obligation: Economic and political forum; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: The EU also takes part.
- **UN Security Council permanent members** (`un_security_council_p5`): usa, gbr, fra, rus, chn.
  - Obligation: Permanent seats and veto power in the UN Security Council.
  - Game: war_join none, side_lock no, rep_spill 0.0.
  - Notes: Descriptive grouping with no alliance effect; rep_spill 0.

### Intelligence alliance

- **Five Eyes (UKUSA Agreement)** (`five_eyes`): usa, gbr, can, aus, nzl.
  - Obligation: Signals-intelligence sharing under the UKUSA Agreement; no defence commitment of its own.
  - Game: war_join none, side_lock yes, rep_spill 0.3.
  - Notes: Kind intelligence_alliance as named in the handoff sheet (not in the base kind list). Defence commitments among these five come from nato and anzus.

### Defence treaty

- **ANZUS Treaty** (`anzus`): usa, aus, nzl (suspended).
  - Obligation: Each party would 'act to meet the common danger' in the event of an armed attack in the Pacific.
  - Game: war_join likely, side_lock yes, rep_spill 0.5.
  - Notes: The US suspended its ANZUS obligations toward New Zealand in 1986 over nuclear-free legislation (member_status suspended); the treaty remains in force between the US and Australia. US-NZ defence cooperation has since been rebuilt under the Wellington (2010) and Washington (2012) declarations.
- **Union State of Russia and Belarus** (`union_state`): rus, blr.
  - Obligation: Treaty on Security Guarantees (December 2024), including Russian nuclear protection of Belarus.
  - Game: war_join auto, side_lock yes, rep_spill 0.5.
  - Notes: Russian tactical nuclear weapons are stationed in Belarus (2023).
- **Russia-DPRK Comprehensive Strategic Partnership Treaty (2024)** (`rus_prk_treaty`): rus, prk.
  - Obligation: Article 4: immediate military assistance if either party is attacked.
  - Game: war_join auto, side_lock yes, rep_spill 0.5.
  - Notes: North Korean troops fought for Russia in the Kursk region in 2024-2025, and North Korea supplies artillery ammunition and missiles.
- **Sino-North Korean Treaty of Friendship (1961)** (`chn_prk_treaty`): chn, prk.
  - Obligation: Article II: immediate military and other assistance if either party is attacked.
  - Game: war_join likely, side_lock yes, rep_spill 0.5.
  - Notes: Renewed automatically every 20 years; China's willingness to honour it in practice is debated, hence likely rather than auto.
- **Shusha Declaration on Allied Relations (Türkiye-Azerbaijan, 2021)** (`tur_aze`): tur, aze.
  - Obligation: Mutual assistance if either faces a threat or attack from a third state.
  - Game: war_join likely, side_lock yes, rep_spill 0.5.
- **Mecca Joint Defence Agreement (Saudi Arabia, Türkiye, Pakistan, 2026)** (`mecca_joint_defence_agreement`): sau, tur, pak.
  - Obligation: Collective defence among the three signatories; on 5 October 2026 the partners agreed to activate collective-defence deployments in Saudi Arabia.
  - Game: war_join likely, side_lock yes, rep_spill 0.5.
  - Notes: Signed 7 August 2026, building on the Saudi-Pakistani Strategic Mutual Defence Agreement of 17 September 2025 (an attack on either is an attack on both). Recorded from the research in sau.json and tur.json.
- **Five Power Defence Arrangements** (`fpda`): gbr, aus, nzl.
  - Obligation: Consultation if Malaysia or Singapore is attacked; no commitment among the roster members themselves.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Non-roster members: Malaysia, Singapore.

### Bilateral treaty

- **US-Japan Treaty of Mutual Cooperation and Security (1960)** (`us_jpn_treaty`): usa, jpn.
  - Obligation: Article V: each party would act to meet an armed attack on territories under Japan's administration.
  - Game: war_join auto, side_lock yes, rep_spill 0.5.
  - Notes: US forces are based in Japan.
- **US-ROK Mutual Defense Treaty (1953)** (`us_kor_treaty`): usa, kor.
  - Obligation: Article III: each party would act to meet an armed attack in the Pacific area on the other's territories.
  - Game: war_join auto, side_lock yes, rep_spill 0.5.
  - Notes: US Forces Korea are based on the peninsula.
- **US-Philippines Mutual Defense Treaty (1951)** (`us_phl_treaty`): usa, phl.
  - Obligation: Article IV: each party would act to meet an armed attack in the Pacific area on the other. The US has stated that it covers armed attacks on Philippine forces, vessels and aircraft in the South China Sea.
  - Game: war_join likely, side_lock yes, rep_spill 0.5.

### Economic bloc

- **BRICS** (`brics`): rus, chn, ind, irn, egy, are, kaz (partner), blr (partner), vnm (partner).
  - Obligation: Economic and political forum; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Full members in the roster: rus, chn, ind, irn, egy, are (plus Brazil, South Africa, Ethiopia and Indonesia). Partner countries (member_status partner): kaz and blr (since January 2025) and vnm (2025). Saudi Arabia's status is ambiguous: BRICS lists it as a member but Riyadh has not confirmed joining, so it is not listed here.
- **Eurasian Economic Union** (`eaeu`): rus, blr, kaz, arm.
  - Obligation: Customs union and single market; no defence commitment.
  - Game: war_join none, side_lock no, rep_spill 0.15.
  - Notes: Non-roster member: Kyrgyzstan.

### Axis

- **Axis of Resistance** (`axis_of_resistance`): irn, hezbollah, houthis, iraqi_militias, hamas, pij.
  - Obligation: Informal Iran-led network: Iranian funding, weapons, training (IRGC Quds Force) and coordinated campaigns; no treaty.
  - Game: war_join likely, side_lock yes, rep_spill 0.3.
  - Notes: Syria left it with the fall of Assad (December 2024). Degradation by October 2026: hamas heavily degraded (Gaza war; ceasefire since October 2025, disarmament framework pending); pij heavily degraded; hezbollah degraded (2024 war, leadership losses, Syrian supply line lost; re-entered war March 2026, Israel occupies much of south Lebanon); iraqi_militias intact but under US strikes and Iraqi disarmament pressure; houthis the least degraded (joined Iran's 2026 war, Bab al-Mandab escalation September 2026); irn at war with the US and Israel since 28 February 2026. Terrorist members are hostile-only to the player; war_join here means 'surge activity', per game_rules.war_join.

### Peacekeeping

- **UN Interim Force in Lebanon** (`unifil`): aut, chn, deu, esp, fin, fra, ind, irl, ita, kaz, kor, pol, srb.
  - Obligation: UN peacekeeping mandate in south Lebanon; the Security Council (August 2025) set the mandate to end on 31 December 2026, with withdrawal during 2027.
  - Game: war_join none, side_lock no, rep_spill 0.0.
  - Notes: Roster troop contributors in lebanon_south (kaz serves with the Indian battalion; deu leads the Maritime Task Force). Neutral: never side-locks and never joins wars. Peacekeepers appear on lebanon_south maps as neutral units.

### Terror network

- **al-Qaeda and affiliates** (`al_qaeda_network`): al_qaeda, aqap, al_shabaab, jnim.
  - Obligation: Pledges of allegiance (bay'ah) to the al-Qaeda leadership.
  - Game: war_join none, side_lock yes, rep_spill 0.3.
  - Notes: Hostile-only to the player. Fights islamic_state_network wherever they overlap (Sahel, Somalia, Yemen). Terror networks never join wars; they surge activity (game_rules.war_join).
- **Islamic State and provinces** (`islamic_state_network`): isis, isis_k.
  - Obligation: Provinces (wilayat) under the Islamic State's central leadership.
  - Game: war_join none, side_lock yes, rep_spill 0.3.
  - Notes: The handoff sheet called this isis_network; the id already used in the faction files (islamic_state_network) is kept. isis covers the Iraq/Syria core plus the Sahel and Somalia provinces. Fights al_qaeda_network and afg_taliban.

## Proposed game rules

All of these are proposals for the design doc (`game_rules` in alliances.json).

- **Side-lock.** Taking a contract against faction X locks the player out of X's contracts, and out of the contracts of every faction whose relation toward the client is -50 or worse. The lock lasts 3 to 10 in-game days, scaled by how severe the contract is. Peacekeeping (UNIFIL) and neutral humanitarian clients (che, aut, irl) never lock.
- **War joining.** When a full member of an alliance is attacked, partners with `war_join: auto` join the simulated war (NATO Article 5, the Union State, the Russia-DPRK treaty, the US treaties with Japan and Korea, the AES). `likely` partners join with probability 0.6 (0.9 at relation +70 or more); `possible` partners join only at relation +70 or more. Suspended, partner, candidate and observer members never trigger or answer it. Terror networks never join wars; they surge activity instead.
- **Reputation spill-over.** Reputation gained or lost with X spreads to each other faction Y as `rep_delta * clamp(relation(Y, X) / 100, -1, 1) * alliance_factor`, with alliance_factor 0.5 for a shared defence treaty or military alliance, 0.3 for another shared alliance and 0.15 otherwise. Negative relations invert it: helping X angers X's enemies.
- **Selling to the player.** Only factions with `player_trade.sellable` true sell: usa, gbr and can (decided), che and aut as arms markets at rep 20/40/60 and krg_peshmerga basic kit at rep 30/50 (Captain-confirmed 2026-10-10), plus the proposals in other files. Selling needs relation +40 or more plus the rep tier; che and aut sell on rep tier alone as neutral markets. Terror groups, cartels, rival PMCs and africa_corps never sell.

## Relations among the major powers

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

## How the matrix was built

1. **File values first.** Every value a faction file lists is kept as that faction's view.
2. **Symmetry.** Where both files list a pair they already agreed in sign and within 30 points, except aze-geo (40 vs 75), set to the rounded mean 58 both ways.
3. **Mirrors.** Where only one file listed a pair (694 entries), the same value was used both ways and written into the other file. This filled the known gaps: the European, Baltic and Asian states' entries for the terror groups, the Nordic/Benelux/Southern European entries for afg_taliban, sdf, krg_peshmerga and sahel_aes, usa's entries for the three PMCs, the terror files' entries for the PMCs and neutral states, and player's entries for che, aut, irl, mex and prk.
4. **Gaps.** The 1,450 pairs no file listed were filled from an explicit list of judged pairs (341), group rules for terror groups, cartels, PMCs and non-state forces (857), and a formula for the remaining state pairs with no strong ties (252): `10 + 35 * west(a) * west(b)`, rounded to 5, with floors for shared alliances. These values are proposals and live only in alliances.json.
5. **Checks.** Every pair agrees in sign and is within 30 points; terror groups are -80 or worse toward the player, never clients and never sellers.

## Changes made to faction files

All 77 faction files were edited in place (load, change, write back with the same 2-space format and key order). Only `relations`, `blocs` and a new `traits` list changed, except for the Captain's decisions listed after the table.

| File | Relations added | Changed values | Blocs / traits |
|---|---|---|---|
| player | 41 | afg_taliban: -70 -> -10 |  |
| usa | 24 |  | blocs updated |
| gbr | 25 |  | blocs updated |
| can | 13 |  | blocs updated |
| aus | 12 |  | blocs updated |
| nzl | 0 |  | blocs updated |
| fra | 12 |  | blocs updated |
| deu | 6 |  | blocs updated |
| ita | 4 |  | blocs updated |
| esp | 0 |  | blocs updated |
| nld | 1 |  | blocs updated |
| bel | 0 |  | blocs updated |
| nor | 0 |  | blocs updated |
| dnk | 0 |  | blocs updated |
| swe | 1 |  | blocs updated |
| fin | 1 |  | blocs updated |
| grc | 0 |  | blocs updated |
| ukr | 5 |  | blocs updated |
| pol | 2 |  | blocs updated |
| est | 4 |  | blocs updated |
| lva | 2 |  | blocs updated |
| ltu | 4 |  | blocs updated |
| rou | 5 |  | blocs updated |
| mda | 0 |  | blocs updated, traits [constitutionally_neutral] |
| geo | 1 | aze: 75 -> 58 | blocs updated |
| rus | 20 |  | blocs updated |
| blr | 17 |  | blocs updated |
| africa_corps | 18 |  | blocs updated, traits [russian_state_expeditionary] |
| kaz | 2 |  | blocs updated |
| srb | 2 |  | blocs updated, traits [csto_pa_observer, militarily_neutral] |
| arm | 1 |  | blocs updated |
| aze | 2 | geo: 40 -> 58 | blocs updated, traits [non_aligned_movement] |
| chn | 27 |  | blocs updated |
| prk | 18 |  | blocs updated |
| jpn | 11 |  | blocs updated |
| kor | 13 |  | blocs updated |
| twn | 0 |  | blocs updated |
| ind | 3 |  | blocs updated |
| pak | 0 |  | blocs updated |
| phl | 1 |  | blocs updated |
| vnm | 0 |  | blocs updated |
| irn | 21 |  |  |
| isr | 19 |  | blocs updated |
| tur | 17 |  | blocs updated, traits [g20] |
| sau | 12 |  | blocs updated, traits [g20] |
| are | 13 |  | blocs updated |
| qat | 11 |  | blocs updated |
| egy | 7 |  | blocs updated |
| jor | 7 |  | blocs updated |
| syr | 11 | sdf: -20 -> 10 |  |
| irq | 10 |  |  |
| pse_pa | 9 |  | blocs updated, traits [plo] |
| hamas | 15 |  |  |
| pij | 14 |  |  |
| hezbollah | 17 |  |  |
| houthis | 18 |  |  |
| iraqi_militias | 17 |  |  |
| al_qaeda | 29 |  |  |
| aqap | 16 |  |  |
| isis | 26 |  |  |
| isis_k | 17 |  |  |
| al_shabaab | 15 |  |  |
| jnim | 16 |  |  |
| che | 0 |  | blocs updated, traits [neutral, efta, schengen] |
| aut | 0 |  | blocs updated, traits [neutral, schengen, european_sky_shield] |
| irl | 0 |  | blocs updated, traits [neutral, un_peacekeeping] |
| mex | 0 |  | blocs updated, traits [usmca, oas, g20] |
| cartel_pacifico | 2 |  | blocs updated, traits [cartel] |
| cartel_jalisco_nueva | 2 |  | blocs updated, traits [cartel] |
| afg_taliban | 11 | player: -65 -> -10 | blocs updated, traits [de_facto_government] |
| sdf | 9 | syr: -15 -> 10 |  |
| krg_peshmerga | 7 |  |  |
| sahel_aes | 9 |  | blocs updated |
| som | 0 |  | blocs updated |
| pmc_halcyon | 5 |  | blocs updated, traits [rival_pmc] |
| pmc_kestrel | 7 |  | blocs updated, traits [rival_pmc] |
| pmc_black_sable | 7 |  | blocs updated, traits [rival_pmc] |

Tag normalisation: `csto_suspended` became `csto` (arm suspended); `eu_candidate` became `eu` (candidate); `eu_partnership` became `eastern_partnership`; `nato_partner` became `nato_partnership_for_peace`. Descriptive tags moved to `traits`: neutral, constitutionally_neutral, militarily_neutral, schengen, efta, european_sky_shield, un_peacekeeping, g20, usmca, oas, plo, non_aligned_movement, csto_pa_observer, de_facto_government, russian_state_expeditionary, rival_pmc and cartel. Where a file's `proposed` list said "blocs (... is a game tag)", it now says "traits (...)".

Captain's decisions applied in the same pass (2026-10-10; details in [factions_handoff.md](../docs/factions_handoff.md)):

- afg_taliban: limited client (player_client true, alignment neutral, relation with player -10 both ways, three as_client contracts), still never sells; its Ranger pickups moved to the new `ford_ranger` catalogue file.
- syr and sdf: +10 each way (were -20 and -15).
- iraqi_militias: campaign_tier early. hezbollah and houthis stay mid.
- pmc_black_sable is the nemesis; pmc_halcyon is an ordinary rival.
- che, aut and krg_peshmerga trade, sahel_aes client terms, syr/irq/pse_pa client roles, the isis provinces and captured-vehicle set pieces, and the single-source al_qaeda/houthis/aqap/al_shabaab values were moved out of `proposed` and noted as Captain-confirmed.
- mex patrol pickups now point at `ford_ranger` (Ford/Ram patrol pickups as its variant).

## Open questions for Captain

- Side-lock length: is a 3-10 in-game-day range right?
- Should NATO allies outside the Five Eyes (for example pol or fra) sell to the player at high reputation? Default no; several European files still carry `sellable: true` as their own proposal.
- Should reputation spill-over apply across the whole matrix or only within alliances? Default: the whole matrix, weighted.
- Israel and the Gulf states: client-only, or also sellers? Default client-only.
- player vs the rival PMCs is -20 to -45 in the files (handoff guidance said about -60), and player vs the cartels is -60 to -65 (guidance about -80). Kept as written; raise them?
- afg_taliban vs pak stays -65 / -60. afg_taliban.json describes an open border war since February 2026, but a ceasefire in mid-2026 could not be confirmed either way; at active-war level it would be -90.
- Membership lists for global_coalition_against_isis and the Islamic Military Counter Terrorism Coalition were verified for the main members only (phl and srb left out of the coalition; qat left out of the IMCTC). They have no war_join or side_lock effect.
