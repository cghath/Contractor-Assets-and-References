#!/usr/bin/env python3
"""Generate loadouts/ (one file per non-player faction, weapons/armor/rounds indexes, README) from the specs in this folder.

usage, from the repo root:
  python3 -I tools/loadouts_gen/gen.py --game <path to the Contractor game repo>

--game defaults to the CONTRACTOR_GAME environment variable, then ../Contractor next to this repo,
then B:/Contractor. Only data/items.json is read from the game repo (read only).
See tools/loadouts_gen/README.md.
"""
import json, math, os, sys, copy, importlib
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from catalog import *

REPO = os.path.dirname(os.path.dirname(HERE))
BLOCS = ['s_five_eyes', 's_nato_west', 's_eastern_flank', 's_russia_csto', 's_asia_pacific',
         's_middle_east_states', 's_me_terror', 's_others']

def _game_dir():
    a = sys.argv[1:]
    if '--game' in a and a.index('--game') + 1 < len(a):
        return a[a.index('--game') + 1]
    for c in (os.environ.get('CONTRACTOR_GAME'), os.path.join(os.path.dirname(REPO), 'Contractor'), 'B:/Contractor'):
        if c and os.path.isfile(os.path.join(c, 'data', 'items.json')):
            return c
    raise SystemExit('ERROR game repo not found: pass --game <path to the Contractor repo>')

GAME_DIR = _game_dir()
GAME_ITEMS = {i['id'] for i in json.load(open(os.path.join(GAME_DIR, 'data', 'items.json'), encoding='utf-8'))['items']}
HEAVY_HELMET_ROLES = {'rifleman', 'autorifleman', 'grenadier', 'at', 'medic', 'squad_leader'}
CORE = ['rifleman', 'autorifleman', 'marksman', 'grenadier', 'at', 'medic', 'squad_leader', 'sniper']
ARMOURED = {'mbt', 'ifv', 'apc', 'mrap'}
AIR = {'attack_heli', 'transport_heli'}
VEH_TYPE = {}
for f in os.listdir(os.path.join(REPO, 'reference', 'vehicles')):
    if f.endswith('.json'):
        VEH_TYPE[f[:-5]] = json.load(open(os.path.join(REPO, 'reference', 'vehicles', f), encoding='utf-8')).get('type')

# ---------------------------------------------------------------- families
GF = {  # grenade families: frag ids (1 or 2), white smoke, signal smokes, flash
 'us': (('m67',), 'an_m8', ['m18_green', 'm18_red', 'm18_violet'], 'm84'),
 'us_supplied': (('m67',), 'an_m8', ['m18_green', 'm18_red'], None),
 'can': (('c13',), 'smoke_white_nato', ['signal_green', 'signal_red', 'signal_violet'], 'stun_nato'),
 'gbr': (('l109a2',), 'smoke_white_nato', ['signal_green', 'signal_red', 'signal_violet'], 'stun_nato'),
 'deu': (('dm51a2',), 'smoke_white_nato', ['signal_green', 'signal_red', 'signal_violet'], 'stun_nato'),
 'che': (('hg85',), 'smoke_white_nato', ['signal_green', 'signal_red'], None),
 'nato': (('frag_nato',), 'smoke_white_nato', ['signal_green', 'signal_red', 'signal_violet'], 'stun_nato'),
 'nato_basic': (('frag_nato',), 'smoke_white_nato', ['signal_green', 'signal_red'], None),
 'kor': (('k400',), 'smoke_white_nato', ['signal_green', 'signal_red'], None),
 'srb': (('m75_srb',), 'smoke_white_nato', [], None),
 'rus': (('rgd5', 'f1'), 'rdg2b', [], None),
 'sov': (('rgd5', 'f1'), 'rdg2b', [], None),
 'chn': (('type82_2',), 'smoke_white_nato', ['signal_green', 'signal_red'], None),
 'copy': (('frag_copy',), 'smoke_white_nato', [], None),
 'ind': (('mmhg',), 'smoke_white_nato', ['signal_green', 'signal_red'], None),
 'irregular': (('f1', 'rgd5'), None, [], None),
 'cartel': (('m67',), None, [], None),
 'none': ((None,), None, [], None),
 'pmc_west': (('m67',), 'an_m8', ['m18_green', 'm18_red', 'm18_violet'], 'm84'),
}

STYLE = {  # optic by weapon class for rifleman-type roles
 'us': {'rifle': 'red_dot_magnifier', 'carbine': 'red_dot_magnifier', 'lmg': 'red_dot', 'gpmg': 'prism4', 'br': 'prism4'},
 'usmc': {'rifle': 'lpvo', 'carbine': 'lpvo', 'lmg': 'lpvo', 'gpmg': 'prism4', 'br': 'lpvo'},
 'west': {'rifle': 'red_dot_magnifier', 'carbine': 'red_dot_magnifier', 'lmg': 'red_dot', 'gpmg': 'prism4', 'br': 'prism4'},
 'west_basic': {'rifle': 'red_dot', 'carbine': 'red_dot', 'lmg': 'iron', 'gpmg': 'iron', 'br': 'iron'},
 'east_modern': {'rifle': 'collimator', 'carbine': 'collimator', 'lmg': 'collimator', 'gpmg': 'iron', 'br': 'iron'},
 'east': {'rifle': 'iron', 'carbine': 'iron', 'lmg': 'iron', 'gpmg': 'iron', 'br': 'iron'},
 'chn': {'rifle': 'chn_optic', 'carbine': 'chn_optic', 'lmg': 'chn_optic', 'gpmg': 'iron', 'br': 'iron'},
 'irregular': {'rifle': 'iron', 'carbine': 'iron', 'lmg': 'iron', 'gpmg': 'iron', 'br': 'iron'},
 'cartel': {'rifle': 'red_dot', 'carbine': 'red_dot', 'lmg': 'iron', 'gpmg': 'iron', 'br': 'iron'},
 'pmc_west': {'rifle': 'lpvo', 'carbine': 'lpvo', 'lmg': 'holo', 'gpmg': 'prism4', 'br': 'lpvo'},
 'pmc_east': {'rifle': 'collimator', 'carbine': 'collimator', 'lmg': 'collimator', 'gpmg': 'collimator', 'br': 'iron'},
}
SL_UPGRADE = {'east': 'collimator', 'irregular': 'iron', 'west_basic': 'red_dot', 'cartel': 'red_dot'}

# kit profile: counts, pistols, backpacks
PROFILES = {
 'west':      dict(rifle=7, rifle_at=5, rifle_med=6, rifle_crew=4, belt200=3, belt100=4, lmgmag=8, dmr20=8, dmr10=8, sn5=6, sn10=5, amr=5, pistol=3,
                  pistol_roles={'squad_leader', 'medic', 'autorifleman', 'marksman', 'sniper', 'crew', 'pilot'}, packs=True),
 'east':      dict(rifle=6, rifle_at=4, rifle_med=4, rifle_crew=3, belt200=2, belt100=3, lmgmag=8, dmr20=6, dmr10=6, sn5=6, sn10=5, amr=4, pistol=2,
                  pistol_roles={'squad_leader', 'sniper', 'crew', 'pilot', 'medic'}, packs=True),
 'irregular': dict(rifle=5, rifle_at=4, rifle_med=4, rifle_crew=3, belt200=2, belt100=2, lmgmag=5, dmr20=4, dmr10=4, sn5=4, sn10=4, amr=3, pistol=2,
                  pistol_roles={'squad_leader'}, packs=False),
 'cartel':    dict(rifle=6, rifle_at=5, rifle_med=5, rifle_crew=4, belt200=2, belt100=2, lmgmag=6, dmr20=5, dmr10=5, sn5=5, sn10=5, amr=3, pistol=2,
                  pistol_roles=set(CORE) | {'crew', 'pilot'}, packs=False),
 'pmc':       dict(rifle=7, rifle_at=5, rifle_med=6, rifle_crew=4, belt200=3, belt100=4, lmgmag=8, dmr20=8, dmr10=8, sn5=6, sn10=5, amr=5, pistol=3,
                  pistol_roles=set(CORE) | {'crew', 'pilot'}, packs=True),
}

MED_NAMES = {
 'tourniquet': 'Tourniquet (CAT / SOF-T class)', 'pressure_bandage': 'Pressure bandage (Israeli bandage / IPP-1 class)',
 'hemostatic_gauze': 'Hemostatic gauze (QuikClot Combat Gauze class)', 'chest_seal': 'Vented chest seal',
 'splint': 'Splint (SAM splint class)', 'morphine': 'Morphine autoinjector', 'npa': 'Nasopharyngeal airway (NPA)',
 'decompression_needle': 'Decompression needle (14 gauge)', 'iv_18g': 'IV access kit, 18 gauge', 'io_fast1': 'IO access device (FAST1 class)',
 'saline_500': 'Saline bag, 500 mL', 'epinephrine': 'Epinephrine autoinjector', 'adenosine': 'Adenosine (game drug: slows a racing heart rate)',
 'atropine': 'Atropine autoinjector (ATNAA / AD-1 class)', 'surgical_kit': 'Surgical kit (hemostat surgery)', 'defibrillator': 'Defibrillator (AED class)',
 'ifak': 'IFAK (individual first aid kit pouch)', 'trauma_kit': 'Medic trauma bag',
}
# medical profiles by ai_tuning.medical_care: full >= .8, standard >= .6, basic >= .4, minimal below
MED_SOLDIER = {
 'full': ('ifak', [('tourniquet', 2), ('pressure_bandage', 2), ('hemostatic_gauze', 1), ('chest_seal', 2), ('npa', 1)]),
 'standard': ('ifak', [('tourniquet', 1), ('pressure_bandage', 2), ('hemostatic_gauze', 1), ('chest_seal', 1)]),
 'basic': ('ifak', [('tourniquet', 1), ('pressure_bandage', 2)]),
 'minimal': (None, [('pressure_bandage', 1)]),
}
MED_MEDIC = {
 'full': ('trauma_kit', [('tourniquet', 4), ('pressure_bandage', 8), ('hemostatic_gauze', 4), ('chest_seal', 4), ('splint', 2), ('npa', 3),
          ('decompression_needle', 2), ('iv_18g', 3), ('io_fast1', 1), ('saline_500', 4), ('morphine', 4), ('epinephrine', 3), ('adenosine', 1),
          ('atropine', 2), ('surgical_kit', 1)]),
 'standard': ('trauma_kit', [('tourniquet', 3), ('pressure_bandage', 6), ('hemostatic_gauze', 2), ('chest_seal', 2), ('splint', 1), ('npa', 2),
          ('decompression_needle', 1), ('iv_18g', 2), ('saline_500', 2), ('morphine', 3), ('epinephrine', 2), ('adenosine', 1), ('atropine', 1),
          ('surgical_kit', 1)]),
 'basic': ('trauma_kit', [('tourniquet', 2), ('pressure_bandage', 6), ('hemostatic_gauze', 1), ('chest_seal', 1), ('splint', 1), ('npa', 1),
          ('iv_18g', 1), ('saline_500', 1), ('morphine', 2), ('epinephrine', 1)]),
 'minimal': (None, [('tourniquet', 2), ('pressure_bandage', 4), ('hemostatic_gauze', 1), ('morphine', 1)]),
}
MED_LEVELS = ['minimal', 'basic', 'standard', 'full']

OTHER_NAMES = {
 'assault_pack': 'Assault pack (24 L)', 'ruck_45': 'Rucksack (45 L)', 'radio': 'Squad radio, national issue',
 'nvg_mono': 'Gen 3 NVG monocular (AN/PVS-14 class)', 'nvg_bino': 'Gen 3 binocular NVG (AN/PVS-31 class)',
 'nvg_envgb': 'AN/PSQ-42 ENVG-B', 'binoculars': 'Binoculars / laser rangefinder',
}

# ---------------------------------------------------------------- helpers
USED = {'weapon': {}, 'ugl': {}, 'ugl_ammo': {}, 'optic': {}, 'mag': {}, 'launcher': {}, 'launcher_round': {}, 'grenade': {},
        'helmet': {}, 'vest': {}, 'plate': {}, 'medical': {}, 'other': {}, 'round': {}}
TIERS_SEEN = {'helmet': {}, 'vest': {}, 'plate': {}}

def use(kind, iid, fid):
    USED[kind].setdefault(iid, set()).add(fid)

def sub_for(cls):
    return {'carbine': 'mk18', 'smg': 'mk18', 'dmr': 'm110', 'sniper': 'm110', 'amr': 'm110', 'pistol': 'm17'}.get(cls, 'm4a1')

SUB_MAG = {'m4a1': ('mag_556', 30), 'mk18': ('mag_556', 30), 'm110': ('mag_762', 20), 'm17': ('mag_9mm', 17)}

def round_for(cal, ammo_fam):
    r = ROUNDS.get(ammo_fam, {}).get(cal) or ROUNDS['default'].get(cal)
    return r

def mag_count(w, role, prof):
    P = PROFILES[prof]
    m = MAGS[w['mag']]
    cls = w['cls']
    if cls == 'pistol':
        return P['pistol']
    if m[2] in ('belt', 'drum'):
        return P['belt200'] if m[3] >= 200 else P['belt100'] if m[3] >= 100 else P['lmgmag']
    if cls == 'lmg':
        return P['lmgmag']
    if cls in ('dmr', 'br') and role in ('marksman', 'sniper'):
        return P['dmr20'] if m[3] >= 20 else P['dmr10']
    if cls == 'sniper':
        return P['sn5'] if m[3] <= 5 else P['sn10']
    if cls == 'amr':
        return P['amr']
    if role == 'at':
        return P['rifle_at']
    if role == 'medic':
        return P['rifle_med']
    if role in ('crew', 'pilot'):
        return P['rifle_crew']
    if w['mag'] == 'mag_68x51_20':
        return 9
    return P['rifle']

def weapon_ref(wid, role, V, fid, optic=None):
    w = WEAPONS[wid]
    use('weapon', wid, fid)
    cal = w['calibre']
    rn = round_for(cal, V['ammo'])
    use('mag', w['mag'], fid)
    use('round', (cal, rn[0], rn[1], rn[2]), fid)
    ref = {'id': wid, 'name': w['name'], 'calibre': cal, 'game_item_id': w['game'] or None}
    if not w['game']:
        ref['game_substitute'] = sub_for(w['cls'])
    if w['cls'] != 'pistol':
        if optic is None:
            optic = V.get('optic_over', {}).get(role) or pick_optic(w, role, V)
        use('optic', optic, fid)
        ref['optic'] = {'id': optic, 'name': OPTICS[optic]}
    mg = w['mag']
    ref['ammo'] = {'id': mg, 'round': rn[0], 'game_round_id': rn[1]}
    if rn[2] != 'exact':
        ref['ammo']['proposed_round_id'] = ROUND_SPECS[rn[0]][0]
    ref['ammo'].update({'rounds_per_mag': w['rounds'], 'count': mag_count(w, role, V['profile']),
                        'game_item_id': mg if mg in GAME_ITEMS else None})
    return ref

def pick_optic(w, role, V):
    cls = w['cls']
    if w['optic'] and (cls in ('dmr', 'sniper', 'amr') or w['optic'] in ('g36_dual', 'aug_15x', 'xm157', 'prism4', 'chn_optic')):
        if w['optic'] in ('prism4', 'chn_optic') and V['optics'] in ('east', 'irregular'):
            pass
        else:
            return w['optic']
    if cls in ('dmr',):
        return 'dmr_scope'
    if cls in ('sniper', 'amr'):
        return 'sniper_scope'
    if role == 'marksman':
        return 'prism4' if V['optics'] not in ('east', 'irregular') else 'pso1' if w['calibre'] == '7.62x54R' else 'collimator'
    o = STYLE[V['optics']].get(cls, 'iron')
    if role == 'squad_leader' and V['optics'] in SL_UPGRADE and o == 'iron':
        o = SL_UPGRADE[V['optics']]
    if V['optics'] == 'cartel' and w['calibre'] != '5.56x45mm':
        o = 'iron'
    return o

def launcher_ref(lid, fid, count_override=None):
    L = LAUNCHERS[lid]
    use('launcher', lid, fid)
    in_game = bool(L[1])
    ref = {'id': lid, 'name': L[0], 'kind': L[4], 'in_game': in_game, 'game_launcher': L[1] or None,
           'game_substitute': None if in_game else (L[3] or None),
           'game_item_id': None}
    if in_game:
        ref['proposed_game_item_id'] = GAME_LAUNCHER_IDS[L[1]]
    rounds = []
    for rname, rtype, cnt in L[2]:
        rr = {'name': rname, 'type': rtype, 'count': cnt}
        if in_game and rname in LAUNCHER_ROUND_IDS:
            rr['proposed_game_item_id'] = LAUNCHER_ROUND_IDS[rname]
        rounds.append(rr)
        use('launcher_round', (lid, rname, rtype), fid)
    ref['rounds'] = rounds
    return ref

def grenade_list(role, V, fid):
    frags, white, signals, flash = GF[V['grenades']]
    prof = V['profile']
    elite = V.get('elite', False)
    out = []
    def add(gid, n):
        if gid and n > 0:
            out.append((gid, n))
    if role in V.get('role_grenades', {}):
        for gid, n in V['role_grenades'][role]:
            add(gid, n)
        prof = 'skip'
    if prof in ('west', 'pmc'):
        nfrag = {'rifleman': 2, 'squad_leader': 1, 'medic': 0, 'crew': 0, 'pilot': 0, 'sniper': 1}.get(role, 1)
        nwhite = {'medic': 2, 'squad_leader': 2, 'pilot': 0}.get(role, 1)
        nflash = 1 if role in ('rifleman', 'squad_leader') else 0
    elif prof == 'east':
        nfrag = {'rifleman': 2, 'squad_leader': 2, 'medic': 0, 'crew': 0, 'pilot': 0}.get(role, 1)
        nwhite = 1 if role in ('squad_leader', 'medic') else 0
        nflash = 0
    elif prof == 'cartel':
        nfrag = {'rifleman': 1, 'squad_leader': 1, 'grenadier': 2}.get(role, 0)
        nwhite = 0
        nflash = 0
    elif prof == 'skip':
        nfrag = nwhite = nflash = 0
    else:  # irregular
        nfrag = {'rifleman': 1, 'squad_leader': 1, 'autorifleman': 1, 'at': 0, 'medic': 0, 'sniper': 0, 'marksman': 0, 'crew': 0}.get(role, 0)
        if role == 'grenadier' and V['w']['gr'][1] is None:
            nfrag = 4
        elif role == 'grenadier':
            nfrag = 1
        if elite:
            nfrag += 1 if role in ('rifleman', 'squad_leader', 'autorifleman', 'at') else 0
        nwhite = 1 if (elite and role == 'squad_leader') else 0
        nflash = 0
    if prof == 'skip':
        pass
    elif len(frags) == 2 and nfrag >= 2:
        add(frags[0], nfrag - nfrag // 2); add(frags[1], nfrag // 2)
    else:
        add(frags[0], nfrag)
    add(white, nwhite)
    if role == 'squad_leader' and prof != 'skip':
        for s in signals:
            add(s, 1)
    if role == 'pilot' and signals:
        add(signals[-1], 1)
    if flash and V['profile'] in ('west', 'pmc'):
        add(flash, nflash)
    res = []
    for gid, n in out:
        name, kind = GRENADES[gid]
        use('grenade', gid, fid)
        g = {'id': gid, 'name': name, 'kind': kind, 'count': n, 'game_item_id': GRENADE_GAME.get(kind)}
        if kind in GRENADE_NEW:
            g['game_substitute'] = 'smoke_grenade'
        res.append(g)
    return res

def plate_game(material, tier):
    if tier == 'light':
        if material == 'polyethylene':
            return 'plate_pe_l3', None
        return None, 'plate_pe_l3'      # light steel / ceramic plate: to build
    if material == 'ceramic':
        return 'plate_ceramic_l4', None
    if material == 'steel':
        return 'plate_steel_l3', None
    return None, 'plate_steel_l3'

def armor_ref(spec, role, V, fid):
    """spec: (helmet, vest, tier, plate, side)"""
    h, v, tier, p, s = spec
    out = {}
    if v:
        use('vest', v, fid)
        TIERS_SEEN['vest'].setdefault(v, set()).add(tier)
        out['vest'] = {'id': v, 'name': VESTS[v][0], 'tier': tier, 'game_item_id': VEST_GAME[tier]}
    else:
        out['vest'] = None
    if v and p:
        P = PLATES[p]
        gi, gs = plate_game(P[1], tier)
        use('plate', p, fid)
        TIERS_SEEN['plate'].setdefault(p, set()).add(tier)
        pr = {'id': p, 'name': P[0], 'material': P[1], 'real_rating': P[3], 'front': True, 'back': tier != 'light',
              'game_rating': {'plate_ceramic_l4': 'IV', 'plate_steel_l3': 'III++', 'plate_pe_l3': 'III'}.get(gi or '', 'III'),
              'game_item_id': gi}
        if gs:
            pr['game_substitute'] = gs
            pr['proposed_game_id'] = 'plate_steel_light' if P[1] == 'steel' else 'plate_ceramic_light'
        out['plates'] = pr
    else:
        out['plates'] = None
    if v and s and tier == 'heavy':
        use('plate', s, fid)
        TIERS_SEEN['plate'].setdefault(s, set()).add('heavy')
        out['side_plates'] = {'id': s, 'name': PLATES[s][0], 'material': PLATES[s][1], 'count': 2, 'game_item_id': 'plate_side'}
    else:
        out['side_plates'] = None
    helmet_roles = V.get('helmet_roles')
    if h and (helmet_roles is None or role in helmet_roles or role in ('crew', 'pilot')):
        H = HELMETS[h]
        htier = H[1]
        use('helmet', h, fid)
        TIERS_SEEN['helmet'].setdefault(h, set()).add(htier)
        out['helmet'] = {'id': h, 'name': H[0], 'tier': htier,
                         'game_rating': {'light': 'IIA', 'medium': 'IIIA', 'heavy': 'III++'}.get(htier),
                         'game_item_id': HELMET_GAME.get(htier)}
        if h in HELMET_NEW:
            out['helmet']['cosmetic'] = True
            out['helmet']['proposed_game_id'] = HELMET_NEW[h]
    else:
        out['helmet'] = None
    return out

def med_level(V, role):
    lvl = V['med']
    if V.get('elite') and lvl != 'full':
        lvl = MED_LEVELS[MED_LEVELS.index(lvl) + 1]
    return lvl

def medical(role, V, fid):
    lvl = med_level(V, role)
    cont, items = (MED_MEDIC if role == 'medic' else MED_SOLDIER)[lvl]
    if role == 'pilot' or role == 'crew':
        cont, items = MED_SOLDIER[lvl]
    res = {'container': cont, 'items': []}
    if cont:
        use('medical', cont, fid)
    for mid, n in items:
        if mid == 'surgical_kit' and V['ai_med'] < 0.7:
            continue
        use('medical', mid, fid)
        res['items'].append({'id': mid, 'count': n, 'game_item_id': mid if mid in GAME_ITEMS else None})
    if role == 'medic' and lvl == 'full' and V['ai_med'] >= 0.85:
        use('medical', 'defibrillator', fid)
        res['items'].append({'id': 'defibrillator', 'count': 1, 'game_item_id': None})
    return res

def other(role, V, fid, launcher):
    res = []
    def add(oid, n=1):
        use('other', oid, fid)
        res.append({'id': oid, 'count': n, 'game_item_id': oid if oid in GAME_ITEMS else None})
    prof = PROFILES[V['profile']]
    if prof['packs']:
        big = role in ('medic', 'sniper') or (role == 'at' and launcher and launcher['kind'] in ('rocket', 'recoilless', 'atgm'))
        if role != 'pilot':
            add('ruck_45' if big else 'assault_pack')
    elif role == 'at' or (role == 'medic' and V['profile'] == 'irregular'):
        add('assault_pack')
    if role == 'squad_leader' and V['profile'] != 'irregular' or (role == 'squad_leader' and V.get('elite')):
        add('radio')
    if role in ('squad_leader', 'sniper') and V['profile'] in ('west', 'pmc', 'east'):
        add('binoculars')
    night = V['night'] + (0.2 if V.get('elite') else 0)
    nvg = V.get('nvg_item') or ('nvg_bino' if night >= 0.9 else 'nvg_mono')
    if role == 'pilot':
        pass
    elif night >= 0.75 or (night >= 0.55 and role in ('squad_leader', 'marksman', 'sniper')) or (night >= 0.4 and role == 'squad_leader'):
        add(nvg)
    return res

def game_kit(role_obj):
    kit = []
    def add(i, n):
        if i and n:
            for k in kit:
                if k[0] == i:
                    k[1] += n
                    return
            kit.append([i, n])
    a = role_obj['armor']
    if a['vest']:
        add(a['vest']['game_item_id'], 1)
        if a['plates']:
            pi = a['plates']['game_item_id'] or a['plates'].get('game_substitute')
            add(pi, 2 if a['plates']['back'] else 1)
        if a['side_plates']:
            add('plate_side', 2)
    if a['helmet'] and a['helmet']['game_item_id']:
        add(a['helmet']['game_item_id'], 1)
    for slot in ('primary', 'secondary'):
        w = role_obj.get(slot)
        if not w:
            continue
        gid = w['game_item_id'] or w['game_substitute']
        add(gid, 1)
        am = w['ammo']
        if am['game_item_id'] and (w['game_item_id'] or SUB_MAG[gid][0] == am['game_item_id']):
            add(am['game_item_id'], am['count'])
        else:
            smag, srnd = SUB_MAG[gid]
            add(smag, min(12, max(2, math.ceil(am['rounds_per_mag'] * am['count'] / srnd))))
    for g in role_obj['grenades']:
        add(g['game_item_id'] or g.get('game_substitute'), g['count'])
    med = role_obj['medical']
    add(med['container'], 1)
    for m in med['items']:
        add(m['game_item_id'], m['count'])
    for o in role_obj['other']:
        add(o['game_item_id'], o['count'])
    return kit

def build_role(role, V, fid):
    w = V['w']
    r = {}
    ugl = None
    launcher_id = None
    if role == 'grenadier':
        wid, ugl = w['gr']
    elif role == 'at':
        wid, launcher_id = w['at']
    elif role == 'crew':
        wid = w['crew']
    elif role == 'pilot':
        wid = w['pilot']
    else:
        wid = w[{'rifleman': 'rif', 'autorifleman': 'ar', 'marksman': 'mk', 'medic': 'med', 'squad_leader': 'sl', 'sniper': 'sn'}[role]]
    if wid is None:
        return {'not_fielded': True, 'note': V.get('not_fielded', {}).get(role, 'Not fielded by this faction.'),
                'stand_in_role': 'rifleman'}
    r['primary'] = weapon_ref(wid, role, V, fid)
    alts = V.get('alt', {}).get(role)
    if alts:
        for a in alts:
            use('weapon', a, fid)
            use('mag', WEAPONS[a]['mag'], fid)
            cal = WEAPONS[a]['calibre']; rn = round_for(cal, V['ammo'])
            use('round', (cal, rn[0], rn[1], rn[2]), fid)
        r['primary']['alternates'] = alts
    if ugl:
        U = UGL[ugl]
        use('ugl', ugl, fid)
        ammo = [(U[2], 10)]
        if U[2] == 'gl_40x46_he' and V['profile'] in ('west', 'pmc'):
            ammo = [(U[2], 10), ('gl_40x46_smoke', 2)]
        if V['profile'] == 'irregular':
            ammo = [(U[2], 6)]
        r['primary']['underbarrel'] = {'id': ugl, 'name': U[0], 'calibre': U[1], 'game_item_id': None,
            'ammo': [{'id': a, 'name': UGL_AMMO[a][0], 'count': n, 'game_item_id': None} for a, n in ammo]}
        for a, n in ammo:
            use('ugl_ammo', a, fid)
    sec = None
    if role in PROFILES[V['profile']]['pistol_roles'] and w.get('pis') and WEAPONS[wid]['cls'] != 'pistol':
        sec = weapon_ref(w['pis'], role, V, fid)
    r['secondary'] = sec
    L = None
    if launcher_id:
        L = launcher_ref(launcher_id, fid)
        if V.get('at_alt'):
            for a in V['at_alt']:
                use('launcher', a, fid)
                for rn, rt, c in LAUNCHERS[a][2]:
                    use('launcher_round', (a, rn, rt), fid)
            L['alternates'] = V['at_alt']
    elif role == 'rifleman' and V.get('rif_launcher'):
        L = launcher_ref(V['rif_launcher'], fid)
    r['launcher'] = L
    r['grenades'] = grenade_list(role, V, fid)
    aspec = V['armor']
    if role == 'crew':
        h, v, t, p, s = aspec
        crew_h = 'tsh_tanker' if V['optics'] in ('east', 'east_modern', 'chn', 'irregular') else 'cvc_helmet'
        aspec = (crew_h, v, 'medium' if t == 'heavy' else t, p, None)
    elif role == 'pilot':
        if V['profile'] in ('west', 'pmc'):
            aspec = ('flight_helmet', 'aircrew_vest', 'light', 'pe_light', None)
        else:
            aspec = ('flight_helmet', None, None, None, None)
    ra = V.get('role_armor', {}).get(role)
    if ra:
        aspec = ra
    if V.get('heavy_helmet') and role in HEAVY_HELMET_ROLES:
        aspec = (V['heavy_helmet'],) + tuple(aspec[1:])
    r['armor'] = armor_ref(aspec, role, V, fid)
    r['medical'] = medical(role, V, fid)
    r['other'] = other(role, V, fid, L)
    r['game_kit'] = game_kit(r)
    note = V.get('role_notes', {}).get(role)
    if note:
        r['notes'] = note
    return r

def resolve(fid, F, faction):
    reg = F['regular']
    out = []
    for ov in [{}] + F.get('variants', []):
        V = copy.deepcopy(reg)
        V['id'] = 'regular'
        V.update({k: copy.deepcopy(v) for k, v in ov.items() if k != 'w_over'})
        if 'w_over' in ov:
            V['w'] = dict(reg['w'], **ov['w_over'])
        tun = (faction.get('doctrine') or {}).get('ai_tuning') or {}
        V['ai_med'] = tun.get('medical_care', 0.5)
        V['night'] = tun.get('night_capability', 0.3)
        mc = V['ai_med']
        if 'med' not in V:
            V['med'] = 'full' if mc >= 0.8 else 'standard' if mc >= 0.6 else 'basic' if mc >= 0.4 else 'minimal'
        V.setdefault('ammo', F.get('ammo', 'default'))
        V.setdefault('grenades', F.get('grenades', 'nato'))
        V.setdefault('profile', F.get('profile', 'west'))
        V.setdefault('optics', F.get('optics', 'west'))
        out.append(V)
    return out

def build(fid, F):
    faction = json.load(open(os.path.join(REPO, 'factions', fid + '.json'), encoding='utf-8'))
    camos = [c.get('name') for c in faction.get('camo') or []]
    vtypes = {VEH_TYPE.get(v['vehicle_id']) for v in faction.get('vehicles') or []}
    has_crew = bool(vtypes & ARMOURED)
    has_pilot = bool(vtypes & AIR)
    roles_list = CORE + (['crew'] if has_crew else []) + (['pilot'] if has_pilot else [])
    variants = []
    for V in resolve(fid, F, faction):
        if has_crew and not V['w'].get('crew'):
            V['w'] = dict(V['w'], crew=F.get('crew_default') or V['w']['med'])
        if has_pilot and not V['w'].get('pilot'):
            V['w'] = dict(V['w'], pilot=V['w'].get('crew') or V['w']['med'])
        roles = {role: build_role(role, V, fid) for role in roles_list}
        team = [launcher_ref(l, fid) for l in V.get('team', [])]
        vo = {'id': V['id'], 'name': V['name'],
              'camo': camos[V.get('camo', 0)] if isinstance(V.get('camo', 0), int) and camos else V.get('camo'),
              'armor_tier': V['armor'][2] or 'none', 'medical_level': med_level(V, 'rifleman'),
              'roles': roles, 'team_weapons': team}
        if V.get('applies_to'):
            vo['applies_to'] = V['applies_to']
        if V.get('vnotes'):
            vo['notes'] = V['vnotes']
        variants.append(vo)
    # role map for unit_templates roles
    tmpl_roles = set()
    for u in faction.get('unit_templates') or []:
        for c in u.get('composition') or []:
            tmpl_roles.add(c.get('role'))
    rmap = {}
    base_map = {'team_leader': 'squad_leader', 'assistant_squad_leader': 'squad_leader', 'leader_hvt': 'squad_leader',
                'courier_hvt': 'rifleman', 'driver': 'crew', 'gunner': 'crew', 'tank_crew': 'crew', 'vehicle_crew': 'crew',
                'ifv_crew': 'crew', 'drone_operator': 'rifleman', 'systems_operator': 'rifleman', 'radio_operator': 'rifleman',
                'lookout': 'rifleman', 'breacher': 'rifleman', 'engineer': 'rifleman', 'riot_shield': 'rifleman', 'mortar_crew': 'rifleman'}
    for tr in sorted(r for r in tmpl_roles if r and r not in roles_list):
        t = base_map.get(tr, 'rifleman')
        if t == 'crew' and not has_crew:
            t = 'rifleman'
        rmap[tr] = t
    doc = {
        'id': fid,
        'faction': faction.get('name'),
        'schema_version': 1,
        'kind': faction.get('kind'),
        'campaign_tier': faction.get('campaign_tier'),
        'default_variant': 'regular',
        'variants': variants,
        'role_map': rmap,
        'notes': F.get('notes', []),
        'proposed': ['mag and medical counts (Q3 default)', 'variants and their armor mapping (Q1, Q9 defaults)',
                     'optics as class ids (Q7 default)', 'medical levels from doctrine.ai_tuning.medical_care (Q6 default)',
                     'game_kit (stand-in kit from items that exist today)'] + F.get('proposed', []),
        'sources': [f'factions/{fid}.json'] + F.get('sources', []),
    }
    return doc

def dumps(o, ind=0, width=150):
    flat = json.dumps(o, ensure_ascii=False)
    if len(flat) + ind <= width or not isinstance(o, (dict, list)) or not o:
        return flat
    pad = ' ' * (ind + 1)
    if isinstance(o, dict):
        items = [pad + json.dumps(k, ensure_ascii=False) + ': ' + dumps(v, ind + 1, width) for k, v in o.items()]
        return '{\n' + ',\n'.join(items) + '\n' + ' ' * ind + '}'
    items = [pad + dumps(v, ind + 1, width) for v in o]
    return '[\n' + ',\n'.join(items) + '\n' + ' ' * ind + ']'

def write_json(path, doc):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(dumps(doc) + '\n')

def write_bloc(mod):
    M = importlib.import_module(mod)
    os.makedirs(os.path.join(REPO, 'loadouts'), exist_ok=True)
    for fid, F in M.SPEC.items():
        doc = build(fid, F)
        write_json(os.path.join(REPO, 'loadouts', fid + '.json'), doc)
    return list(M.SPEC)

if __name__ == '__main__':
    done = []
    for m in BLOCS:
        done += write_bloc(m)
    sys.modules['gen'] = sys.modules['__main__']
    import index, readme
    wi, ai, ri = index.write_all(done)
    readme.write(done, wi, ai, ri)
    print('wrote %d loadout files, 3 indexes and README.md to %s' % (len(done), os.path.join(REPO, 'loadouts')))
