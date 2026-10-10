from sutil import W, A, NONE
from s_me_terror import T, elite

# Central Africa bloc (eastern DR Congo): added in Job 7, own bloc by Captain's decision (2026-10-10).
# adf reuses the terror-bloc helpers T and elite from s_me_terror.py; m23 and cod are plain specs.
SPEC = {
 'adf': T('ADF forest bands',
   W('ak47', 'pkm', 'akm', ('akm', None), ('akm', 'rpg7'), 'ak47', 'akm', None, 'pm_makarov'),
   alt={'rifleman': ['type56', 'akm'], 'squad_leader': ['akms']}, optic_over={'marksman': 'iron'},
   not_fielded={'sniper': 'The faction file lists no dedicated snipers; the marksman carries an AKM.'},
   elite_v=elite("ADF core cadres (commanders' guards)", camo=1, armor=NONE, helmet_roles=None,
                 vnotes=['Faction file: no body armour at all, so the elite variant differs only in training (medical and night capability one step up).']),
   notes=["Armor: none for regulars and elites; the faction file records no body armour, which overrides the Q9 elite default.",
          "The faction file grenadier is an AKM with hand grenades, so the grenadier has no launcher and carries 4 grenades.",
          'Added in Job 7 (Captain, 2026-10-10).']),

 'm23': dict(grenades='sov', profile='east', optics='east',
  regular=dict(name='M23 sections', camo=0,
    w=W('ak47', 'pkm', 'svd', ('akm', 'gp25'), ('akm', 'rpg7'), 'ak47', 'akm', 'svd', 'pm_makarov', crew='akms'),
    alt={'rifleman': ['type56', 'akm']}, armor=A('steel_helmet', 'soft_vest', 'light', None),
    helmet_roles=['squad_leader', 'autorifleman', 'at']),
  variants=[dict(id='assault', name='M23 assault units', camo=1, elite=True,
    armor=A('steel_helmet', 'soft_vest', 'light', 'steel_light'), helmet_roles=None,
    vnotes=['Faction file: assault units wear helmets and light vests with a steel plate (needs plate_steel_light; plate_pe_l3 stands in).'])],
  notes=['Real armed non-state group (hostile non-client, Captain-confirmed 2026-10-10); real-world weapons and kit.',
         'UN experts reported MANPADS and anti-aircraft weapons; they are modelled as air-denial zones and technicals, not as loadout items.',
         'Crew role for the captured T-55 set piece.', 'Added in Job 7 (Captain, 2026-10-10).'], sources=[]),

 'cod': dict(grenades='sov', profile='east', optics='east',
  regular=dict(name='FARDC infantry', camo=0,
    w=W('akm', 'pkm', 'svd', ('akm', 'gp25'), ('akm', 'rpg7'), 'ak47', 'akm', 'svd', 'pm_makarov', crew='akms', pilot='akms'),
    alt={'rifleman': ['ak47', 'type56'], 'autorifleman': ['rpk']}, armor=A('steel_helmet', None, None),
    helmet_roles=['squad_leader', 'autorifleman', 'at']),
  variants=[
   dict(id='republican_guard', name='Republican Guard and rapid-reaction units', camo=2, elite=True,
    armor=A('steel_helmet', 'plate_carrier_nat', 'light', 'steel_light'), helmet_roles=None,
    vnotes=['Faction file: helmets and light plate carriers (the light steel plate needs plate_steel_light; plate_pe_l3 stands in).']),
   dict(id='wazalendo', name='Wazalendo pro-government militia auxiliaries', camo=1, profile='irregular', optics='irregular', grenades='irregular',
    w_over=dict(rif='ak47', ar='pkm', mk='akm', gr=('ak47', None), at=('ak47', 'rpg7'), med='ak47', sl='akm', sn=None),
    optic_over={'marksman': 'iron'}, not_fielded={'sniper': 'Wazalendo militias field no snipers.'}, armor=NONE, helmet_roles=None,
    vnotes=['Faction file: Wazalendo militias have no armour.'])],
  notes=['Regular units: helmets on leaders, gunners and AT men only and few vests (faction file), so the regular armor tier is none.',
         'Browning-pattern pistols are a sidearm alternate.', 'Added in Job 7 (Captain, 2026-10-10).'], sources=[]),
}
