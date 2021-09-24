"""
voices: 3
concert A: 432hz
notes: C major scale
temperament: equal
time signature:  6/8
tempo: 60 bm
duration: 10 seconds
"""

from jc3000 import Sequence
import random


def silent() -> bool:
    return random.random() > 0.5


def main():
    voices = 3
    s = Sequence(fundamental=432, equal=True, voices=voices)
    notes = list("abcdefg")

    notes_to_harmonies = {}
    for note in notes:
        if not notes_to_harmonies.get(note, False):
            notes_to_harmonies[note] = {}
        third = s.get_minor_third(note)
        if third not in notes:
            third = s.get_major_third(note)
        notes_to_harmonies[note]["3"] = third
        notes_to_harmonies[note]["5"] = s.get_fifth(note)

    time_sig_num = 6
    time_sig_den = 8
    bpm = 60
    song_duration_secs = 10

    last_four_chosen = []
    i = 1

    while song_duration_secs > 0:
        note = random.choice(notes)

        while note in last_four_chosen:
            note = random.choice(notes)
        i += 1

        if i == 4:
            last_four_chosen = []
            i = 0

        duration = ((random.randint(1, time_sig_num) / time_sig_den) * 60) / bpm
        song_duration_secs -= duration

        s.add_note(note, duration, random.randint(-1, 1), voice=0, silent=silent())
        s.add_note(
            notes_to_harmonies[note]["5"], duration, random.randint(-1, 1), voice=1, silent=silent()
        )
        s.add_note(
            notes_to_harmonies[note]["3"], duration, random.randint(-1, 1), voice=2, silent=silent()
        )

    s.write_file("a432.wav")


if __name__ == "__main__":
    main()
