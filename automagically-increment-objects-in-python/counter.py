from collections import Counter
import json


def update_my_piano_ballad_recordings(
    song_name: str, num_recordings: int, data: Counter
):
    return data.update({song_name: num_recordings})


def log_my_piano_ballad_recordings(data: Counter):
    result = json.dumps(dict(data))
    print(result)
    return result


def main():
    print("A main program to demonstrate the collections.Counter subclass.")
    my_piano_ballad_recordings = Counter({"Colder Weather": 2, "Mad World": 1})
    print(my_piano_ballad_recordings)
    print('Adding another recording of "Colder Weather".')
    my_piano_ballad_recordings.update({"Colder Weather": 1})
    assert my_piano_ballad_recordings["Colder Weather"] == 3
    assert my_piano_ballad_recordings["Mad World"] == 1
    print(my_piano_ballad_recordings)
    print(
        'Now adding our first recording of "Jolene" and two more recordings of "Mad World".'
    )
    my_piano_ballad_recordings.update({"Jolene": 1, "Mad World": 2})
    assert "Jolene" in my_piano_ballad_recordings
    assert my_piano_ballad_recordings["Jolene"] == 1
    print(my_piano_ballad_recordings)


if __name__ == "__main__":  # pragma: no cover
    main()
