# some_data_structure.py
import json
from datetime import datetime, timezone


class SomeDataStructureEncoder(json.JSONEncoder):
    """A custom encoder class for SomeDataStructure"""

    def default(
        self,
        o,
    ):
        """
        A custom default encoder.
        In reality this should work for nearly any iterable.
        """
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, o)


class SomeDataStructure:
    """A bullshit data structure for example's sake."""

    def __init__(
        self,
    ):
        self.shoe_size_meters = 0.25  # Shaq, watch out!
        self.initialization_dt = datetime.now(timezone.utc)

    def __iter__(
        self,
    ):
        """
        Return a generator of the data initialized in the self.__init__
        func.
        """
        yield {
            "shoe_size_meters": self.shoe_size_meters,
            "initialization_dt": self.initialization_dt.strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
        }

    def __str__(
        self,
    ):
        return json.dumps(
            self,
            cls=SomeDataStructureEncoder,
        )

    def __repr__(
        self,
    ):
        return self.__str__()
