from jc3000 import Sequence
from dataclasses import dataclass


@dataclass
class Note:
    note: str = ""
    octave: int = 0


def play_chord(s, chord):
    n = chord[0]
    duration = 0.5

    s.add_note(n.note, duration=duration, octave=n.octave, voice=0)
    for i in range(1, len(chord)):
        s.add_note(n.note, duration=duration, voice=i, silent=True)

    duration = 0.25
    s.add_note(n.note, duration=duration, octave=n.octave, voice=0)
    for i in range(1, len(chord)):
        s.add_note(n.note, duration=duration, voice=i, silent=True)

    for voice, note in enumerate(chord):
        if note.note != "":
            s.add_note(
                note.note,
                duration=0.5,
                octave=note.octave,
                voice=voice,
            )
        else:
            s.add_note(
                "a",
                duration=0.5,
                voice=voice,
                silent=True,
            )

    for voice, note in enumerate(chord):
        if note.note != "":
            s.add_note(
                note.note,
                duration=0.25,
                octave=note.octave,
                voice=voice,
            )
        else:
            s.add_note(
                "a",
                duration=0.25,
                voice=voice,
                silent=True,
            )


def main():
    s = Sequence(voices=6)

    c = [Note("c"), Note("e"), Note("g", -1), Note("c", 1), Note("e"), Note()]
    a_min = [Note("a"), Note("e"), Note("g", 1), Note("c", 1), Note("e", 1), Note()]
    f = [Note("f", -1), Note("c"), Note("f"), Note("a", 1), Note("c", 1), Note("e", 1)]
    g = [Note("g", -1), Note("b"), Note("d"), Note("g", 1), Note("b", 1), Note("f", 1)]
    chords = [c, a_min, f, g] * 60

    for chord in chords:
        play_chord(s, chord)

    s.write_file("heart_and_soul")


if __name__ == "__main__":
    main()
