import managedb
import pytest
from inventory import Inventory
import collections
import os


@pytest.fixture(scope="function")
def test_inventory():
    return Inventory(id="test-inventory", data=dict(foo=3, bar=4))


@pytest.fixture(scope="function")
def test_counter():
    return collections.Counter(foo=3, bar=4)


@pytest.fixture(scope="function")
def test_filename():
    cwd = os.getcwd()
    return f"test-counter.json"


def test_save_local_inventory(test_inventory, test_counter, test_filename):
    test_filepath = managedb.save_local_inventory(
        test_counter,
        filename=test_filename,
    )
    assert os.path.exists(test_filepath)
    os.remove(test_filepath)
    assert not os.path.exists(test_filepath)

    filepath = test_inventory.save()
    assert os.path.exists(filepath)
    os.remove(filepath)
    assert not os.path.exists(filepath)


def test_load_local_inventory(
    test_inventory,
):
    filepath = test_inventory.save()
    loaded_inventory_data = managedb.load_local_inventory(
        f"inventory-{test_inventory.id}.json"
    )
    inventory = Inventory(
        id=test_inventory.id,
        data=loaded_inventory_data,
    )
    assert isinstance(inventory, collections.Counter)
    for key in test_inventory:
        assert inventory[key]

    filepath2 = inventory.save()
    assert filepath == filepath2

    os.remove(filepath)
    assert not os.path.exists(filepath)

    try:
        managedb.load_local_inventory("not there")
    except FileNotFoundError as ferr:
        assert "does not exist." in f"{ferr}"
