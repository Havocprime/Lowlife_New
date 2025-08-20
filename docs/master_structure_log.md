# Master Structure Log — Lowlife Society

> Living blueprint. Update this as systems evolve.

## Modules (flat layout)
- **bot.py** — Entrypoint; loads env, registers commands.
- **rules.py** — Rules & templates loader.
- **embeds.py** — Embed builders; tileset definitions.
- **combat_loadout.py** — Weapon profiles, range logic.
- **inventory.py** — Equip/get inventory hooks.
- **inventory_cmds.py** — Slash commands for inventory.
- **players.py** — Player profile (/create, /sheet).
- **updates.py** — Updatelog posting & watcher.
- **duel_core.py** — Legacy combat math/utils.
- **duel_legacy.py** — Legacy duel flow for reference.

## Assets
- **assets/embeds/** — seals, footers, headers.
- **assets/tilesets/** — optional JSON presets (background glyph, borders, fills).

## Tile Presets (idea)
```json
{
  "braille": {"bg":"\u2800","fill":"█","empty":"·","cursor":"▣"},
  "light":   {"bg":"·","fill":"░","empty":" ","cursor":"■"}
}
```

## Versioning
- Runtime version: `version.py` (`__version__`).
- Updatelogs & embeds should import and display version.

## Roadmap Stubs
- [ ] Convert to `src/` package layout.
- [ ] Add persistence (SQLite/Postgres) for items & players.
- [ ] Coverage on combat math.
- [ ] Asset pipeline (SVG → PNG variants).
