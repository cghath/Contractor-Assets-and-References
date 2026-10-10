from sutil import W, A, NONE

ELITE_ARMOR = A('captured_helmet', 'soft_vest', 'light', 'steel_light')
Q9 = 'Armor follows the Q9 default: regular fighters none; elites a light vest with an improvised or captured steel plate, and only squad leaders get a helmet.'

def elite(name, camo=0, **kw):
    d = dict(id='elite', name=name, camo=camo, elite=True, optics='west_basic', armor=ELITE_ARMOR, helmet_roles=['squad_leader'])
    d.update(kw)
    return d

def T(regular_name, w, alt=None, team=None, armor=NONE, elite_v=None, notes=(), at_alt=None, **kw):
    reg = dict(name=regular_name, camo=0, w=w, alt=alt or {}, team=team or [], armor=armor)
    if at_alt:
        reg['at_alt'] = at_alt
    reg.update(kw)
    return dict(grenades='irregular', profile='irregular', optics='irregular', regular=reg,
                variants=[elite_v] if elite_v else [], notes=list(notes), sources=[])

SPEC = {
 'hamas': T('Qassam Brigades fighters',
   W('akm', 'pkm', 'svd', ('akm', None), ('akm', 'rpg7'), 'akm', 'akm', 'al_ghoul', 'pm_makarov', crew='akms'),
   alt={'rifleman': ['type56', 'ar15_pattern'], 'autorifleman': ['rpk'], 'squad_leader': ['akms', 'ar15_pattern'], 'sniper': ['steyr_hs50']},
   team=['kornet'], elite_v=elite('Nukhba (Qassam elite) fighters', camo=0),
   notes=[Q9, "The faction file grenadier is an AKM with hand grenades, so the grenadier has no launcher and carries 4 grenades.",
          "Locally made 'Yassin-105' tandem rounds are not in the game; the RPG-7 loads PG-7V and OG-7V.", 'Tokarev-pattern and Glock-type pistols are sidearm alternates.']),
 'pij': T('al-Quds Brigades fighters',
   W('ar15_pattern', 'pkm', 'ar15_pattern', ('akm', None), ('akm', 'rpg7'), 'akm', 'ar15_pattern', 'steyr_hs50', 'glock17'),
   alt={'rifleman': ['akm']}, team=['kornet'], optic_over={'marksman': 'prism4'},
   elite_v=elite('al-Quds Brigades veteran cell', camo=0),
   notes=[Q9, "Faction file rifles are M16/M4-pattern, often locally assembled (ar15_pattern id).", 'The Steyr HS .50-type sniper rifle is Gaza only (faction file).',
          'Carlo-type improvised submachine guns (West Bank) are not catalogued.']),
 'hezbollah': T('Hezbollah fighters',
   W('akm', 'pkm', 'svd', ('akm', 'gp25'), ('akm', 'rpg7'), 'akm', 'm4', 'svd', 'glock17', crew='akms'),
   alt={'rifleman': ['ak74', 'm4'], 'grenadier': ['m4'], 'squad_leader': ['akms'], 'sniper': ['am50']},
   at_alt=['rpg29'], team=['kornet', 'konkurs', 'toophan', 'almas', 'dehlavieh'], armor=A(None, 'soft_vest', 'light', None),
   elite_v=elite('Radwan Force', camo=1),
   notes=['Faction file: regular fighters wear chest rigs and soft vests (light, no plate).',
          "Radwan wears the terror-elite kit (light vest with an improvised or captured steel plate, helmets on squad leaders). This differs from the faction file's medium rating by Captain's decision (2026-10-10).",
          'RPG-29 maps to RPG-7.']),
 'houthis': T('Ansar Allah fighters',
   W('akm', 'pkm', 'svd', ('akm', 'gp25'), ('akm', 'rpg7'), 'akm', 'akms', 'svd', 'pm_makarov', crew='akms'),
   alt={'rifleman': ['type56', 'g3a3'], 'autorifleman': ['rpk'], 'squad_leader': ['type56'], 'sniper': ['am50']},
   team=['kornet', 'dehlavieh', 'toophan'], elite_v=elite('Houthi veteran assault units', camo=1),
   notes=[Q9, 'Faction file says none-to-light for the regulars; none is used.', 'SPG-9 is a technical-mounted weapon and is left out.']),
 'iraqi_militias': T("Kata'ib Hezbollah / Nujaba fighters",
   W('akm', 'pkm', 'svd', ('akm', 'gp25'), ('akm', 'rpg7'), 'akm', 'm4', 'am50', 'glock17'),
   alt={'rifleman': ['type56', 'm4', 'm16a4'], 'sniper': ['svd']}, team=['toophan', 'dehlavieh'], armor=A(None, 'soft_vest', 'light', None),
   elite_v=elite("Kata'ib Hezbollah core fighters", camo=2),
   notes=['Faction file: light, some medium (PMF-issued plate carriers on some fighters). Regulars get a light soft vest; elites the Q9 light vest with a steel plate.',
          "Armor is kept at light because iraqi_militias is early tier (Captain's decision, 2026-10-10).",
          '107 mm rockets are an off-map event and are not a loadout item.']),
 'al_qaeda': T('al-Qaeda fighters',
   W('akm', 'pkm', 'svd', ('akm', None), ('akm', 'rpg7'), 'akm', 'akms', 'svd', 'pm_makarov'),
   alt={'rifleman': ['type56', 'm4', 'm16a2'], 'autorifleman': ['rpk']}, elite_v=elite('Leader guard detail (HVT guards)', camo=1),
   notes=[Q9, 'Faction file: a leader\'s guards may have captured plate carriers; game none, light for HVT guards.', 'Tokarev-pattern pistols are a sidearm alternate.']),
 'aqap': T('AQAP fighters',
   W('akm', 'pkm', 'svd', ('akm', None), ('akm', 'rpg7'), 'akm', 'akms', 'svd', 'pm_makarov'),
   alt={'rifleman': ['type56'], 'autorifleman': ['rpk'], 'squad_leader': ['m4']}, elite_v=elite('AQAP veteran fighters', camo=2),
   notes=[Q9, 'SPG-9 is a technical-mounted weapon and is left out.']),
 'isis': T('Islamic State fighters',
   W('akm', 'pkm', 'svd', ('akm', 'gp25'), ('akm', 'rpg7'), 'akm', 'm4', 'svd', 'glock17', crew='akms'),
   alt={'rifleman': ['type56', 'm16a4', 'm4'], 'autorifleman': ['rpk'], 'squad_leader': ['akms']}, at_alt=['m72'], team=['kornet', 'konkurs'],
   elite_v=elite('Inghimasi assault fighters', camo=0),
   notes=[Q9, 'Faction file says none-to-light with captured plates on leaders; elites cover that.', 'Makarov-pattern pistols are a sidearm alternate.']),
 'isis_k': T('ISIS-K fighters',
   W('akm', 'pkm', 'svd', ('akm', None), ('akm', 'rpg7'), 'akm', 'm4', 'svd', 'pm_makarov'),
   alt={'rifleman': ['type56', 'm4', 'm16a2'], 'squad_leader': ['akms']}, elite_v=elite('ISIS-K veteran fighters', camo=1),
   notes=[Q9, 'Faction file: chest rigs only, captured vests rare.']),
 'al_shabaab': T('al-Shabaab fighters',
   W('akm', 'pkm', 'svd', ('akm', None), ('akm', 'rpg7'), 'akm', 'akms', 'svd', 'pm_makarov'),
   alt={'rifleman': ['type56'], 'autorifleman': ['rpk'], 'squad_leader': ['g3a3', 'm16a2']}, elite_v=elite('al-Shabaab veteran fighters', camo=1),
   notes=[Q9, 'SPG-9 and M40 recoilless guns are technical-mounted and left out.']),
 'jnim': T('JNIM fighters',
   W('akm', 'pkm', 'svd', ('akm', None), ('akm', 'rpg7'), 'akm', 'akms', 'svd', 'pm_makarov'),
   alt={'rifleman': ['type56'], 'autorifleman': ['rpk']}, elite_v=elite('JNIM veteran fighters (captured army kit)', camo=1),
   notes=[Q9, "Faction file sidearm is 'assorted pistols'; the Makarov PM is a proposed pick.", 'Captured recoilless guns are vehicle weapons and left out.']),
}
