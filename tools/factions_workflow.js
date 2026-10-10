export const meta = {
  name: 'contractor-factions-worldspaces',
  description: 'Build real-world faction data (alliances, gear, real vehicles with references) for Contractor, then proc-gen worldspaces, then validate',
  phases: [
    { title: 'Factions', detail: '8 regional bloc agents write faction JSON and a shared real-vehicle catalogue' },
    { title: 'Worldspaces', detail: '2 agents write modern-inspired proc-gen region JSON (final concern)' },
    { title: 'Validate', detail: 'cross-check ids, relations, theatres, vehicles; write READMEs' },
  ],
}

const REPO = '/home/claude/contractor-assets-and-references'

const ROSTER = {
  five_eyes: ['usa', 'gbr', 'can', 'aus', 'nzl'],
  nato_west: ['fra', 'deu', 'ita', 'esp', 'nld', 'bel', 'nor', 'dnk', 'swe', 'fin', 'grc'],
  eastern_flank: ['ukr', 'pol', 'est', 'lva', 'ltu', 'rou', 'mda', 'geo'],
  russia_csto: ['rus', 'blr', 'africa_corps', 'kaz', 'srb', 'arm', 'aze'],
  asia_pacific: ['chn', 'prk', 'jpn', 'kor', 'twn', 'ind', 'pak', 'phl', 'vnm'],
  middle_east_states: ['irn', 'isr', 'tur', 'sau', 'are', 'qat', 'egy', 'jor', 'syr', 'irq', 'pse_pa'],
  me_terror: ['hamas', 'pij', 'hezbollah', 'houthis', 'iraqi_militias', 'al_qaeda', 'aqap', 'isis', 'isis_k', 'al_shabaab', 'jnim', 'adf'],
  others: ['che', 'aut', 'irl', 'mex', 'cartel_pacifico', 'cartel_jalisco_nueva', 'afg_taliban', 'sdf', 'krg_peshmerga', 'sahel_aes', 'som', 'pmc_halcyon', 'pmc_kestrel', 'pmc_black_sable', 'm23', 'cod'],
}
const ALL_IDS = ['player'].concat(Object.values(ROSTER).flat())

const THEATRES = {
  europe_asia_americas: ['baltic_coast', 'suwalki_gap', 'eastern_ukraine', 'black_sea_coast', 'arctic_north', 'caucasus', 'alpine_europe', 'taiwan_strait', 'korean_dmz', 'south_china_sea', 'kashmir_loc', 'mexico_cartel_belt', 'mindanao_sulu'],
  middle_east_africa: ['levant_syria', 'lebanon_south', 'israel', 'gaza_west_bank', 'iran_zagros', 'persian_gulf_coast', 'mesopotamia', 'yemen_red_sea', 'sahel', 'horn_of_africa', 'afghan_highlands', 'iraq_iran_border', 'eastern_congo'],
}
const ALL_THEATRES = Object.values(THEATRES).flat()

const CONTEXT = `
You are helping build CONTRACTOR, a near-future tactical FPS (Godot 4.7.2 + Voxel Tools, 5 cm voxel art, procedural) with physical inventory, AI squadmates and a persistent MW5-style campaign. Repo: ${REPO} (branch factions-worldspaces is checked out). Write ONLY the files your task names. Do not run git, do not edit scripts/ or showcase/, and never call any mcp__hearthbot__ tool.

Settled design decisions you must respect (Captain's word wins over realism):
- The player faction is a PMC company (faction id "player"). Friendly factions include the USA, GB and Canada; with reputation the player can BUY gear and vehicles from these allies.
- Enemy factions use Chinese, Russian, Iranian or terrorist-style gear depending on region.
- Early game sees a lot of fighting against terrorist groups (Middle East and affiliates).
- Contracts come from a regional contract board and from faction fixers. Taking work from one side locks the player out of that side's enemies' contracts for a while. The world is persistent: factions fight simulated operations between missions and move the front; the war posts matching contracts.
- Mission scale: contract zone ~2-4 km2 (40-90 min); hot zone ~8-16 km2 (2-4 h), player chooses when to extract. Both share map regions. Supports deploy from an LHD (coastal) or FOB (inland).
- Civilians are on maps; casualties caused by players or their AI cost money and reputation; 8 voids a contract.
- Vehicle armor is immune to small-calibre rounds; only 7.62x54R and larger can penetrate or disable vehicles. Launchers in game: AT4, RPG-7 (PG-7V, OG-7V), Javelin, MAAWS, NLAW, SMAW.
- Armor tiers (game rules): vests are aramid soft armor. LIGHT vest = frontal fragment + some ballistic; light plate stops regular .223 at most. MEDIUM = front/back plates, HEAVY = front/back/sides; plates ceramic (weaken and break) or steel (spall). Helmets light/medium/heavy (heavy = NIJ III++).
- Squads are 8 strong for the player; all AI uses battle-buddy pairs and real infantry tactics with grenades, flashbangs, smokes. Medical: blood volume, no HP.
- Existing voxel vehicle models (model ids): uh60 (UH-60 Black Hawk), ah1z (AH-1Z Viper), aav7 (AAV-7A1), maxxpro (MaxxPro MRAP), matv (Oshkosh M-ATV), bradley (M2 Bradley), abrams (M1 Abrams), technical_dshk, technical_zu23, technical_spg9, technical_m40, technical_rockets (Type 63 107 mm), technical_zpu (Toyota Hilux / Land Cruiser 79 technicals). Which game faction fields the AH-1Z, MRAPs, Bradley and Abrams is an OPEN design question: record real-world operators as fact, and any game assignment only as a proposal.

Canonical faction ids (use exactly these in relations and cross-references): ${ALL_IDS.join(', ')}.
Canonical theatre ids (use exactly these): ${ALL_THEATRES.join(', ')}.

Content rules:
- Use real names for nation-states and for the real terrorist organisations in the roster. Cartels and rival PMCs are FICTIONAL (give an "inspired_by" description, no real cartel or company names). Worldspace towns are fictional, inspired by regions, never replicas of real cities.
- Be factual and neutral, not propaganda. Describe tactics only at game-design level (ambushes, tunnels, IEDs as map hazards, drones); never real-world construction or operational how-to.
- Terrorist groups are hostile-only: never a contract client of the player, never sell to the player.
- Anything you invent for gameplay (ai_tuning numbers, rep thresholds, prices, game assignments) goes in the faction's "proposed" list so the design doc can tune it.

Web research: load the web tools with ToolSearch query "select:WebSearch,WebFetch" and use them to verify what each faction is actually KNOWN FOR fielding today (vehicles above all, then small arms and camo). Wikipedia article pages fetch fine through WebFetch; image hosts (upload.wikimedia.org, commons) and curl are blocked, so do not try to download photos. Instead record photo reference pages as URLs (the en.wikipedia article, and the Wikimedia Commons category URL https://commons.wikimedia.org/wiki/Category:<Name> when you know the category name). Cite sources. Keep research proportionate: verify signature vehicles and current service status; don't exhaustively research every rifle.
`

const FACTION_SPEC = `
Write one file per faction at ${REPO}/factions/<id>.json (pretty-printed JSON, 2-space indent) with this shape:
{
  "id": "<canonical id>", "name": "...", "short": "...",
  "kind": "state" | "non_state" | "pmc" | "criminal",
  "inspired_by": null or "<real-world type, for fictional factions>",
  "flag_colors": ["#hex", ...],
  "blocs": ["nato", "five_eyes", "eu", "csto", "axis_of_resistance", "aes", ...],
  "campaign_tier": "early" | "mid" | "late",
  "alignment_to_player": "friendly" | "neutral" | "hostile" | "varies",
  "player_client": true/false,   // can hire the player
  "relations": {"<faction id>": -100..100, ...},   // the notable ones (allies, enemies, rivals) incl. "player"; real-world 2026 alignments
  "theatres": ["<theatre id>", ...], "languages": ["..."], "callout_language": "...",
  "doctrine": {"summary": "...", "squad_size": n, "fireteam": "...", "tactics": ["..."],
     "ai_tuning": {"aggression":0-1,"discipline":0-1,"suppression_resistance":0-1,"flanking":0-1,"grenade_use":0-1,"medical_care":0-1,"night_capability":0-1,"marksmanship":0-1,"morale":0-1}},
  "camo": [{"name": "...", "palette": ["#hex", ...], "use": "..."}],
  "small_arms": {"rifleman": ["weapon (calibre)"], "autorifleman": [], "marksman": [], "grenadier": [], "at": [], "medic": [], "squad_leader": [], "sniper": [], "sidearm": []},
  "launchers": ["..."],   // flag which are in the game list above
  "body_armor": {"helmet": "none|light|medium|heavy", "vest": "none|light|medium|heavy", "plates": "none|steel|ceramic|mixed", "notes": "..."},
  "vehicles": [{"vehicle_id": "<catalogue id>", "role": "mbt|ifv|apc|mrap|light|technical|truck|artillery|mlrs|air_defense|attack_heli|transport_heli|uav|boat|other", "prevalence": "signature|common|uncommon|rare", "notes": "..."}],
  "unit_templates": [{"id": "...", "name": "...", "composition": [{"role": "...", "count": n}], "vehicle_id": null or "..."}],
  "support_assets": ["artillery / CAS / drones / EW they bring, game-level"],
  "player_trade": {"sellable": true/false, "rep_tiers": [{"rep": n, "unlocks": ["..."]}]},
  "contract_types": {"as_client": ["..."], "as_target": ["..."]},
  "notes": "...", "proposed": ["field paths that are gameplay proposals"], "sources": ["urls"]
}
Each faction should list the 4-12 vehicles it is best KNOWN for using in 2026 (signature first), verified on the web.

Shared real-vehicle catalogue: for every vehicle_id you reference, ensure ${REPO}/reference/vehicles/<vehicle_id>.json exists. FIRST list that directory: other agents write there in parallel; if the vehicle (or its family) already has a file, reuse that id and only add your faction ids to its "operators" (re-read the file right before editing, keep the edit small). Ids: lowercase family designation, e.g. t72b3, t90m, bmp2, bmp3, btr82a, mtlb, leopard2a6, challenger2, cv90, boxer, stryker, lav6, merkava4, namer, type99a, zbd04a, k2_black_panther, mi24, ka52, mi8, toyota_hilux. For vehicles that already have voxel models use the model id (abrams, bradley, uh60, ah1z, aav7, maxxpro, matv, technical_* ). Variants go in a "variants" list, not new files. Catalogue file shape:
{
  "id": "...", "name": "...", "aliases": [], "origin": "country", "type": "<role as above>",
  "operators": ["<faction ids>"], "crew": n, "passengers": n,
  "dimensions_m": {"length": x, "width": x, "height": x}, "weight_t": x,
  "armament": ["..."], "protection": "real-world notes + how it sits under the game's armor rule",
  "visual_notes": ["distinctive features a voxel modeller needs: hull/turret shape, road wheels or axles count, ERA/slat/cope cages, hatches, optics, stowage..."],
  "colour_schemes": [{"name": "...", "palette": ["#hex"]}],
  "variants": [], "existing_model": "<model id>" or null,
  "model_priority": "high|medium|low",   // high = signature vehicle of an early-game or major faction
  "reference_pages": ["https://en.wikipedia.org/wiki/...", "https://commons.wikimedia.org/wiki/Category:..."],
  "sources": ["urls"]
}
`

const BLOCS = [
  { key: 'five_eyes', title: 'US and Five Eyes', extra: 'Model the USA as one faction covering US Army and USMC (note branch-specific kit, e.g. USMC AH-1Z and AAV-7/ACV, Army Bradley, Abrams, Stryker, JLTV, M-ATV/MaxxPro). GBR and CAN are friendly to the player with reputation purchases (decided); give AUS/NZL proposals. Also write ${REPO}/factions/player.json for the player PMC (kind pmc, friendly to usa/gbr/can, starting kit per design: M4, 2 spare mags, 1 smoke, 1 frag; vehicles = existing models it might field as a proposal; LHD/FOB supports).' },
  { key: 'nato_west', title: 'Western Europe and Nordics', extra: 'Include NATO and EU membership in blocs. Sweden and Finland are NATO members.' },
  { key: 'eastern_flank', title: 'Ukraine and NATO eastern flank', extra: 'Ukraine fields a mix of Soviet-legacy and Western-donated kit plus heavy FPV/drone use; capture that. Moldova and Georgia are non-NATO.' },
  { key: 'russia_csto', title: 'Russia, CSTO and the Caucasus', extra: 'africa_corps is the Russian state-controlled successor to Wagner operating in Africa (real organisation; kind pmc; hostile rival contractor). Note Armenia\'s cooled CSTO ties and the Armenia-Azerbaijan situation as of 2026. Russian vehicles in 2026 commonly carry cope cages and anti-drone screens: capture that in visual_notes.' },
  { key: 'asia_pacific', title: 'Asia-Pacific', extra: 'China, DPRK, Japan, ROK, Taiwan, India, Pakistan, Philippines, Vietnam.' },
  { key: 'middle_east_states', title: 'Middle East states', extra: 'irn covers both the Artesh and the IRGC (note the split). Check the current (2026) Syrian government after the fall of Assad and describe it accurately. pse_pa is the Palestinian Authority Security Forces. Israel and Iran are central theatres (regions israel, gaza_west_bank, iran_zagros, persian_gulf_coast).' },
  { key: 'me_terror', title: 'Middle East terrorist and armed non-state groups', extra: 'Captain asked specifically for groups like Hamas and al-Qaeda, and EARLY GAME sees a lot of fighting against terrorists: set campaign_tier early for most, give rich unit_templates (cells, ambush teams, technical crews, suicide-drone teams as game hazards), heavy use of the existing technical_* models, captured/looted army vehicles, Toyota pickups, motorbikes. Gear is "terrorist-style": AK-pattern rifles, PKM, RPG-7, DShK, improvised armor or none. hostile to player, player_client false, sellable false. aqap, isis_k, al_shabaab and jnim are affiliates: link them in relations. adf (Allied Democratic Forces, Islamic State Central Africa Province, added in Job 7) is an islamic_state_network affiliate in eastern DR Congo. Be strictly factual and non-glorifying.' },
  { key: 'others', title: 'Neutrals, Africa, Central Asia, cartels and rival PMCs', extra: 'che, aut, irl are neutral states (mostly appear as staging/arms markets/neutral contract sources). afg_taliban is the de facto Afghan government. sahel_aes is the Alliance of Sahel States juntas (Mali, Burkina Faso, Niger) working with africa_corps. cartel_* are FICTIONAL cartels inspired by real Mexican cartel types (no real names). pmc_* are FICTIONAL rival contractor companies (recurring enemy rivals of the player; one Western, one Eastern-European/Russian-linked, one Gulf-funded is a good spread). Added in Job 7 for eastern_congo: m23 (M23/AFC rebel movement, real name, armed non-state group, not a client) and cod (FARDC, the DR Congo armed forces, the state client on that map).' },
]

phase('Factions')
const blocResults = await parallel(BLOCS.map(b => () => agent(
  `${CONTEXT}\n\nYOUR TASK: build the "${b.title}" bloc. Factions (canonical ids): ${ROSTER[b.key].join(', ')}.\n${b.extra}\n${FACTION_SPEC}\nReturn which files you wrote.`,
  {
    label: `factions:${b.key}`,
    phase: 'Factions',
    schema: {
      type: 'object',
      properties: {
        factions_written: { type: 'array', items: { type: 'string' } },
        vehicles_written_or_updated: { type: 'array', items: { type: 'string' } },
        open_questions: { type: 'array', items: { type: 'string' } },
        notes: { type: 'string' },
      },
      required: ['factions_written', 'vehicles_written_or_updated', 'open_questions', 'notes'],
    },
  },
)))
const blocs = blocResults.map((r, i) => ({ bloc: BLOCS[i].key, result: r }))
blocs.filter(b => !b.result).forEach(b => log(`Bloc ${b.bloc} failed and wrote nothing`))

const WORLD_SPEC = `
Write one file per theatre at ${REPO}/worldspaces/<theatre id>.json (pretty JSON). These are MODERN-DAY-INSPIRED procedural worldspaces for Voxel Tools (5 cm voxel art; terrain is generated in code). First read ${REPO}/factions/*.json (all of them) so factions_present and frontlines match the faction data. Shape:
{
  "id": "...", "name": "fictional region name", "inspired_by": "real region(s), described",
  "map_size_km": [w, h],   // proposed; must hold several contract zones (2-4 km2) and at least one hot zone (8-16 km2)
  "climate": "...", "seasons": ["..."],
  "biomes": [{"id": "...", "share": 0-1, "vegetation": ["..."], "ground_palette": ["#hex"], "foliage_palette": ["#hex"]}],
  "terrain": {"elevation_range_m": [a, b], "relief": "...", "features": ["wadis, terraces, karst..."], "water": "...",
     "generator": {"approach": "suggested VoxelGeneratorGraph / heightmap recipe", "noise_layers": [{"type": "...", "frequency": x, "amplitude_m": x, "purpose": "..."}], "erosion": "...", "rivers": "...", "notes": "..."}},
  "settlements": [{"type": "village|town|city_district|camp|farm|compound", "share": 0-1, "pop_range": [a, b], "architecture": "...", "materials": ["..."], "palette": ["#hex"], "layout_rules": ["..."], "example_names": ["fictional"]}],
  "infrastructure": {"roads": "...", "rail": "...", "power": "...", "ports": "...", "airfields": "...", "checkpoints": "..."},
  "pois": [{"type": "...", "description": "...", "loot_tier": "low|medium", "intel_chance": 0-1}],   // zone loot caps at medium tier
  "weather": {"conditions": ["..."], "visibility_notes": "...", "dust_or_snow": "..."},
  "civilians": {"density": "none|low|medium|high|very_high", "behaviour": "...", "vehicles": ["..."]},
  "factions_present": [{"faction_id": "...", "role": "occupier|defender|insurgent|patrol|militia|rival_pmc|bounty_hunters", "strength": "low|medium|high", "where": "..."}],
  "frontline": "how the simulated faction war moves here",
  "contract_hooks": ["mission types that fit, e.g. HVT capture, convoy ambush, cache raid, retake outpost"],
  "insertion": {"lhd": true/false, "fob": "..."},
  "early_game_suitable": true/false,
  "ambient_audio": ["..."],
  "proposed": ["what is a proposal"], "sources": ["urls"]
}
Use web research for climate, terrain, vegetation, architecture and palettes (text only; image hosts are blocked). For israel, gaza_west_bank and iran_zagros (added at Captain's request) be especially careful: fictional towns, high civilian density where real, the game's civilian-casualty penalties apply, factual and neutral framing. Early-game theatres (terrorist-heavy) should be marked early_game_suitable.
`

phase('Worldspaces')
const worldResults = await parallel(Object.entries(THEATRES).map(([k, ids]) => () => agent(
  `${CONTEXT}\n\nYOUR TASK: write the worldspaces for theatres: ${ids.join(', ')}.\n${WORLD_SPEC}\nReturn which files you wrote.`,
  {
    label: `worldspaces:${k}`,
    phase: 'Worldspaces',
    schema: {
      type: 'object',
      properties: {
        worldspaces_written: { type: 'array', items: { type: 'string' } },
        open_questions: { type: 'array', items: { type: 'string' } },
        notes: { type: 'string' },
      },
      required: ['worldspaces_written', 'open_questions', 'notes'],
    },
  },
)))

phase('Validate')
const validation = await agent(
  `${CONTEXT}\n\nYOUR TASK: validate and document the faction pack in ${REPO}. Use python3 scripts (write them under /tmp/claude-validate/, not in the repo).
1. Every file in factions/, reference/vehicles/, worldspaces/ parses as JSON. Fix syntax errors.
2. Every canonical faction id has a factions/<id>.json (missing: ${ALL_IDS.join(', ')} minus present). Every theatre id has a worldspaces file. Report gaps; do not invent whole factions.
3. relations keys and factions_present ids are canonical ids; theatres are canonical theatre ids. Fix typos to the canonical id.
4. Relations between two factions that both list each other should agree in sign and be within 30 points; where they don't, set both to the rounded mean unless one is clearly wrong. Add missing reciprocal entries for strong ties (|value| >= 50).
5. Every vehicle_id referenced by a faction has reference/vehicles/<id>.json; operators lists include every faction that references it. Merge duplicate vehicle files describing the same family (keep one id, move the other into variants, update references).
6. Terrorist factions: player_client false, player_trade.sellable false, hostile to player.
7. Write factions/README.md: what the pack is, the schema (short), a roster table (id, name, bloc, tier, alignment to player, theatres), an alliance matrix (markdown table, -/0/+ symbols) for the major powers usa, gbr, can, fra, deu, pol, ukr, rus, blr, chn, prk, irn, isr, tur, sau and the terror groups as one column group, and a "Proposals to settle" list collected from "proposed" fields and open questions: ${JSON.stringify(blocs.map(b => ({ bloc: b.bloc, open: b.result ? b.result.open_questions : ['agent failed'] })))} ${JSON.stringify(worldResults.map(w => w ? w.open_questions : ['agent failed']))}.
8. Write reference/vehicles/README.md: catalogue table (id, name, type, operators, existing_model, model_priority) sorted by priority, a "next voxel models to build" list (high priority, no existing model, early-game first), and the note that photo pages are linked per vehicle because image hosts are blocked from the build container.
9. Write worldspaces/README.md: table of theatres (id, name, inspired_by, size, early_game_suitable, main factions) and how they map to contract zones and hot zones.
10. Append a short "Factions, vehicles and worldspaces" section to ${REPO}/README.md pointing at these folders.
Return a summary.`,
  {
    label: 'validate',
    phase: 'Validate',
    schema: {
      type: 'object',
      properties: {
        faction_count: { type: 'number' },
        vehicle_count: { type: 'number' },
        worldspace_count: { type: 'number' },
        missing: { type: 'array', items: { type: 'string' } },
        fixes_made: { type: 'array', items: { type: 'string' } },
        next_models_to_build: { type: 'array', items: { type: 'string' } },
        open_questions: { type: 'array', items: { type: 'string' } },
        summary: { type: 'string' },
      },
      required: ['faction_count', 'vehicle_count', 'worldspace_count', 'missing', 'fixes_made', 'next_models_to_build', 'open_questions', 'summary'],
    },
  },
)

return { blocs, worldResults, validation }
