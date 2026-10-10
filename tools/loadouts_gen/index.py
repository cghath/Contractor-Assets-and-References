"""Index and README writer; run via gen.py REPO <all spec modules> --index"""
import json, os
from catalog import *
import gen
from gen import USED, TIERS_SEEN, GAME_ITEMS, write_json, MED_NAMES, OTHER_NAMES, REPO

def U(kind, key):
    return sorted(USED[kind].get(key, ()))

def weapons_index():
    w = []
    for wid in sorted(USED['weapon']):
        x = WEAPONS[wid]
        e = {'id': wid, 'name': x['name'], 'calibre': x['calibre'], 'class': x['cls'], 'mag': x['mag'], 'rounds_per_mag': x['rounds'],
             'in_game': bool(x['game']), 'game_item_id': x['game'] or None}
        if not x['game']:
            e['game_substitute'] = gen.sub_for(x['cls'])
        e['users'] = U('weapon', wid)
        w.append(e)
    rounds = {}
    for (cal, name, gid, match), users in USED['round'].items():
        rounds.setdefault(cal, []).append({'round': name, 'game_round_id': gid, 'game_match': match, 'users': sorted(users)})
    cals = [{'calibre': c, 'in_game': any(r['game_round_id'] for r in rs), 'rounds': sorted(rs, key=lambda r: r['round'])} for c, rs in sorted(rounds.items())]
    mags = [{'id': m, 'name': MAGS[m][0], 'calibre': MAGS[m][1], 'kind': MAGS[m][2], 'rounds': MAGS[m][3], 'in_game': m in GAME_ITEMS,
             'game_item_id': m if m in GAME_ITEMS else None, 'users': U('mag', m)} for m in sorted(USED['mag'])]
    optics = [{'id': o, 'name': OPTICS[o], 'in_game': False, 'game_item_id': None, 'users': U('optic', o)} for o in sorted(USED['optic'])]
    ugl = [{'id': u, 'name': UGL[u][0], 'calibre': UGL[u][1], 'ammo': UGL[u][2], 'in_game': False, 'game_item_id': None, 'users': U('ugl', u)} for u in sorted(USED['ugl'])]
    ugl_ammo = [{'id': a, 'name': UGL_AMMO[a][0], 'calibre': UGL_AMMO[a][1], 'in_game': False, 'game_item_id': None, 'users': U('ugl_ammo', a)} for a in sorted(USED['ugl_ammo'])]
    launchers = []
    for lid in sorted(USED['launcher']):
        L = LAUNCHERS[lid]
        e = {'id': lid, 'name': L[0], 'kind': L[4], 'in_game': bool(L[1]), 'game_launcher': L[1] or None,
             'game_substitute': None if L[1] else (L[3] or None), 'game_item_id': None,
             'proposed_game_item_id': GAME_LAUNCHER_IDS.get(L[1]) if L[1] else None,
             'rounds': [dict({'name': n, 'type': t, 'count': c},
                             **({'proposed_game_item_id': LAUNCHER_ROUND_IDS[n]} if L[1] and n in LAUNCHER_ROUND_IDS else {}))
                        for n, t, c in L[2]], 'users': U('launcher', lid)}
        launchers.append(e)
    lr = {}
    for (lid, rname, rtype), users in USED['launcher_round'].items():
        fam = LAUNCHERS[lid][1] or ('(' + LAUNCHERS[lid][0] + ')')
        k = (fam, rname, rtype)
        lr.setdefault(k, set()).update(users)
    lrounds = [{'launcher': k[0], 'round': k[1], 'type': k[2], 'in_game_launcher': not k[0].startswith('('), 'users': sorted(v)}
               for k, v in sorted(lr.items())]
    gren = []
    for gid in sorted(USED['grenade']):
        name, kind = GRENADES[gid]
        e = {'id': gid, 'name': name, 'kind': kind, 'in_game': kind in GRENADE_GAME, 'game_item_id': GRENADE_GAME.get(kind),
             'game_match': 'generic' if kind in GRENADE_GAME else None}
        if kind in GRENADE_NEW:
            e['proposed_game_id'] = GRENADE_NEW[kind]
            e['game_substitute'] = 'smoke_grenade'
        e['users'] = U('grenade', gid)
        gren.append(e)
    med = [{'id': m, 'name': MED_NAMES[m], 'in_game': m in GAME_ITEMS, 'game_item_id': m if m in GAME_ITEMS else None, 'users': U('medical', m)}
           for m in sorted(USED['medical'])]
    oth = [{'id': o, 'name': OTHER_NAMES[o], 'in_game': o in GAME_ITEMS, 'game_item_id': o if o in GAME_ITEMS else None, 'users': U('other', o)}
           for o in sorted(USED['other'])]
    return {
        'schema_version': 1,
        '_note': 'Every weapon, calibre and round, magazine, optic, underbarrel launcher, launcher and grenade used by loadouts/<faction id>.json, with its users (faction ids). in_game: an item for it exists in the game repo (data/items.json; rounds: data/rounds.json; launchers: one of the 6 design-doc launchers, which have no items.json entry yet). medical and other list the non-weapon kit for the build summary. Regenerated with the loadout files; ids are stable.',
        'weapons': w, 'calibres': cals, 'magazines': mags, 'optics': optics, 'underbarrel_launchers': ugl, 'underbarrel_ammo': ugl_ammo,
        'launchers': launchers, 'launcher_rounds': lrounds, 'grenades': gren, 'medical': med, 'other': oth,
    }

def armor_index():
    hel = []
    for h in sorted(USED['helmet']):
        H = HELMETS[h]
        hel.append({'id': h, 'name': H[0], 'tier': H[1], 'designation': H[2], 'real_rating': H[3],
                    'game_rating': {'light': 'IIA', 'medium': 'IIIA', 'heavy': 'III++'}.get(H[1]),
                    'game_item_id': gen.HELMET_GAME.get(H[1]), 'game_match': 'generic' if H[1] in gen.HELMET_GAME else None})
        if h in HELMET_NEW:
            hel[-1]['cosmetic'] = True
            hel[-1]['proposed_game_id'] = HELMET_NEW[h]
        hel[-1]['users'] = U('helmet', h)
    vests = []
    for v in sorted(USED['vest']):
        tiers = sorted(TIERS_SEEN['vest'].get(v, ()), key=['light', 'medium', 'heavy'].index)
        vests.append({'id': v, 'name': VESTS[v][0], 'designation': VESTS[v][1], 'tiers': tiers,
                      'game_item_ids': {t: gen.VEST_GAME[t] for t in tiers}, 'game_match': 'generic', 'users': U('vest', v)})
    plates = []
    for p in sorted(USED['plate']):
        P = PLATES[p]
        tiers = sorted(TIERS_SEEN['plate'].get(p, ()), key=['light', 'medium', 'heavy'].index)
        side = p in ('esbi', 'side_plates')
        gi = {}
        for t in tiers:
            if side:
                gi[t] = 'plate_side'
            else:
                a, b = gen.plate_game(P[1], t)
                gi[t] = a or ('NEW plate_steel_light (substitute ' + b + ')' if P[1] == 'steel' else 'NEW (substitute ' + b + ')')
        plates.append({'id': p, 'name': P[0], 'material': P[1], 'designation': P[2], 'real_rating': P[3], 'side_plate': side,
                       'vest_tiers': tiers, 'game_item_ids': gi, 'users': U('plate', p)})
    return {
        'schema_version': 1,
        '_note': "Every helmet, vest / plate carrier and plate used by loadouts/<faction id>.json, with tier and users. Game tiers follow the design doc: light vest = front plate only (light plates only, NIJ III); medium = front and back; heavy = front, back and sides; helmets light IIA, medium IIIA, heavy III++. designation 'class' marks a generic entry where no specific model name was confirmed. game_item_ids map each tier the item is worn at to the generic game item.",
        'tiers': {'vest': {'light': 'plate_carrier_light', 'medium': 'plate_carrier', 'heavy': 'plate_carrier_heavy'},
                  'helmet': {'light': 'helmet_bump', 'medium': 'helmet', 'heavy': 'helmet_heavy', 'none': None},
                  'plate': {'ceramic medium/heavy': 'plate_ceramic_l4 (IV)', 'steel medium/heavy': 'plate_steel_l3 (III++)',
                            'polyethylene light': 'plate_pe_l3 (III)', 'steel light': 'NEW plate_steel_light (III, proposed)', 'side': 'plate_side (III++)'}},
        'helmets': hel, 'vests': vests, 'plates': plates,
    }

def rounds_index():
    specs = {}
    for (cal, name, gid, match), users in USED['round'].items():
        if match == 'exact':
            continue
        rid, rcal, proj, mv, mass, level, cls = ROUND_SPECS[name]
        e = specs.setdefault(rid, {'id': rid, 'calibre': rcal, 'designations': [], 'projectile': proj, 'muzzle_velocity_mps': mv,
                                   'mass_g': mass, 'class': cls, 'game_level': level, 'stopped_by': [], 'defeats': [],
                                   'current_game_round_id': gid, 'in_game': False, 'users': set()})
        if name not in e['designations']:
            e['designations'].append(name)
        e['users'] |= set(users)
    out = []
    for rid in sorted(specs):
        e = specs[rid]
        lv = LADDER.index(e['game_level'])
        e['stopped_by'] = [a for a, r in GAME_ARMOR_RATINGS if LADDER.index(r) >= lv]
        e['defeats'] = [a for a, r in GAME_ARMOR_RATINGS if LADDER.index(r) < lv]
        e['designations'].sort()
        e['users'] = sorted(e['users'])
        out.append(e)
    return {
        'schema_version': 1,
        '_note': "Proposed round specs for the game's data/rounds.json (Captain, 2026-10-10): every round the loadouts use that has no exact match there. Spec only: nothing here is in the game yet (in_game false). game_level is the round's threat level on the design doc's NIJ-named ladder; armor with a rating at or above it stops the round. current_game_round_id is the generic round the loadouts point at until this one exists (null if none). Velocities and masses are approximate starting points to check against ACE3 configs.",
        'ladder': LADDER, 'game_armor_ratings': [{'armor': a, 'rating': r} for a, r in GAME_ARMOR_RATINGS],
        'rounds': out,
    }

def write_all(fids):
    wi = weapons_index(); ai = armor_index(); ri = rounds_index()
    write_json(os.path.join(REPO, 'loadouts', 'weapons_index.json'), wi)
    write_json(os.path.join(REPO, 'loadouts', 'armor_index.json'), ai)
    write_json(os.path.join(REPO, 'loadouts', 'rounds_index.json'), ri)
    return wi, ai, ri
