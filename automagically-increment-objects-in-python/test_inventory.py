from inventory import Inventory
import collections
import pytest
import uuid
from random import randint
import os


@pytest.fixture(scope="function")
def product_codes():
    """Return a random uuid code to represent a product."""
    return [str(uuid.uuid4()) for _ in range(10)]


@pytest.fixture(scope="function")
def product_inventory(product_codes):
    """Return 'random' inventory numbers for each product code."""
    return [randint(1, 100) for _ in enumerate(product_codes)]


@pytest.fixture(scope="function")
def inventory_data(
    product_codes,
    product_inventory,
):
    """Combine product codes and 'random' inventory into a dictionary."""
    return {key: val for key, val in zip(product_codes, product_inventory)}


def test_Inventory_class(inventory_data):
    # test barebones
    test_inventory = Inventory()
    assert isinstance(test_inventory, collections.Counter)
    test_inventory["test"] = 3
    test_inventory.update(dict(test=3))
    assert test_inventory["test"] == 6
    # test custom data
    test_inventory = Inventory(data=inventory_data)
    for key in list(inventory_data):
        assert test_inventory[key]

    test_inventory_path = test_inventory.save()
    assert os.path.exists(test_inventory_path)

    os.remove(test_inventory_path)
    assert not os.path.exists(test_inventory_path)
    # test custom id
    test_inventory = Inventory(id="record-store", data=inventory_data)
    for key in list(inventory_data):
        assert test_inventory[key]

    test_inventory_path = test_inventory.save()
    assert os.path.exists(test_inventory_path)
    test_loaded_inventory = test_inventory.load()
    assert test_loaded_inventory is not None
    os.remove(test_inventory_path)
    assert not os.path.exists(test_inventory_path)

    for key in list(inventory_data):
        test_inventory.remove(key)

    for key in list(inventory_data):
        assert not test_inventory[key]

    assert test_inventory.load() is None
