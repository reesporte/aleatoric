from jc3000 import Sequence


def play_chord(s, chord):
    note = chord[0]
    duration = 0.5
    octave = 0 if chord[0] != "f" and chord[0] != "g" else -1

    s.add_note(note, duration=duration, octave=octave, voice=0)
    s.add_note(note, duration=duration, octave=octave, voice=1, silent=True)
    s.add_note(note, duration=duration, octave=octave, voice=2, silent=True)

    duration = 0.25

    s.add_note(note, duration=duration, octave=octave, voice=0)
    s.add_note(note, duration=duration, octave=octave, voice=1, silent=True)
    s.add_note(note, duration=duration, octave=octave, voice=2, silent=True)

    for voice, note in enumerate(chord):
        s.add_note(
            note, duration=0.5, octave=1 if chord[0] != "f" and chord[0] != "g" else 0, voice=voice
        )

    for voice, note in enumerate(chord):
        s.add_note(
            note, duration=0.25, octave=1 if chord[0] != "f" and chord[0] != "g" else 0, voice=voice
        )


def main():
    s = Sequence(voices=3)

    c = ["c", "e", "g"]
    f = ["f", "a", "c"]
    a_min = ["a", "c", "e"]
    g = ["g", "b", "d"]
    chords = [c, a_min, f, g] * 60

    for chord in chords:
        play_chord(s, chord)

    s.write_file("heart_and_soul")


if __name__ == "__main__":
    main()
