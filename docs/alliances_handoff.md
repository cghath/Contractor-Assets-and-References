# Alliances and the relations matrix: handoff sheet

**Status (final, 2026-10-10): done.** Job 4 wrote `factions/alliances.json` (47 alliances; 48 since Job 7 added `monusco`), `factions/ALLIANCES.md` and the relations matrix, now 80 x 80 for the 80-id roster, and reconciled every faction file. All of its open questions were answered by Captain on 2026-10-10 (below). Job 9 (final validation) lowered the usa/gbr/can selling thresholds to 5/15/30/45/60/75 (Captain-confirmed). The validator reports 0 errors and 0 warnings. The brief below is kept as written for the record.

Original brief (snapshot as of 2026-10-10 09:30 UTC). Branch `factions-worldspaces` (draft PR #2). This was job 4 of 5, run one job at a time:

1. middle_east_states
2. me_terror
3. others
4. **alliances**
5. worldspaces

It started only after all faction files existed (77 at the time, not 76 as first written; the roster has 80 since Job 7), because it reconciles all of them. Game rules are in [factions_handoff.md](factions_handoff.md).

## Why this job matters

The campaign is a persistent war, with contracts negotiated MW5-style, and alliances drive most of it:

- **Side-locking:** working for one side locks the player out of its enemies' contracts for a while. The game needs to know who counts as an "enemy" of whom.
- **War joining:** when a faction is attacked in the simulated war, its treaty partners may join. That moves fronts and posts contracts.
- **Reputation spill-over:** helping or hurting a faction moves the player's reputation with its allies and enemies.
- **Selling to the player:** the USA, GB and Canada sell gear and vehicles once the player has enough reputation. Whether other allies sell too was an open question. Answered (Captain, 2026-10-10): the non-Five-Eyes NATO members sell at rep 20/40/60/80 (tur does not), sau, are and qat at rep 40/60/80, che and aut at 20/40/60 and krg_peshmerga basic kit at 30/50; usa, gbr and can sell at 5/15/30/45/60/75.

Today each faction file carries its own `relations` (about 1,400 entries across the 41 existing files) and free-form `blocs` tags. These were written by different agents, so they aren't symmetric, and some tags are inconsistent. This job turns them into one source of truth.

## Read first, in this order

1. This sheet.
2. `CONTEXT` in [tools/factions_workflow.js](../tools/factions_workflow.js), for the canonical ids, and step 4 of the Validate prompt in the same file, for the reciprocity rule.
3. [factions_handoff.md](factions_handoff.md): settled decisions, including side-locking and the fact that terror groups are hostile only.
4. **Every** `factions/*.json`: `blocs`, `relations`, `alignment_to_player`, `player_client` and `player_trade`.
5. [tools/validate_pack.py](../tools/validate_pack.py). It already checks `factions/alliances.json`: every alliance `members` id and every `relations_matrix` key must be a canonical faction id. The file is skipped as a faction record.

## What to build

1. **`factions/alliances.json`**, with this shape:
   ```json
   {
     "as_of": "2026-10",
     "alliances": [
       {
         "id": "nato",
         "name": "North Atlantic Treaty Organization",
         "kind": "military_alliance | defence_treaty | bilateral_treaty | political_bloc | economic_bloc | strategic_partnership | axis | terror_network | peacekeeping",
         "members": ["<faction ids>"],
         "member_status": {"<faction id>": "full | suspended | observer | partner | candidate | de_facto"},
         "obligations": "real-world obligation, e.g. Article 5 collective defence",
         "game_effect": {"war_join": "auto | likely | possible | none", "side_lock": true, "rep_spill": 0.0},
         "notes": "...", "sources": ["urls"]
       }
     ],
     "game_rules": {
       "side_lock": {...}, "war_join": {...}, "rep_spillover": {...}, "player_trade": {...}
     },
     "relations_matrix": {"<faction id>": {"<faction id>": -100..100, ...}, ...},
     "proposed": ["..."],
     "sources": ["urls"]
   }
   ```
2. **`factions/ALLIANCES.md`**, a human-readable version:
   - each alliance with its members and obligations
   - the proposed game rules in plain words
   - a compact matrix for the major powers (usa, gbr, can, fra, deu, pol, ukr, rus, blr, chn, prk, irn, isr, tur, sau, plus the terror groups as one column group), using `++ + 0 - --` symbols
   - a "changes made to faction files" log and open questions
3. **Reconcile the faction files** to the matrix: their `relations` and `blocs` fields, edited in place. Keep every other field untouched.

## Alliances to model (verify the 2026 membership of each)

Members are listed by canonical id only. Non-roster members are named in `notes`.

| id | Kind | Members in the roster (verify) | Notes |
|---|---|---|---|
| nato | military_alliance | usa gbr can fra deu ita esp nld bel nor dnk swe fin grc pol est lva ltu rou tur | Article 5. Sweden joined in 2024 and Finland in 2023. |
| eu | political_bloc | fra deu ita esp nld bel dnk swe fin grc pol est lva ltu rou aut irl | Article 42.7 mutual assistance. Candidates (member_status candidate): ukr mda geo srb tur. |
| five_eyes | intelligence alliance | usa gbr can aus nzl | |
| aukus | defence_treaty | usa gbr aus | |
| anzus | defence_treaty | usa aus nzl (nzl status limited) | |
| quad | strategic_partnership | usa jpn ind aus | |
| us_bilateral | bilateral_treaty (one entry per treaty, or one with notes) | usa+jpn, usa+kor, usa+phl | Mutual defence treaties. Taiwan has the Taiwan Relations Act, not a treaty, so model it as partnership-level. |
| csto | military_alliance | rus blr kaz arm | Armenia froze its participation in 2024 (member_status suspended). Non-roster members: Kyrgyzstan, Tajikistan. |
| union_state | defence_treaty | rus blr | |
| rus_prk_treaty | defence_treaty | rus prk | The 2024 Comprehensive Strategic Partnership, with a mutual-assistance clause. |
| chn_prk_treaty | defence_treaty | chn prk | The 1961 treaty. |
| sco | political_bloc | chn rus ind pak kaz irn blr | |
| brics | economic_bloc | rus chn ind irn egy are (plus Brazil and South Africa, non-roster); sau's status is ambiguous | |
| axis_of_resistance | axis | irn hezbollah houthis iraqi_militias hamas pij | Syria left it after the fall of Assad. Mark how much each member is degraded in 2026. |
| gcc | political_bloc | sau are qat | Plus non-roster members. |
| abraham_accords | political_bloc | isr are | Plus Bahrain and Morocco. Jordan and Egypt have separate peace treaties with Israel; model them as relations, not an alliance. |
| aes | military_alliance | sahel_aes (africa_corps as partner) | The confederation of Mali, Burkina Faso and Niger. |
| cis, eaeu | political or economic bloc | rus blr kaz arm (and others) | Low game effect. |
| guam | political_bloc | geo ukr aze mda | |
| organization_of_turkic_states | political_bloc | tur aze kaz | |
| tur_aze | defence_treaty | tur aze | The 2021 Shusha Declaration. |
| jef, nordefco, bucharest_nine, weimar_triangle, nb8, benelux, fpda, e3 | regional | per the existing `blocs` tags | Low to medium game effect. |
| unifil | peacekeeping | the roster contributors in lebanon_south | Neutral. Never side-locks. |
| al_qaeda_network | terror_network | al_qaeda aqap al_shabaab jnim | Hostile only, and fights isis_network. |
| isis_network | terror_network | isis isis_k | Fights al_qaeda_network and afg_taliban. |

Existing `blocs` tags found in faction files (at this snapshot): anzus, asean, aukus, benelux, brics, bucharest_nine, cis, constitutionally_neutral, csto, csto_pa_observer, csto_suspended, e3, eaeu, eu, eu_candidate, eu_partnership, five_eyes, fpda, g7, guam, jef, militarily_neutral, nato, nato_partner, nb8, nordefco, organization_of_turkic_states, quad, russian_state_expeditionary, sco, un_security_council_p5, union_state, weimar_triangle.

Normalise these:

- `blocs` lists **alliance ids from `alliances.json`** only.
- A status such as suspended, observer, candidate or partner moves into that alliance's `member_status`. For example, `csto_suspended` becomes `csto` with `member_status.arm = "suspended"`.
- Descriptive tags such as `militarily_neutral` or `un_security_council_p5` move into a faction field `traits` (add it if needed), or into the alliance list as kind `political_bloc` if they're useful there.

## Building the relations matrix

1. **Start from the faction files.** For each ordered pair (a, b), use `a.relations[b]` where it exists. These were researched per faction.
2. **Make it symmetric where both sides exist.** If both files give a value, they should agree in sign and sit within 30 points. Otherwise set both to the rounded mean, unless one is clearly wrong; in that case fix it and log the change. The matrix may stay slightly asymmetric (a's view of b), but never more than 30 points apart, and never with opposite signs unless that's deliberate and noted.
3. **Fill the gaps from alliances.**
   - Shared defence treaty: about +70.
   - Shared alliance: about +50.
   - Strategic partners: about +40.
   - Rivals or opposed blocs: about -40 to -70.
   - Active war: -90 or below. Examples: rus-ukr, isr-hamas, isr-hezbollah where it applies in 2026, every state against IS, the Taliban against ISIS-K.
   - Everything else: 0 to ±20, by real diplomatic ties.
4. **Include the `player` row and column.**
   - usa, gbr and can: +40 to +60 (friendly; they sell with reputation).
   - Terror groups: -80 to -100.
   - Cartels: about -80.
   - Rival PMCs: about -60.
   - africa_corps: about -50.
   - Everything else is near 0, by `alignment_to_player`.
5. **Cover every pair.** The matrix has all 76 x 76 ids. The diagonal is omitted or 100.
6. **Write back to each faction file.**
   - Keep the faction file's notable `relations`, its "notable ones" list, adjusted to the matrix.
   - Add the missing reciprocal entries for strong ties (|value| >= 50).
   - Don't paste all 75 entries into every file; the full matrix lives in `alliances.json`.

## Proposed game rules (put them in `game_rules` and mark them `proposed`)

- **side_lock:**
  - Taking a contract against faction X locks the player out of X's contracts. It also locks out the contracts of everyone with a relation of -50 or below toward the client.
  - Proposed duration: 3 to 10 in-game days, scaled by contract severity.
  - Peacekeeping and neutral clients never lock.
- **war_join:**
  - When X is attacked, treaty partners with `war_join: auto` (for example NATO Article 5 or union_state) join the simulated war.
  - `likely` partners join with a probability, and `possible` partners join only if relations are +70 or higher.
  - Terror networks never "join" a war; they surge activity instead.
- **rep_spillover:**
  - Reputation gained or lost with X spreads to each other faction Y as `rep_delta * spill`, where `spill = clamp(relation(X, Y) / 100, -1, 1) * alliance_factor`.
  - Proposed `alliance_factor`: 0.5 for a shared defence treaty, 0.3 for a shared alliance, 0.15 otherwise.
  - Negative relations invert the delta: helping X angers X's enemies.
- **player_trade:**
  - Only factions with `player_trade.sellable` true sell to the player. Today that means usa, gbr, can, and possibly che and aut as arms markets.
  - Selling requires a relation of at least +40 plus the faction's rep tier.

## Checks before handing back

1. Run the validator (CI uses Python; Captain's desktop uses the Perl port in the session scratchpad). There must be 0 errors. All 76 faction files and `alliances.json` must pass.
2. For every pair where both faction files list each other: same sign, within 30 points.
3. Every faction's `blocs` contains only alliance ids that exist in `alliances.json`, and it's listed in that alliance's `members`.
4. Terror groups: hostile to `player` (-80 or below), `player_client` false, and `sellable` false.
5. Don't run git. The auto-save loop pushes every 10 minutes when the validator passes. Since this job edits all 76 files, keep each edit small and the JSON valid at all times; write each file in one go.
6. Update the Status section of `docs/factions_handoff.md`, and the factions part of `factions/README.md` if it exists by then.

## Open questions for Captain

All answered by Captain on 2026-10-10 and applied in Job 4 (thresholds for usa/gbr/can in Job 9); see "Captain's decisions (2026-10-10)" in [factions_handoff.md](factions_handoff.md).

- Side-lock length: is a 3-10 in-game-day range right?
  - **Answered:** 2-4 in-game weeks (14-28 days), scaled by contract severity.
- Should NATO non-Five-Eyes allies (for example pol or fra) sell to the player at high reputation? The default was no.
  - **Answered:** yes, at higher thresholds than usa/gbr/can (rep 20/40/60/80); tur does not sell.
- Should reputation spill-over apply across the whole matrix or only within alliances? The default was the whole matrix.
  - **Answered:** only between factions that share an alliance.
- Israel and the Gulf states: client-only, or also sellers? The default was client-only.
  - **Answered:** sau, are and qat sell at high reputation (rep 40/60/80; the unlock lists are proposed); isr hires the player but never sells.
