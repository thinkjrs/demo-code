import pytest
import json
from some_data_structure import SomeDataStructure, SomeDataStructureEncoder


@pytest.mark.parametrize(
    "class_attribute", ["shoe_size_meters", "initialization_dt"]
)
def test_SomeDataStructure(class_attribute):

    sds = SomeDataStructure()

    assert isinstance(str(sds), str)
    assert isinstance(repr(sds), str)
    assert repr(sds) == str(sds)
    assert class_attribute in str(sds)
    json_obj = json.loads(str(sds))
    assert isinstance(json_obj, list)
    assert class_attribute in json_obj[0]


class ClassNoIter:
    def __init__(
        self,
    ):
        self.shoe_size_meters = 0.25


@pytest.mark.parametrize(
    "classes",
    [
        dict(test=15),
        [
            dict(test=15),
        ],
        tuple(dict(test=15).items()),
        set([15, 14, 13]),
        SomeDataStructure(),
        ClassNoIter(),
    ],
    ids=[
        "dict",
        "list",
        "tuple",
        "set",
        "Class with __iter__ method",
        "Class without __iter__ method",
    ],
)
def test_SomeDataStructureEncoder(classes):
    try:
        json.dumps(classes, cls=SomeDataStructureEncoder)
    except Exception as err:
        assert "JSON" in f"{err}"
