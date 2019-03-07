# Musical_Robot
Source code of musical robot project. Lead by Professor Steven Kemper at Rutgers University.

## Convert audio source to pieces of MIDI file
Go to the Musical_Robot folder, and run the following command in terminal: <br />
```bash
>python gui.py
```
**How to use GUI?** <br />
First, choose an audio source, either from input stream (i.e. microphone) or an existing audio file. <br />
Second, choose how you would like your melody to be. BPM(beats per min) indicates the tempo of the track. Smoothness indicates the smoothness of your pitch sequence. Min-duration indicates the minimum length of each note.<br />
Third, choose a pre-trained model from your library. The model should be in .mag format. We have provided some sample model stored in /model directory.<br />
Last, click "Generate your melody" to get your own products!

## Use pretrained neural network model based on Magenta project

## Train your own model

# Dependencies
- Requires python 2.7 (will most likely crash on python 3, untested)<br />
- Melodia melody extraction Vamp plugin: http://mtg.upf.edu/technologies/melodia<br />
- Librosa: https://github.com/librosa/librosa<br />
- Vamp python module: https://pypi.python.org/pypi/vamp<br />
- midiutil: https://code.google.com/p/midiutil/<br />
- NumPy & SciPy: http://www.scipy.org/<br />
- JAMS: https://github.com/marl/jams<br />
- Pyaudio: https://people.csail.mit.edu/hubert/pyaudio/<br />
