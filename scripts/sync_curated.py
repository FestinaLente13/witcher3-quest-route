#!/usr/bin/env python3
"""Turn the curator's personal save into data/curated.json.

Usage:
  python3 scripts/sync_curated.py SAVE.json [--translations EN.json] [--by NAME]

SAVE.json is the curator's progress document. Only the free-quest planning is
published: "after" (do this free quest after route quest X), "nt" (short note),
"mk" (map marker) and "ord" (custom order of a free-quest block). Completed
quests, tip checks and level stay private.

Notes are written in Portuguese. Their English versions come from
--translations (a {quest_id: english_text} JSON) or are carried over from the
existing curated.json when the Portuguese text hasn't changed. Any note still
missing an English version is listed in data/curated.missing.json (and the
script exits 3) so whoever runs the sync can translate it and run again.
"""
import json, sys, argparse, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKERS = {'skull', 'tri', 'info', 'x', 'flag', 'diamond'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('save')
    ap.add_argument('--translations')
    ap.add_argument('--by', default='Festina Lente')
    a = ap.parse_args()

    save = json.load(open(a.save))
    save = save.get('data', save)  # accept a raw db read ({id, data, ...}) too
    guide = json.load(open(ROOT / 'data/guide.json'))
    cur_path = ROOT / 'data/curated.json'
    old = json.load(open(cur_path)) if cur_path.exists() else {}
    tr = json.load(open(a.translations)) if a.translations else {}

    free, route, blocks = set(), set(), set()
    for ch in guide['chapters']:
        items = ch['items']
        for i, it in enumerate(items):
            if it['t'] == 'q':
                (free if it.get('any') else route).add(it['id'])
            elif it['t'] == 'note' and it['k'] == 'any' and i + 1 < len(items) and items[i + 1]['t'] == 'q':
                blocks.add(items[i + 1]['id'])

    after = {k: v for k, v in (save.get('after') or {}).items() if k in free and v in route}
    notes = {k: v.strip()[:80] for k, v in (save.get('nt') or {}).items() if k in free and isinstance(v, str) and v.strip()}
    marks = {k: v for k, v in (save.get('mk') or {}).items() if k in free and v in MARKERS}
    order = {k: [i for i in v if i in free] for k, v in (save.get('ord') or {}).items() if k in blocks and isinstance(v, list)}

    picks, missing = {}, {}
    for qid in sorted(set(after) | set(notes) | set(marks), key=lambda s: int(s[1:])):
        p = {}
        if qid in after: p['after'] = after[qid]
        if qid in marks: p['mk'] = marks[qid]
        if qid in notes:
            pt = notes[qid]
            prev = (old.get('picks', {}).get(qid) or {}).get('note') or {}
            en = tr.get(qid) or (prev.get('en') if prev.get('pt-BR') == pt else None)
            p['note'] = {'pt-BR': pt}
            if en: p['note']['en'] = en
            else: missing[qid] = pt
        picks[qid] = p

    out = {
        'by': a.by or old.get('by', ''),
        'updated': datetime.date.today().isoformat(),
        'picks': picks,
        'order': order,
    }
    changed = {k: v for k, v in out.items() if k != 'updated'} != {k: v for k, v in old.items() if k != 'updated'}
    if changed or not old:
        json.dump(out, open(cur_path, 'w'), ensure_ascii=False, indent=1)
    miss_path = ROOT / 'data/curated.missing.json'
    if missing:
        json.dump(missing, open(miss_path, 'w'), ensure_ascii=False, indent=1)
        print(f'{len(missing)} note(s) need an English translation: {miss_path}')
        sys.exit(3)
    if miss_path.exists(): miss_path.unlink()
    print(f'picks: {len(picks)}  order blocks: {len(order)}  changed: {changed}')


if __name__ == '__main__':
    main()
