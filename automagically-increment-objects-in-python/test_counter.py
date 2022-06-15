from collections import Counter
import pytest
import counter


@pytest.fixture(scope="function")
def recording_data():
    return Counter({"Colder Weather": 2, "Mad World": 1})


def test_update_my_piano_ballad_recordings(recording_data):
    assert recording_data["Colder Weather"] == 2
    assert (
        counter.update_my_piano_ballad_recordings(
            "Colder Weather", 2, recording_data
        )
        is None
    )
    assert recording_data["Colder Weather"] == 4


def test_log_my_piano_ballad_recordings(recording_data):
    assert isinstance(
        counter.log_my_piano_ballad_recordings(recording_data), str
    )


def test_main():
    counter.main()
