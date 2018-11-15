# Musical_Robot
Source code of musical robot project. Lead by Professor Steven Kemper at Rutgers University.

# Convert audio source to pieces of MIDI file
Usage: audio_to_midi.py [-h] mode [--smooth SMOOTH] [--minduration MINDURATION] [--jams] outfile bpm<br />
mode 0 is to use input stream; mode 1 is to use audio file<br />
Example: python audio_to_midi.py 1 --smooth 0.25 --minduration 0.1 --jams ~/song.mid 60<br />

# Dependencies
Requires python 2.7 (will most likely crash on python 3, untested)<br />
Melodia melody extraction Vamp plugin: http://mtg.upf.edu/technologies/melodia<br />
Librosa: https://github.com/librosa/librosa<br />
Vamp python module: https://pypi.python.org/pypi/vamp<br />
midiutil: https://code.google.com/p/midiutil/<br />
NumPy & SciPy: http://www.scipy.org/<br />
JAMS: https://github.com/marl/jams<br />
Pyaudio: https://people.csail.mit.edu/hubert/pyaudio/<br />

