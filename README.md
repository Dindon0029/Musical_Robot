# Musical_Robot
Source code of musical robot project. Lead by Professor Steven Kemper at Rutgers University. <br />
Our research provides a machine learning framework which takes an audio file as primer and produces a meaningful melody as output. The input audio file is first converted into MIDI format, and then passes through a pre-trained recurrent neural network model. The model incorporates input audio and produces an output MIDI file. Finally, the MIDI file is transmitted and played either by MIDI software or MIDI instruments. In our research, a self-made Vibration Motor Actuated robotic string instrument stands as an output instrument. However, the program itself is stand-alone, thus can be generally used for any output sources. <br />

## Run the program using pre-trained model
We create a Graphical User Interface for easy use <br />

Usage: 
```bash
>python gui.py
```

## Train your own model
The construction of neural network is built on Google Magenta project (https://github.com/tensorflow/magenta)

# Dependencies
- Requires python 2.7 (will most likely crash on python 3, untested)<br />
- Melodia melody extraction Vamp plugin: http://mtg.upf.edu/technologies/melodia<br />
- Librosa: https://github.com/librosa/librosa<br />
- Vamp python module: https://pypi.python.org/pypi/vamp<br />
- midiutil: https://code.google.com/p/midiutil/<br />
- NumPy & SciPy: http://www.scipy.org/<br />
- JAMS: https://github.com/marl/jams<br />
- Pyaudio: https://people.csail.mit.edu/hubert/pyaudio/<br />
- Pygame: 
- Mido:
- Py-midi:
- Rtmidi:
