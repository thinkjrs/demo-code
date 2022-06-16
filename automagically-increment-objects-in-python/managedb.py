import json
import collections
import logging
from typing import Union, Dict, Any
import os

CWD = os.getcwd()


def save_local_inventory(
    inventory: collections.Counter,
    filename: str = "local-inventory.json",
):
    """Save a given Counter object to a local file."""
    filepath = f"{CWD}/{filename}"
    with open(filepath, "a+") as f:
        logging.info(f"Writing latest to file {filepath}.")
        f.write(json.dumps(dict(inventory)))
        return filepath


def load_local_inventory(
    filename: str = "local-inventory.json",
) -> Union[Dict[str, Union[int, float]], None]:
    filepath = f"{CWD}/{filename}"
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} does not exist.")

    with open(filepath, "r") as f:
        inventory = json.loads(f.read())
        return inventory
