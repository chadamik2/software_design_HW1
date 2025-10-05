import pytest
from software_design_HW1.src.domain.inventory import InventoryNumberRegistry


def test_inventory_reserve_and_release():
    reg = InventoryNumberRegistry()
    assert reg.is_free(5) is True
    reg.reserve(5)
    assert reg.is_free(5) is False
    with pytest.raises(ValueError):
        reg.reserve(5)
    reg.release(5)
    assert reg.is_free(5) is True
