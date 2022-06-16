"""
inventory.py 

A module for simple inventory management for a record store.

Features: 
    - Create an inventory
    - Save an inventory 
    - Update an inventory with items (records)
    - Remove items from an inventory 
    - Get diagnostics an inventory
"""
import collections
import uuid
import os
from typing import Union, Dict, Any
import managedb
import logging


class Inventory(collections.Counter):
    """An Inventory class. Inherits from `collections` `Counter` and add
    saving and a removal functionality."""

    def __init__(
        self,
        id: Union[str, None] = None,
        data: Union[Dict[str, Any], None] = None,
    ):
        super().__init__(data)
        self.id = id or str(uuid.uuid4())
        self.filename = f"inventory-{self.id}.json"
        self.filepath = self.load()

    def save(
        self,
    ):
        """Save the inventory object to the local database."""
        self.filepath = managedb.save_local_inventory(
            self, filename=self.filename
        )
        return self.filepath

    def load(
        self,
    ):
        result = None
        try:
            result = managedb.load_local_inventory(self.filename)

            self.filepath = f"{os.getcwd()}/{self.filename}"
            if not result:
                return
            for key, val in result.items():
                self[key] = val
            return self

        except FileNotFoundError:
            logging.info(f"Attempted to load {self.filename}. Not found.")

    def remove(
        self,
        key: str,
    ):
        """Remove an inventory item"""
        del self[key]
