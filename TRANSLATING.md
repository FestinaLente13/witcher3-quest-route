# Translating

Thanks for helping! Each language is a single JSON file in `i18n/`.

## Steps

1. Copy `i18n/template.json` to `i18n/<code>.json`, using a standard language code: `de`, `fr`, `es`, `pl`, `it`, `ru`, `pt-BR`…
2. Fill in `meta.name` (your language's name, written in that language, e.g. `Deutsch`) and `meta.credit` (your name or handle).
3. Translate the **values**, never the keys. You don't have to finish everything: anything you leave in English or delete falls back to English.
4. Add your language to `i18n/index.json`:
   ```json
   {"code": "de", "name": "Deutsch", "credit": "your-handle"}
   ```
5. Open a pull request. If GitHub isn't your thing, open an issue and attach the file.

## What's in the file

| Section | What it is | Tip |
|---|---|---|
| `ui` | Buttons, labels, messages (~150 strings) | Start here: it's quick and makes the app feel native |
| `content.quests` | Quest names, keyed by id | Use the **official names from your language's version of the game** where you know them. The English name always shows underneath, so players can still search the wiki. |
| `content.chapters`, `content.notes` | Chapter titles and route notes | |
| `content.tips` | 900+ tips | The big one. Partial is fine. |
| `content.gwent` | Faction names, card names, card locations | Keep character names as the game spells them |
| `content.extras` | Extras tab: witcher school names (`schools`), gear pieces and where to buy the maps (`gear`, keyed by the English text), trophy requirements (`trophies`), challenge runs as `[name, description]` (`challenges`) | Trophy names stay in English in the app, so only translate the requirement |

## Rules of thumb

- Keep `{placeholders}` exactly as they are, e.g. `"Level {lv}"` → `"Stufe {lv}"`.
- Keep the curly quotes, `@0:19` video timestamps and `#23`-style numbers.
- Short beats literal: these strings live on a phone screen.
- Don't run the tips through a machine translator and paste the result unreviewed. Rough but reviewed is better than fluent but wrong.

## Testing locally

```sh
python3 -m http.server
# then open http://localhost:8000 and pick your language in Settings
```
