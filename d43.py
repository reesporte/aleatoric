"""
voices: 3
notes: D major 
concert A: 440hz
temperament: equal
time signature:  4/3
tempo: 60 bpm
duration: 10 seconds
"""

from jc3000 import Sequence
import random


def main():
    voices = 3
    s = Sequence(fundamental=440, equal=True, voices=voices)
    notes = ["d", "e", "f#", "g", "a", "b", "c#"]
    time_sig_num = 4
    time_sig_den = 3
    bpm = 120
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

        s.add_note(note, duration, random.randint(-1, 1), voice=0)
        s.add_note(s.get_fifth(note), duration, random.randint(-1, 1), voice=1)
        s.add_note(s.get_major_third(note), duration, random.randint(-1, 1), voice=2)

    s.write_file("d43.wav")


if __name__ == "__main__":
    main()
