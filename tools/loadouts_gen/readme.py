import json, os, re
from catalog import *
import gen
from gen import REPO, GAME_ITEMS

BLOC_NAMES = {'five_eyes': 'US and Five Eyes', 'nato_west': 'Western Europe and Nordics', 'eastern_flank': 'Ukraine and eastern flank',
              'russia_csto': 'Russia, CSTO, Caucasus', 'asia_pacific': 'Asia-Pacific', 'middle_east_states': 'Middle East states',
              'me_terror': 'ME terrorist / armed groups', 'others': 'Neutrals, Africa, cartels, PMCs',
              'central_africa': 'Central Africa'}

def roster_blocs():
    src = open(os.path.join(REPO, 'tools', 'factions_workflow.js'), encoding='utf-8').read()
    m = re.search(r"const\s+ROSTER\s*=\s*\{(.*?)\n\}", src, re.S)
    out = {}
    for key, body in re.findall(r"(\w+)\s*:\s*\[([^\]]*)\]", m.group(1)):
        for i in re.findall(r"'([^']+)'", body):
            out[i] = key
    return out

def tier_of(fid):
    return json.load(open(os.path.join(REPO, 'loadouts', fid + '.json'), encoding='utf-8')).get('campaign_tier')

def write(fids, wi, ai, ri):
    blocs = roster_blocs()
    docs = {f: json.load(open(os.path.join(REPO, 'loadouts', f + '.json'), encoding='utf-8')) for f in fids}
    early = {f for f, d in docs.items() if d.get('campaign_tier') == 'early'}
    L = []
    L.append('# AI default loadouts\n')
    L.append(f'Default AI loadouts for the {len(fids)} non-player factions in `factions/` (every faction id except `player`), as of 2026-10-10. '
             'Weapons, ammunition, armor and helmets use real-world designations (Captain, 2026-10-10); fictional cartels and PMCs use real gear. '
             'The schema is in [docs/loadouts_handoff.md](../docs/loadouts_handoff.md). Counts, optics, medical levels and the game kits are proposals (`proposed` in each file).\n')
    L.append('- `loadouts/<faction id>.json`: one file per faction: variants, each with every role\'s weapons, ammunition, launcher, grenades, armor, medical kit, other kit and a `game_kit` built only from items that exist in the game today.')
    L.append('- [weapons_index.json](weapons_index.json): every weapon, calibre and round, magazine, optic, underbarrel launcher, launcher, launcher round and grenade (plus medical and other kit), with users and in-game flags.')
    L.append('- [armor_index.json](armor_index.json): every helmet, vest / plate carrier and plate, with tier, game mapping and users.')
    L.append("- [rounds_index.json](rounds_index.json): proposed specs for every round with no exact match in the game's `data/rounds.json` (Captain, 2026-10-10): calibre, designation, projectile, approximate muzzle velocity and mass, level on the game's armor ladder, which game armor stops it, users. Spec only; the loadouts point at these through `proposed_round_id`.")
    L.append('- [../tools/loadouts_gen/](../tools/loadouts_gen/): the generator that writes everything in this folder (see its README).')
    L.append('- Validate with `python3 tools/validate_pack.py` (loadouts checks included).\n')
    L.append('## Roster\n')
    L.append('Armor is the regular variant\'s vest tier (helmet tier); AT is the at role\'s launcher, with the in-game launcher or its substitute in brackets.\n')
    L.append('| id | Bloc | Tier | Variants | Rifleman | Armor | AT | Crew / pilot |')
    L.append('|---|---|---|---|---|---|---|---|')
    order = [f for b in BLOC_NAMES for f in fids if blocs.get(f) == b]
    for f in order:
        d = docs[f]
        v0 = d['variants'][0]
        r = v0['roles']
        rif = r['rifleman']['primary']['name']
        vest = r['rifleman']['armor']['vest']
        hel = r['rifleman']['armor']['helmet']
        arm = (vest['tier'] if vest else 'none') + ' (' + (hel['tier'] if hel else 'none') + ')'
        at = r['at']
        if at.get('not_fielded'):
            ats = 'none'
        else:
            l = at['launcher']
            ats = l['name'] + ' [' + (l['game_launcher'] if l['in_game'] else 'sub ' + str(l['game_substitute'])) + ']'
        cp = '/'.join(x for x in ('crew', 'pilot') if x in r) or '-'
        L.append(f"| {f} | {BLOC_NAMES[blocs[f]]} | {d['campaign_tier']} | {', '.join(v['id'] for v in d['variants'])} | {rif} | {arm} | {ats} | {cp} |")
    L.append('')
    # ---- build summary
    W = wi['weapons']
    wb = [w for w in W if not w['in_game']]
    mags_b = [m for m in wi['magazines'] if not m['in_game']]
    cal_b = [c for c in wi['calibres'] if not c['in_game']]
    rounds_generic = sorted({(c['calibre'], r['round']) for c in wi['calibres'] for r in c['rounds'] if r['game_match'] == 'generic'})
    lnch = wi['launchers']
    l_in = [l for l in lnch if l['in_game']]
    l_out = [l for l in lnch if not l['in_game']]
    fams = sorted({l['game_launcher'] for l in l_in})
    optics = wi['optics']
    ugl = wi['underbarrel_launchers']; ugla = wi['underbarrel_ammo']
    gren_new = sorted({g['proposed_game_id'] for g in wi['grenades'] if g.get('proposed_game_id')})
    med_new = [m for m in wi['medical'] if not m['in_game']]
    oth_new = [o for o in wi['other'] if not o['in_game']]
    hel = ai['helmets']; ves = ai['vests']; pla = ai['plates']
    nonbal = [h for h in hel if h['tier'] == 'none']
    lightsteel = {f for f, d in docs.items() for v in d['variants'] for r in v['roles'].values()
                  if ((r.get('armor') or {}).get('plates') or {}).get('proposed_game_id') == 'plate_steel_light'}
    L.append('## What has to be built\n')
    L.append(f"Counted from the {len(fids)} loadout files against the game's `data/items.json` ({len(GAME_ITEMS)} items) and `data/rounds.json`. Full lists with users are in the two index files.\n")
    L.append('| Category | Used | Already in game | To build |')
    L.append('|---|---|---|---|')
    L.append(f"| Weapons (primary, sidearm, alternates) | {len(W)} | {len(W) - len(wb)} ({', '.join(w['id'] for w in W if w['in_game'])}) | {len(wb)} |")
    L.append(f"| Magazines and belts | {len(wi['magazines'])} | {len(wi['magazines']) - len(mags_b)} ({', '.join(m['id'] for m in wi['magazines'] if m['in_game'])}) | {len(mags_b)} |")
    L.append(f"| Rounds (rounds.json) | {len(wi['calibres'])} calibres | {len(wi['calibres']) - len(cal_b)} calibres have a round | {len(ri['rounds'])} round specs in rounds_index.json: {len(cal_b)} calibres with no round, plus {len(rounds_generic)} designations that use a generic round today |")
    lrids = sorted({r['proposed_game_item_id'] for l in l_in for r in l['rounds'] if r.get('proposed_game_item_id')})
    L.append(f"| Launchers | {len(lnch)} | {len(l_in)} map to the 6 design-doc launchers, which have no items.json entry yet | 6 launcher items ({', '.join(GAME_LAUNCHER_IDS[f] for f in fams)}) and {len(lrids)} round items ({', '.join(lrids)}); AT4 and NLAW are single-shot; {len(l_out)} other launchers use a game_substitute |")
    L.append(f"| Underbarrel launchers / their ammo | {len(ugl)} / {len(ugla)} | 0 | {len(ugl)} / {len(ugla)} |")
    L.append(f"| Optics (class ids) | {len(optics)} | 0 | {len(optics)} |")
    L.append(f"| Hand grenades | {len(wi['grenades'])} models | frag, white smoke and stun covered by frag_grenade, smoke_grenade, flashbang | {len(gren_new)} signal smokes ({', '.join(gren_new)}) |")
    L.append(f"| Helmets | {len(hel)} models | {len(hel) - len(nonbal)} map to helmet_bump / helmet / helmet_heavy by tier | {len(nonbal)} cosmetic non-ballistic helmets ({', '.join(h['proposed_game_id'] for h in nonbal)}); models are skins of the tier items |")
    L.append(f"| Vests / plate carriers | {len(ves)} models | all map to the 3 carrier tiers | visual variants only |")
    L.append(f"| Plates | {len(pla)} models | ceramic, steel, PE and side plates map to existing plates | 1 new item: plate_steel_light (light-tier steel plate; used by {len(lightsteel)} factions: {', '.join(sorted(lightsteel))}). Until it is built, `game_kit` uses plate_pe_l3 in its place |")
    L.append(f"| Medical | {len(wi['medical'])} | {len(wi['medical']) - len(med_new)} | {len(med_new)} ({', '.join(m['id'] for m in med_new)}) |")
    L.append(f"| Other kit | {len(wi['other'])} | {len(wi['other']) - len(oth_new)} (backpacks) | {len(oth_new)} ({', '.join(o['id'] for o in oth_new)}) |")
    L.append('')
    heavy = []
    for f in fids:
        for v in docs[f]['variants']:
            if any((r.get('armor') or {}).get('helmet') and r['armor']['helmet']['tier'] == 'heavy' for r in v['roles'].values()):
                heavy.append(f + ' ' + v['id'])
    L.append('Heavy (III++) helmets go only to elite, SOF and PMC assault variants (Captain, 2026-10-10), on the assault roles (marksman and sniper keep the standard helmet): ' + ', '.join(heavy) + '.\n')
    L.append('### Early game first\n')
    L.append(f"The early game is mostly fighting terrorist groups (Captain). These are the items to build first, ranked by how many of the {len(early)} early-tier factions use them.\n")
    def early_rank(items, key='id', n=15):
        rows = []
        for it in items:
            e = len(set(it['users']) & early)
            if e:
                rows.append((e, len(it['users']), it))
        rows.sort(key=lambda r: (-r[0], -r[1], r[2][key]))
        return rows[:n]
    L.append('| Item | Kind | Early-tier users | All users |')
    L.append('|---|---|---|---|')
    for e, a, it in early_rank(wb, n=15):
        L.append(f"| {it['name']} (`{it['id']}`) | weapon, {it['calibre']} | {e} | {a} |")
    for e, a, it in early_rank(mags_b, n=6):
        L.append(f"| {it['name']} (`{it['id']}`) | magazine | {e} | {a} |")
    for e, a, it in early_rank([l for l in l_in], n=4):
        L.append(f"| {it['name']} (`{it['id']}`) | launcher, game {it['game_launcher']} | {e} | {a} |")
    for e, a, it in early_rank(ugl, n=3):
        L.append(f"| {it['name']} (`{it['id']}`) | underbarrel launcher | {e} | {a} |")
    L.append('')
    L.append('Calibres with no round in `data/rounds.json`: ' + ', '.join(c['calibre'] for c in cal_b) + '.\n')
    L.append('Designations that currently use a generic round (same calibre, different load): ' + '; '.join(f"{r}" for c, r in rounds_generic) + '.\n')
    L.append('### Weapons to build, by number of users\n')
    L.append('| Weapon | Class | Calibre | Users | Game substitute |')
    L.append('|---|---|---|---|---|')
    for w in sorted(wb, key=lambda w: (-len(w['users']), w['id']))[:40]:
        L.append(f"| {w['name']} (`{w['id']}`) | {w['class']} | {w['calibre']} | {len(w['users'])} | {w['game_substitute']} |")
    rest = sorted(wb, key=lambda w: (-len(w['users']), w['id']))[40:]
    L.append(f"\nThe other {len(rest)} weapons to build are used by {max((len(w['users']) for w in rest), default=0)} factions or fewer each; see weapons_index.json.\n")
    L.append('## Conventions\n')
    L.append('- Ids are stable snake_case and reuse `tools/loadouts_catalog_wip.pl` (one WIP id was dropped: `m110_sniper`, a duplicate of `m110`).')
    L.append('- `game_item_id` is set only where the item exists in the game repo; armor, grenades and medical items map to the generic game item of their kind. `game_substitute` names the existing item that stands in until the real one is built.')
    L.append('- Launchers: `in_game` is true when the launcher is one of the 6 design-doc launchers (AT4, RPG-7, Javelin, MAAWS, NLAW, SMAW); otherwise `game_substitute` names one of the 6 (MANPADS have none).')
    L.append('- `count` is the total carried, including the magazine in the weapon.')
    L.append('- `role_map` maps every role used by the faction\'s unit_templates that has no loadout of its own to the role whose loadout it uses.')
    L.append('- Roles a faction does not field are marked `not_fielded` with a `stand_in_role` (only pse_pa: at and sniper).')
    L.append('- `proposed_round_id` (in `ammo`) points at a rounds_index.json spec wherever `game_round_id` is missing or only a generic match; `proposed_game_item_id` gives the proposed items.json id for the 6 in-game launchers and their rounds; `proposed_game_id` marks other new items (plate_steel_light, signal smokes, cosmetic helmets).\n')
    open(os.path.join(REPO, 'loadouts', 'README.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
