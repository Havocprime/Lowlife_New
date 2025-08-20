import importlib
import pytest

def test_duel_legacy_imports():
    try:
        mod = importlib.import_module("duel_legacy")
    except ModuleNotFoundError:
        pytest.skip("duel_legacy not present")
        return
    # Sanity check: module object loaded
    assert hasattr(mod, "__name__")
