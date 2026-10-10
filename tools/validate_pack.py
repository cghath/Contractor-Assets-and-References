#!/usr/bin/env python3
"""Validate the Contractor faction pack (stdlib only).

Checks the JSON in factions/, reference/vehicles/, worldspaces/ and loadouts/:
  * every file parses;
  * faction files have the required top-level keys and their id matches the filename;
  * relation keys, theatre ids and vehicle_ids are known;
  * every referenced vehicle_id has a reference/vehicles/<id>.json file;
  * terrorist factions (bloc me_terror in ROSTER) have player_client false;
  * loadouts/<id>.json (the three index files are skipped): the id is a canonical non-player faction id
    matching the filename, a 'regular' variant exists, every variant has the core roles, in_game
    launchers are among the 6 in-game launchers (others name one of them or null as game_substitute),
    and vest and helmet tiers are valid.

The canonical faction and theatre ids are read from tools/factions_workflow.js (ROSTER, THEATRES).

ERROR lines fail the run (exit 1). WARN lines are soft issues, including missing faction or
worldspace files, because the pack is still being generated.

usage: python3 tools/validate_pack.py [--strict]   (--strict also fails on warnings)
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOW = os.path.join(ROOT, "tools", "factions_workflow.js")
FACTION_KEYS = ["id", "name", "kind", "relations", "theatres", "vehicles"]
# Files in factions/ that are not faction records.
NON_FACTION_FILES = {"alliances"}
# Files in loadouts/ that are not per-faction loadouts.
LOADOUT_INDEX_FILES = {"weapons_index", "armor_index", "rounds_index"}
CORE_ROLES = ["rifleman", "autorifleman", "marksman", "grenadier", "at", "medic", "squad_leader", "sniper"]
GAME_LAUNCHERS = {"AT4", "RPG-7", "Javelin", "MAAWS", "NLAW", "SMAW"}
VEST_TIERS = {"light", "medium", "heavy"}
HELMET_TIERS = {"none", "light", "medium", "heavy"}

errors = []
warnings = []


def error(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def rel(path):
    return os.path.relpath(path, ROOT)


def parse_js_lists(src, const_name):
    """Parse `const NAME = { key: ['a', 'b'], ... }` into {key: [ids]}."""
    m = re.search(r"const\s+" + const_name + r"\s*=\s*\{(.*?)\n\}", src, re.S)
    if not m:
        raise SystemExit("ERROR could not find const %s in %s" % (const_name, rel(WORKFLOW)))
    out = {}
    for key, body in re.findall(r"(\w+)\s*:\s*\[([^\]]*)\]", m.group(1)):
        out[key] = re.findall(r"['\"]([^'\"]+)['\"]", body)
    if not out:
        raise SystemExit("ERROR const %s in %s has no lists" % (const_name, rel(WORKFLOW)))
    return out


def load_json_dir(sub):
    """Parse every *.json in a folder. Returns {stem: data} for files that parse."""
    folder = os.path.join(ROOT, sub)
    found = {}
    if not os.path.isdir(folder):
        return None
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(folder, name)
        try:
            with open(path, encoding="utf-8") as f:
                found[name[:-5]] = json.load(f)
        except (ValueError, UnicodeDecodeError) as e:
            error("%s: invalid JSON: %s" % (rel(path), e))
    return found


def check_launcher(path, where, ln):
    if not isinstance(ln, dict):
        error("%s: %s is not an object" % (path, where))
        return
    in_game = ln.get("in_game")
    if not isinstance(in_game, bool):
        error("%s: %s in_game must be true or false" % (path, where))
    elif in_game and ln.get("game_launcher") not in GAME_LAUNCHERS:
        error("%s: %s is in_game but game_launcher %r is not one of the 6 in-game launchers"
              % (path, where, ln.get("game_launcher")))
    elif not in_game and ln.get("game_substitute") not in GAME_LAUNCHERS | {None}:
        error("%s: %s game_substitute %r is not one of the 6 in-game launchers"
              % (path, where, ln.get("game_substitute")))


def check_loadout(stem, lo, faction_ids):
    path = "loadouts/%s.json" % stem
    if not isinstance(lo, dict):
        error("%s: top level is not an object" % path)
        return
    if lo.get("id") != stem:
        error("%s: id %r does not match the filename" % (path, lo.get("id")))
    if stem not in faction_ids or stem == "player":
        error("%s: %r is not a canonical non-player faction id" % (path, stem))
    variants = lo.get("variants")
    if not isinstance(variants, list) or not variants:
        error("%s: variants must be a non-empty list" % path)
        return
    ids = [v.get("id") for v in variants if isinstance(v, dict)]
    if "regular" not in ids:
        error("%s: no 'regular' variant" % path)
    if len(set(ids)) != len(ids):
        error("%s: duplicate variant ids" % path)
    for v in variants:
        if not isinstance(v, dict):
            error("%s: a variant is not an object" % path)
            continue
        vid = v.get("id")
        roles = v.get("roles")
        if not isinstance(roles, dict):
            error("%s: variant %r has no roles object" % (path, vid))
            continue
        for r in CORE_ROLES:
            if r not in roles:
                error("%s: variant %r is missing core role %r" % (path, vid, r))
        if v.get("armor_tier") not in VEST_TIERS | {"none"}:
            error("%s: variant %r armor_tier %r is not none/light/medium/heavy" % (path, vid, v.get("armor_tier")))
        for i, ln in enumerate(v.get("team_weapons") or []):
            check_launcher(path, "variant %r team_weapons[%d]" % (vid, i), ln)
        for rname, role in roles.items():
            where = "variant %r role %r" % (vid, rname)
            if not isinstance(role, dict):
                error("%s: %s is not an object" % (path, where))
                continue
            if role.get("not_fielded"):
                if role.get("stand_in_role") not in roles:
                    warn("%s: %s is not_fielded without a valid stand_in_role" % (path, where))
                continue
            if not isinstance(role.get("primary"), dict):
                error("%s: %s has no primary weapon" % (path, where))
            if role.get("launcher") is not None:
                check_launcher(path, where + " launcher", role["launcher"])
            armor = role.get("armor") or {}
            vest = armor.get("vest")
            if vest is not None and (not isinstance(vest, dict) or vest.get("tier") not in VEST_TIERS):
                error("%s: %s vest tier %r is not light/medium/heavy"
                      % (path, where, vest.get("tier") if isinstance(vest, dict) else vest))
            helmet = armor.get("helmet")
            if helmet is not None and (not isinstance(helmet, dict) or helmet.get("tier") not in HELMET_TIERS):
                error("%s: %s helmet tier %r is not none/light/medium/heavy"
                      % (path, where, helmet.get("tier") if isinstance(helmet, dict) else helmet))
            if armor.get("side_plates") and (not isinstance(vest, dict) or vest.get("tier") != "heavy"):
                error("%s: %s has side plates on a vest that is not heavy" % (path, where))
        for tr, target in (lo.get("role_map") or {}).items():
            if target not in roles:
                warn("%s: role_map %r -> %r is not a role of variant %r" % (path, tr, target, vid))


def main():
    strict = "--strict" in sys.argv[1:]
    with open(WORKFLOW, encoding="utf-8") as f:
        src = f.read()
    roster = parse_js_lists(src, "ROSTER")
    theatres_by_group = parse_js_lists(src, "THEATRES")
    faction_ids = {"player"} | {i for ids in roster.values() for i in ids}
    terror_ids = set(roster.get("me_terror", []))
    theatre_ids = {i for ids in theatres_by_group.values() for i in ids}

    factions = load_json_dir("factions")
    vehicles = load_json_dir(os.path.join("reference", "vehicles"))
    worlds = load_json_dir("worldspaces")
    extras = {k: (factions or {}).pop(k) for k in NON_FACTION_FILES if k in (factions or {})}
    alliances = extras.get("alliances")

    if vehicles is None:
        error("reference/vehicles/ is missing")
        vehicles = {}
    if factions is None:
        warn("factions/ does not exist yet")
        factions = {}
    if worlds is None:
        warn("worldspaces/ does not exist yet (generated after the factions)")
        worlds = {}

    # Vehicle catalogue: id should match the filename.
    for stem, v in vehicles.items():
        path = "reference/vehicles/%s.json" % stem
        if not isinstance(v, dict):
            error("%s: top level is not an object" % path)
        elif v.get("id") != stem:
            warn("%s: id %r does not match the filename" % (path, v.get("id")))
        else:
            for op in v.get("operators") or []:
                if op not in faction_ids:
                    warn("%s: operator %r is not a canonical faction id" % (path, op))

    # Factions.
    for stem, d in factions.items():
        path = "factions/%s.json" % stem
        if not isinstance(d, dict):
            error("%s: top level is not an object" % path)
            continue
        missing = [k for k in FACTION_KEYS if k not in d]
        if missing:
            error("%s: missing required keys: %s" % (path, ", ".join(missing)))
        if "id" in d and d["id"] != stem:
            error("%s: id %r does not match the filename" % (path, d["id"]))
        if stem not in faction_ids:
            error("%s: %r is not a canonical faction id" % (path, stem))

        relations = d.get("relations")
        if relations is not None and not isinstance(relations, dict):
            error("%s: relations is not an object" % path)
        elif relations:
            for k, val in relations.items():
                if k not in faction_ids:
                    error("%s: relation key %r is not a canonical faction id" % (path, k))
                elif k == stem:
                    warn("%s: relation with itself" % path)
                if not isinstance(val, (int, float)) or isinstance(val, bool) or not -100 <= val <= 100:
                    error("%s: relation %r value %r is not a number in -100..100" % (path, k, val))

        ths = d.get("theatres")
        if ths is not None and not isinstance(ths, list):
            error("%s: theatres is not a list" % path)
        elif ths:
            for t in ths:
                if t not in theatre_ids:
                    error("%s: theatre %r is not a canonical theatre id" % (path, t))

        vs = d.get("vehicles")
        if vs is not None and not isinstance(vs, list):
            error("%s: vehicles is not a list" % path)
        elif vs:
            for i, v in enumerate(vs):
                vid = v.get("vehicle_id") if isinstance(v, dict) else None
                if not vid:
                    error("%s: vehicles[%d] has no vehicle_id" % (path, i))
                elif vid not in vehicles:
                    error("%s: vehicle_id %r has no reference/vehicles/%s.json" % (path, vid, vid))

        for i, u in enumerate(d.get("unit_templates") or []):
            vid = u.get("vehicle_id") if isinstance(u, dict) else None
            if vid and vid not in vehicles:
                warn("%s: unit_templates[%d] vehicle_id %r has no catalogue file" % (path, i, vid))

        if stem in terror_ids and d.get("player_client") is not False:
            error("%s: terrorist faction must have player_client false (got %r)"
                  % (path, d.get("player_client")))

    # Alliances: member ids and relations-matrix keys must be canonical faction ids.
    if alliances is not None:
        path = "factions/alliances.json"
        if not isinstance(alliances, dict):
            error("%s: top level is not an object" % path)
        else:
            for a in alliances.get("alliances") or []:
                for m in (a.get("members") or []) if isinstance(a, dict) else []:
                    if m not in faction_ids:
                        error("%s: alliance %r member %r is not a canonical faction id" % (path, a.get("id"), m))
            matrix = alliances.get("relations_matrix") or {}
            for a, row in matrix.items() if isinstance(matrix, dict) else []:
                for b in [a] + list(row if isinstance(row, dict) else []):
                    if b not in faction_ids:
                        error("%s: relations_matrix key %r is not a canonical faction id" % (path, b))

    for fid in sorted(faction_ids - set(factions)):
        warn("factions/%s.json is missing (still generating?)" % fid)

    # Worldspaces.
    for stem, w in worlds.items():
        path = "worldspaces/%s.json" % stem
        if not isinstance(w, dict):
            error("%s: top level is not an object" % path)
            continue
        if stem not in theatre_ids:
            error("%s: %r is not a canonical theatre id" % (path, stem))
        if "id" in w and w["id"] != stem:
            error("%s: id %r does not match the filename" % (path, w["id"]))
        fp = w.get("factions_present")
        for entry in fp if isinstance(fp, list) else []:
            fid = entry.get("faction_id") or entry.get("id") if isinstance(entry, dict) else entry
            if isinstance(fid, str) and fid not in faction_ids:
                error("%s: factions_present %r is not a canonical faction id" % (path, fid))
    for tid in sorted(theatre_ids - set(worlds)):
        warn("worldspaces/%s.json is missing (still generating?)" % tid)

    loadouts = load_json_dir("loadouts")
    if loadouts is None:
        warn("loadouts/ does not exist yet")
        loadouts = {}
    for k in LOADOUT_INDEX_FILES:
        loadouts.pop(k, None)
    for stem, lo in loadouts.items():
        check_loadout(stem, lo, faction_ids)
    for fid in sorted(faction_ids - {"player"} - set(loadouts)):
        warn("loadouts/%s.json is missing" % fid)

    for w in warnings:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    print("\n%d factions, %d vehicles, %d worldspaces, %d loadouts checked: %d error(s), %d warning(s)"
          % (len(factions), len(vehicles), len(worlds), len(loadouts), len(errors), len(warnings)))
    return 1 if errors or (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
