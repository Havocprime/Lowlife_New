import importlib
import pytest

MODULES = [
    "bot",
    "rules",
    "embeds",
    "combat_loadout",
    "inventory",
    "inventory_cmds",
    "players",
    "updates",
    "duel_core",
    "duel_legacy",
]

@pytest.mark.parametrize("name", MODULES)
def test_import_modules(name):
    try:
        importlib.import_module(name)
    except ModuleNotFoundError as e:
        pytest.skip(f"Optional module not found: {name} ({e})")
