from jc3000 import Sequence
import numpy as np


def main():
    s = Sequence(voices=2)

    notes = list("abcdefga")

    for i in range(60):
        # voice 1
        for note in notes[:-1]:
            s.add_note(note, 1, 0, voice=0)
        s.add_note(notes[-1], 1, 1, voice=0)

    for i in range(30):
        # voice 2
        for note in notes[:-1]:
            s.add_note(note, 2, 0, voice=1)
        s.add_note(notes[-1], 2, 1, voice=1)

    s.write_file("overlapping.wav")


if __name__ == "__main__":
    main()
