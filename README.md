# Witcher 3 Quest Route

> **This tool is entirely based on [ChrisRi](https://buymeacoffee.com/ChrisRi)'s [_Witcher 3 Optimal Quest Order Guide_](https://docs.google.com/spreadsheets/d/12H5lZC6vLFj0JToLSD2ZE7EcMN6MrmltL9SM_G6EUNU/edit?usp=sharing), with extra details by xLetalis.**
> The quest order, the suggested levels and every one of the 900+ tips are their work. This project is only a phone-friendly way to view that guide while you play, built with the help of AI.
>
> ### ☕ If it helps you, [buy ChrisRi a coffee](https://buymeacoffee.com/ChrisRi).
>
> The original Google Sheet has a lot more than this viewer shows: the full alchemy ingredient guide, scavenger hunt maps, the trophy list, challenge runs and Chris's changelog. **[Open the original guide](https://docs.google.com/spreadsheets/d/12H5lZC6vLFj0JToLSD2ZE7EcMN6MrmltL9SM_G6EUNU/edit?usp=sharing)**.

A free, phone-friendly checklist for playing **The Witcher 3** (base game + Hearts of Stone + Blood and Wine) in the optimal quest order.

**Open it:** https://festinalente13.github.io/witcher3-quest-route/

## What it does

- Shows the **next quest on the route**, with its suggested level and the most important tip
- Flags **missable quests**, and counts how many are still pending in each chapter
- Groups the **free quests** (doable any time) by region. You can reorder them, plan them right after a route quest ("do this after #23"), give them one of the in-game map markers and add a short note.
- **Curator's picks** (by *Festina Lente*): while playing along the route, the curator slots free quests next to nearby route quests of a similar level, with short notes. They update weekly, and you can turn them off in Settings.
- All the guide's tips, with video and map links where the original had them
- Gwent card checklist with where to find each copy
- No account, no ads, no cookies. Progress stays in your browser, and you can export it to a file and import it on another device. The only thing sent anywhere is an anonymous visit count ([GoatCounter](https://www.goatcounter.com/), which stores no personal data), so the maintainer can see whether people use it. Forks don't send it.

## Your data vs. the curator's picks

The two never touch:

- **Your progress and your own plans** (checks, level, notes, markers, order) live only in your browser's local storage. Site updates never change them.
- **Curator's picks** come from one read-only file, `data/curated.json`, which is replaced on each weekly update. Wherever you made your own choice, yours wins. You can also switch the picks off entirely.

**Forks:** to keep receiving the curator's updates without merging anything into your repo, set `curatedUrl` in `index.html` to
`https://raw.githubusercontent.com/FestinaLente13/witcher3-quest-route/main/data/curated.json`.

## Translations

The interface and all content can be translated. English is the default, and Português (Brasil) is complete. Want to add your language? See [TRANSLATING.md](TRANSLATING.md).

## How it's built

A single static page (`index.html`) that loads:

| File | What's in it |
|---|---|
| `data/guide.json` | Quest order, levels, categories, tips and Gwent cards, from ChrisRi's guide (English) |
| `data/curated.json` | Curator's picks: free-quest placement, notes, map markers, order |
| `i18n/*.json` | One file per language: interface strings and content translations |

No build step and no dependencies.

Region illustrations are drawn in code. Fan project: free, and not affiliated with CD PROJEKT RED.

## License

The code is MIT-licensed (see `LICENSE`). The guide content belongs to ChrisRi and xLetalis. Translations belong to their credited translators.
