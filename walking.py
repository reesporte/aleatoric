from jc3000 import Sequence
from dataclasses import dataclass


@dataclass
class Note:
    note: str = ""
    octave: int = 0
    duration: int = 0.25
    voice: int = 0


def play(s, chord):
    for _ in range(4):
        for n in chord:
            s.add_note(n.note, duration=n.duration, octave=n.octave, voice=n.voice)


def main():
    s = Sequence(voices=2)

    chords = [
        [
            Note("g#", duration=0.75, octave=-1),
            Note("g#", octave=-1, voice=1),
            Note("g#", voice=1),
            Note("b", voice=1),
        ],
        [
            Note("f#", duration=0.75, octave=-1),
            Note("f#", octave=-1, voice=1),
            Note("g#", voice=1),
            Note("b", voice=1),
        ],
        [
            Note("e", duration=0.75, octave=-1),
            Note("e", octave=-1, voice=1),
            Note("g#", voice=1),
            Note("b", voice=1),
        ],
        [
            Note("d#", duration=0.75, octave=-1),
            Note("d#", octave=-1, voice=1),
            Note("g#", voice=1),
            Note("b", voice=1),
        ],
        [
            Note("d", duration=0.75, octave=-1),
            Note("d", octave=-1, voice=1),
            Note("g#", voice=1),
            Note("b", voice=1),
        ],
        [
            Note("c#", duration=0.75, octave=-1),
            Note("c#", octave=-1, voice=1),
            Note("g#", voice=1),
            Note("b", voice=1),
        ],
        [
            Note("b", duration=0.75, octave=-1),
            Note("b", octave=-1, voice=1),
            Note("g#", voice=1),
            Note("b", voice=1),
        ],
        [
            Note("a", duration=0.75, octave=-1),
            Note("a", octave=-1, voice=1),
            Note("g#", voice=1),
            Note("b", voice=1),
        ],
    ]

    chords *= 2

    chords.append(
        [
            Note("e", duration=0.75, octave=-1),
            Note("e", octave=-1, voice=1),
            Note("g#", voice=1),
            Note("b", voice=1),
        ]
    )

    chords.append(
        [
            Note("e", duration=0.75, octave=-1),
            Note("e", octave=-1, voice=1),
            Note("e", octave=-1, voice=1),
            Note("e", octave=-1, voice=1),
        ]
    )

    for chord in chords:
        play(s, chord)

    s.write_file("walking")


if __name__ == "__main__":
    main()
