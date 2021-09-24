from jc3000 import Sequence

s = Sequence(voices=2)

s.add_note("c", duration=10, voice=0)
s.add_note(s._get_note_by_interval("c", 9), duration=1, voice=1)
s.add_note(s._get_note_by_interval("c", 10), duration=1, voice=1)
s.add_note(s._get_note_by_interval("c", 11), duration=1, voice=1)
s.add_note(s._get_note_by_interval("c", 12), duration=1, voice=1)
s.add_note(s._get_note_by_interval("c", 9), duration=1, voice=1)
s.add_note(s._get_note_by_interval("c", 7), octave=-1, duration=1, voice=1)
s.add_note(s._get_note_by_interval("c", 5), octave=-1, duration=1, voice=1)
s.add_note(s._get_note_by_interval("c", 4), octave=-1, duration=3, voice=1)
s.write_file("harm")
